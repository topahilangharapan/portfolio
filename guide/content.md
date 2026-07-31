# Content Source of Truth

**For:** whoever edits the facts on this site next.
**Rule:** every factual claim on `index.html` and `for-committees.html` must trace back
to a line in this file. To change a fact, change it here first, then propagate it to
every page that repeats it. If a page and this file disagree, this file is right and
the page is a bug.

This file does not specify layout or voice — that's [design-guide.md](design-guide.md).
It only specifies facts, so an edit never has to re-derive them from prose.

---

## Identity

| Field | Value |
|---|---|
| name | Musthofa Joko Anggoro |
| tagline | computer architecture researcher — phd aspirant |
| status | open to phd positions |
| field | computer architecture, fpga design, eda, rtl design |

## Education

| Field | Value |
|---|---|
| institution | Universitas Indonesia, Fasilkom |
| degree | BSc Computer Science, graduated Jul 2026 |
| major | information systems |
| gpa | 3.85 / 4.00 |
| advisor | Prof. Dr. Ir. Petrus Mursanto, M.Sc. |

## Thesis

| Field | Value |
|---|---|
| title | Bridging the Gap Between the Mano Register-Transfer Model and FPGA Realization Through a Synthesisable VHDL-93 Architecture |
| venue | undergraduate thesis, Universitas Indonesia Fasilkom — 2026 |
| supervisor | Prof. Dr. Ir. Petrus Mursanto, M.Sc. |
| tools | VHDL-93, Xilinx ISE 14.x, XST Synthesizer, ISim / GHDL |
| board | Xilinx Spartan-3AN starter board |
| clock | 58.648 MHz |
| utilization | 1,675 LUTs (14%), 638 flip-flops (5%) |
| status | completed, 2026 |
| publication | extended paper submitted, ICACSIS 2026 — decision pending |
| abstract | Complete synthesisable VHDL-93 implementation of the Mano register-transfer model. Systematic gap analysis of the Mano model's undefined engineering constraints — register organisation, instruction encoding, control mechanism, memory partitioning, I/O interface — each mapped to a concrete VHDL-93 design decision, producing a verified 8-bit datapath implementing the full microoperation sequence with board-level testing. |

Full text and paper proceedings are not linked for direct download — available on request, same as the transcript.

## Research

| Item | Descriptor |
|---|---|
| undergraduate thesis | vhdl-93, fpga, spartan-3an — 2026 |
| impress — iot energy/space sensing | esp32, zigbee2mqtt, home assistant — 2025 |

## Work experience

| Role | Org | Dates |
|---|---|---|
| Software Engineer Intern | Traveloka | aug 2025 – jul 2026 |
| Full Stack Developer (internship) | PT Magna Solusi Indonesia | jan–jun 2025 |

Traveloka summary: owned the booking process for a high-traffic production system,
maintaining and fixing bugs under system load and capacity constraints. Built and
improved an internal credential management system to reduce fraud. Proposed a new
framework for automating the reschedule process, adopted after team review — cut
turnaround from 2 months to 2 weeks and raised success rate from 60% to about 85%.

## Projects

| Item | Links | Descriptor |
|---|---|---|
| sispa | [frontend](https://github.com/topahilangharapan/sispa-frontend), [api](https://github.com/topahilangharapan/sispa-backend) | event-organiser information system — spring boot, vue, postgresql — 2025 |
| apap medika | [web](https://github.com/topahilangharapan/apap-medika-web), [insurance](https://github.com/topahilangharapan/apap-medika-insurance), [profile](https://github.com/topahilangharapan/apap-medika-profile) | clinic web app, 3 services — spring boot, vue, postgresql — 2024 |
| libpanda | [web](https://github.com/PBP-E15/LibPanda), [mobile](https://github.com/PBP-E15/LibPanda-mobile) | library management, web + mobile — django, flutter — 2023 |
| marmut merah jambu | [repo](https://github.com/BASDAT-F7/marmut_merah_jambu) | music & podcast streaming — django, postgresql — 2024 |
| used car sales prediction | — | price prediction model — python, scikit-learn — 2025 |
| pathfinder | — | career guidance app, ux design — figma — 2024 |

## Recognitions / other roles

| Item | Descriptor |
|---|---|
| vice pic, ui/ux | COMPFEST, 11 designers — 2023 |
| mentor, programming foundations 0 | Universitas Indonesia, Fasilkom |
| inspirasi–ntu summer program | nanyang technological university (ntu) x indonesia universities, lpdp-funded — 2025 |

## English proficiency

| Test | Overall | Listening | Reading | Writing | Speaking |
|---|---|---|---|---|---|
| IELTS Academic | 7.5 | 8.0 | 8.5 | 6.5 | 6.0 |

## References

| Role | Name |
|---|---|
| advisor | Prof. Dr. Ir. Petrus Mursanto, M.Sc. — thesis supervisor, Universitas Indonesia Fasilkom |
| reference | Prof. Dr. Dra. Kasiyah, M.Sc. (Kasiyah Junus) — linear algebra course lecturer, Universitas Indonesia Fasilkom |

Additional references available on request. Official transcript available on request.

## Contact

| Channel | Value |
|---|---|
| email | musthofaja.topa@gmail.com |
| linkedin | https://www.linkedin.com/in/musthofa-joko-anggoro/ |
| github | https://github.com/topahilangharapan |

## Files

| Asset | Path |
|---|---|
| cv | `assets/pdf/cv-musthofa-joko-anggoro.pdf` |

Thesis PDF is not published as a site asset (not linked for download, same as transcript — see Thesis section above).

## Images

None yet — `assets/img/` doesn't exist. Tracked here so a fact update that would
benefit from one isn't silently skipped or silently smuggled in outside the rules.

| Category (design-guide.md §3) | Status |
|---|---|
| thesis/technical figure | none |
| project screenshot | none |
| profile photo | none |
| personal-interests | section doesn't exist |

Adding one: the image must fit a §3 category, live under `assets/img/`, and follow
that section's markup/styling/budget exactly — then update this table. A fact update
does not get an image by default; most don't need one.

## Pages this file feeds

- `index.html` — summary facts table, selected work, research, experience (work
  experience), elsewhere (contact links, projects, recognitions/other roles)
- `for-committees.html` — facts, cv, thesis, work experience, transcript note, english
  proficiency, references, contact
