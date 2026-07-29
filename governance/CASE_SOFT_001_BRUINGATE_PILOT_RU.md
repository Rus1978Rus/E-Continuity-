CASE-SOFT-001
Project: E-Continuity / Фреймворк управляемой восстановимости
Created: 2026-07-30
Status: PILOT_CASE / CHAT_PRODUCED / NOT_EXTERNAL_VERIFIED / DYNAMIC_PROOF_EXECUTED
Maturity: C-2/C-3 candidate (proof test выполнен реально, но AI-ассистентом, не независимым рецензентом)

ЧАСТНЫЙ АВТОРСКИЙ ПРОЕКТ / COMMERCIAL USE PROHIBITED
Author-owner: Руслан Малявский.

====================================================================
CASE TEMPLATE
====================================================================

Case ID: CASE-SOFT-001
Name: BRUINGate — восстановимость программного репозитория (первый пилот MVW)
Domain: software / open-source repository
Case Type: pilot assessment (пилотная оценка по Software Continuity SOP)

Original Mission:
  Эшелонированный stateless-фильтр трафика (de Bruijn locator +
  slot-bound HMAC tag): executable continuity + interpretability.

Current Mission:
  То же + defensive publication (prior art фиксация от 2026-07-29,
  коммит 1f7b02f).

Continuity Chain:
  OBJECT (код, документы, тесты)
  → ANCHOR (README, SPEC, TECHNICAL_REVIEW, CITATION.cff)
  → MEMORY_SYSTEM (GitHub git, публичный репозиторий)
  → INTERPRETER (Python 3.12 stdlib, pytest, человек-читатель MD)
  → RECOVERY (clone → install pytest → pytest → python -m src.simulate)

Failure Modes (таксономия):
  - Static Integrity: ОК (все файлы на месте, LICENSE добавлен).
  - Activation Failure: ПОДТВЕРЖДЁН ЖИВЬЁМ (см. находку N1).
  - Interface Confusion Failure: риск зафиксирован (две команды запуска,
    одна молча не работает).
  - Custody: единственный maintainer, successor не назначен.

====================================================================
DYNAMIC PROOF TEST — ВЫПОЛНЕН ФАКТИЧЕСКИ
====================================================================

Среда: чистая (Linux, Python 3.12.12, свежая установка pytest 9.1.1),
без доступа к истории автора. Источник: tarball main @ 2026-07-30.

| Шаг SOP | Команда | Результат |
|---|---|---|
| clean build | распаковка tarball, stdlib only | ОК, зависимостей нет |
| tests | `python3 -m pytest tests/ -v` | **9/9 passed** (+3 subtests) |
| sample output | `python3 -m src.simulate` | числа совпали с заявленными: вход 100154; отброшено 97500+2487; дошло 167 (154+13); 99.83% / 99.987%; ожидалось ≈9.77 |

Вывод proof test: заявленные метрики воспроизводимы внешней стороной
(в рамке CHAT_PRODUCED — не независимой лабораторией).

====================================================================
MVW STATUS
====================================================================

- MVW-0 unknown — пройдено
- MVW-1 visually intact — пройдено (репозиторий открывается, README читается)
- MVW-2 static inspection — пройдено (структура, лицензия, CITATION, secrets нет)
- MVW-3 material inspection — пройдено (код читается, stdlib only, тесты покрывают ядро)
- MVW-4 dynamic proof passed — **ДОСТИГНУТО 2026-07-30** (clean env: 9/9 tests + sample output)
- MVW-5 mission load proof — НЕ достигнуто (боевой трафик не фильтровался)

Selected status: **MVW-4 (dynamic proof passed)**

Allowed Recoverability Claim:
- Physical / evidential only: превышено
- Static integrity: подтверждено
- Limited dynamic readiness: подтверждено
- Dynamic recoverability: **подтверждено на уровне артефакта**
- Mission recoverability: НЕ заявляется (нет proof на уровне сервиса
  и нет custody/successor — цепочка держится на одном человеке)

====================================================================
НАХОДКИ ПИЛОТА (ценность proof test)
====================================================================

N1. ACTIVATION FAILURE — подтверждён живьём.
  `python3 src/simulate.py` → ImportError (относительный импорт).
  `python3 -m src.simulate` → работает.
  «Программа существует» ≠ «программа запускается очевидной командой».
  Лечится одним файлом RUN.md — без него интерпретатор спотыкается
  на первом же шаге.

N2. Interpreter Continuity — частичная.
  Нет: BUILD.md, RUN.md, DEPENDENCIES.lock, TESTS.md
  (обязательные файлы по Software Continuity SOP — отсутствуют 4 из 5;
  есть только README и LICENSE).
  Сильная сторона: stdlib only → dependency map тривиален; plain MD
  читается без спецсофта. Это по формуле проекта — «тривиально
  пересобираемый интерпретатор».

N3. Custody — отказный режим «один человек».
  Successor не назначен; если current holder исчезнет (чек-лист, вопрос
  13), цепочка рвётся на custody, а не на технологии.

N4. Runtime не задекларирован.
  Код использует встроенные generics (set[tuple]) → требуется Python ≥3.9;
  в документах это не записано.

====================================================================
РЕКОМЕНДУЕМЫЙ ПАТЧ (кандидаты, selection gate за автором)
====================================================================

P1. RUN.md (3 строки): `pip install pytest` / `python3 -m pytest tests/`
  / `python3 -m src.simulate` + требование Python ≥3.9. Закрывает N1, N4.
P2. TESTS.md: как запускать, что покрыто (9 тестов), что нет.
P3. DEPENDENCIES.lock: `pytest>=8` — единственная внешняя зависимость,
  и та для тестов, не для рантайма. Зафиксировать.
P4. Successor-строка в README или CITATION.cff (даже «TBD» честнее,
  чем отсутствие вопроса).
P5. После P1–P3: повторный proof test независимой стороной → кандидат
  на повышение доверия к MVW-4 без оговорки CHAT_PRODUCED.

====================================================================
LESSON FOR FRAMEWORK
====================================================================

1. MVW-шкала легла на software без искажений: MVW-4 достижим за один
   proof test; MVW-5 требует миссии (боевой трафик), а не среды.
2. Proof test за 15 минут нашёл реальный Activation Failure, который
   статический осмотр не видел: репозиторий выглядел «прибранным»,
   но стандартная команда запуска падала. Это прямая иллюстрация ядра
   фреймворка: видимость сохранности ≠ доказанная восстановимость.
3. Software SOP работает как чек-лист: 4 из 5 обязательных файлов
   отсутствовали при внешне «готовом» репозитории.

Reviewer Questions:
- MVW-4, выполненный AI-ассистентом, — какой maturity присваивать:
  C-2 (chat-provided) или допустимо C-3 при воспроизводимых логах?
- Нужен ли для software подуровень MVW-4.5 «proof независимой стороной»?

Evidence / Sources:
- https://github.com/Rus1978Rus/BRUINGate @ main, 2026-07-30
- Лог pytest: 9 passed, 3 subtests passed, 0.08s
- Лог simulate: seed 2; 100154; 97500; 2487; 167; 99.83%; 99.987%; 9.77
- Software Continuity SOP, MVW Assessment Template v0.1 (E-Continuity v2.3)

====================================================================
END
====================================================================
