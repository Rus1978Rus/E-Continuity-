# E-Continuity v2.3.1
_E-Continuity v2.3.1 / rename-only release; историческое имя (former name): Template E; методологическое содержание не изменено._

_Case Library RU / библиотека кейсов_

## Назначение Case Library

Case Library нужна, чтобы Template E проверялся не на красивых аналогиях, а на реальных и пограничных ситуациях, где recoverability сохраняется, ломается, реконструируется или меняет mission.

## Case format

```
Case ID
Domain
Original Mission
Current Mission
Recoverability Levels
Continuity Chain Analysis
Failure Modes
Metrics
Evidence / Sources
Lesson for Framework
```

## Core Case Set

| Case ID | Name | Type | Main lesson | Maturity |
| --- | --- | --- | --- | --- |
| CASE-SOFT-001 | Legacy Software Collapse | Negative / dependency / executable continuity | source code preservation != executable continuity | C-4 |
| CASE-NII-001 | Закрытый НИИ / Orphan Documentation | Negative / custody / institutional collapse | documentation survived, recoverability died | C-3 |
| CASE-BIO-001 | Adult Murine Hippocampus Vitrification | Positive / functional recoverability | structural preservation is not enough | C-4 |
| CASE-INFRA-001 | Qanats / кяризы | Low-dependency / infrastructure | simplicity amplifies continuity | C-4 |
| CASE-ARCHAEO-001 | Antikythera Mechanism | Reconstructive / evidential | object survived; operator chain died | C-4 |
| CASE-CIV-001 | Monastic Continuity Network | Institutional / distributed memory | distributed institutions preserve operators | C-3/C-4 |
| CASE-MIL-001 | Tank Storage | Operational asset / component recoverability | asset is a recoverability graph | C-2/C-3 |
| CASE-MED-ORTHO-001 | Arthroplasty under regenerative pressure | Medical capability / managed sunset | medical capability must outlive peak demand | C-2/C-3 |
| CASE-CULT-001 | Chimney Sweep Brush | Transformative / craft | operational knowledge may become cultural knowledge | C-1/C-2 |
| CASE-REL-001 | Temple to Museum | Transformative / heritage | mission phase transition | C-1/C-2 |
| CASE-MEDIA-001 | VHS / Magnetic Tape Archive | Migration / playback infrastructure | media survival != playback recoverability | planned |
| CASE-AIR-001 | Aircraft Donor Storage | Component / donor continuity | donor storage is mission reclassification | planned |
| CASE-IND-001 | Mothballed Industrial Plant | Negative technical / economics / operator loss | physical conservation can fail operationally | planned |
| CASE-LANG-001 | Language Death / Liturgical Survival | Cultural / transformative | daily mission may die while interpretive mission remains | planned |
| CASE-MUSEUM-001 | Conservation vs Function Conflict | Evidence vs operation | evidence preservation may sacrifice function | planned |

## Приоритеты развития

| Priority | Case | Почему |
| --- | --- | --- |
| P1 | Software Collapse | инженерный, понятный reviewer-ам, сильная проверка DD/ETIG |
| P1 | NII / Orphan Documentation | сильный custody failure, близок к постсоветскому institutional shock |
| P1 | Biobank SOP | проверяет перенос OAIS-подобной логики на биологические объекты |
| P1 | Industrial Mothballing | negative technical case с economics/operator/material failure |
| P1 | Qanat | контрпример high-tech migration logic через low-dependency continuity |
| P2 | Antikythera | reconstructive recoverability |
| P2 | Monastic Network | distributed institutional memory |
| P2 | Military Storage | asset as recoverability graph |
| P2 | VHS Archive | playback chain collapse |
| P2 | Museum Conflict | evidence vs function |

## CASE-SOFT-001 Summary

Исходники могут сохраниться, но executable continuity умирает из-за dependency collapse, build chain collapse, operator collapse, institutional custody collapse и silent migration damage. Proof test: чистая машина, README, установка зависимостей, сборка, тесты, воспроизведение примера.

## CASE-NII-001 Summary

Закрытый НИИ показывает, что документы могут сохраниться физически, но без successor, custody transfer, tacit knowledge capture и proof test становятся orphan technical memory.

## CASE-MED-ORTHO-001 Summary

Если регенеративные методы снизят спрос на первичное эндопротезирование, ревизионная хирургия, реестр имплантов, совместимые компоненты и surgical expertise должны сохраняться до исчезновения legacy dependency.

## Case anti-bloat rule

Кейс входит в ядро только если он уточняет границу, failure mode, SOP, metric или governance rule. Иначе он идёт в приложение как иллюстрация.

---

# CASE-SPACE-001

## CASE-SPACE-001 — Apollo-Era Propulsion Hardware

| Field | Value |
| --- | --- |
| Domain | Aerospace / operational asset recoverability |
| Case type | Negative / partial-positive material degradation case |
| Core lesson | static preservation != dynamic recoverability |
| Main failure mode | material aging, seal degradation, corrosion, missing test infrastructure |
| Template E layer | Structural Recoverability + Proof Testing + Material Viability Window |
| Maturity | C-3/C-4 after source verification |

### Case summary

Apollo-era propulsion hardware and Saturn V F-1 components demonstrate the difference between physical/evidential preservation and dynamic operational recoverability. Museum artifacts and stored components may preserve structure, documentation and evidential value, but decades of material aging, seal degradation, corrosion, and loss of original test infrastructure can prevent safe full-function return without disassembly, inspection, replacement and partial proof testing.

### What failed

- Эластомеры и уплотнения могут терять эластичность и разрушаться при давлении, хотя внешне выглядят сохранными.
- Остатки агрессивных сред или соли/коррозионные агенты могут продолжать локальную деградацию.
- Сварные/паяные соединения и тонкие каналы могут иметь hidden defects, проявляющиеся только при нагрузке.
- Test infrastructure and qualified operators may be partially lost, making full mission proof unsafe or impossible.

### Recoverability levels

| Level | Status |
| --- | --- |
| Physical | high / artifact survives |
| Evidential | high / historical engineering evidence |
| Structural | partial / requires inspection |
| Dynamic functional | uncertain without proof testing and component replacement |
| Operational / mission | not claimed without modern safety review and dynamic test |

### Lesson for Template E

A static object can pass visual inspection and still fail at activation. For any dormant dynamic system with seals, elastomers, lubricants, propellant residues, pressure circuits, thermal loads or moving joints, dynamic proof testing must be separated from static preservation claims.

### Safe wording

Use: “Apollo-era propulsion hardware demonstrates static preservation vs dynamic recoverability.” Avoid: “Apollo-11 lunar module engine was restarted and failed” unless a specific primary source is provided.


## CASE-SPACE-001 — Apollo-Era Propulsion Hardware

### Domain

Aerospace / operational asset recoverability / material aging.

### Type

Negative / partial-positive material degradation case. C-3 / C-4 candidate.

### Safe claim

CASE-SPACE-001 does **not** claim a verified failed restart of an Apollo-11 lunar module engine. The correct claim is narrower:

> Apollo-era propulsion hardware and rocket-engine sealing-aging literature demonstrate the general risk that static preservation does not prove dynamic recoverability.

### Evidence status

| Evidence | Status |
| --- | --- |
| NASA F-1 gas generator hot-fire, 2013 | official NASA source |
| F-1 Rocket Engine Technical Manual, 1967 | historical technical baseline |
| silicone rubber sealing-ring ageing literature | peer-reviewed / technical source |
| specific Apollo-11 LM engine failure | not claimed |

### Recoverability analysis

| Level | Status |
| --- | --- |
| Physical | high for preserved/museum hardware |
| Evidential | high |
| Static Integrity | may be present |
| Dynamic Recoverability | requires proof test |
| Mission Recoverability | not claimable without mission load proof |

### Lesson

# Static Integrity != Dynamic Recoverability

A dormant system can look intact and still fail when returned to pressure, heat, vibration, chemical exposure, movement or mission load.

### Failure mode

# Activation Failure

Failure appears at activation, not during storage.

## Case Maturity Rules v2.3

| Level | Requirement |
| --- | --- |
| C-0 | idea only |
| C-1 | short description |
| C-2 | Template E analysis |
| C-3 | credible secondary sources |
| C-4 | primary / technical / institutional sources |
| C-5 | domain reviewer checked |

C-4 must not be assigned without primary source, technical report, institutional record, peer-reviewed source or official evidence for the key claim.
