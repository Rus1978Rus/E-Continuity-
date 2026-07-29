# E-Continuity v2.3 — публичный canonical package

Это содержательное ядро v2.3, восстановленное из переданного автором пакета
`Template_E_v2_3_Full_Master_Archive_RU.zip`.

Историческое имя `Template E` сохранено внутри файлов для доказательной
целостности. Активное имя проекта — **E-Continuity / Фреймворк управляемой
восстановимости**. Планируемая v2.3.1 должна выполнить контролируемый
rename-only переход и не менять методологическое содержание.

## Статус

- `CURRENT_CONTENT_PACKAGE`
- не Gold Master;
- не отраслевой стандарт;
- не подтверждённая независимая научная или инженерная валидация;
- CASE-SPACE-001 сохраняет статус C-3/C-4 candidate;
- MVW сохраняет статус operational metric v0.1.

## Лицензия

Непрограммные материалы распространяются по CC BY-NC-ND 4.0 согласно
корневому `LICENSE-MATERIALS.md`. Код и скрипты — согласно
`LICENSE-CODE.md`.

## Контроль происхождения

Исходный внешний контейнер:
`01_CURRENT_V2_3_RELEASE_AND_REVIEWER_PACKAGES.zip`.

Вложенный canonical package:
`Template_E_v2_3_Full_Master_Archive_RU.zip`.

SHA-256 вложенного ZIP:
`817f94365620abf4fe5dbd6507524853046169e145bce5e18bb4e44308f156d7`.

Файлы опубликованы как извлечённое содержимое canonical ZIP; служебные
`__MACOSX`/AppleDouble записи исключены.

## Пострелизные редакционные изменения

2026-07-29 — редакционная интеграция в MD-источниках, без изменения
методологического содержания:

- `03_Documents_MD/01_Full_Technical_Edition_RU.md`: канонической объявлена
  компактная 5-блочная формула (раздел 3); расширенная 13-компонентная
  формула перенесена в Appendix A с мэппингом на блоки. Закрывает
  внутреннее противоречие трёх конкурирующих core formula (AR-008).
- `03_Documents_MD/08_References_RU.md`: добавлен Standards & Adjacent
  Fields Addendum — мэппинг на IEC 62402/DMSMS, ISO 22301, ISO 31000,
  IAEA NKM, NDSA Levels, DPC RAM, CoreTrustSeal (M-015).

SHA-256 исходного canonical ZIP выше остаётся исторической привязкой
переданного пакета. DOCX/PDF-слои соответствуют исходному ZIP и до
пересборки в v2.3.1 отстают от MD; source of truth — Markdown-файлы.
Полный diff изменений — в git history.

