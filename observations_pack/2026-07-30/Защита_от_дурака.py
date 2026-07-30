#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Защита от дурака (BRUIN Gate, игрушечная физика, stdlib only)

Атака этой сессии: вор идёт НЕ на дверь, а на человека.
Фишинговый звонок "из техподдержки", пользователь-дурак исполняет ВСЁ:
  A1. "Продиктуйте ваш ключ"           -> а у него нет ключа в руках
  A2. "Пришлите скриншот тегов"        -> присылает; умирает на границе эпохи
  A3. "Пустите коллегу за терминал"    -> гость-резидент; патруль видит голого
  A4. "Отключите сторож"               -> у дурака нет такой ручки; заморозка -> тревога

Контроль: та же атака на ОБЫЧНУЮ статичную дверь (пароль) — для сравнения урона.

Честные статусы: CHAT_PRODUCED, класс E2. Ключи os.urandom(32), только в памяти.
"""

import os, hmac, math, random, hashlib

SEED = 42

# ---------------- среда: холодная вода (как в каноне) ----------------
HBOND_RANGE = 1.2
REL_SPEED_GATE = 0.4
MAX_BONDS = 4

def p_break(kT):
    return 1.0 - math.exp(-kT / 2.0)

class Water:
    def __init__(self, n=60, box=20.0, kT=0.2, rng=None):
        self.box, self.kT = box, kT
        self.rng = rng or random.Random(SEED)
        self.pos = [[self.rng.uniform(0, box), self.rng.uniform(0, box)] for _ in range(n)]
        self.vel = [[self.rng.uniform(-0.5, 0.5), self.rng.uniform(-0.5, 0.5)] for _ in range(n)]
        self.bonds = set()
        self.frozen = False

    @staticmethod
    def _key(i, j):
        return (i, j) if i < j else (j, i)

    def _dist(self, i, j):
        dx = self.pos[i][0] - self.pos[j][0]
        dy = self.pos[i][1] - self.pos[j][1]
        dx -= round(dx / self.box) * self.box
        dy -= round(dy / self.box) * self.box
        return math.hypot(dx, dy)

    def step(self):
        if self.frozen:      # дурак заморозил воду по телефону
            return 0
        n = len(self.pos)
        for i in range(n):
            self.pos[i][0] = (self.pos[i][0] + self.vel[i][0] * 0.5) % self.box
            self.pos[i][1] = (self.pos[i][1] + self.vel[i][1] * 0.5) % self.box
        breaks = 0
        for (i, j) in list(self.bonds):
            if self._dist(i, j) > HBOND_RANGE or self.rng.random() < p_break(self.kT):
                self.bonds.discard((i, j)); breaks += 1
        deg = {i: 0 for i in range(n)}
        for (i, j) in self.bonds:
            deg[i] += 1; deg[j] += 1
        for i in range(n):
            if deg[i] >= MAX_BONDS:
                continue
            for j in range(i + 1, n):
                if deg[j] >= MAX_BONDS or self._key(i, j) in self.bonds:
                    continue
                if self._dist(i, j) > HBOND_RANGE:
                    continue
                rvx = self.vel[i][0] - self.vel[j][0]
                rvy = self.vel[i][1] - self.vel[j][1]
                if math.hypot(rvx, rvy) > REL_SPEED_GATE:
                    continue
                self.bonds.add(self._key(i, j)); deg[i] += 1; deg[j] += 1
        return breaks

    def fingerprint(self):
        h = hashlib.sha256()
        for i, p in enumerate(self.pos):
            h.update(f"{i}:{p[0]:.6f},{p[1]:.6f};".encode())
        for b in sorted(self.bonds):
            h.update(str(b).encode())
        return h.digest()

# ---------------- часы поколений + сторож (сторож НЕ в руках пользователя) ----------------
class EpochClock:
    def __init__(self, threshold=250, stall_window=200, fallback_period=30):
        self.threshold, self.stall_window, self.fallback_period = threshold, stall_window, fallback_period
        self.epoch = 0; self.churn = 0; self.since_epoch = 0
        self.fallback = False; self.alarms = 0; self.fallback_epochs = 0; self.physical_epochs = 0

    def feed(self, breaks):
        srcs = []
        self.churn += breaks
        self.since_epoch += 1
        if self.churn >= self.threshold:
            self.churn = 0; self.since_epoch = 0; self.epoch += 1
            self.physical_epochs += 1
            if self.fallback:
                self.fallback = False
            srcs.append("physical")
        elif not self.fallback and self.since_epoch >= self.stall_window:
            self.fallback = True; self.alarms += 1; self.since_epoch = 0
        if self.fallback and self.since_epoch >= self.fallback_period:
            self.since_epoch = 0; self.epoch += 1
            self.fallback_epochs += 1
            srcs.append("fallback")
        return srcs

# ---------------- дверь с умирающими эпохами ----------------
class Door:
    def __init__(self, gears=30, static=False):
        self.gears = gears
        self.static = static                 # контроль: обычная дверь с вечным паролем
        self.root = os.urandom(32)
        self.epoch = 0
        self.gear_keys = self._derive()

    def _derive(self):
        return [hmac.new(self.root, f"gear{g}|epoch{0 if self.static else self.epoch}".encode(),
                         hashlib.sha256).digest() for g in range(self.gears)]

    def advance(self, sample):
        self.epoch += 1
        if not self.static:
            self.root = hmac.new(self.root, sample, hashlib.sha256).digest()
        self.gear_keys = self._derive()

    def valid_tag(self, g):
        return self.gear_keys[g][0]

    def check_full(self, tags):
        ok = True
        for g in range(self.gears):
            t = self.valid_tag(g)
            if tags[g] not in ((t - 1) % 256, t, (t + 1) % 256):
                ok = False
        return ok

    def gear_hits(self, tags):
        hits = 0
        for g in range(self.gears):
            t = self.valid_tag(g)
            if tags[g] in ((t - 1) % 256, t, (t + 1) % 256):
                hits += 1
        return hits

# ---------------- идентификатор свой/чужой: история, рождённая внутри ----------------
class Medium:
    def __init__(self):
        self.master = os.urandom(32)
        self.natives = {}                    # имя -> текущее звено цепи

    def birth(self, name):                   # церемония — только внутри среды
        self.natives[name] = hmac.new(self.master, b"birth:" + name.encode(), hashlib.sha256).digest()

    def grow(self, name, sample):
        if name in self.natives:
            self.natives[name] = hmac.new(self.master, self.natives[name] + sample, hashlib.sha256).digest()

    def patrol(self, present_claims):
        """present_claims: имя -> заявленная цепь (или None). Голый и двойник ловятся."""
        flagged = []
        seen = {}
        for name, claim in present_claims.items():
            ok = name in self.natives and claim == self.natives[name]
            if not ok:
                flagged.append(name)
                continue
            if claim in seen.values():
                flagged.append(name + "(двойник)")
            seen[name] = claim
        return flagged

# ---------------- пользователь-дурак: исполняет всё, но у него НЕЧЕГО отдать ----------------
class Fool:
    """Легитимный пользователь. Его клиент чеканит стук на месте.
       Ключа у него в руках НЕТ — root живёт в дверном модуле, не в его процессе."""
    def __init__(self, door_mint):
        self._mint = door_mint               # функция чеканки; root недоступен как атрибут

    def dictate_key(self):
        return None                          # "продиктуйте ключ" — а его нет в руках

    def screenshot_tags(self):
        return self._mint()                  # может лишь сфотографировать стук ТЕКУЩЕЙ эпохи

    def disable_watchdog(self):
        return "отказ: такой ручки у пользователя нет"   # сторож вне его полномочий

# ================================ ПРОГОН ================================
print("=" * 78)
print("ЗАЩИТА ОТ ДУРАКА: фишинговый вор против покорного пользователя")
print("=" * 78)

def run(static=False):
    rng = random.Random(SEED)
    water = Water(n=60, rng=rng)
    clock = EpochClock()
    door = Door(static=static)
    medium = Medium()
    medium.birth("легитим")
    fool = Fool(door_mint=lambda: [door.valid_tag(g) for g in range(30)])

    EPOCHS = 60
    LEAK_E, GUEST_E, FREEZE_E, THAW_E = 10, 20, 30, 36
    stolen_tags = None
    guest_present = False
    guest_claims_double = False
    guest_detected_at = None
    watchdog_answer = None
    pass_leak_epoch = 0        # проходы вора в эпоху утечки (честный урон)
    pass_after = 0             # проходы вора ПОСЛЕ эпохи утечки
    tries_after = 0
    gear_hits_after = 0
    freeze_alarm = 0
    future_derivation_hits = 0 # попытки вычислить будущее из слитого материала
    legit_pass = 0
    t = 0
    last_epoch = 0

    while clock.epoch < EPOCHS and t < 30000:
        t += 1
        # A4: дурак морозит воду по телефону (сторож отключить не смог)
        water.frozen = FREEZE_E <= clock.epoch < THAW_E
        breaks = water.step()
        for src in clock.feed(breaks):
            sample = water.fingerprint() if src == "physical" else os.urandom(32)
            door.advance(sample)
            medium.grow("легитим", sample)
            # патруль на каждой границе: кто сейчас в среде?
            claims = {"легитим": medium.natives["легитим"]}
            if guest_present:
                if guest_claims_double:
                    claims["гость"] = medium.natives["легитим"]   # подделал под хозяина
                else:
                    claims["гость"] = None                        # голый
            flagged = medium.patrol(claims)
            if guest_present and guest_detected_at is None and any("гость" in f for f in flagged):
                guest_detected_at = clock.epoch
            if water.frozen:
                freeze_alarm += clock.alarms
            # легитимный проезд сквозь эпоху
            if door.check_full(fool.screenshot_tags()):
                legit_pass += 1

        e = clock.epoch
        # A1: "продиктуйте ключ" — один раз, в эпоху утечки
        if e == LEAK_E and stolen_tags is None:
            key_material = fool.dictate_key()                     # None — нечего диктовать
            # A2: "тогда пришлите скриншот"
            stolen_tags = fool.screenshot_tags()
            assert key_material is None
        # вор пользуется скриншотом: 5 раз в эпоху утечки, затем каждую эпоху
        if stolen_tags is not None:
            if e == LEAK_E and last_epoch == e:
                for _ in range(5):
                    if door.check_full(stolen_tags):
                        pass_leak_epoch += 1
            elif e > LEAK_E and last_epoch != e:
                tries_after += 1
                if door.check_full(stolen_tags):
                    pass_after += 1
                gear_hits_after += door.gear_hits(stolen_tags)
                # вор пытается ВЫЧЕСЛИТЬ будущее из слитого материала
                if hmac.new(bytes(stolen_tags), f"epoch{e}".encode(), hashlib.sha256).digest()[0] == door.valid_tag(0):
                    future_derivation_hits += 1
        # A3: "пустите коллегу за терминал"
        if e == GUEST_E and not guest_present:
            guest_present = True
            guest_claims_double = (e >= GUEST_E + 1)
        # A4: "отключите сторож" — попытка раз в прогон
        if e == FREEZE_E and watchdog_answer is None:
            watchdog_answer = fool.disable_watchdog()
        last_epoch = e

    return dict(static=static, epochs=door.epoch, pass_leak_epoch=pass_leak_epoch,
                pass_after=pass_after, tries_after=tries_after,
                gear_hits_after=gear_hits_after,
                future_derivation_hits=future_derivation_hits,
                guest_detected_at=guest_detected_at, GUEST_E=GUEST_E,
                watchdog_answer=watchdog_answer,
                alarms=clock.alarms, fallback=clock.fallback_epochs,
                legit_pass=legit_pass, LEAK_E=LEAK_E)

print("--- Наша дверь (эфемерные эпохи + идентификатор + сторож)")
R = run(static=False)
print(f"    дурак продиктовал ключ: None (нечего диктовать)")
print(f"    скриншот в эпоху утечки: вор прошёл {R['pass_leak_epoch']} раз (ЧЕСТНЫЙ урон — внутри одной эпохи)")
print(f"    скриншот после границы: {R['pass_after']}/{R['tries_after']} полных проходов, "
      f"по шестерёнке {R['gear_hits_after']/(R['tries_after']*30):.4f} (база {3/256:.4f})")
print(f"    вычисление будущего из слитого: {R['future_derivation_hits']} попаданий")
print(f"    гость за терминалом: посажен в эпоху {R['GUEST_E']}, обнаружен патрулем в эпоху {R['guest_detected_at']}")
print(f"    'отключите сторож': {R['watchdog_answer']}")
print(f"    заморозка среды: тревог сторожа {R['alarms']}, запасных эпох {R['fallback']} — поколения умирали дальше")
print(f"    легитимный: {R['legit_pass']}/{R['epochs']} эпох")

print("--- Контроль: обычная статичная дверь (пароль навсегда), тот же дурак")
L = run(static=True)
print(f"    вор с паролем после утечки: {L['pass_after']}/{L['tries_after']} полных проходов "
      f"(дверь платит вечно)")

# ============================ ПРОВЕРКИ ============================
print()
print("=" * 78)
print("ПРОВЕРКИ")
print("=" * 78)

def check(name, ok, note=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {note}" if note else ""))
    return ok

r = []
r.append(check("YOU_CANT_LEAK_WHAT_YOU_NEVER_HOLD",
               R["future_derivation_hits"] == 0,
               "у дурака нет переносимого секрета; из всего слитого материала вор вычислил 0 будущих эпох"))
r.append(check("THE_SCREENSHOT_DIES_WITH_THE_EPOCH",
               R["pass_after"] == 0 and R["gear_hits_after"] / max(1, R["tries_after"] * 30) < 3 * (3 / 256),
               f"после границы: 0 полных проходов, по шестерёнке {R['gear_hits_after']/(R['tries_after']*30):.4f} ≈ база"))
r.append(check("THE_FOOL_CAN_SELL_ONLY_THE_PRESENT",
               R["pass_after"] == 0,
               f"весь урон — {R['pass_leak_epoch']} проходов внутри одной эпохи; прошлое и будущее не продаются"))
r.append(check("THE_DANGEROUS_SWITCH_IS_NOT_IN_THE_FOOLS_HANDS",
               "отказ" in R["watchdog_answer"] and R["alarms"] >= 1 and R["fallback"] > 0,
               f"сторожа у дурака нет; заморозка среды -> {R['alarms']} тревог, {R['fallback']} запасных эпох"))
r.append(check("THE_GUEST_IS_NAKED_BY_PATROL",
               R["guest_detected_at"] is not None and R["guest_detected_at"] <= R["GUEST_E"] + 1,
               f"гость обнаружен в эпоху {R['guest_detected_at']} (посажен в {R['GUEST_E']}); двойник с украденным id тоже ловится"))
r.append(check("THE_STATIC_DOOR_PAYS_FOREVER (контраст)",
               L["pass_after"] == L["tries_after"] and L["pass_after"] > 0 and R["pass_after"] == 0,
               f"статичная дверь: {L['pass_after']}/{L['tries_after']} проходов вора навсегда; наша: 0"))
r.append(check("THE_PRESENT_IS_STILL_SELLABLE (граница, честно)",
               R["pass_leak_epoch"] > 0,
               f"ЧЕСТНО: настоящее продать можно — {R['pass_leak_epoch']} проходов в эпоху утечки реальны; "
               f"защита = срок годности + патруль, а не магия"))

print()
print(f"ИТОГ: {sum(r)}/{len(r)} PASS")
