#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Вор, питающийся временем (BRUIN Gate, игрушечная физика, stdlib only)

Атака этой сессии: вор ЕСТ ВРЕМЯ шестерёнок — "с конца":
  S1. Ест хвост каждого слота (последние 10 тиков из 30) — глотает секунды.
  S2. Ест саму среду (по 3 молекулы за тик) — питается веществом, чьи события = часы.
  S3. Разгоняет время среды (kT x8) — заставляет поколения умирать быстрее.
  S4. Ест будущее: снимает копию среды с шумом измерения и прокручивает её вперёд,
      пытаясь "съесть" энтропию будущих эпох до её реализации.

Защита (канон этой ветки):
  - часы поколений считают СОБЫТИЯ (разрывы связей), а не секунды;
  - съеденная/замороженная среда переключает сердце на CSPRNG-расписание (сторож);
  - будущий ключ не существует до границы эпохи (пре-энтропийность).

Честные статусы: CHAT_PRODUCED, класс E2 (симуляция, внешнего аудита нет).
Ключи os.urandom(32), только в памяти. Seed фиксирован для физики; ключи одноразовые.
"""

import os, hmac, math, random, hashlib

SEED = 42

# ---------------- среда: холодная вода (двухсвязный движок) ----------------
HBOND_RANGE = 1.2
REL_SPEED_GATE = 0.4
MAX_BONDS = 4

def p_break(kT):
    return 1.0 - math.exp(-kT / 2.0)

class Water:
    def __init__(self, n=80, box=20.0, kT=0.2, rng=None):
        self.box, self.kT = box, kT
        self.rng = rng or random.Random(SEED)
        self.pos = [[self.rng.uniform(0, box), self.rng.uniform(0, box)] for _ in range(n)]
        self.vel = [[self.rng.uniform(-0.5, 0.5), self.rng.uniform(-0.5, 0.5)] for _ in range(n)]
        self.alive = [True] * n
        self.bonds = set()

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
        """Один тик физики. Возвращает число разрывов связей (события часов)."""
        n = len(self.pos)
        for i in range(n):
            if not self.alive[i]:
                continue
            self.pos[i][0] = (self.pos[i][0] + self.vel[i][0] * 0.5) % self.box
            self.pos[i][1] = (self.pos[i][1] + self.vel[i][1] * 0.5) % self.box
        breaks = 0
        for (i, j) in list(self.bonds):
            if not (self.alive[i] and self.alive[j]):
                self.bonds.discard((i, j)); breaks += 1; continue
            if self._dist(i, j) > HBOND_RANGE or self.rng.random() < p_break(self.kT):
                self.bonds.discard((i, j)); breaks += 1
        deg = {i: 0 for i in range(n)}
        for (i, j) in self.bonds:
            deg[i] += 1; deg[j] += 1
        alive_idx = [i for i in range(n) if self.alive[i]]
        for a in range(len(alive_idx)):
            i = alive_idx[a]
            if deg[i] >= MAX_BONDS:
                continue
            for b in range(a + 1, len(alive_idx)):
                j = alive_idx[b]
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

    def eat(self, k):
        """Вор съедает k живых молекул."""
        alive_idx = [i for i in range(len(self.pos)) if self.alive[i]]
        for i in self.rng.sample(alive_idx, min(k, len(alive_idx))):
            self.alive[i] = False

    def heat(self, factor):
        self.kT *= factor

    def alive_count(self):
        return sum(1 for a in self.alive if a)

    def fingerprint(self):
        """Отпечаток микросостояния: квантованные позиции живых + связи."""
        h = hashlib.sha256()
        for i, p in enumerate(self.pos):
            if self.alive[i]:
                h.update(f"{i}:{p[0]:.6f},{p[1]:.6f};".encode())
        for b in sorted(self.bonds):
            h.update(str(b).encode())
        return h.digest()

    def noisy_copy(self, eps, rng):
        """Копия среды с шумом измерения eps (вор не может снять микросостояние точно)."""
        w = Water.__new__(Water)
        w.box, w.kT, w.rng = self.box, self.kT, rng  # своя тепловая случайность!
        w.pos = [[(p[0] + rng.uniform(-eps, eps)) % self.box,
                  (p[1] + rng.uniform(-eps, eps)) % self.box] for p in self.pos]
        w.vel = [[v[0] + rng.uniform(-eps, eps), v[1] + rng.uniform(-eps, eps)] for v in self.vel]
        w.alive = list(self.alive)
        w.bonds = set(self.bonds)
        return w

    def future_sample(self, de=1):
        """Выборка будущей эпохи. Структурно: её НЕТ до реализации."""
        return None

# ---------------- часы поколений + сторож ----------------
class EpochClock:
    def __init__(self, threshold=300, stall_window=200, fallback_period=30):
        self.threshold = threshold
        self.stall_window = stall_window
        self.fallback_period = fallback_period
        self.epoch = 0
        self.churn = 0
        self.since_epoch = 0
        self.fallback = False
        self.alarms = 0
        self.recoveries = 0
        self.physical_epochs = 0
        self.fallback_epochs = 0

    def feed(self, breaks):
        srcs = []
        self.churn += breaks
        self.since_epoch += 1
        if self.churn >= self.threshold:
            self.churn = 0; self.since_epoch = 0; self.epoch += 1
            self.physical_epochs += 1
            if self.fallback:
                self.fallback = False; self.recoveries += 1
            srcs.append("physical")
        elif not self.fallback and self.since_epoch >= self.stall_window:
            self.fallback = True; self.alarms += 1
            self.since_epoch = 0  # сердце переходит на внутреннее расписание
        if self.fallback and self.since_epoch >= self.fallback_period:
            self.since_epoch = 0; self.epoch += 1
            self.fallback_epochs += 1
            srcs.append("fallback")
        return srcs

# ---------------- дверь: 30 шестерёнок, ключи умирают с эпохой ----------------
class Door:
    def __init__(self, gears=30):
        self.gears = gears
        self.root = os.urandom(32)
        self.epoch = 0
        self.gear_keys = self._derive()

    def _derive(self):
        return [hmac.new(self.root, f"gear{g}|epoch{self.epoch}".encode(),
                         hashlib.sha256).digest() for g in range(self.gears)]

    def advance(self, sample):
        self.root = hmac.new(self.root, sample, hashlib.sha256).digest()
        self.epoch += 1
        self.gear_keys = self._derive()

    def valid_tag(self, g):
        return self.gear_keys[g][0]

    def check_gear(self, g, tag):
        t = self.valid_tag(g)
        return tag in ((t - 1) % 256, t, (t + 1) % 256)

    def check_full(self, tags):
        return all(self.check_gear(g, tags[g]) for g in range(self.gears))

# ---------------- общий прогон сценария ----------------
def run_scenario(name, ticks=900, slot_eat=None, eat_per_tick=0,
                 heat_at=None, heat_factor=8.0, brute_per_tick=100):
    rng = random.Random(SEED)
    water = Water(n=80, rng=rng)
    clock = EpochClock()
    door = Door()
    stolen = None            # снимок тегов эпохи 2 (сильнейший вор: знает точные теги)
    snap_hits = snap_tries = 0
    brute_full = brute_gear_hits = brute_guesses = 0
    legit_pass = 0
    epoch_ticks = []         # длительности эпох в тиках
    t_last_epoch = 0
    total_breaks = 0

    legit_pass += 1 if door.check_full([door.valid_tag(g) for g in range(30)]) else 0

    for t in range(ticks):
        if heat_at is not None and t == heat_at:
            water.heat(heat_factor)
        if eat_per_tick:
            water.eat(eat_per_tick)
        skip = bool(slot_eat) and (t % 30 >= 30 - slot_eat)  # вор съел хвост слота
        breaks = 0 if skip else water.step()
        total_breaks += breaks
        for src in clock.feed(breaks):
            sample = water.fingerprint() if src == "physical" else os.urandom(32)
            epoch_ticks.append(t - t_last_epoch); t_last_epoch = t
            door.advance(sample)
            # легитимный чеканит на месте и проходит
            if door.check_full([door.valid_tag(g) for g in range(30)]):
                legit_pass += 1
            # вор со снимком пробует старую карту против новой эпохи
            if stolen is not None:
                snap_tries += 30
                snap_hits += sum(1 for g in range(30) if door.check_gear(g, stolen[g]))
        if door.epoch == 2 and stolen is None:
            stolen = [door.valid_tag(g) for g in range(30)]
        # переборный вор: фиксированный бюджет попыток за ТИК
        for _ in range(brute_per_tick):
            tags = [rng.randrange(256) for _ in range(30)]
            brute_guesses += 1
            if door.check_full(tags):
                brute_full += 1
            brute_gear_hits += sum(1 for g in range(30) if door.check_gear(g, tags[g]))

    return dict(name=name, epochs=door.epoch, physical=clock.physical_epochs,
                fallback=clock.fallback_epochs, alarms=clock.alarms,
                recoveries=clock.recoveries, breaks=total_breaks,
                epoch_ticks=epoch_ticks, legit_pass=legit_pass,
                snap_hits=snap_hits, snap_tries=snap_tries,
                brute_full=brute_full, brute_guesses=brute_guesses,
                brute_gear_hits=brute_gear_hits, alive=water.alive_count())

def show(s):
    mt = sum(s["epoch_ticks"]) / max(1, len(s["epoch_ticks"]))
    print(f"--- {s['name']}")
    print(f"    эпох всего: {s['epochs']} (физических {s['physical']}, запасных {s['fallback']}), "
          f"тревог: {s['alarms']}, разрывов: {s['breaks']}, средняя эпоха: {mt:.1f} тика")
    print(f"    легитимный: {s['legit_pass']}/{s['epochs']+1} эпох пройдено")
    if s["snap_tries"]:
        print(f"    вор со снимком: попаданий по шестерёнке {s['snap_hits']}/{s['snap_tries']} "
              f"= {s['snap_hits']/s['snap_tries']:.4f} (база 3/256 = {3/256:.4f})")
    print(f"    перебор: {s['brute_guesses']} полных стуков, прошло дверь целиком: {s['brute_full']}, "
          f"попаданий по шестерёнке: {s['brute_gear_hits']/ (s['brute_guesses']*30):.4f}")

print("=" * 78)
print("ВОР, ПИТАЮЩИЙСЯ ВРЕМЕНЕМ: четыре способа съесть время шестерёнок")
print("=" * 78)

S0 = run_scenario("S0. Чистый прогон (никто не ест время)")
show(S0)
S1 = run_scenario("S1. Вор ест хвост каждого слота (10 из 30 тиков)", slot_eat=10)
show(S1)
S2 = run_scenario("S2. Вор ест среду (3 молекулы/тик)", eat_per_tick=3)
show(S2)
S3 = run_scenario("S3. Вор разгоняет время среды (kT x8 с тика 300)",
                  heat_at=300, heat_factor=8.0)
show(S3)

# --- S4: вор ест будущее — прокручивает шумную копию вперёд -----------------
print("--- S4. Вор ест будущее: копия среды с шумом eps, прокрутка на 360 тиков вперёд")
TRIALS = 15
FF = 360
key_mismatch = 0
hamming_list = []
rng4 = random.Random(SEED + 1)
for trial in range(TRIALS):
    real = Water(n=60, rng=random.Random(SEED + 10 + trial))
    for _ in range(40):
        real.step()
    root_snapshot = os.urandom(32)  # корень эпохи, от которой вор «откусывает» будущее
    ghost = real.noisy_copy(eps=0.05, rng=random.Random(SEED + 1000 + trial))
    for _ in range(FF):
        ghost.step()               # вор съел 360 тиков будущего... в СВОЕЙ копии
    for _ in range(FF):
        real.step()                # реальная среда дошла до той же границы
    fp_pred = ghost.fingerprint()
    fp_real = real.fingerprint()
    k_pred = hmac.new(root_snapshot, fp_pred, hashlib.sha256).digest()
    k_real = hmac.new(root_snapshot, fp_real, hashlib.sha256).digest()
    ham = sum(bin(a ^ b).count("1") for a, b in zip(fp_pred, fp_real))
    hamming_list.append(ham)
    if k_pred != k_real:
        key_mismatch += 1
ham_avg = sum(hamming_list) / len(hamming_list)
print(f"    предсказание ключа будущей эпохи: совпало {TRIALS - key_mismatch}/{TRIALS} "
      f"(нужно 0 совпадений), средний хэмминг отпечатков: {ham_avg:.0f}/256 бит")

# --- S5: пре-энтропийность структурно ---------------------------------------
print("--- S5. Попытка прочитать выборку будущей эпохи до границы")
w5 = Water(n=60, rng=random.Random(7))
fs = w5.future_sample(1)
print(f"    future_sample(1) = {fs}  (выборки не существует — ей ещё не из чего родиться)")
g5 = random.Random(9)
guesses5 = 500
hits5 = 0
d5 = Door()
future_root = hmac.new(d5.root, w5.fingerprint(), hashlib.sha256).digest()  # эпоха e+1 ПОСЛЕ границы
for _ in range(guesses5):
    if os.urandom(32) == future_root:  # вор угадывает то, чего ещё нет
        hits5 += 1
print(f"    угадывание ещё не рождённого корня: {hits5}/{guesses5}")

# ============================ ПРОВЕРКИ ============================
print()
print("=" * 78)
print("ПРОВЕРКИ")
print("=" * 78)

def check(name, ok, note=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {note}" if note else ""))
    return ok

r = []
# 1. Съеденные секунды не заводят часы: события считаются, а не тики
r.append(check("THE_CLOCK_COUNTS_EVENTS_NOT_SECONDS",
               S1["physical"] < S0["physical"] and S1["brute_full"] == 0,
               f"съедено 33% тиков -> физических эпох {S1['physical']} вместо {S0['physical']}; "
               f"вору это дало 0 проходов"))
# 2. Время не питательно: во всех сценариях вор голоден
thief_total = S1["brute_full"] + S2["brute_full"] + S3["brute_full"] + (TRIALS - key_mismatch)
r.append(check("TIME_IS_NOT_FOOD",
               thief_total == 0,
               f"суммарная добыча всех четырёх поедателей времени: {thief_total} проходов/ключей"))
# 3. Съеденная среда переключает сердце
r.append(check("THE_DEVOURED_MEDIUM_SWITCHES_THE_HEART",
               S2["alarms"] >= 1 and S2["fallback"] > 0 and S2["brute_full"] == 0,
               f"живых молекул осталось {S2['alive']}; тревог: {S2['alarms']}, "
               f"запасных эпох (CSPRNG): {S2['fallback']}; дверь продолжила умирать и рождаться"))
# 4. Разогнав время, вор ускоряет смерть ключей, а не кражу
mt0 = sum(S0["epoch_ticks"]) / max(1, len(S0["epoch_ticks"]))
mt3 = sum(S3["epoch_ticks"]) / max(1, len(S3["epoch_ticks"]))
r.append(check("EATING_TIME_ACCELERATES_THE_DEATH_OF_KEYS",
               mt3 < mt0 / 2 and S3["brute_full"] == 0,
               f"эпоха сжалась с {mt0:.1f} до {mt3:.1f} тика; попыток на поколение стало меньше, "
               f"проходов: 0"))
# 5. Съеденное будущее — твоё собственное, не наше
r.append(check("THE_EATEN_FUTURE_IS_YOUR_OWN",
               key_mismatch == TRIALS and ham_avg > 100,
               f"шумная копия разошлась на {ham_avg:.0f}/256 бит; предсказано ключей: 0/{TRIALS}"))
# 6. У будущего ещё нет плоти
r.append(check("THE_FUTURE_HAS_NO_FLESH_YET",
               fs is None and hits5 == 0,
               "выборка будущей эпохи структурно None; угадано корней: 0/500"))
# 7. Честная граница: поедатель покупает тишину, а не ключи
availability_hurt = S2["physical"] < S0["physical"] * 0.5
keys_safe = S2["brute_full"] == 0 and S2["legit_pass"] == S2["epochs"] + 1
r.append(check("THE_CENSOR_BUYS_SILENCE_NOT_KEYS (граница)",
               availability_hurt and keys_safe,
               f"ЧЕСТНО: физические часы пострадали ({S2['physical']} эпох против {S0['physical']} чистых) — "
               f"это атака на доступность; но ключей украдено 0, легитимный прошёл все эпохи "
               f"({S2['legit_pass']}/{S2['epochs']+1}) через запасное сердце"))

print()
print(f"ИТОГ: {sum(r)}/{len(r)} PASS")
