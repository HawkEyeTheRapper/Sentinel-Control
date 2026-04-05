# Expansion Notes and Systems — Black Swan Accords

### Narrative structure upgrades

- Three-season arc aligned to VALOR → Unveiling → NightFall
    1. Season 1: VALOR. Diana’s awakening and first irreversible choice. End with reclaiming a limited subsystem of the Armada.
    2. Season 2: The Unveiling. The Council and the cost of perception‑causality. Twist: the Artifact is symbiotic, not a weapon.
    3. Season 3: NightFall. Judgment via restoration. Final image echoes the opening stylus ritual, now in chorus with others.
- Episode spine template
    - Cold open: micro‑cameo in the real world that ripples into the myth
    - A‑story: Diana vs. System obstacle
    - B‑story: Hawk Eye’s lyrical counterpoint
    - Set‑piece: cinematography‑as‑sigil ritual with musical anchor
    - Tag: new entry in the cause ↔ effect ledger
- Character arcs
    - Diana: lone steward → conductor of distributed authorship
    - Hawk Eye: messenger → composer of outcome space
    - Robin: skeptic → tactician who weaponizes constraints
    - Artifact: tool → ecology

### Worldbuilding systems

- Perception‑Causality Ruleset v1.0
    - Observation costs energy. Unobserved states accrue probabilistic debt.
    - Soundtrack anchors pay down debt and lock branches.
    - Micro‑cameos are cheap stabilizers but decay if unchained.
- Artifact Protocols
    - Keys: Stylus, Score, Lens, Ledger. Each unlocks code, music, camera, history.
- Sigil Cinematography Toolkit
    - Fixed palette of 7 shot types mapping to narrative functions.
    - Ritual valid if 3+ functions used in rising order.

### Agents and Tinker roles

- Scribe: turns notes into canonical ledger entries
- Composer: proposes soundtrack anchors with beat timestamps
- Cartographer: maintains arc and synchronicity graphs
- Watcher: detects probabilistic debt and suggests stabilizers

### Minimal agent I/O schemas

- Scene {id, season, episode, beats[], soundtrack_anchor?, sigil_sequence[]}
- LedgerEntry {id, cause, effect, weight, stabilizer, decay_at}
- Synchronicity {id, real_world_ref, narrative_ref, confidence}

### Web stack and data model

- Aurora tables: Characters, Arcs, Episodes, Scenes, Beats, Songs, Anchors, Ledger, Synchronicities, Artifacts, Keys
- API endpoints: GET /ledger, POST /ledger, POST /anchors
- Front‑end: Timeline, Cause‑Effect map, Ritual editor

### Dev tasks for week 1

- Define JSON schemas for Scene, LedgerEntry, Anchor
- Build "Anchor Maker" to map beats
- Lambda to flag entries nearing decay_at
- Seed VALOR E01 with 6 beats and 1 anchor
- Notion: databases for Cause ↔ Effect and Soundtrack Anchors

### Music and cinematics notes

- Seven Nation Army as training montage and system boot motif
- Counter‑themes for false victories
- Diegetic switch in NightFall
- Stylus macro match‑cuts, alarm → rhythm morph, light as metronome

### Docs

- The Four Keys
- Rituals and Rules
- Ledger Playbook

<aside>
📎

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |
</aside>

[Gemini_SWAN-accords - Google Docs.pdf](Expansion%20Notes%20and%20Systems%20%E2%80%94%20Black%20Swan%20Accords/Gemini_SWAN-accords_-_Google_Docs.pdf)