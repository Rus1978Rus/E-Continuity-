# Template E v2.3

_Operational SOP Pack RU / практические протоколы_

## Назначение SOP Pack

Этот документ переводит Template E из conceptual framework в executable procedures. Каждый SOP должен иметь mission, critical assets, dependency map, custody rules, proof testing, migration rules, emergency recovery, successor procedure.

## Universal Continuity Audit Checklist

1. Какая mission должна быть recoverable?
2. Что является object?
3. Есть ли metadata?
4. Есть ли recovery protocol?
5. Есть ли current custodian?
6. Есть ли successor?
7. Есть ли operator layer?
8. Есть ли tools/materials?
9. Есть ли dependency map?
10. Проводился ли proof test?
11. Есть ли risk register?
12. Есть ли managed sunset, если технология уходит?
13. Что произойдёт, если current holder исчезнет?
14. Что произойдёт, если формат/оборудование устареет?
15. Какой уровень recoverability реально заявляется?

## Archive Continuity SOP

| Раздел | Требование |
| --- | --- |
| Mission | retrieval + readability + interpretability |
| Critical assets | documents, metadata, finding aids, provenance records |
| Proof testing | новый пользователь находит и интерпретирует документ |
| Review | metadata audit yearly, custody review yearly, format review every 3 years |
| Emergency | freeze deletion, emergency inventory, temporary custodian, duplicate metadata |

## Software Continuity SOP

| Раздел | Требование |
| --- | --- |
| Mission | executable continuity |
| Critical assets | source, dependencies, build system, runtime, tests, configs |
| Required files | README, BUILD.md, RUN.md, DEPENDENCIES.lock, TESTS.md, LICENSE |
| Proof testing | clean build + tests + sample output |
| Mitigation | lockfiles, containers/VM, reproducible builds, dependency mirrors, successor maintainer |

## Biobank Continuity SOP

| Раздел | Требование |
| --- | --- |
| Mission | biological usability + provenance + interpretability |
| Critical assets | samples, metadata, consent, SOP, cryostorage, chain of custody |
| Proof testing | witness aliquot thawing + viability/QC + metadata check |
| Emergency | freezer failure transfer protocol, temperature exposure log, viability assessment |
| Rule | sample without metadata/SOP/custody is not full recoverable object |

## NII Shutdown & Transfer SOP

| Шаг | Действие |
| --- | --- |
| 1 | freeze disposal / остановить уничтожение и хаотичный вывоз |
| 2 | full inventory / инвентаризация документации, образцов, оборудования |
| 3 | critical knowledge package classification |
| 4 | temporary custodian + successor institution |
| 5 | technical interviews + tacit knowledge capture |
| 6 | document-equipment map |
| 7 | custody transfer act |
| 8 | future review date |

## Military / Operational Asset Storage SOP

| Раздел | Требование |
| --- | --- |
| Mission | operational readiness or component recoverability |
| Critical layers | platform, engine, electronics, spare parts, documentation, operators, logistics |
| Material tracking | Material Viability Window for critical components |
| Proof testing | engine start, mobility, component, safety, compatibility tests |
| Donor strategy | controlled donor continuity if full operational return impossible |

## Managed Sunset SOP

| Шаг | Действие |
| --- | --- |
| 1 | assess installed base / legacy dependency |
| 2 | evaluate remaining life and failure consequence |
| 3 | define minimum operator reserve |
| 4 | archive tools/materials/specifications |
| 5 | capture tacit knowledge |
| 6 | assign custodian and successor |
| 7 | choose CP class: CP-0 to CP-6 |
| 8 | schedule review and proof practice |

## Capability Preservation Playbook

| Status | Action |
| --- | --- |
| Stable | monitor, registry entry, light review |
| Watch | interviews, training review, installed base assessment |
| At Risk | SOP, tools/materials list, proof practice, custodian |
| Critical | emergency tacit capture, video, tools archive, minimal training module |
| Crisis | save core recoverability, last-operator interview, reconstruction notes |
| Reconstructive | source gathering, artifact analysis, confidence labels |
| Lost | record limits, separate facts from hypotheses, evidential only |

---

# Dynamic Proof Testing SOP

## v2.3 Operational Patch — Dynamic Proof Testing SOP

Для dormant dynamic systems требуется отдельный dynamic proof testing layer. Static inspection не является достаточным основанием для mission recoverability claim.

| Risk factor | Required check |
| --- | --- |
| Elastomers / seals | age, elasticity, cracks, pressure-cycle test or replacement |
| Lubricants / greases | chemical stability, viscosity, contamination, replacement schedule |
| Pressure circuits | low-pressure leak test before full load |
| Propellant / aggressive residues | internal inspection, corrosion risk assessment |
| Hydraulics | cycle test under controlled load |
| Welded / brazed joints | NDT where feasible, pressure proof test |
| Electronics / capacitors | burn-in/load test, not only power-on self-test |
| Mission claim | must pass mission-relevant dynamic test or be downgraded to evidential/reconstructive recoverability |

Rule: visible integrity != structural viability; static proof != dynamic proof; dynamic proof != mission proof.


## Dynamic Return-to-Service Gate v2.3

Для dormant dynamic systems static inspection is not enough. Перед operational recoverability claim нужно пройти gate.

| Risk Factor | Required Check |
| --- | --- |
| Elastomers / seals | hardness, compression set, leak test |
| Lubricants | chemical condition, viscosity, contamination |
| Pressurized circuits | hydro/pneumatic pressure proof |
| Hydraulics | cycling test |
| Fuel / oxidizer residues | corrosion inspection |
| Batteries | load test |
| Electronics | powered test under load |
| Moving parts | motion cycle test |
| Welded joints | NDT / pressure / load test |
| Software-controlled systems | runtime proof under expected scenario |

### Proof levels

| Level | Claim allowed |
| --- | --- |
| Static Proof | physical/static integrity only |
| Dynamic Proof | dynamic recoverability |
| Mission Proof | mission recoverability |

## MVW Operational Procedure v0.1

For each critical component:

1. identify material / component;
2. identify storage environment;
3. identify active stress profile;
4. identify known ageing modes;
5. assign inspection method;
6. assign dynamic proof test;
7. define replace-before-use rule;
8. assign MVW status.

| MVW Status | Meaning | Claim |
| --- | --- | --- |
| MVW-0 | unknown | no dynamic claim |
| MVW-1 | visually intact | physical/evidential only |
| MVW-2 | static inspection passed | static integrity only |
| MVW-3 | material inspection passed | limited dynamic readiness |
| MVW-4 | dynamic proof passed | dynamic recoverability |
| MVW-5 | mission load proof passed | mission recoverability |

## Biobank SOP Delta v2.3

Template E adds the following to generic biobank practice:

| Template E element | Required practice |
| --- | --- |
| Operator != Custodian | separate storage responsibility from recovery capability |
| New-Operator Proof Test | a new operator must understand metadata package without oral explanation |
| Witness Aliquot Dynamic Proof | aliquot must pass thawing / unloading / QC |
| Interpretability Audit | provenance, consent, protocol version, freeze-thaw history must be readable |
| Capability Registry | track people who can thaw/QC/interpret samples |
| Managed Sunset | define what happens when old protocol becomes obsolete |
| Activation Failure | sample may look preserved but fail recovery after thawing |

Rule:

# Sample preservation without operator-readable metadata and witness aliquot recovery testing is physical preservation, not biological recoverability.
