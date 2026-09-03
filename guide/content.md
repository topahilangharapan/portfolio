# Content Source of Truth

**For:** whoever edits the facts on this site next.
**Rule:** every factual claim on any page of this site must trace back to a line in
this file. To change a fact, change it here first, then propagate it to every page
that repeats it. If a page and this file disagree, this file is right and the page is
a bug.

This file does not specify layout or voice — that's [design-guide.md](design-guide.md).
It only specifies facts, so an edit never has to re-derive them from prose.

---

## Identity

| Field | Value |
|---|---|
| name | Musthofa Joko Anggoro |
| tagline | computer architecture researcher — phd aspirant |
| status | open to research and engineering opportunities |
| field | computer architecture, fpga design, eda, rtl design, iot & embedded systems |

## Openness

Audience-specific openness statements. The homepage stays neutral (see status
above); each statement below belongs on the list page for its audience —
`research.html` (and `for-committees.html`) for graduate study,
`experience.html` for full-time roles — not on the homepage.

| Audience | Statement |
|---|---|
| graduate study | open to a funded master's, phd, or integrated master's+phd — fpga/vlsi and reconfigurable computing, eda, computer architecture, digital hardware design; iot/cyber-physical systems, embedded systems, smart buildings and energy sensing |
| full-time roles | open to full-time software engineering and embedded/hardware engineering roles |

Compact form for a facts-table `status` cell (the field row already carries the
subject-area list, so don't repeat it there): graduate study →
`open to a funded master's, phd, or integrated master's+phd`. Full-time roles →
`open to full-time engineering roles` fits `experience.html`'s framing line as-is.

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
| impress — iot energy/space sensing | esp32, zigbee2mqtt, home assistant — 2026 |

## Work experience

| Role | Org | Dates |
|---|---|---|
| Research Assistant | Universitas Indonesia (Project IMPRESS) | jul 2026 – present |
| Software Engineer Intern | Traveloka | aug 2025 – jul 2026 |
| Full Stack Developer (internship) | PT Magna Solusi Indonesia | jan–jun 2025 |

IMPRESS summary (used on the homepage and `for-committees.html`): Research Assistant
on Project IMPRESS, an IoT energy/space sensing initiative funded under a university
innovation grant (P2/P3), Fasilkom UI, PIs Aprinaldi, S.Kom., M.Kom., Ph.D.Eng. and
Denny, S.Kom., M.I.T., Ph.D. Built sensing and monitoring infrastructure using ESP32,
Zigbee2MQTT, and Home Assistant. Current sensing uses quadrature noise subtraction
cross-validated across six calibration sessions to within about 4% agreement against
a nameplate-rated reference load; root-caused and fixed two hardware noise bugs (an
unbuffered CT signal loading a resistor divider, and an indirect ground path through
a breadboard rail) with before/after measurements. Broker-to-dashboard telemetry
stack (Mosquitto, InfluxDB, Grafana, Node-RED) verified end-to-end on the faculty
server; per-circuit sensing in the building itself is pending faculty electrical
work authorization.

IMPRESS role detail (`experience/impress-research-assistant.html` — scope and duties
of the RA role, not the research write-up): owns both the applied-research track
(grant-proposal authorship, architecture/protocol options comparison, data-collection
methodology) and the engineering build. Manages a 2-person student-intern team
building a parallel subsystem (RFID + camera classroom attendance), including
escalating its face-data privacy/consent/retention question to the faculty for
sign-off. Liaises with an embedded-systems course instructor on a coursework track
that can feed back into the project. Designed the data-collection methodology, device
naming taxonomy, and MQTT signal tagging that keeps the eventual dataset
analysis-ready.

IMPRESS engineering depth (`research/impress.html` only — the full research write-up):
- Signal-processing calibration: current sensing (CT clamp) uses quadrature noise
  subtraction (`signal = √(measured² − noise²)`) rather than naive subtraction,
  cross-validated across six calibration sessions against a nameplate-rated appliance
  (an AC unit's compressor, 5.2 A rated), converging to within about 4% agreement
  between two independently validated continuous-run sessions after diagnosing and
  discarding an outlier session. Voltage sensing adds a Goertzel single-frequency
  filter to extract the 50 Hz mains component, because the voltage channel can never
  be fully unloaded for a clean noise-floor reference the way the current channel can.
- Synchronized dual-channel real-power sampling: `P = mean(v[i] × i[i])` computed from
  time-aligned voltage/current samples rather than two separate RMS figures
  multiplied together — the correct approach for a non-unity-power-factor load.
- Root-caused two distinct hardware noise bugs by isolating variables on the bench: a
  bias-loading bug traced to an unbuffered CT signal dragging down a resistor divider
  (fixed with a DC-blocking capacitor), and a noise-floor issue traced to an indirect
  ground path through a breadboard rail (fixed by direct-wiring the ground reference)
  — both confirmed with before/after measurements.
- Calibration state persisted to flash (NVS), with auto-calibration on first boot and
  a live confidence score (low/medium/high, derived from stability across
  sub-windows of the calibration pass) published alongside every sensor reading over
  MQTT.
- No-reflash Wi-Fi provisioning: an always-on SoftAP plus web portal (NVS-backed
  credentials, live connection status, non-blocking network scan) built as a reusable
  template for future sensor nodes.
- Shared library extraction: promoted repeated logic (Wi-Fi connection, MQTT
  connection, Wi-Fi provisioning, connection-status logging, DHT22 sensor, RFID
  reader, IR transceiver, OLED status display, IR signal store) out of individual
  bring-up sketches into a shared library tree once a second sketch needed the same
  helper.
- Delivered a production-shape telemetry stack (Mosquitto, InfluxDB, Grafana,
  Node-RED) to a faculty-provisioned Linux VM over OpenVPN, verified end-to-end with
  a manual MQTT publish landing in InfluxDB and showing on the Grafana dashboard.
- Status: bench-validated single-phase sensing prototype, production telemetry
  infrastructure already live end-to-end; building-wide per-circuit rollout is
  pending faculty electrical work authorization — not yet a live building deployment.

Traveloka summary (used on the homepage and `for-committees.html`): owned the
booking process for a high-traffic production system, maintaining and fixing bugs
under system load and capacity constraints. Built and improved an internal
credential management system to reduce fraud. Proposed a new framework for
automating the reschedule process, adopted after team review — cut turnaround from
2 months to 2 weeks and raised success rate from 60% to about 85%.

Traveloka detail (`experience/traveloka.html` only):
- Owned the booking process for a high-traffic production system: fixed bugs and
  maintained stability under real load and capacity constraints.
- Built and maintained an internal credential management platform letting employees
  use shared accounts without direct access to the underlying credentials — cut
  fraud attempts by about 90% (from about 10/month to 0–1/month). Published
  credential data to a Tableau dashboard to monitor stale/unrotated credentials,
  most-active credentials, and flag suspicious activity. Served as primary support
  contact: resolved access issues, escalated platform bugs to engineering.
- Proposed a new framework to automate the reschedule process; adopted after team
  review — cut turnaround from 2 months to 2 weeks and raised success rate from 60%
  to about 85%. Published success/failure rates to a Tableau dashboard so business
  units could track the automation's impact.
- Built and maintained a ticket-tracking dashboard (single source of truth) for the
  department's support workflow: automatic status updates, stale-ticket alerts, and
  a self-service portal for other teams to submit requests. Adopted as the team's
  system of record.
- Built a logging and monitoring dashboard for the internal booking system, cutting
  incident resolution time (mean time to resolution) from hours to minutes.

Magna Solusi summary (used on the homepage and `for-committees.html`): full stack
developer intern building the client's school management system end-to-end (Spring
Boot, Angular) to replace a manual, paper-based administration process, deployed in
production. Owned the billing module: the manual process it replaced drove a
20–30% late-payment rate from unbilled or lost-track bills; the new trackable
billing dashboard closed that gap. Designed RESTful microservices in
Docker/Kubernetes handling 10k+ daily requests at under 200ms latency, and tuned
PostgreSQL (query tuning, indexing, stored procedures) to cut response times by 35%.

Magna Solusi detail (`experience/magna-solusi.html` only):
- Analyzed the client's manual, paper-based school administration process,
  identified its flaws, and gathered requirements directly from the client to scope
  the digital replacement. Designed and built the resulting system end-to-end with
  Spring Boot and Angular, deployed in a live production environment.
- Owned the billing module specifically: the manual process it replaced regularly
  let bills go unbilled or lost track of, driving a 20–30% late-payment rate. Built
  a trackable billing dashboard that turned those unbilled/lost bills into tracked,
  chargeable ones, closing that gap.
- Designed RESTful microservices in Docker/Kubernetes handling 10k+ daily requests
  at under 200ms latency, and tuned PostgreSQL (query tuning, indexing, stored
  procedures) to cut response times by 35%.
- Served as primary support contact for the system: trained non-technical staff
  (mainly teachers) on usage, resolved issues directly, and escalated deeper
  code-level bugs to senior engineers when needed.

## Projects

| Item | Links | Descriptor |
|---|---|---|
| sispa | [frontend](https://github.com/topahilangharapan/sispa-frontend), [api](https://github.com/topahilangharapan/sispa-backend) | event-organiser information system — spring boot, vue, postgresql — 2025 |
| apap medika | [web](https://github.com/topahilangharapan/apap-medika-web), [insurance](https://github.com/topahilangharapan/apap-medika-insurance), [profile](https://github.com/topahilangharapan/apap-medika-profile) | clinic web app, 3 services — spring boot, vue, postgresql — 2024 |
| libpanda | [web](https://github.com/PBP-E15/LibPanda), [mobile](https://github.com/PBP-E15/LibPanda-mobile) | library management, web + mobile — django, flutter — 2023 |
| marmut merah jambu | [repo](https://github.com/BASDAT-F7/marmut_merah_jambu) | music & podcast streaming — django, postgresql — 2024 |
| used car sales prediction | — | price prediction model — python, scikit-learn — 2025 |
| pathfinder | — | career guidance app, ux design — figma — 2024 |
| jarkomdat networking coursework | — | cisco cli, subnetting, packet analysis, go sockets, gcp — 2025 |

jarkomdat detail (`projects/jarkomdat.html` only): computer networks coursework at
Universitas Indonesia Fasilkom. Simulator/lab-level work (Packet Tracer, GCP
free-tier VMs), not certified or production enterprise-hardware experience.

- Cisco topology design and router CLI configuration across a progression: intro
  topology, a subnetted multi-site business network with DHCP pools, NAT + OSPF
  dynamic routing, and a self-directed project simulating a real school's network
  topology with a recorded presentation.
- Full subnet allocation (VLSM): network/broadcast address, mask, usable host
  range, and gateway sized to real device counts per site/division.
- Packet analysis with Wireshark and tcpdump, including TLS decryption via
  SSLKEYLOGFILE, HTTP/2 message inspection, and TCP three-way handshake/teardown
  analysis.
- TCP vs UDP client-server socket programming in Go, comparing connectionless and
  connection-oriented behavior.
- GCP VM provisioning, SSH access, firewall rule configuration, and a
  cross-VM applied project: a Spring Boot + PostgreSQL service, containerized and
  deployed across two GCP VMs, tested end-to-end.
- File transfer/integrity checks between VMs with rsync and sha256sum
  verification.

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

- `index.html` — summary facts table, selected work, 1–2 highlights per category
  plus a count-descriptor link to each list page
- `for-committees.html` — facts, cv, thesis, work experience (summary form),
  transcript note, english proficiency, references, contact, graduate-study
  openness statement
- `research.html` — list page: thesis, IMPRESS research; graduate-study openness
  statement
  - `research/thesis.html` — thesis detail (same content as
    `for-committees.html#thesis`)
  - `research/impress.html` — IMPRESS engineering-depth detail
- `experience.html` — list page: 3 work-experience roles (summary form) plus
  recognitions/other roles; full-time-roles openness statement
  - `experience/impress-research-assistant.html` — IMPRESS role detail
  - `experience/traveloka.html` — Traveloka detail
  - `experience/magna-solusi.html` — Magna Solusi detail
- `projects.html` — list page: all Projects table rows
  - `projects/sispa.html`, `projects/apap-medika.html`, `projects/libpanda.html`,
    `projects/marmut-merah-jambu.html`, `projects/used-car-sales-prediction.html`,
    `projects/pathfinder.html`, `projects/jarkomdat.html` — one per row
