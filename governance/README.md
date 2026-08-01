GOVERNANCE / слой управления проектом
Project: E-Continuity / Фреймворк управляемой восстановимости
Created: 2026-07-30

Назначение папки: единое место для правил, guard-ов, реестров и очередей,
которые раньше жили только в локальной среде автора.

Состав:
- CURRENT_RULES_GUARDS_PATCHES_REGISTER_RU.txt — свод активных правил и guard-ов.
- PENDING_INTEGRATION_QUEUE_RU.txt — очередь внедрения (10 пунктов).
- CONVEYOR_AND_REVIEW_LOG_RU.txt — журнал ревью/конвейера.
- ILLUSTRATIVE_OBSERVATIONS_REGISTER_RU.txt — реестр иллюстративных наблюдений.
- GLOSSARY_ADDENDUM_RU.txt — дополнение к глоссарию (8 терминов).
- AI_INTERPRETER_GOVERNANCE_GUARD_v0_1_RU.md — guard управления AI-операциями
  (статус: PROPOSED / PENDING_INTEGRATION; интеграция после v2.3.1).
- REJUVENATION_LOOP_SOP_v0_1_RU.md — SOP петли омоложения: триггеры T-INT/T-EXT,
  обязательный gate воспроизведения, запрет самоустановки
  (статус: v0.1 / PROPOSED / CHAT_PRODUCED; интеграция — решением автора).
- CASE_SOFT_001_BRUINGATE_PILOT_RU.md — первый пилот фреймворка: BRUINGate оценён
  на MVW-4 с выполненным proof test; найденные пробелы задокументированы
  (статус: PILOT / CHAT_PRODUCED, 2026-07-30).

Правило: эта папка — рабочая зона управления; изменения правил проходят
PERMANENT_RULE_PREFLIGHT_GUARD_v0_1.
