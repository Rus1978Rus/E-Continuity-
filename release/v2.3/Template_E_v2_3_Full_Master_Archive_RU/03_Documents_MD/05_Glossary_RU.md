# Template E v2.3

_Glossary RU / канонический словарь_

## Назначение словаря

Словарь фиксирует канонические термины Template E v2.3. Термин допускается в ядро только если помогает ответить: что сохраняется, какая mission, какой уровень recoverability, кто отвечает, кто умеет восстановить, какие зависимости есть, как проверяется, где failure и какая mitigation.

## Core Glossary

| Term | Definition |
| --- | --- |
| Template E | инженерный framework управляемой recoverability объектов, mission и capabilities через время |
| E-system | система, построенная для сохранения recoverability на заданном уровне |
| Continuity | непрерывность цепи, позволяющей объекту/знанию/навыку/mission оставаться recoverable |
| Recoverability | возможность вернуть объект, функцию, навык или mission к заданному уровню использования |
| Mission | целевая функция, ради которой объект, система или capability сохраняется |
| Capability | воспроизводимая способность выполнять mission |
| Continuity Chain | цепь объектов, документов, форматов, людей, институтов и зависимостей |
| Custody | ответственность за объект, документ, образец, технологию или capability |
| Orphan Documentation | документация без владельца, successor, статуса и review cycle |
| Institutional Recovery Custodian | процедура/институт восстановления custody при потере людей |
| Proof Testing | проверка recoverability через учебный или реальный тест восстановления |
| Migration Governance | управляемая система миграции с проверками, журналами, rollback и audit |
| Dependency Depth | число критических слоёв, нужных для recoverability |
| Continuity Debt | накопленный риск из-за отложенного обслуживания continuity |
| Managed Sunset | управляемый вывод технологии из массового применения с сохранением legacy recoverability |
| Skill Extinction Risk | риск исчезновения навыка как operational capability |
| Legacy Dependency Pressure | степень зависимости старых систем от уходящей capability |
| Material Viability Window | окно структурной пригодности материала/компонента |
| Mission Phase Transition | переход объекта из одной mission в другую |
| Reconstructive Recoverability | возможность частичной реконструкции функции/смысла по источникам |

## Terms to avoid

| Не использовать | Почему |
| --- | --- |
| вечное хранение | ложное обещание |
| бессмертие | уводит в метафизику |
| дух цивилизации | неоперационально |
| судьба народа | слишком широко и непроверяемо |
| объект сохранился - значит всё сохранено | смешивает physical и mission recoverability |
| полностью восстановимо | без уровня recoverability и proof test некорректно |
| архив всего | без mission это data hoarding |
| точная вероятность выживания | fake precision |

## Preferred language

- Вместо “объект сохранился” писать: “объект сохранил physical recoverability, но mission recoverability требует проверки”.
- Вместо “знание сохранилось” писать: “сохранены носитель, representation information, operator path и proof-tested interpretability”.
- Вместо “профессия исчезает” писать: “capability chain показывает высокий Skill Extinction Risk из-за decline training pipeline, operator aging и tooling loss”.

---

# v2.3 Glossary Additions

## v2.3 Glossary Additions

| Term | Definition |
| --- | --- |
| Static Integrity | состояние, при котором объект выглядит целым и стабильным без рабочей нагрузки |
| Dynamic Recoverability | способность объекта выдержать рабочую нагрузку, давление, циклы, нагрев, вибрацию или среду возврата |
| Activation Failure | отказ, проявляющийся в момент возврата dormant system к нагрузке |
| Dynamic Proof Test | проверка объекта под controlled operational load до заявления functional/mission recoverability |
| Dynamic Recoverability Risk | риск того, что static preserved system провалит dynamic return из-за скрытой деградации материалов, уплотнений, соединений или рабочих сред |


## v2.3 Stabilization Terms

| Term | Definition |
| --- | --- |
| Static Integrity | сохранность объекта в покое: визуальная целостность, наличие, static hold |
| Dynamic Recoverability | способность выдержать рабочую нагрузку при возврате из dormant state |
| Mission Proof Test | проверка, что система выполняет целевую mission в рабочем сценарии |
| Activation Failure | отказ, который проявляется при возврате к нагрузке, а не во время хранения |
| MVW Status | статус доказанной пригодности материала: MVW-0...MVW-5 |
| Dynamic Return-to-Service Gate | обязательная проверка перед operational или mission recoverability claim |
| Static Proof | проверка существования/целостности в покое |
| Dynamic Proof | проверка под нагрузкой, циклом, давлением, движением, thawing, build или запуском |
