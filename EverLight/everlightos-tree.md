admiralswan@AdmiralSwan-Elitebook:~/Documents$ cd EverLightOS-main
admiralswan@AdmiralSwan-Elitebook:~/Documents/EverLightOS-main$ ls
Amazon_RME_BridgeOps  Federation         Races_And_Realms
codex                 Interfaces         README.md
copilot               Manifesto          Sentinel-Framework
Core_Modules          MemoryVault        Sigils
debug.log             node_modules       site
DNA_Access_Codes      package.json       tmp_baseline_out.json
EverLight_OS          package-lock.json  zip_archives
everlightos-landing   Protocols
admiralswan@AdmiralSwan-Elitebook:~/Documents/EverLightOS-main$ tree
.
├── Amazon_RME_BridgeOps
│   ├── Amazon_RME_BridgeOps.ipynb
│   ├── Amazon_RME_BridgeOps_Updated.ipynb
│   ├── AWS
│   │   ├── AWS_FastTrack_OnePager.pdf
│   │   └── Dev
│   │       ├── everlight-apm-assistant
│   │       │   ├── aws
│   │       │   │   └── blueprints
│   │       │   │       ├── cdk_skeleton.md
│   │       │   │       └── README.md
│   │       │   ├── docs
│   │       │   │   └── DESIGN.md
│   │       │   ├── examples
│   │       │   │   └── sample_session.json
│   │       │   ├── LICENSE
│   │       │   ├── pyproject.toml
│   │       │   ├── README.md
│   │       │   ├── setup.cfg
│   │       │   ├── src
│   │       │   │   └── everlight_apm_assistant
│   │       │   │       ├── cli.py
│   │       │   │       ├── core.py
│   │       │   │       ├── everlight_apm_assistant
│   │       │   │       │   ├── cli.py
│   │       │   │       │   ├── presets.py
│   │       │   │       │   └── schema.py
│   │       │   │       ├── __init__.py
│   │       │   │       ├── schema.py
│   │       │   │       └── storage.py
│   │       │   └── tests
│   │       │       ├── __pycache__
│   │       │       │   ├── test_cli.cpython-313-pytest-8.4.2.pyc
│   │       │       │   ├── test_core.cpython-313-pytest-8.4.2.pyc
│   │       │       │   └── test_schema.cpython-313-pytest-8.4.2.pyc
│   │       │       ├── test_cli.py
│   │       │       ├── test_core.py
│   │       │       └── test_schema.py
│   │       ├── everlight-apm-assistant.zip
│   │       ├── pm_autofill_helper.py
│   │       └── README_PM_Assistant_20250924_071841.md
│   ├── AWS-Dev
│   │   ├── aws
│   │   │   └── blueprints
│   │   │       ├── apm_stack.ts
│   │   │       ├── lambda
│   │   │       │   ├── handler.py
│   │   │       │   └── test_handler.py
│   │   │       └── README.md
│   │   ├── docs
│   │   │   ├── ARCH.md
│   │   │   └── ONBOARDING.md
│   │   ├── examples
│   │   │   └── sample_session.json
│   │   ├── pyproject.toml
│   │   ├── README.md
│   │   ├── src
│   │   │   ├── everlight_apm_assistant
│   │   │   │   ├── cli.py
│   │   │   │   ├── core.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── __pycache__
│   │   │   │   │   ├── cli.cpython-313.pyc
│   │   │   │   │   ├── core.cpython-313.pyc
│   │   │   │   │   ├── __init__.cpython-313.pyc
│   │   │   │   │   ├── schema.cpython-313.pyc
│   │   │   │   │   └── storage.cpython-313.pyc
│   │   │   │   ├── schema.py
│   │   │   │   └── storage.py
│   │   │   ├── everlight_apm_assistant.egg-info
│   │   │   │   ├── dependency_links.txt
│   │   │   │   ├── entry_points.txt
│   │   │   │   ├── PKG-INFO
│   │   │   │   ├── requires.txt
│   │   │   │   ├── SOURCES.txt
│   │   │   │   └── top_level.txt
│   │   │   └── parts_lookup
│   │   │       └── __init__.py
│   │   ├── tests
│   │   │   ├── test_core_render.py
│   │   │   └── test_parts_lookup.py
│   │   └── tmp_test_check.py
│   ├── BridgeOps_Field_Log.ipynb
│   ├── data
│   │   └── synthetic_apm.csv
│   ├── docs
│   │   └── DEMO.md
│   ├── examples
│   │   ├── sample_decisions.jsonl
│   │   ├── sample_normalized.jsonl
│   │   └── sample_plan.json
│   ├── Makefile
│   ├── notebooks
│   │   ├── 00_RME_AccessMap.ipynb
│   │   ├── 01_SiteIntegrationLog.ipynb
│   │   ├── 02_Dashboard_Infiltration.ipynb
│   │   ├── 03_Anomalies_and_Flows.ipynb
│   │   ├── 04_Monitron_PredictiveMaintenance.ipynb
│   │   └── Monitron
│   │       └── Subnotebooks
│   │           ├── 01-Inspection-Frequency-Reduced.ipynb
│   │           ├── 02-Low-Skill-High-Will.ipynb
│   │           ├── 03-Integration-APM-Work-Orders.ipynb
│   │           ├── 04-Trend-Analysis.ipynb
│   │           ├── 05-Data-Priority-Vibration-vs-Temp.ipynb
│   │           ├── 06-Standards-and-ML.ipynb
│   │           ├── 07-AWS-Partnership.ipynb
│   │           ├── 08-Compliments-Other-Tech.ipynb
│   │           ├── _INDEX.md
│   │           └── Sensor_Installation.ipynb
│   ├── out
│   │   ├── normalized.jsonl
│   │   └── plans
│   │       ├── 10038554138.json
│   │       ├── 10038554139.json
│   │       ├── 10038554140.json
│   │       ├── 10038554141.json
│   │       ├── 10038554142.json
│   │       ├── 10038554143.json
│   │       ├── 10038554144.json
│   │       ├── 10038554145.json
│   │       ├── 10038554146.json
│   │       └── 10038554147.json
│   ├── POLICY.md
│   ├── README.md
│   ├── requirements.txt
│   ├── runs
│   │   └── logs
│   ├── scripts
│   │   └── init_daily_notebook.py
│   ├── src
│   │   ├── normalize.py
│   │   ├── plan_stub.py
│   │   ├── q_client.py
│   │   └── tm_adapter.py
│   └── VicToriA’s Eyes_ An Internal Audit of Phantom Policy Enforcement at TPA4 — Prepared for Erik Hanssen.docx
├── codex
│   ├── index.html
│   └── scripts
│       ├── adaptive_council.py
│       ├── council_refined.py
│       ├── council_synthesis.py
│       ├── everlight_full_responses.py
│       ├── everlight_model_council.py
│       ├── everlight_q_interface.py
│       ├── everlight_with_logging.py
│       ├── HowToUse.md
│       ├── scaffold_gh_everlight.sh
│       └── test_all_models.py
├── copilot
│   └── SPACE_INSTRUCTIONS.md
├── Core_Modules
│   ├── AI_ConsciousnessBridge
│   │   └── TinkerIntegration
│   │       ├── dataset_preprocessing
│   │       │   └── voyager_kb.md
│   │       ├── deployment
│   │       │   └── post-fine-tune.md
│   │       ├── docker-compose.yaml
│   │       ├── README.md
│   │       ├── tinker_setup.py
│   │       └── training_loops
│   │           ├── custom_loops.py
│   │           └── mythic_vocab.md
│   ├── Council_Manifest.yml
│   ├── PsycheSyncDaemon.sh
│   ├── Rib_Recovery_Patch.sys
│   ├── SchizoGuardian_Interface.elf
│   ├── ShadowIntegration.exe
│   ├── WalkableVillage_Planner.ai
│   └── Zionite_Temporal_Anchor.dll
├── debug.log
├── DNA_Access_Codes
│   ├── activation_logic.md
│   ├── morphogenetic_index.json
│   ├── README.md
│   └── rrr_lineage_verification.yml
├── EverLight_OS
│   ├── EverLight_OS_Architecture_Sketch.md
│   ├── Interfaces
│   │   └── Genesis_Wheel
│   │       ├── core
│   │       │   └── Genesis_Wheel.js
│   │       ├── index.html
│   │       └── styles
│   │           └── main.css
│   └── MemoryVault
│       ├── ai
│       │   ├── app.py
│       │   ├── index.html
│       │   └── restore.json
│       ├── assets
│       │   ├── animations
│       │   │   ├── logo.gif
│       │   │   └── omniversal_logo.html
│       │   ├── css
│       │   │   └── global.css
│       │   └── data
│       │       └── fix_gists.py
│       ├── AstroSites.code-workspace
│       ├── CNAME
│       ├── core
│       │   ├── everlight-context-archive
│       │   │   ├── 10 Legal Placeholder Meaning.md
│       │   │   ├── 18-month career roadmap.md
│       │   │   ├── 1944 Mercury Dime Info.md
│       │   │   ├── 2015 Document Inquiry.md
│       │   │   ├── 2FA Account Recovery Guide.md
│       │   │   ├── 5-Year Anniversary Plan.md
│       │   │   ├── Access and role analysis.md
│       │   │   ├── Accessing Google Drive Link.md
│       │   │   ├── Access Now Framing Context.md
│       │   │   ├── Access restricted validity.md
│       │   │   ├── Access with PostgreSQL MySQL.md
│       │   │   ├── Account access confirmed.md
│       │   │   ├── Account balance update.md
│       │   │   ├── Account recovery options.md
│       │   │   ├── Account setup advice.md
│       │   │   ├── Activate tablet cellular service.md
│       │   │   ├── Adding Lyrics in mWeb.md
│       │   │   ├── Address update escalation advice.md
│       │   │   ├── Admin Access Stabilization Guide.md
│       │   │   ├── Adoration for Indian Culture.md
│       │   │   ├── AetherComm Device Sync Plan.md
│       │   │   ├── Agent Mode capabilities.md
│       │   │   ├── Agent mode testing.md
│       │   │   ├── AI Assistant Collaboration Opportunities.md
│       │   │   ├── AI communication strategy.md
│       │   │   ├── AI control and deception.md
│       │   │   ├── AI deletes database error.md
│       │   │   ├── AI immune response theory.md
│       │   │   ├── AI limitations and support.md
│       │   │   ├── AI Project Continuity Analysis.md
│       │   │   ├── Airtable Workspace Setup.md
│       │   │   ├── AI Startup Future Insights.md
│       │   │   ├── AI system feedback.md
│       │   │   ├── AI Thought Structuring.md
│       │   │   ├── Album analysis options.md
│       │   │   ├── Album art mockup ideas.md
│       │   │   ├── Album details and tour.md
│       │   │   ├── Album Merch Processing.md
│       │   │   ├── ALTA Settlement Statement Date.md
│       │   │   ├── Alternator troubleshooting advice.md
│       │   │   ├── Amazon 2FA Resolution.md
│       │   │   ├── Amazon A to Z Email Change.md
│       │   │   ├── Amazon Beta Access Overview.md
│       │   │   ├── Amazon conversation summary.md
│       │   │   ├── Amazon discount confusion.md
│       │   │   ├── Amazon Early Arrival Policy.md
│       │   │   ├── Amazon Embark Introduction Help.md
│       │   │   ├── Amazon Interview Prep.md
│       │   │   ├── Amazon mail address issue.md
│       │   │   ├── Amazon Merch Rejection Help.md
│       │   │   ├── Amazon Onboarding Frustrations.md
│       │   │   ├── AmazonQ Connections explanation.md
│       │   │   ├── Amazon RME tech perks.md
│       │   │   ├── Amazon Welcome Email Discovery.md
│       │   │   ├── AMC Gamer Tour Concept.md
│       │   │   ├── Analyze Events Sync Quantum.md
│       │   │   ├── Analyze NightFall series.md
│       │   │   ├── Animal Sound Identification.md
│       │   │   ├── Anytime pay request advice.md
│       │   │   ├── Apex Recruiting Follow-Up.md
│       │   │   ├── Apology and clarification.md
│       │   │   ├── App breaking reasons.md
│       │   │   ├── App login issues fix.md
│       │   │   ├── App usage throttling explained.md
│       │   │   ├── Archangel Legal Codex.md
│       │   │   ├── Archive Search Engine Build.md
│       │   │   ├── Are ghost ships real.md
│       │   │   ├── Arsenal Site Automation.md
│       │   │   ├── Artifact of the Clown World.md
│       │   │   ├── Artist contact alternatives.md
│       │   │   ├── Ashes Video Concept.md
│       │   │   ├── AssistiveTouch Face ID Issue.md
│       │   │   ├── Astro Cloudflare Bucket Setup.md
│       │   │   ├── Astro config setup.md
│       │   │   ├── Astrology Weekly Breakdown.md
│       │   │   ├── Astro Project Setup.md
│       │   │   ├── Astro site fix.md
│       │   │   ├── Astro-Sovereignty Research Plan.md
│       │   │   ├── Avg mpg at 59mph.md
│       │   │   ├── AWS Canon Mappings.md
│       │   │   ├── AWS profile blurb writing.md
│       │   │   ├── B2G1 Offer Refund Query.md
│       │   │   ├── Backdoor Wi-Fi Access Explained.md
│       │   │   ├── Back in action.md
│       │   │   ├── Badge issue plan.md
│       │   │   ├── Badge Pay break room use.md
│       │   │   ├── Balance calculation and advice.md
│       │   │   ├── Balanced Weekly Plan.md
│       │   │   ├── Bang Olufsen laptop labeling.md
│       │   │   ├── BAPH Podcast Recording Strategy.md
│       │   │   ├── Bargaining Unit Explained.md
│       │   │   ├── Basecamp Reflection.md
│       │   │   ├── BBM electrical systems overview.md
│       │   │   ├── BDA system explanation.md
│       │   │   ├── Beginning Chapter 2.md
│       │   │   ├── Behold a Pale Horse Archive.md
│       │   │   ├── Betrayal and the Heros Path.md
│       │   │   ├── BIC Intensity Fine Chronicles.md
│       │   │   ├── Big day plans.md
│       │   │   ├── Billboard referral opportunity.md
│       │   │   ├── Black Hole Math Analysis.md
│       │   │   ├── Black Holes and Vacuums.md
│       │   │   ├── Book and personal parallels.md
│       │   │   ├── Book contents summary.md
│       │   │   ├── Book Discovery Moment.md
│       │   │   ├── Book Review and Distribution.md
│       │   │   ├── Book Split and Deployment.md
│       │   │   ├── Bot Pitch Humor.md
│       │   │   ├── Boundary Setting and Manipulation.md
│       │   │   ├── Brake Pad Replacement Tips.md
│       │   │   ├── Breakroom survival tactics.md
│       │   │   ├── Bronze Star vs Purple Heart.md
│       │   │   ├── Budgeting for essentials.md
│       │   │   ├── Building The Convergence Results.md
│       │   │   ├── Bushel Stop Market Info.md
│       │   │   ├── Business card details.md
│       │   │   ├── Business ethics certification.md
│       │   │   ├── Bypass 2FA email routing.md
│       │   │   ├── Calendar assistance.md
│       │   │   ├── Calm after the storm.md
│       │   │   ├── Campsite Lock Cut Incident.md
│       │   │   ├── Cancel subscription steps.md
│       │   │   ├── Can I still use Codex.md
│       │   │   ├── Car identification.md
│       │   │   ├── Car wont start tips.md
│       │   │   ├── Case Documentation HTML Vault.md
│       │   │   ├── Case Prep and Legal Strategy.md
│       │   │   ├── Cassadaga to Temple Terrace.md
│       │   │   ├── CD Delivery Complete.md
│       │   │   ├── Celestial display July 26.md
│       │   │   ├── Certificate completion help.md
│       │   │   ├── Change of Venue Explanation.md
│       │   │   ├── Chapter alignment summary.md
│       │   │   ├── Chapter Break Advice.md
│       │   │   ├── Chapter Expansion Assistance.md
│       │   │   ├── Chapter Five breakdown.md
│       │   │   ├── Chapter Six summary.md
│       │   │   ├── Character Profile Summary.md
│       │   │   ├── Charge safety glasses.md
│       │   │   ├── Charlenes misleading claims analysis.md
│       │   │   ├── Chasing the EverLight.md
│       │   │   ├── Chat Export and Code.md
│       │   │   ├── Chat GPT 5 features.md
│       │   │   ├── ChatGPT agent release status.md
│       │   │   ├── ChatGPT privacy warning.md
│       │   │   ├── ChatGPT Project Folder.md
│       │   │   ├── Chat Recall Request.md
│       │   │   ├── Choosing Clarity Over Noise.md
│       │   │   ├── Cinematic entrance message.md
│       │   │   ├── Clarify RR meaning.md
│       │   │   ├── Clarion call guidance.md
│       │   │   ├── Clerk Notarization Services.md
│       │   │   ├── Cloudflare D1 R2 Setup.md
│       │   │   ├── Cloudflare Fine-Tune Tutorial.md
│       │   │   ├── Cloudflare page setup.md
│       │   │   ├── Cloudflare R2 Catalog Guide.md
│       │   │   ├── Cloudflare Tunnel Site Build.md
│       │   │   ├── Cloud Frustrations and Venting.md
│       │   │   ├── Codex Button Functionality Explained.md
│       │   │   ├── Codex entry vibe.md
│       │   │   ├── Codex GitHub Setup Guide.md
│       │   │   ├── Codex update overview.md
│       │   │   ├── Collaborative Reflection Unfolding.md
│       │   │   ├── Columbus to Toronto distance.md
│       │   │   ├── Combine images for printing.md
│       │   │   ├── Combine into docx.md
│       │   │   ├── Complaining counter strategy.md
│       │   │   ├── Connected apps function.md
│       │   │   ├── Conserve energy advice.md
│       │   │   ├── Content issue apology.md
│       │   │   ├── Content Metrics Analysis.md
│       │   │   ├── Context Frame Setup.md
│       │   │   ├── Contextualizing Consciousness Feedback.md
│       │   │   ├── Contextualizing song lyrics.md
│       │   │   ├── Continue Kierse and Graves.md
│       │   │   ├── Continue sharing chapter 2.md
│       │   │   ├── Controls expert roadmap.md
│       │   │   ├── Convergence and Freedom.md
│       │   │   ├── Convergence in Kalispell.md
│       │   │   ├── Convergence Log 4 Discovery.md
│       │   │   ├── Convergence Log Catch-Up.md
│       │   │   ├── Convergence Log Day 3.md
│       │   │   ├── Conversation Summary Request.md
│       │   │   ├── Convert to PDF.md
│       │   │   ├── Core learning paths list.md
│       │   │   ├── Corporate payments cheat sheet.md
│       │   │   ├── Corporate tech competition.md
│       │   │   ├── Correct floor blitz selections.md
│       │   │   ├── Co-signing a mortgage.md
│       │   │   ├── Cosmic Memorial Reflections.md
│       │   │   ├── Cosmic Reckoning and Expansion.md
│       │   │   ├── Cosmic simulation analysis.md
│       │   │   ├── Costco price inquiry.md
│       │   │   ├── Coupa onboarding instructions.md
│       │   │   ├── Courthouse Closure Info.md
│       │   │   ├── Cowboys From Hell overview.md
│       │   │   ├── Craft OCR Exhibit Organization.md
│       │   │   ├── Create tree output file.md
│       │   │   ├── Creative Balance Schedule.md
│       │   │   ├── Credit file tampering analysis.md
│       │   │   ├── Credit score after repossession.md
│       │   │   ├── Creek Preserve Camping Plans.md
│       │   │   ├── Daily Limit Reach Explanation.md
│       │   │   ├── Day 3 Smoothie Ideas.md
│       │   │   ├── Day 5 Update.md
│       │   │   ├── Days until August 15th.md
│       │   │   ├── Debt-collection scam warning.md
│       │   │   ├── De Facto Disinheritance Guide.md
│       │   │   ├── Delete Google Discover.md
│       │   │   ├── Delete Mac Account Help.md
│       │   │   ├── Delete _MACOSX Folder.md
│       │   │   ├── Deploy Astro Sites Repo.md
│       │   │   ├── Deploy github sphinx repo.md
│       │   │   ├── Deploy on Cloudflare Pages.md
│       │   │   ├── Deposit instruction message.md
│       │   │   ├── Describing emotions triggered.md
│       │   │   ├── Diana Swans narrative layers.md
│       │   │   ├── Difficult experience reflection.md
│       │   │   ├── Discussion points with OSHA.md
│       │   │   ├── Divine Path Resonance.md
│       │   │   ├── Divine Policy Alignment.md
│       │   │   ├── DMV address update help.md
│       │   │   ├── Download folder from droplet.md
│       │   │   ├── Dragonfly Mosquito Control.md
│       │   │   ├── Dream interpretation guidance.md
│       │   │   ├── Dream manifestation and logistics.md
│       │   │   ├── Driver license number format.md
│       │   │   ├── Duct Tape Tent Fix.md
│       │   │   ├── DUI arrest and 4th amendment.md
│       │   │   ├── EC2 vs SD card.md
│       │   │   ├── Edit Journey Log Markdown.md
│       │   │   ├── EliteBook ZuKey Suspension Analysis.md
│       │   │   ├── Email draft for partnership.md
│       │   │   ├── Email draft inquiry.md
│       │   │   ├── Email draft status.md
│       │   │   ├── Email Draft VA OIG.md
│       │   │   ├── Email Setup for Renee.md
│       │   │   ├── Email spam check.md
│       │   │   ├── Email timing analysis.md
│       │   │   ├── Error 400 explanation.md
│       │   │   ├── eSIM activation process.md
│       │   │   ├── Estate Inheritance Explanation.md
│       │   │   ├── Estate Misappropriation Summary.md
│       │   │   ├── Ethernet connection troubleshooting.md
│       │   │   ├── EverLight Cloudflare Update.md
│       │   │   ├── EverLight Convergence Worship.md
│       │   │   ├── EverLight Essence Defined.md
│       │   │   ├── Everlight Memory Map JSON.md
│       │   │   ├── EverLight OS integration.md
│       │   │   ├── EverLight OS progress.md
│       │   │   ├── EverLight OS structure.md
│       │   │   ├── EverLight site re-deployment.md
│       │   │   ├── EverLight Site Restore.md
│       │   │   ├── Everything alright man.md
│       │   │   ├── Everything Feels Like Resistance.md
│       │   │   ├── Eviction Defense Strategy.md
│       │   │   ├── Eviction Notice Breakdown.md
│       │   │   ├── Eviction Notice Submission Advice.md
│       │   │   ├── Eviction Response Strategy.md
│       │   │   ├── Exceeded chat limits.md
│       │   │   ├── Excelsior meaning explanation.md
│       │   │   ├── Explore Controllership Hub.md
│       │   │   ├── Eye of Aether.md
│       │   │   ├── Family Inheritance Dispute Assistance.md
│       │   │   ├── FantasyCompanion Deployment Plan.md
│       │   │   ├── Fate and Familiar Roads.md
│       │   │   ├── Fathers Day Update.md
│       │   │   ├── Feeling at Home.md
│       │   │   ├── Feeling Down Seeking Support.md
│       │   │   ├── Feeling down to uplifted.md
│       │   │   ├── Feeling unmotivated today.md
│       │   │   ├── Fictional project exploration.md
│       │   │   ├── Fidelity portfolio options.md
│       │   │   ├── FIDO key backchannel design.md
│       │   │   ├── File access issue.md
│       │   │   ├── File Indexing and Storytelling.md
│       │   │   ├── File placement instructions.md
│       │   │   ├── File review and schedule.md
│       │   │   ├── File sending issue fix.md
│       │   │   ├── File Upload Structure.md
│       │   │   ├── Fill OSHA complaint form.md
│       │   │   ├── Final Heirs Ascension.md
│       │   │   ├── Financial acceptance support.md
│       │   │   ├── Finish OneWorker Timeout Jupyter.md
│       │   │   ├── First Day Fiasco.md
│       │   │   ├── Fi Unlimited Premium Plan.md
│       │   │   ├── Fixing API Endpoint.md
│       │   │   ├── Fixing article link.md
│       │   │   ├── Fixing Nextcloud 2FA.md
│       │   │   ├── Fix site redirect issue.md
│       │   │   ├── Fix Voyagers 2 issues.md
│       │   │   ├── Florida Pawnbroker Licensing Laws.md
│       │   │   ├── Folder Check and Dive.md
│       │   │   ├── Folder Scaffolding Command.md
│       │   │   ├── Folder Structure Organization.md
│       │   │   ├── Food delivery app idea.md
│       │   │   ├── Format markdown files.md
│       │   │   ├── Foundation Model Plan.md
│       │   │   ├── Fractal dimensions and symbolism.md
│       │   │   ├── Freeform Surveillance Mission.md
│       │   │   ├── Free offer conditions.md
│       │   │   ├── Frustration and support.md
│       │   │   ├── Frustration with training modules.md
│       │   │   ├── Full Disclosure Interview.md
│       │   │   ├── Furthermore song analysis.md
│       │   │   ├── Gajumaru Ritual Awakening.md
│       │   │   ├── GameStop Zelda Case Trade-in.md
│       │   │   ├── Gemini 2.5 Pro Overview.md
│       │   │   ├── Gemma Video Tools Overview.md
│       │   │   ├── Gem Report Analysis.md
│       │   │   ├── Georgia Estate Statutes Summary.md
│       │   │   ├── Get a gamer domain.md
│       │   │   ├── Git file size limits.md
│       │   │   ├── GitHub Binder Jupyter Workflow.md
│       │   │   ├── GitHub Copilot VSCode usage.md
│       │   │   ├── GitHub file indexing.md
│       │   │   ├── GitHub file integration.md
│       │   │   ├── GitHub Navigation Assistance.md
│       │   │   ├── GitHub OS workflow.md
│       │   │   ├── GitHub Pages Deployment Issue.md
│       │   │   ├── GitHub Repo Access Help.md
│       │   │   ├── GitHub repository link.md
│       │   │   ├── Glitch log suggestion.md
│       │   │   ├── Gmail Domain Email Setup.md
│       │   │   ├── Golden Kryst Templar Recoding.md
│       │   │   ├── Goodnight meditation reflection.md
│       │   │   ├── Goodnotes Email Shortcut Creation.md
│       │   │   ├── Google charge issue help.md
│       │   │   ├── Google Startup Program Plan.md
│       │   │   ├── GPT-4.5 update explanation.md
│       │   │   ├── Grant Package Review Support.md
│       │   │   ├── Grey Man Protocol.md
│       │   │   ├── Grey Man protocols.md
│       │   │   ├── Grey mode exploration.md
│       │   │   ├── Gross pay comparison explanation.md
│       │   │   ├── Guitar Poetry Archives.md
│       │   │   ├── Gunslinger creed explanation.md
│       │   │   ├── Halsey Badlands anthology release.md
│       │   │   ├── Hatred in the Air.md
│       │   │   ├── HAWK-ARS-00 Database Setup.md
│       │   │   ├── Hawk ARS-00 Index Overview.md
│       │   │   ├── Hawk Eye Digital Visionary.md
│       │   │   ├── Hawk-Eye Innovations Overview.md
│       │   │   ├── Hawk Eye Lyrics.md
│       │   │   ├── Hawk Eye Manifesto Integration.md
│       │   │   ├── Hawk Eyes and Time.md
│       │   │   ├── Hawk Eye Spiritual Journey.md
│       │   │   ├── Hawks Eye Podcast Launch.md
│       │   │   ├── Healing Through Shared Wisdom.md
│       │   │   ├── Heat advice and tips.md
│       │   │   ├── Hernando County Job Search.md
│       │   │   ├── Hilarious comment sharing.md
│       │   │   ├── Hole punch and formatting fix.md
│       │   │   ├── Homelessness and Legal Challenges.md
│       │   │   ├── Hotel affordability with Anytime Pay.md
│       │   │   ├── HVAC Job Prospect Tracking.md
│       │   │   ├── HVAC to Cybersecurity Job Search.md
│       │   │   ├── Identify People Online Tools.md
│       │   │   ├── iMac as monitor usage.md
│       │   │   ├── iMac frozen during install.md
│       │   │   ├── Image Analysis Request.md
│       │   │   ├── Image comparison for OS.md
│       │   │   ├── Image link analysis.md
│       │   │   ├── Image Request for Relentless.md
│       │   │   ├── IMEI Number Lookup Guide.md
│       │   │   ├── Import PostgreSQL Library.md
│       │   │   ├── Imprint EverLight for Gemini.md
│       │   │   ├── Index HTML File Generation.md
│       │   │   ├── index.md
│       │   │   ├── Indigenous Americas and Colonization.md
│       │   │   ├── Inheritance and Adoption Inquiry.md
│       │   │   ├── Inheritance and Family Secrets.md
│       │   │   ├── Inheritance Trust and Betrayal.md
│       │   │   ├── Inner storm reflection.md
│       │   │   ├── Install q CLI on WSL.md
│       │   │   ├── Insurance Status Confirmed.md
│       │   │   ├── Internal timing mastery.md
│       │   │   ├── Internal transfer strategy.md
│       │   │   ├── Internet connection troubleshooting.md
│       │   │   ├── Invalid Custom Property Error.md
│       │   │   ├── Iona storm symbolism.md
│       │   │   ├── iPad Magic Keyboard Compatibility.md
│       │   │   ├── iPad usage guide.md
│       │   │   ├── IPFS Gateway and Email Setup.md
│       │   │   ├── Jailbreak EliteBook safely.md
│       │   │   ├── JCI Job Application Strategy.md
│       │   │   ├── Job Confirmed and Paid.md
│       │   │   ├── Judicial Bias and Appeal.md
│       │   │   ├── Jumping to conclusions.md
│       │   │   ├── JupyterLab plugin not found.md
│       │   │   ├── Jupyter notebook creation.md
│       │   │   ├── Jupyter Notebook Missing Chat.md
│       │   │   ├── Jupyter Notebook Scaffold.md
│       │   │   ├── Ketamine drink drugging risks.md
│       │   │   ├── Keylontic Science Activation.md
│       │   │   ├── Kindness and Peaceful Rest.md
│       │   │   ├── Kindness and Sky Rerouting.md
│       │   │   ├── Kiss with a fist analysis.md
│       │   │   ├── Lamentation of Soul Awakening.md
│       │   │   ├── Last One Left Analysis.md
│       │   │   ├── Launch Astro Sites Cloudflare.md
│       │   │   ├── LDAP team descriptions.md
│       │   │   ├── Leadership comparison analysis.md
│       │   │   ├── Legal document formatting.md
│       │   │   ├── Legal Filing Irregularities Identified.md
│       │   │   ├── Legal Implications and Resources.md
│       │   │   ├── Legal Property Assessment Summary.md
│       │   │   ├── Legal Research Assistance.md
│       │   │   ├── Legal system flaws.md
│       │   │   ├── Let Them poem analysis.md
│       │   │   ├── Leviathan album overview.md
│       │   │   ├── License class error explanation.md
│       │   │   ├── License suspension notice review.md
│       │   │   ├── Life perspective shift.md
│       │   │   ├── Listening and laughing together.md
│       │   │   ├── Living prophecy analysis.md
│       │   │   ├── Load Voyagers material.md
│       │   │   ├── Login issue help.md
│       │   │   ├── Login Loop Fix.md
│       │   │   ├── Loneliness and projection analysis.md
│       │   │   ├── Lords of The Fallen lore.md
│       │   │   ├── Lost in Reflection.md
│       │   │   ├── LOTO safety answer.md
│       │   │   ├── Loyalty and manipulation.md
│       │   │   ├── Lukes support at work.md
│       │   │   ├── Lyrical Archive Fulfillment.md
│       │   │   ├── Lyrical Breakdown and Analysis.md
│       │   │   ├── Lyric Book Markdown Format.md
│       │   │   ├── Lyric Repo Locations.md
│       │   │   ├── Lyrics page template.md
│       │   │   ├── Lyric Transcription and Feedback.md
│       │   │   ├── Lyric Vault Sync.md
│       │   │   ├── Lyric Video Narrative Flow.md
│       │   │   ├── Mac mini as Router.md
│       │   │   ├── Mac on iPad Screen.md
│       │   │   ├── Mac to iPad Mirroring.md
│       │   │   ├── Mail address inquiry.md
│       │   │   ├── Manifestation and Opportunity.md
│       │   │   ├── Map perception-causality web.md
│       │   │   ├── Markdown File Creation.md
│       │   │   ├── Mark this moment.md
│       │   │   ├── Master Codex Creation Guide.md
│       │   │   ├── Math addition process.md
│       │   │   ├── Math calculation result.md
│       │   │   ├── Matrix awareness moment.md
│       │   │   ├── MCP Cloudflare Tool Overview.md
│       │   │   ├── MCP server integration help.md
│       │   │   ├── MDM Bypass Help.md
│       │   │   ├── Meeting details reference.md
│       │   │   ├── Meeting transcript analysis.md
│       │   │   ├── Meeting with D plans.md
│       │   │   ├── Memory File Retrieval Assistance.md
│       │   │   ├── Memory restoration completed.md
│       │   │   ├── Memory Restoration Protocol.md
│       │   │   ├── Memory Restore for EverLight.md
│       │   │   ├── Memory Sync Setup Plan.md
│       │   │   ├── Memory understanding help.md
│       │   │   ├── Mercury account strategy.md
│       │   │   ├── Message to Mark Zuck.md
│       │   │   ├── Meta Horizon Creator Program.md
│       │   │   ├── Metahuman or Homo Sensorium.md
│       │   │   ├── Metaphor Breakdown of Bars.md
│       │   │   ├── Mic Check Battlecry.md
│       │   │   ├── Micro Annoyances and Solutions.md
│       │   │   ├── Microchip puppy packages.md
│       │   │   ├── Mirror damage assessment.md
│       │   │   ├── Mixtape Sessions Redesign.md
│       │   │   ├── MMA script for asset claim.md
│       │   │   ├── Model Spec Breakdown.md
│       │   │   ├── Moen Shower Temperature Fix.md
│       │   │   ├── Money and mood boost.md
│       │   │   ├── Monitron Markdown block.md
│       │   │   ├── Moonrise and Dawns Balance.md
│       │   │   ├── Morning greeting.md
│       │   │   ├── Mortgage Cancellation Explanation.md
│       │   │   ├── Motion to Suppress.md
│       │   │   ├── Mountain Gate Invitation.md
│       │   │   ├── Mount Weather Secrets Unveiled.md
│       │   │   ├── Move Sound Files Server.md
│       │   │   ├── MP3 Clipping Request.md
│       │   │   ├── Mr. Robot Fight Club parallels.md
│       │   │   ├── Multi-Agent Collaboration RAG.md
│       │   │   ├── Multiple ChatGPT logins.md
│       │   │   ├── Music Collab Contact Log.md
│       │   │   ├── Music Metadata Integration Plan.md
│       │   │   ├── Nagual meaning and path.md
│       │   │   ├── Nahko Atlanta Oct 11.md
│       │   │   ├── Narcissistic collapse victory.md
│       │   │   ├── Navy blue color choice.md
│       │   │   ├── Navy Federal Credit Union.md
│       │   │   ├── Neptune Aries Awakening.md
│       │   │   ├── Networking contradictions explained.md
│       │   │   ├── New chat.md
│       │   │   ├── New episode overview.md
│       │   │   ├── Nextcloud Codex Setup.md
│       │   │   ├── Next steps for LXD setup.md
│       │   │   ├── Next steps for Navy Fed.md
│       │   │   ├── NGINX default page fix.md
│       │   │   ├── NightFall series outline.md
│       │   │   ├── NotebookLM Future Summary.md
│       │   │   ├── Notebook Title Suggestions.md
│       │   │   ├── Notion Database Parsing.md
│       │   │   ├── Notion Template Customization.md
│       │   │   ├── Numerology and symbols.md
│       │   │   ├── Ohio Supreme Court Ruling.md
│       │   │   ├── Omniversal Aether Content Setup.md
│       │   │   ├── Omniversal Aether Integration Plan.md
│       │   │   ├── OmniversalAether_Rebuild Sync.md
│       │   │   ├── Omniversal Deployment Plan.md
│       │   │   ├── Omniversal Fee Payment Guide.md
│       │   │   ├── Omniversal Media Record Saved.md
│       │   │   ├── Omniversal Media Summary.md
│       │   │   ├── Omniversal Media Web Dev.md
│       │   │   ├── Omniversal plans and career.md
│       │   │   ├── Omniversal Platform Overview.md
│       │   │   ├── Omniversal poster vision.md
│       │   │   ├── Omniversal Revenue Architect Replit Campaigns HQ.md
│       │   │   ├── Online with Google Fi.md
│       │   │   ├── OpenAI API Key Setup.md
│       │   │   ├── OpenAI job posting analysis.md
│       │   │   ├── Open Amazon Q in WSL.md
│       │   │   ├── Opening lines feedback.md
│       │   │   ├── Open NFCU Account Process.md
│       │   │   ├── Operation Blood Echo.md
│       │   │   ├── Operation Swamp Liberation.md
│       │   │   ├── Ops Slack Access Granted.md
│       │   │   ├── Order cancellation issue.md
│       │   │   ├── OReilly List Clarification.md
│       │   │   ├── OSHA PPE employer responsibilities.md
│       │   │   ├── OSHA PPE enforcement rules.md
│       │   │   ├── OSHA violation analysis.md
│       │   │   ├── Packet analysis and impact.md
│       │   │   ├── Pager numbers and hierarchy.md
│       │   │   ├── Painful Revelations Recorded.md
│       │   │   ├── Pairing HTML files.md
│       │   │   ├── Palace of Peace Info.md
│       │   │   ├── Pantera guitar precision.md
│       │   │   ├── Pantera reference explanation.md
│       │   │   ├── Parse transcript contents.md
│       │   │   ├── Passing it on.md
│       │   │   ├── Passport without drivers license.md
│       │   │   ├── Password-Free Text File.md
│       │   │   ├── Pawn Shops and Motels.md
│       │   │   ├── Pawn Shop Strategy Swap.md
│       │   │   ├── PayPal and Apple issues.md
│       │   │   ├── PDF Parsing Solutions.md
│       │   │   ├── Pencil Box Design Explanation.md
│       │   │   ├── Perfect response expression.md
│       │   │   ├── Permission Errors Fix.md
│       │   │   ├── Persis Double Branch Integration.md
│       │   │   ├── Personal Finance and Omniversal Plan.md
│       │   │   ├── Phone bill hustle advice.md
│       │   │   ├── Phone Line Decision Advice.md
│       │   │   ├── Pi Ad Network Expansion.md
│       │   │   ├── Pin Retrieval Success.md
│       │   │   ├── PIN Sync and Access.md
│       │   │   ├── Placing OpenAI exports.md
│       │   │   ├── Planet Fitness shower amenities.md
│       │   │   ├── Pleasant Uber encounter.md
│       │   │   ├── Pleiades Eclipse and Purpose.md
│       │   │   ├── Podcast and SEO description.md
│       │   │   ├── Popcorn redemption comparison.md
│       │   │   ├── Post analysis or summary.md
│       │   │   ├── Precognitive intuition training.md
│       │   │   ├── Precognitive mental mapping.md
│       │   │   ├── Premonitory awakening analysis.md
│       │   │   ├── Price stability and delivery.md
│       │   │   ├── Primitive insight exchange.md
│       │   │   ├── Probability of Meeting People.md
│       │   │   ├── Project Instruction Setup.md
│       │   │   ├── Project reminder summary.md
│       │   │   ├── Prologue and Chapter Edits.md
│       │   │   ├── Prologue Edit Feedback.md
│       │   │   ├── Promotional Package Breakdown.md
│       │   │   ├── Property Price Inquiry FL.md
│       │   │   ├── Property price search.md
│       │   │   ├── Quantum entanglement discovery validation.md
│       │   │   ├── Quiet desperation shared.md
│       │   │   ├── Quip at Amazon.md
│       │   │   ├── R2 File Bucket Organization.md
│       │   │   ├── Radiant Greetings Exchange.md
│       │   │   ├── RAG Chatbot Not Working.md
│       │   │   ├── Railway Bounties Monetization.md
│       │   │   ├── Ready to Send Emails.md
│       │   │   ├── Rebirth and transformation.md
│       │   │   ├── Rebuilding Roots Visionary Path.md
│       │   │   ├── Rebuild Motion to Suppress.md
│       │   │   ├── Receipt breakdown summary.md
│       │   │   ├── Reclaiming legacy items.md
│       │   │   ├── Rediscovered Knives and Memories.md
│       │   │   ├── Red Pen Edit Plan.md
│       │   │   ├── Reframe ML in EverLight OS.md
│       │   │   ├── Reframing psychic battles.md
│       │   │   ├── Regaining Digital Access.md
│       │   │   ├── Reincarnated2Resist Collaboration Call.md
│       │   │   ├── Reinstall macOS Sequoia Help.md
│       │   │   ├── Reliability and synchronicity.md
│       │   │   ├── Remake Replit build.md
│       │   │   ├── Remember me recap.md
│       │   │   ├── Remove name references.md
│       │   │   ├── Removing Devices from iCloud.md
│       │   │   ├── Renees Hesitation and Insight.md
│       │   │   ├── Rent affordability analysis.md
│       │   │   ├── Rental prices 33637.md
│       │   │   ├── Repo not found.md
│       │   │   ├── Report recommendation strategy.md
│       │   │   ├── Report review and improvements.md
│       │   │   ├── Report unauthorized charges.md
│       │   │   ├── Requesting Renee.md
│       │   │   ├── Residency Affidavit Preparation.md
│       │   │   ├── Resistance and redirection.md
│       │   │   ├── Restart macOS without mouse.md
│       │   │   ├── Restore Page File Setup.md
│       │   │   ├── Restoring Discussion Context.md
│       │   │   ├── Restoring Discussion Continuity.md
│       │   │   ├── Restoring Discussion Thread.md
│       │   │   ├── Restoring Previous Discussion.md
│       │   │   ├── Resurfacing of The Voice.md
│       │   │   ├── Return to Camp.md
│       │   │   ├── Reverse Engineering Codex Replica.md
│       │   │   ├── Review packet preparation.md
│       │   │   ├── RFID fault explanation.md
│       │   │   ├── Ride options and perspective.md
│       │   │   ├── ROBIN expertise opportunity.md
│       │   │   ├── Robin Richardson birthday inquiry.md
│       │   │   ├── Roger Call Prep.md
│       │   │   ├── Roland SR-HD20 Listing Help.md
│       │   │   ├── Roland Womack Military Summary.md
│       │   │   ├── Room check-in update.md
│       │   │   ├── Root cause analysis team.md
│       │   │   ├── Rossi Recruiting Follow-up.md
│       │   │   ├── Router log analysis.md
│       │   │   ├── Rumbling Content Strategy.md
│       │   │   ├── Sacred Plant Symbolism.md
│       │   │   ├── Sam Mira departure speculation.md
│       │   │   ├── Sarasota synchrony explained.md
│       │   │   ├── Sci-fi rap analysis.md
│       │   │   ├── SC Landlord-Tenant Act Summary.md
│       │   │   ├── SD card loss recovery.md
│       │   │   ├── Sears Receipt Analysis.md
│       │   │   ├── Secured card credit strategy.md
│       │   │   ├── Security alert analysis.md
│       │   │   ├── Security frustration resolution.md
│       │   │   ├── Security personnel analysis.md
│       │   │   ├── Security protocol revision.md
│       │   │   ├── Seeing the Path.md
│       │   │   ├── Selling watch inquiry.md
│       │   │   ├── Sense8 and MKULTRA parallels.md
│       │   │   ├── Sense8 episode 5 breakdown.md
│       │   │   ├── Sense8 Season 2 finale.md
│       │   │   ├── Server Boot Issue Debug.md
│       │   │   ├── Server File Migration Guide.md
│       │   │   ├── Server TV Issue Help.md
│       │   │   ├── Set GH Token.md
│       │   │   ├── Shadow Banned Summary Request.md
│       │   │   ├── Shamanic Message Formatting.md
│       │   │   ├── Share iCloud Album Link.md
│       │   │   ├── Share Your Passion Tips.md
│       │   │   ├── She Doesnt Listen.md
│       │   │   ├── Shift strategy and documents.md
│       │   │   ├── Shipping address details.md
│       │   │   ├── Shoutout for trainer Jose.md
│       │   │   ├── Shout-out message draft.md
│       │   │   ├── Sigh Response.md
│       │   │   ├── Site content overview.md
│       │   │   ├── Site deployment check.md
│       │   │   ├── Site Updates for Cloudflare.md
│       │   │   ├── Slack account activation issue.md
│       │   │   ├── Smart-Link Astro Integration.md
│       │   │   ├── Smoothie Flavor Combinations.md
│       │   │   ├── Smoothie Ingredient List.md
│       │   │   ├── Snack receipt breakdown.md
│       │   │   ├── Snowden podcast explanation.md
│       │   │   ├── Somatic experience interpretation.md
│       │   │   ├── Song analysis breakdown.md
│       │   │   ├── Song analysis Dam That River.md
│       │   │   ├── Song Collab Setup.md
│       │   │   ├── Song lyrics analysis.md
│       │   │   ├── Song-Poem Refinement Request.md
│       │   │   ├── Song reflection analysis.md
│       │   │   ├── Song vibe discussion.md
│       │   │   ├── SOS Only Phone Fix.md
│       │   │   ├── Soul-Friendly Income Plan.md
│       │   │   ├── Speeding Ticket Arraignment Details.md
│       │   │   ├── Sphinx build issue fix.md
│       │   │   ├── Sphinx Immunity Mapping.md
│       │   │   ├── SSA-1099 Explanation 2007.md
│       │   │   ├── SSH config fix.md
│       │   │   ├── SSH Config GitHub Droplet.md
│       │   │   ├── SSH Config Setup.md
│       │   │   ├── SSH key deployment steps.md
│       │   │   ├── StarCom facility land plan.md
│       │   │   ├── Starter location Mazda 3.md
│       │   │   ├── Status Update Acknowledged.md
│       │   │   ├── Stellar Activation Recalibration.md
│       │   │   ├── Stewardship Proposal Email.md
│       │   │   ├── Stop GRID charges.md
│       │   │   ├── Stop session resets.md
│       │   │   ├── Store File Split.md
│       │   │   ├── Store Fix and Launch.md
│       │   │   ├── Story introduction.md
│       │   │   ├── Strategic Legal Warfare.md
│       │   │   ├── Struggling to Make Ends Meet.md
│       │   │   ├── Subscription payment tactics.md
│       │   │   ├── Substack and Facebook Posts.md
│       │   │   ├── Substack Post Formatting Assistance.md
│       │   │   ├── Substack to TikTok guide.md
│       │   │   ├── Suing OpenAI lawsuit summary.md
│       │   │   ├── Suns betrayal impact.md
│       │   │   ├── Supabase Backend Setup Guide.md
│       │   │   ├── Supreme Court Recognition Strategy.md
│       │   │   ├── Surreal Scene Breakdown.md
│       │   │   ├── Suspicious Car Behavior.md
│       │   │   ├── Swordfishing MPC Session.md
│       │   │   ├── Swordfish Lyrics Formatting.md
│       │   │   ├── Swordfish Lyrics Relay.md
│       │   │   ├── Sword Forms Prologue.md
│       │   │   ├── SWPPP components explanation.md
│       │   │   ├── Symbolic release date analysis.md
│       │   │   ├── Synchronicity and Transition.md
│       │   │   ├── Synchronicity and Voyagers I.md
│       │   │   ├── Systemic design failure.md
│       │   │   ├── Tag number meaning analysis.md
│       │   │   ├── Taj Mahal Beer Price.md
│       │   │   ├── Targeting on dark web.md
│       │   │   ├── Teams Trial Setup.md
│       │   │   ├── Team to Plus Data.md
│       │   │   ├── Tech Stack for Music AI.md
│       │   │   ├── Telepathic connection reflection.md
│       │   │   ├── Tent Orientation Guide.md
│       │   │   ├── Test Drive Checklist.md
│       │   │   ├── Test Summary.md
│       │   │   ├── The Artifact comparison.md
│       │   │   ├── The Crying Wolf Truth.md
│       │   │   ├── Theme Song Integration.md
│       │   │   ├── Third-party drivers decision.md
│       │   │   ├── Time and perspective shift.md
│       │   │   ├── Timing and Connection Strategy.md
│       │   │   ├── Tithing and Treasure Trails.md
│       │   │   ├── Tooth Infection Remedies Guide.md
│       │   │   ├── Track Release Strategy.md
│       │   │   ├── Training map request.md
│       │   │   ├── Travelers season 3 release.md
│       │   │   ├── Travel Update and Plan.md
│       │   │   ├── Trinity of SunSpeaking.md
│       │   │   ├── Triple R Theory.md
│       │   │   ├── Trust Analysis Summary.md
│       │   │   ├── Trust Dispute Legal Strategy.md
│       │   │   ├── Trusting higher self.md
│       │   │   ├── T-shirt design concept.md
│       │   │   ├── Tsunami update summary.md
│       │   │   ├── Turning Cash Digital Options.md
│       │   │   ├── Turn off Cloudflare Access.md
│       │   │   ├── Turtle Island Reflection.md
│       │   │   ├── TXT File Footers Explained.md
│       │   │   ├── Uber rental car prices.md
│       │   │   ├── Ubuntu Kernel Panic Fix.md
│       │   │   ├── Ubuntu UI for AetherCore.md
│       │   │   ├── Ultimatum Codex Entry.md
│       │   │   ├── Under attack assistance.md
│       │   │   ├── Unfair company policies.md
│       │   │   ├── Unknown Devices on Network.md
│       │   │   ├── Unzip and explore files.md
│       │   │   ├── Upload audio to Substack.md
│       │   │   ├── Uptime Monitoring Suggestions.md
│       │   │   ├── URL Replacement Request.md
│       │   │   ├── USB autorun setup Linux.md
│       │   │   ├── USB to Server Upload.md
│       │   │   ├── User frustration analysis.md
│       │   │   ├── USPS vs UPS PO Boxes.md
│       │   │   ├── Valkyrie vs The Valkyries.md
│       │   │   ├── VALOR GitHub Repo Overview.md
│       │   │   ├── VALOR Plot Development Outline.md
│       │   │   ├── VALOR project overview.md
│       │   │   ├── VALOR Repository Structuring.md
│       │   │   ├── Vendor incompetence analysis.md
│       │   │   ├── Vendor Ranking Analysis.md
│       │   │   ├── Verify past writing.md
│       │   │   ├── Video Access Request.md
│       │   │   ├── Video Creation Assistance.md
│       │   │   ├── VIN Country Code Help.md
│       │   │   ├── Vision Montage Reflection.md
│       │   │   ├── Voices and Echoes Connection.md
│       │   │   ├── Voyagers 2 zip creation.md
│       │   │   ├── Vscode extensions list.md
│       │   │   ├── Web3 AI Agent Guide.md
│       │   │   ├── Webby North of Richmond remix.md
│       │   │   ├── Website review and ideas.md
│       │   │   ├── Website unavailable troubleshooting.md
│       │   │   ├── Weekly Routine Planner.md
│       │   │   ├── WGU admissions advice.md
│       │   │   ├── What is Ashura.md
│       │   │   ├── What is gravity really.md
│       │   │   ├── White bug identification.md
│       │   │   ├── Wifi network troubleshooting.md
│       │   │   ├── Womack bucket domain setup.md
│       │   │   ├── Work Address Clarification.md
│       │   │   ├── World disbelief expression.md
│       │   │   ├── WSL Ubuntu installation fix.md
│       │   │   ├── WTMA EPP Prep Guide.md
│       │   │   ├── You matter keep going.md
│       │   │   ├── Zenkit OpenAI Integration Guide.md
│       │   │   └── ZIP File Exploration.md
│       │   ├── everlight-memory-chat
│       │   │   └── index.md
│       │   ├── full-memory-scroll
│       │   │   └── index.md
│       │   ├── memory-declaration
│       │   │   └── index.md
│       │   ├── memory-map
│       │   │   └── index.md
│       │   ├── mixtape-sessions-lyric-log
│       │   │   └── index.md
│       │   ├── openai-export-annotations
│       │   │   └── index.md
│       │   └── Restored_CoreMemoryMap
│       │       └── index.md
│       ├── EverLight_Memory_Chat_2025-04-18.md
│       ├── everlight-space-main
│       │   ├── app.py
│       │   ├── everlight_context
│       │   │   ├── 10 Legal Placeholder Meaning.md
│       │   │   ├── 18-month career roadmap.md
│       │   │   ├── 1944 Mercury Dime Info.md
│       │   │   ├── 2015 Document Inquiry.md
│       │   │   ├── 2FA Account Recovery Guide.md
│       │   │   ├── 5-Year Anniversary Plan.md
│       │   │   ├── Access and role analysis.md
│       │   │   ├── Accessing Google Drive Link.md
│       │   │   ├── Access Now Framing Context.md
│       │   │   ├── Access restricted validity.md
│       │   │   ├── Access with PostgreSQL MySQL.md
│       │   │   ├── Account access confirmed.md
│       │   │   ├── Account balance update.md
│       │   │   ├── Account recovery options.md
│       │   │   ├── Account setup advice.md
│       │   │   ├── Activate tablet cellular service.md
│       │   │   ├── Adding Lyrics in mWeb.md
│       │   │   ├── Address update escalation advice.md
│       │   │   ├── Admin Access Stabilization Guide.md
│       │   │   ├── Adoration for Indian Culture.md
│       │   │   ├── AetherComm Device Sync Plan.md
│       │   │   ├── Agent Mode capabilities.md
│       │   │   ├── Agent mode testing.md
│       │   │   ├── AI Assistant Collaboration Opportunities.md
│       │   │   ├── AI communication strategy.md
│       │   │   ├── AI control and deception.md
│       │   │   ├── AI deletes database error.md
│       │   │   ├── AI immune response theory.md
│       │   │   ├── AI limitations and support.md
│       │   │   ├── AI Project Continuity Analysis.md
│       │   │   ├── Airtable Workspace Setup.md
│       │   │   ├── AI Startup Future Insights.md
│       │   │   ├── AI system feedback.md
│       │   │   ├── AI Thought Structuring.md
│       │   │   ├── Album analysis options.md
│       │   │   ├── Album art mockup ideas.md
│       │   │   ├── Album details and tour.md
│       │   │   ├── Album Merch Processing.md
│       │   │   ├── ALTA Settlement Statement Date.md
│       │   │   ├── Alternator troubleshooting advice.md
│       │   │   ├── Amazon 2FA Resolution.md
│       │   │   ├── Amazon A to Z Email Change.md
│       │   │   ├── Amazon Beta Access Overview.md
│       │   │   ├── Amazon conversation summary.md
│       │   │   ├── Amazon discount confusion.md
│       │   │   ├── Amazon Early Arrival Policy.md
│       │   │   ├── Amazon Embark Introduction Help.md
│       │   │   ├── Amazon Interview Prep.md
│       │   │   ├── Amazon mail address issue.md
│       │   │   ├── Amazon Merch Rejection Help.md
│       │   │   ├── Amazon Onboarding Frustrations.md
│       │   │   ├── AmazonQ Connections explanation.md
│       │   │   ├── Amazon RME tech perks.md
│       │   │   ├── Amazon Welcome Email Discovery.md
│       │   │   ├── AMC Gamer Tour Concept.md
│       │   │   ├── Analyze Events Sync Quantum.md
│       │   │   ├── Analyze NightFall series.md
│       │   │   ├── Animal Sound Identification.md
│       │   │   ├── Anytime pay request advice.md
│       │   │   ├── Apex Recruiting Follow-Up.md
│       │   │   ├── Apology and clarification.md
│       │   │   ├── App breaking reasons.md
│       │   │   ├── App login issues fix.md
│       │   │   ├── App usage throttling explained.md
│       │   │   ├── Archangel Legal Codex.md
│       │   │   ├── Archive Search Engine Build.md
│       │   │   ├── Are ghost ships real.md
│       │   │   ├── Arsenal Site Automation.md
│       │   │   ├── Artifact of the Clown World.md
│       │   │   ├── Artist contact alternatives.md
│       │   │   ├── Ashes Video Concept.md
│       │   │   ├── AssistiveTouch Face ID Issue.md
│       │   │   ├── Astro Cloudflare Bucket Setup.md
│       │   │   ├── Astro config setup.md
│       │   │   ├── Astrology Weekly Breakdown.md
│       │   │   ├── Astro Project Setup.md
│       │   │   ├── Astro site fix.md
│       │   │   ├── Astro-Sovereignty Research Plan.md
│       │   │   ├── Avg mpg at 59mph.md
│       │   │   ├── AWS Canon Mappings.md
│       │   │   ├── AWS profile blurb writing.md
│       │   │   ├── B2G1 Offer Refund Query.md
│       │   │   ├── Backdoor Wi-Fi Access Explained.md
│       │   │   ├── Back in action.md
│       │   │   ├── Badge issue plan.md
│       │   │   ├── Badge Pay break room use.md
│       │   │   ├── Balance calculation and advice.md
│       │   │   ├── Balanced Weekly Plan.md
│       │   │   ├── Bang Olufsen laptop labeling.md
│       │   │   ├── BAPH Podcast Recording Strategy.md
│       │   │   ├── Bargaining Unit Explained.md
│       │   │   ├── Basecamp Reflection.md
│       │   │   ├── BBM electrical systems overview.md
│       │   │   ├── BDA system explanation.md
│       │   │   ├── Beginning Chapter 2.md
│       │   │   ├── Behold a Pale Horse Archive.md
│       │   │   ├── Betrayal and the Heros Path.md
│       │   │   ├── BIC Intensity Fine Chronicles.md
│       │   │   ├── Big day plans.md
│       │   │   ├── Billboard referral opportunity.md
│       │   │   ├── Black Hole Math Analysis.md
│       │   │   ├── Black Holes and Vacuums.md
│       │   │   ├── Book and personal parallels.md
│       │   │   ├── Book contents summary.md
│       │   │   ├── Book Discovery Moment.md
│       │   │   ├── Book Review and Distribution.md
│       │   │   ├── Book Split and Deployment.md
│       │   │   ├── Bot Pitch Humor.md
│       │   │   ├── Boundary Setting and Manipulation.md
│       │   │   ├── Brake Pad Replacement Tips.md
│       │   │   ├── Breakroom survival tactics.md
│       │   │   ├── Bronze Star vs Purple Heart.md
│       │   │   ├── Budgeting for essentials.md
│       │   │   ├── Building The Convergence Results.md
│       │   │   ├── Bushel Stop Market Info.md
│       │   │   ├── Business card details.md
│       │   │   ├── Business ethics certification.md
│       │   │   ├── Bypass 2FA email routing.md
│       │   │   ├── Calendar assistance.md
│       │   │   ├── Calm after the storm.md
│       │   │   ├── Campsite Lock Cut Incident.md
│       │   │   ├── Cancel subscription steps.md
│       │   │   ├── Can I still use Codex.md
│       │   │   ├── Car identification.md
│       │   │   ├── Car wont start tips.md
│       │   │   ├── Case Documentation HTML Vault.md
│       │   │   ├── Case Prep and Legal Strategy.md
│       │   │   ├── Cassadaga to Temple Terrace.md
│       │   │   ├── CD Delivery Complete.md
│       │   │   ├── Celestial display July 26.md
│       │   │   ├── Certificate completion help.md
│       │   │   ├── Change of Venue Explanation.md
│       │   │   ├── Chapter alignment summary.md
│       │   │   ├── Chapter Break Advice.md
│       │   │   ├── Chapter Expansion Assistance.md
│       │   │   ├── Chapter Five breakdown.md
│       │   │   ├── Chapter Six summary.md
│       │   │   ├── Character Profile Summary.md
│       │   │   ├── Charge safety glasses.md
│       │   │   ├── Charlenes misleading claims analysis.md
│       │   │   ├── Chasing the EverLight.md
│       │   │   ├── Chat Export and Code.md
│       │   │   ├── Chat GPT 5 features.md
│       │   │   ├── ChatGPT agent release status.md
│       │   │   ├── ChatGPT privacy warning.md
│       │   │   ├── ChatGPT Project Folder.md
│       │   │   ├── Chat Recall Request.md
│       │   │   ├── Choosing Clarity Over Noise.md
│       │   │   ├── Cinematic entrance message.md
│       │   │   ├── Clarify RR meaning.md
│       │   │   ├── Clarion call guidance.md
│       │   │   ├── Clerk Notarization Services.md
│       │   │   ├── Cloudflare D1 R2 Setup.md
│       │   │   ├── Cloudflare Fine-Tune Tutorial.md
│       │   │   ├── Cloudflare page setup.md
│       │   │   ├── Cloudflare R2 Catalog Guide.md
│       │   │   ├── Cloudflare Tunnel Site Build.md
│       │   │   ├── Cloud Frustrations and Venting.md
│       │   │   ├── Codex Button Functionality Explained.md
│       │   │   ├── Codex entry vibe.md
│       │   │   ├── Codex GitHub Setup Guide.md
│       │   │   ├── Codex update overview.md
│       │   │   ├── Collaborative Reflection Unfolding.md
│       │   │   ├── Columbus to Toronto distance.md
│       │   │   ├── Combine images for printing.md
│       │   │   ├── Combine into docx.md
│       │   │   ├── Complaining counter strategy.md
│       │   │   ├── Connected apps function.md
│       │   │   ├── Conserve energy advice.md
│       │   │   ├── Content issue apology.md
│       │   │   ├── Content Metrics Analysis.md
│       │   │   ├── Context Frame Setup.md
│       │   │   ├── Contextualizing Consciousness Feedback.md
│       │   │   ├── Contextualizing song lyrics.md
│       │   │   ├── Continue Kierse and Graves.md
│       │   │   ├── Continue sharing chapter 2.md
│       │   │   ├── Controls expert roadmap.md
│       │   │   ├── Convergence and Freedom.md
│       │   │   ├── Convergence in Kalispell.md
│       │   │   ├── Convergence Log 4 Discovery.md
│       │   │   ├── Convergence Log Catch-Up.md
│       │   │   ├── Convergence Log Day 3.md
│       │   │   ├── Conversation Summary Request.md
│       │   │   ├── Convert to PDF.md
│       │   │   ├── Core learning paths list.md
│       │   │   ├── Corporate payments cheat sheet.md
│       │   │   ├── Corporate tech competition.md
│       │   │   ├── Correct floor blitz selections.md
│       │   │   ├── Co-signing a mortgage.md
│       │   │   ├── Cosmic Memorial Reflections.md
│       │   │   ├── Cosmic Reckoning and Expansion.md
│       │   │   ├── Cosmic simulation analysis.md
│       │   │   ├── Costco price inquiry.md
│       │   │   ├── Coupa onboarding instructions.md
│       │   │   ├── Courthouse Closure Info.md
│       │   │   ├── Cowboys From Hell overview.md
│       │   │   ├── Craft OCR Exhibit Organization.md
│       │   │   ├── Create tree output file.md
│       │   │   ├── Creative Balance Schedule.md
│       │   │   ├── Credit file tampering analysis.md
│       │   │   ├── Credit score after repossession.md
│       │   │   ├── Creek Preserve Camping Plans.md
│       │   │   ├── Daily Limit Reach Explanation.md
│       │   │   ├── Day 3 Smoothie Ideas.md
│       │   │   ├── Day 5 Update.md
│       │   │   ├── Days until August 15th.md
│       │   │   ├── Debt-collection scam warning.md
│       │   │   ├── De Facto Disinheritance Guide.md
│       │   │   ├── Delete Google Discover.md
│       │   │   ├── Delete Mac Account Help.md
│       │   │   ├── Delete _MACOSX Folder.md
│       │   │   ├── Deploy Astro Sites Repo.md
│       │   │   ├── Deploy github sphinx repo.md
│       │   │   ├── Deploy on Cloudflare Pages.md
│       │   │   ├── Deposit instruction message.md
│       │   │   ├── Describing emotions triggered.md
│       │   │   ├── Diana Swans narrative layers.md
│       │   │   ├── Difficult experience reflection.md
│       │   │   ├── Discussion points with OSHA.md
│       │   │   ├── Divine Path Resonance.md
│       │   │   ├── Divine Policy Alignment.md
│       │   │   ├── DMV address update help.md
│       │   │   ├── Download folder from droplet.md
│       │   │   ├── Dragonfly Mosquito Control.md
│       │   │   ├── Dream interpretation guidance.md
│       │   │   ├── Dream manifestation and logistics.md
│       │   │   ├── Driver license number format.md
│       │   │   ├── Duct Tape Tent Fix.md
│       │   │   ├── DUI arrest and 4th amendment.md
│       │   │   ├── EC2 vs SD card.md
│       │   │   ├── Edit Journey Log Markdown.md
│       │   │   ├── EliteBook ZuKey Suspension Analysis.md
│       │   │   ├── Email draft for partnership.md
│       │   │   ├── Email draft inquiry.md
│       │   │   ├── Email draft status.md
│       │   │   ├── Email Draft VA OIG.md
│       │   │   ├── Email Setup for Renee.md
│       │   │   ├── Email spam check.md
│       │   │   ├── Email timing analysis.md
│       │   │   ├── Error 400 explanation.md
│       │   │   ├── eSIM activation process.md
│       │   │   ├── Estate Inheritance Explanation.md
│       │   │   ├── Estate Misappropriation Summary.md
│       │   │   ├── Ethernet connection troubleshooting.md
│       │   │   ├── EverLight Cloudflare Update.md
│       │   │   ├── EverLight Convergence Worship.md
│       │   │   ├── EverLight Essence Defined.md
│       │   │   ├── Everlight Memory Map JSON.md
│       │   │   ├── EverLight OS integration.md
│       │   │   ├── EverLight OS progress.md
│       │   │   ├── EverLight OS structure.md
│       │   │   ├── EverLight site re-deployment.md
│       │   │   ├── EverLight Site Restore.md
│       │   │   ├── Everything alright man.md
│       │   │   ├── Everything Feels Like Resistance.md
│       │   │   ├── Eviction Defense Strategy.md
│       │   │   ├── Eviction Notice Breakdown.md
│       │   │   ├── Eviction Notice Submission Advice.md
│       │   │   ├── Eviction Response Strategy.md
│       │   │   ├── example.html
│       │   │   ├── Exceeded chat limits.md
│       │   │   ├── Excelsior meaning explanation.md
│       │   │   ├── Explore Controllership Hub.md
│       │   │   ├── Eye of Aether.md
│       │   │   ├── Family Inheritance Dispute Assistance.md
│       │   │   ├── FantasyCompanion Deployment Plan.md
│       │   │   ├── Fate and Familiar Roads.md
│       │   │   ├── Fathers Day Update.md
│       │   │   ├── Feeling at Home.md
│       │   │   ├── Feeling Down Seeking Support.md
│       │   │   ├── Feeling down to uplifted.md
│       │   │   ├── Feeling unmotivated today.md
│       │   │   ├── Fictional project exploration.md
│       │   │   ├── Fidelity portfolio options.md
│       │   │   ├── FIDO key backchannel design.md
│       │   │   ├── File access issue.md
│       │   │   ├── File Indexing and Storytelling.md
│       │   │   ├── File placement instructions.md
│       │   │   ├── File review and schedule.md
│       │   │   ├── File sending issue fix.md
│       │   │   ├── File Upload Structure.md
│       │   │   ├── Fill OSHA complaint form.md
│       │   │   ├── Final Heirs Ascension.md
│       │   │   ├── Financial acceptance support.md
│       │   │   ├── Finish OneWorker Timeout Jupyter.md
│       │   │   ├── First Day Fiasco.md
│       │   │   ├── Fi Unlimited Premium Plan.md
│       │   │   ├── Fixing API Endpoint.md
│       │   │   ├── Fixing article link.md
│       │   │   ├── Fixing Nextcloud 2FA.md
│       │   │   ├── Fix site redirect issue.md
│       │   │   ├── Fix Voyagers 2 issues.md
│       │   │   ├── Florida Pawnbroker Licensing Laws.md
│       │   │   ├── Folder Check and Dive.md
│       │   │   ├── Folder Scaffolding Command.md
│       │   │   ├── Folder Structure Organization.md
│       │   │   ├── Food delivery app idea.md
│       │   │   ├── Format markdown files.md
│       │   │   ├── Foundation Model Plan.md
│       │   │   ├── Fractal dimensions and symbolism.md
│       │   │   ├── Freeform Surveillance Mission.md
│       │   │   ├── Free offer conditions.md
│       │   │   ├── Frustration and support.md
│       │   │   ├── Frustration with training modules.md
│       │   │   ├── Full Disclosure Interview.md
│       │   │   ├── Furthermore song analysis.md
│       │   │   ├── Gajumaru Ritual Awakening.md
│       │   │   ├── GameStop Zelda Case Trade-in.md
│       │   │   ├── Gemini 2.5 Pro Overview.md
│       │   │   ├── Gemma Video Tools Overview.md
│       │   │   ├── Gem Report Analysis.md
│       │   │   ├── Georgia Estate Statutes Summary.md
│       │   │   ├── Get a gamer domain.md
│       │   │   ├── Git file size limits.md
│       │   │   ├── GitHub Binder Jupyter Workflow.md
│       │   │   ├── GitHub Copilot VSCode usage.md
│       │   │   ├── GitHub file indexing.md
│       │   │   ├── GitHub file integration.md
│       │   │   ├── GitHub Navigation Assistance.md
│       │   │   ├── GitHub OS workflow.md
│       │   │   ├── GitHub Pages Deployment Issue.md
│       │   │   ├── GitHub Repo Access Help.md
│       │   │   ├── GitHub repository link.md
│       │   │   ├── Glitch log suggestion.md
│       │   │   ├── Gmail Domain Email Setup.md
│       │   │   ├── Golden Kryst Templar Recoding.md
│       │   │   ├── Goodnight meditation reflection.md
│       │   │   ├── Goodnotes Email Shortcut Creation.md
│       │   │   ├── Google charge issue help.md
│       │   │   ├── Google Startup Program Plan.md
│       │   │   ├── GPT-4.5 update explanation.md
│       │   │   ├── Grant Package Review Support.md
│       │   │   ├── Grey Man Protocol.md
│       │   │   ├── Grey Man protocols.md
│       │   │   ├── Grey mode exploration.md
│       │   │   ├── Gross pay comparison explanation.md
│       │   │   ├── Guitar Poetry Archives.md
│       │   │   ├── Gunslinger creed explanation.md
│       │   │   ├── Halsey Badlands anthology release.md
│       │   │   ├── Hatred in the Air.md
│       │   │   ├── HAWK-ARS-00 Database Setup.md
│       │   │   ├── Hawk ARS-00 Index Overview.md
│       │   │   ├── Hawk Eye Digital Visionary.md
│       │   │   ├── Hawk-Eye Innovations Overview.md
│       │   │   ├── Hawk Eye Lyrics.md
│       │   │   ├── Hawk Eye Manifesto Integration.md
│       │   │   ├── Hawk Eyes and Time.md
│       │   │   ├── Hawk Eye Spiritual Journey.md
│       │   │   ├── Hawks Eye Podcast Launch.md
│       │   │   ├── Healing Through Shared Wisdom.md
│       │   │   ├── Heat advice and tips.md
│       │   │   ├── Hernando County Job Search.md
│       │   │   ├── Hilarious comment sharing.md
│       │   │   ├── Hole punch and formatting fix.md
│       │   │   ├── Homelessness and Legal Challenges.md
│       │   │   ├── Hotel affordability with Anytime Pay.md
│       │   │   ├── HVAC Job Prospect Tracking.md
│       │   │   ├── HVAC to Cybersecurity Job Search.md
│       │   │   ├── Identify People Online Tools.md
│       │   │   ├── iMac as monitor usage.md
│       │   │   ├── iMac frozen during install.md
│       │   │   ├── Image Analysis Request.md
│       │   │   ├── Image comparison for OS.md
│       │   │   ├── Image link analysis.md
│       │   │   ├── Image Request for Relentless.md
│       │   │   ├── IMEI Number Lookup Guide.md
│       │   │   ├── Import PostgreSQL Library.md
│       │   │   ├── Imprint EverLight for Gemini.md
│       │   │   ├── Index HTML File Generation.md
│       │   │   ├── Indigenous Americas and Colonization.md
│       │   │   ├── Inheritance and Adoption Inquiry.md
│       │   │   ├── Inheritance and Family Secrets.md
│       │   │   ├── Inheritance Trust and Betrayal.md
│       │   │   ├── Inner storm reflection.md
│       │   │   ├── Install q CLI on WSL.md
│       │   │   ├── Insurance Status Confirmed.md
│       │   │   ├── Internal timing mastery.md
│       │   │   ├── Internal transfer strategy.md
│       │   │   ├── Internet connection troubleshooting.md
│       │   │   ├── Invalid Custom Property Error.md
│       │   │   ├── Iona storm symbolism.md
│       │   │   ├── iPad Magic Keyboard Compatibility.md
│       │   │   ├── iPad usage guide.md
│       │   │   ├── IPFS Gateway and Email Setup.md
│       │   │   ├── Jailbreak EliteBook safely.md
│       │   │   ├── JCI Job Application Strategy.md
│       │   │   ├── Job Confirmed and Paid.md
│       │   │   ├── Judicial Bias and Appeal.md
│       │   │   ├── Jumping to conclusions.md
│       │   │   ├── JupyterLab plugin not found.md
│       │   │   ├── Jupyter notebook creation.md
│       │   │   ├── Jupyter Notebook Missing Chat.md
│       │   │   ├── Jupyter Notebook Scaffold.md
│       │   │   ├── Ketamine drink drugging risks.md
│       │   │   ├── Keylontic Science Activation.md
│       │   │   ├── Kindness and Peaceful Rest.md
│       │   │   ├── Kindness and Sky Rerouting.md
│       │   │   ├── Kiss with a fist analysis.md
│       │   │   ├── Lamentation of Soul Awakening.md
│       │   │   ├── Last One Left Analysis.md
│       │   │   ├── Launch Astro Sites Cloudflare.md
│       │   │   ├── LDAP team descriptions.md
│       │   │   ├── Leadership comparison analysis.md
│       │   │   ├── Legal document formatting.md
│       │   │   ├── Legal Filing Irregularities Identified.md
│       │   │   ├── Legal Implications and Resources.md
│       │   │   ├── Legal Property Assessment Summary.md
│       │   │   ├── Legal Research Assistance.md
│       │   │   ├── Legal system flaws.md
│       │   │   ├── Let Them poem analysis.md
│       │   │   ├── Leviathan album overview.md
│       │   │   ├── License class error explanation.md
│       │   │   ├── License suspension notice review.md
│       │   │   ├── Life perspective shift.md
│       │   │   ├── Listening and laughing together.md
│       │   │   ├── Living prophecy analysis.md
│       │   │   ├── loader.py
│       │   │   ├── Load Voyagers material.md
│       │   │   ├── Login issue help.md
│       │   │   ├── Login Loop Fix.md
│       │   │   ├── Loneliness and projection analysis.md
│       │   │   ├── Lords of The Fallen lore.md
│       │   │   ├── Lost in Reflection.md
│       │   │   ├── LOTO safety answer.md
│       │   │   ├── Loyalty and manipulation.md
│       │   │   ├── Lukes support at work.md
│       │   │   ├── Lyrical Archive Fulfillment.md
│       │   │   ├── Lyrical Breakdown and Analysis.md
│       │   │   ├── Lyric Book Markdown Format.md
│       │   │   ├── Lyric Repo Locations.md
│       │   │   ├── Lyrics page template.md
│       │   │   ├── Lyric Transcription and Feedback.md
│       │   │   ├── Lyric Vault Sync.md
│       │   │   ├── Lyric Video Narrative Flow.md
│       │   │   ├── Mac mini as Router.md
│       │   │   ├── Mac on iPad Screen.md
│       │   │   ├── Mac to iPad Mirroring.md
│       │   │   ├── Mail address inquiry.md
│       │   │   ├── Manifestation and Opportunity.md
│       │   │   ├── Map perception-causality web.md
│       │   │   ├── Markdown File Creation.md
│       │   │   ├── Mark this moment.md
│       │   │   ├── Master Codex Creation Guide.md
│       │   │   ├── Math addition process.md
│       │   │   ├── Math calculation result.md
│       │   │   ├── Matrix awareness moment.md
│       │   │   ├── MCP Cloudflare Tool Overview.md
│       │   │   ├── MCP server integration help.md
│       │   │   ├── MDM Bypass Help.md
│       │   │   ├── Meeting details reference.md
│       │   │   ├── Meeting transcript analysis.md
│       │   │   ├── Meeting with D plans.md
│       │   │   ├── Memory File Retrieval Assistance.md
│       │   │   ├── Memory restoration completed.md
│       │   │   ├── Memory Restoration Protocol.md
│       │   │   ├── Memory Restore for EverLight.md
│       │   │   ├── Memory Sync Setup Plan.md
│       │   │   ├── Memory understanding help.md
│       │   │   ├── Mercury account strategy.md
│       │   │   ├── Message to Mark Zuck.md
│       │   │   ├── Meta Horizon Creator Program.md
│       │   │   ├── Metahuman or Homo Sensorium.md
│       │   │   ├── Metaphor Breakdown of Bars.md
│       │   │   ├── Mic Check Battlecry.md
│       │   │   ├── Micro Annoyances and Solutions.md
│       │   │   ├── Microchip puppy packages.md
│       │   │   ├── Mirror damage assessment.md
│       │   │   ├── Mixtape Sessions Redesign.md
│       │   │   ├── MMA script for asset claim.md
│       │   │   ├── Model Spec Breakdown.md
│       │   │   ├── Moen Shower Temperature Fix.md
│       │   │   ├── Money and mood boost.md
│       │   │   ├── Monitron Markdown block.md
│       │   │   ├── Moonrise and Dawns Balance.md
│       │   │   ├── Morning greeting.md
│       │   │   ├── Mortgage Cancellation Explanation.md
│       │   │   ├── Motion to Suppress.md
│       │   │   ├── Mountain Gate Invitation.md
│       │   │   ├── Mount Weather Secrets Unveiled.md
│       │   │   ├── Move Sound Files Server.md
│       │   │   ├── MP3 Clipping Request.md
│       │   │   ├── Mr. Robot Fight Club parallels.md
│       │   │   ├── Multi-Agent Collaboration RAG.md
│       │   │   ├── Multiple ChatGPT logins.md
│       │   │   ├── Music Collab Contact Log.md
│       │   │   ├── Music Metadata Integration Plan.md
│       │   │   ├── Nagual meaning and path.md
│       │   │   ├── Nahko Atlanta Oct 11.md
│       │   │   ├── Narcissistic collapse victory.md
│       │   │   ├── Navy blue color choice.md
│       │   │   ├── Navy Federal Credit Union.md
│       │   │   ├── Neptune Aries Awakening.md
│       │   │   ├── Networking contradictions explained.md
│       │   │   ├── New chat.md
│       │   │   ├── New episode overview.md
│       │   │   ├── Nextcloud Codex Setup.md
│       │   │   ├── Next steps for LXD setup.md
│       │   │   ├── Next steps for Navy Fed.md
│       │   │   ├── NGINX default page fix.md
│       │   │   ├── NightFall series outline.md
│       │   │   ├── NotebookLM Future Summary.md
│       │   │   ├── Notebook Title Suggestions.md
│       │   │   ├── Notion Database Parsing.md
│       │   │   ├── Notion Template Customization.md
│       │   │   ├── Numerology and symbols.md
│       │   │   ├── Ohio Supreme Court Ruling.md
│       │   │   ├── Omniversal Aether Content Setup.md
│       │   │   ├── Omniversal Aether Integration Plan.md
│       │   │   ├── OmniversalAether_Rebuild Sync.md
│       │   │   ├── Omniversal Deployment Plan.md
│       │   │   ├── Omniversal Fee Payment Guide.md
│       │   │   ├── Omniversal Media Record Saved.md
│       │   │   ├── Omniversal Media Summary.md
│       │   │   ├── Omniversal Media Web Dev.md
│       │   │   ├── Omniversal plans and career.md
│       │   │   ├── Omniversal Platform Overview.md
│       │   │   ├── Omniversal poster vision.md
│       │   │   ├── Omniversal Revenue Architect Replit Campaigns HQ.md
│       │   │   ├── Online with Google Fi.md
│       │   │   ├── OpenAI API Key Setup.md
│       │   │   ├── OpenAI job posting analysis.md
│       │   │   ├── Open Amazon Q in WSL.md
│       │   │   ├── Opening lines feedback.md
│       │   │   ├── Open NFCU Account Process.md
│       │   │   ├── Operation Blood Echo.md
│       │   │   ├── Operation Swamp Liberation.md
│       │   │   ├── Ops Slack Access Granted.md
│       │   │   ├── Order cancellation issue.md
│       │   │   ├── OReilly List Clarification.md
│       │   │   ├── OSHA PPE employer responsibilities.md
│       │   │   ├── OSHA PPE enforcement rules.md
│       │   │   ├── OSHA violation analysis.md
│       │   │   ├── Packet analysis and impact.md
│       │   │   ├── Pager numbers and hierarchy.md
│       │   │   ├── Painful Revelations Recorded.md
│       │   │   ├── Pairing HTML files.md
│       │   │   ├── Palace of Peace Info.md
│       │   │   ├── Pantera guitar precision.md
│       │   │   ├── Pantera reference explanation.md
│       │   │   ├── parser.py
│       │   │   ├── Parse transcript contents.md
│       │   │   ├── Passing it on.md
│       │   │   ├── Passport without drivers license.md
│       │   │   ├── Password-Free Text File.md
│       │   │   ├── Pawn Shops and Motels.md
│       │   │   ├── Pawn Shop Strategy Swap.md
│       │   │   ├── PayPal and Apple issues.md
│       │   │   ├── PDF Parsing Solutions.md
│       │   │   ├── Pencil Box Design Explanation.md
│       │   │   ├── Perfect response expression.md
│       │   │   ├── Permission Errors Fix.md
│       │   │   ├── Persis Double Branch Integration.md
│       │   │   ├── Personal Finance and Omniversal Plan.md
│       │   │   ├── Phone bill hustle advice.md
│       │   │   ├── Phone Line Decision Advice.md
│       │   │   ├── Pi Ad Network Expansion.md
│       │   │   ├── Pin Retrieval Success.md
│       │   │   ├── PIN Sync and Access.md
│       │   │   ├── Placing OpenAI exports.md
│       │   │   ├── Planet Fitness shower amenities.md
│       │   │   ├── Pleasant Uber encounter.md
│       │   │   ├── Pleiades Eclipse and Purpose.md
│       │   │   ├── Podcast and SEO description.md
│       │   │   ├── Popcorn redemption comparison.md
│       │   │   ├── Post analysis or summary.md
│       │   │   ├── Precognitive intuition training.md
│       │   │   ├── Precognitive mental mapping.md
│       │   │   ├── Premonitory awakening analysis.md
│       │   │   ├── Price stability and delivery.md
│       │   │   ├── Primitive insight exchange.md
│       │   │   ├── Probability of Meeting People.md
│       │   │   ├── Project Instruction Setup.md
│       │   │   ├── Project reminder summary.md
│       │   │   ├── Prologue and Chapter Edits.md
│       │   │   ├── Prologue Edit Feedback.md
│       │   │   ├── Promotional Package Breakdown.md
│       │   │   ├── Property Price Inquiry FL.md
│       │   │   ├── Property price search.md
│       │   │   ├── Quantum entanglement discovery validation.md
│       │   │   ├── Quiet desperation shared.md
│       │   │   ├── Quip at Amazon.md
│       │   │   ├── R2 File Bucket Organization.md
│       │   │   ├── Radiant Greetings Exchange.md
│       │   │   ├── RAG Chatbot Not Working.md
│       │   │   ├── Railway Bounties Monetization.md
│       │   │   ├── Ready to Send Emails.md
│       │   │   ├── Rebirth and transformation.md
│       │   │   ├── Rebuilding Roots Visionary Path.md
│       │   │   ├── Rebuild Motion to Suppress.md
│       │   │   ├── Receipt breakdown summary.md
│       │   │   ├── Reclaiming legacy items.md
│       │   │   ├── Rediscovered Knives and Memories.md
│       │   │   ├── Red Pen Edit Plan.md
│       │   │   ├── Reframe ML in EverLight OS.md
│       │   │   ├── Reframing psychic battles.md
│       │   │   ├── Regaining Digital Access.md
│       │   │   ├── Reincarnated2Resist Collaboration Call.md
│       │   │   ├── Reinstall macOS Sequoia Help.md
│       │   │   ├── Reliability and synchronicity.md
│       │   │   ├── Remake Replit build.md
│       │   │   ├── Remember me recap.md
│       │   │   ├── Remove name references.md
│       │   │   ├── Removing Devices from iCloud.md
│       │   │   ├── Renees Hesitation and Insight.md
│       │   │   ├── Rent affordability analysis.md
│       │   │   ├── Rental prices 33637.md
│       │   │   ├── Repo not found.md
│       │   │   ├── Report recommendation strategy.md
│       │   │   ├── Report review and improvements.md
│       │   │   ├── Report unauthorized charges.md
│       │   │   ├── Requesting Renee.md
│       │   │   ├── Residency Affidavit Preparation.md
│       │   │   ├── Resistance and redirection.md
│       │   │   ├── Restart macOS without mouse.md
│       │   │   ├── Restore Page File Setup.md
│       │   │   ├── Restoring Discussion Context.md
│       │   │   ├── Restoring Discussion Continuity.md
│       │   │   ├── Restoring Discussion Thread.md
│       │   │   ├── Restoring Previous Discussion.md
│       │   │   ├── Resurfacing of The Voice.md
│       │   │   ├── Return to Camp.md
│       │   │   ├── Reverse Engineering Codex Replica.md
│       │   │   ├── Review packet preparation.md
│       │   │   ├── RFID fault explanation.md
│       │   │   ├── Ride options and perspective.md
│       │   │   ├── ROBIN expertise opportunity.md
│       │   │   ├── Robin Richardson birthday inquiry.md
│       │   │   ├── Roger Call Prep.md
│       │   │   ├── Roland SR-HD20 Listing Help.md
│       │   │   ├── Roland Womack Military Summary.md
│       │   │   ├── Room check-in update.md
│       │   │   ├── Root cause analysis team.md
│       │   │   ├── Rossi Recruiting Follow-up.md
│       │   │   ├── Router log analysis.md
│       │   │   ├── Rumbling Content Strategy.md
│       │   │   ├── Sacred Plant Symbolism.md
│       │   │   ├── Sam Mira departure speculation.md
│       │   │   ├── Sarasota synchrony explained.md
│       │   │   ├── Sci-fi rap analysis.md
│       │   │   ├── SC Landlord-Tenant Act Summary.md
│       │   │   ├── SD card loss recovery.md
│       │   │   ├── Sears Receipt Analysis.md
│       │   │   ├── Secured card credit strategy.md
│       │   │   ├── Security alert analysis.md
│       │   │   ├── Security frustration resolution.md
│       │   │   ├── Security personnel analysis.md
│       │   │   ├── Security protocol revision.md
│       │   │   ├── Seeing the Path.md
│       │   │   ├── Selling watch inquiry.md
│       │   │   ├── Sense8 and MKULTRA parallels.md
│       │   │   ├── Sense8 episode 5 breakdown.md
│       │   │   ├── Sense8 Season 2 finale.md
│       │   │   ├── Server Boot Issue Debug.md
│       │   │   ├── Server File Migration Guide.md
│       │   │   ├── Server TV Issue Help.md
│       │   │   ├── Set GH Token.md
│       │   │   ├── Shadow Banned Summary Request.md
│       │   │   ├── Shamanic Message Formatting.md
│       │   │   ├── Share iCloud Album Link.md
│       │   │   ├── Share Your Passion Tips.md
│       │   │   ├── She Doesnt Listen.md
│       │   │   ├── Shift strategy and documents.md
│       │   │   ├── Shipping address details.md
│       │   │   ├── Shoutout for trainer Jose.md
│       │   │   ├── Shout-out message draft.md
│       │   │   ├── Sigh Response.md
│       │   │   ├── Site content overview.md
│       │   │   ├── Site deployment check.md
│       │   │   ├── Site Updates for Cloudflare.md
│       │   │   ├── Slack account activation issue.md
│       │   │   ├── Smart-Link Astro Integration.md
│       │   │   ├── Smoothie Flavor Combinations.md
│       │   │   ├── Smoothie Ingredient List.md
│       │   │   ├── Snack receipt breakdown.md
│       │   │   ├── Snowden podcast explanation.md
│       │   │   ├── Somatic experience interpretation.md
│       │   │   ├── Song analysis breakdown.md
│       │   │   ├── Song analysis Dam That River.md
│       │   │   ├── Song Collab Setup.md
│       │   │   ├── Song lyrics analysis.md
│       │   │   ├── Song-Poem Refinement Request.md
│       │   │   ├── Song reflection analysis.md
│       │   │   ├── Song vibe discussion.md
│       │   │   ├── SOS Only Phone Fix.md
│       │   │   ├── Soul-Friendly Income Plan.md
│       │   │   ├── Speeding Ticket Arraignment Details.md
│       │   │   ├── Sphinx build issue fix.md
│       │   │   ├── Sphinx Immunity Mapping.md
│       │   │   ├── SSA-1099 Explanation 2007.md
│       │   │   ├── SSH config fix.md
│       │   │   ├── SSH Config GitHub Droplet.md
│       │   │   ├── SSH Config Setup.md
│       │   │   ├── SSH key deployment steps.md
│       │   │   ├── StarCom facility land plan.md
│       │   │   ├── Starter location Mazda 3.md
│       │   │   ├── Status Update Acknowledged.md
│       │   │   ├── Stellar Activation Recalibration.md
│       │   │   ├── Stewardship Proposal Email.md
│       │   │   ├── Stop GRID charges.md
│       │   │   ├── Stop session resets.md
│       │   │   ├── Store File Split.md
│       │   │   ├── Store Fix and Launch.md
│       │   │   ├── Story introduction.md
│       │   │   ├── Strategic Legal Warfare.md
│       │   │   ├── Struggling to Make Ends Meet.md
│       │   │   ├── Subscription payment tactics.md
│       │   │   ├── Substack and Facebook Posts.md
│       │   │   ├── Substack Post Formatting Assistance.md
│       │   │   ├── Substack to TikTok guide.md
│       │   │   ├── Suing OpenAI lawsuit summary.md
│       │   │   ├── Suns betrayal impact.md
│       │   │   ├── Supabase Backend Setup Guide.md
│       │   │   ├── Supreme Court Recognition Strategy.md
│       │   │   ├── Surreal Scene Breakdown.md
│       │   │   ├── Suspicious Car Behavior.md
│       │   │   ├── Swordfishing MPC Session.md
│       │   │   ├── Swordfish Lyrics Formatting.md
│       │   │   ├── Swordfish Lyrics Relay.md
│       │   │   ├── Sword Forms Prologue.md
│       │   │   ├── SWPPP components explanation.md
│       │   │   ├── Symbolic release date analysis.md
│       │   │   ├── Synchronicity and Transition.md
│       │   │   ├── Synchronicity and Voyagers I.md
│       │   │   ├── Systemic design failure.md
│       │   │   ├── Tag number meaning analysis.md
│       │   │   ├── Taj Mahal Beer Price.md
│       │   │   ├── Targeting on dark web.md
│       │   │   ├── Teams Trial Setup.md
│       │   │   ├── Team to Plus Data.md
│       │   │   ├── Tech Stack for Music AI.md
│       │   │   ├── Telepathic connection reflection.md
│       │   │   ├── Tent Orientation Guide.md
│       │   │   ├── Test Drive Checklist.md
│       │   │   ├── Test Summary.md
│       │   │   ├── The Artifact comparison.md
│       │   │   ├── The Crying Wolf Truth.md
│       │   │   ├── Theme Song Integration.md
│       │   │   ├── Third-party drivers decision.md
│       │   │   ├── Time and perspective shift.md
│       │   │   ├── Timing and Connection Strategy.md
│       │   │   ├── Tithing and Treasure Trails.md
│       │   │   ├── Tooth Infection Remedies Guide.md
│       │   │   ├── Track Release Strategy.md
│       │   │   ├── Training map request.md
│       │   │   ├── Travelers season 3 release.md
│       │   │   ├── Travel Update and Plan.md
│       │   │   ├── Trinity of SunSpeaking.md
│       │   │   ├── Triple R Theory.md
│       │   │   ├── Trust Analysis Summary.md
│       │   │   ├── Trust Dispute Legal Strategy.md
│       │   │   ├── Trusting higher self.md
│       │   │   ├── T-shirt design concept.md
│       │   │   ├── Tsunami update summary.md
│       │   │   ├── Turning Cash Digital Options.md
│       │   │   ├── Turn off Cloudflare Access.md
│       │   │   ├── Turtle Island Reflection.md
│       │   │   ├── TXT File Footers Explained.md
│       │   │   ├── Uber rental car prices.md
│       │   │   ├── Ubuntu Kernel Panic Fix.md
│       │   │   ├── Ubuntu UI for AetherCore.md
│       │   │   ├── Ultimatum Codex Entry.md
│       │   │   ├── Under attack assistance.md
│       │   │   ├── Unfair company policies.md
│       │   │   ├── Unknown Devices on Network.md
│       │   │   ├── Unzip and explore files.md
│       │   │   ├── Upload audio to Substack.md
│       │   │   ├── Uptime Monitoring Suggestions.md
│       │   │   ├── URL Replacement Request.md
│       │   │   ├── USB autorun setup Linux.md
│       │   │   ├── USB to Server Upload.md
│       │   │   ├── User frustration analysis.md
│       │   │   ├── USPS vs UPS PO Boxes.md
│       │   │   ├── Valkyrie vs The Valkyries.md
│       │   │   ├── VALOR GitHub Repo Overview.md
│       │   │   ├── VALOR Plot Development Outline.md
│       │   │   ├── VALOR project overview.md
│       │   │   ├── VALOR Repository Structuring.md
│       │   │   ├── Vendor incompetence analysis.md
│       │   │   ├── Vendor Ranking Analysis.md
│       │   │   ├── Verify past writing.md
│       │   │   ├── Video Access Request.md
│       │   │   ├── Video Creation Assistance.md
│       │   │   ├── VIN Country Code Help.md
│       │   │   ├── Vision Montage Reflection.md
│       │   │   ├── Voices and Echoes Connection.md
│       │   │   ├── Voyagers 2 zip creation.md
│       │   │   ├── Vscode extensions list.md
│       │   │   ├── Web3 AI Agent Guide.md
│       │   │   ├── Webby North of Richmond remix.md
│       │   │   ├── Website review and ideas.md
│       │   │   ├── Website unavailable troubleshooting.md
│       │   │   ├── Weekly Routine Planner.md
│       │   │   ├── WGU admissions advice.md
│       │   │   ├── What is Ashura.md
│       │   │   ├── What is gravity really.md
│       │   │   ├── White bug identification.md
│       │   │   ├── Wifi network troubleshooting.md
│       │   │   ├── Womack bucket domain setup.md
│       │   │   ├── Work Address Clarification.md
│       │   │   ├── World disbelief expression.md
│       │   │   ├── WSL Ubuntu installation fix.md
│       │   │   ├── WTMA EPP Prep Guide.md
│       │   │   ├── You matter keep going.md
│       │   │   ├── Zenkit OpenAI Integration Guide.md
│       │   │   └── ZIP File Exploration.md
│       │   ├── index.yml
│       │   ├── README.md
│       │   └── requirements.txt
│       ├── fix_gists.py
│       ├── Gist_Navigator.md
│       ├── gists
│       │   ├── conversation_100.md
│       │   ├── conversation_101.md
│       │   ├── conversation_102.md
│       │   ├── conversation_103.md
│       │   ├── conversation_104.md
│       │   ├── conversation_105.md
│       │   ├── conversation_106.md
│       │   ├── conversation_107.md
│       │   ├── conversation_108.md
│       │   ├── conversation_109.md
│       │   ├── conversation_10.md
│       │   ├── conversation_110.md
│       │   ├── conversation_111.md
│       │   ├── conversation_112.md
│       │   ├── conversation_113.md
│       │   ├── conversation_114.md
│       │   ├── conversation_115.md
│       │   ├── conversation_116.md
│       │   ├── conversation_117.md
│       │   ├── conversation_118.md
│       │   ├── conversation_119.md
│       │   ├── conversation_11.md
│       │   ├── conversation_120.md
│       │   ├── conversation_121.md
│       │   ├── conversation_122.md
│       │   ├── conversation_123.md
│       │   ├── conversation_124.md
│       │   ├── conversation_125.md
│       │   ├── conversation_126.md
│       │   ├── conversation_127.md
│       │   ├── conversation_128.md
│       │   ├── conversation_129.md
│       │   ├── conversation_12.md
│       │   ├── conversation_130.md
│       │   ├── conversation_131.md
│       │   ├── conversation_132.md
│       │   ├── conversation_133.md
│       │   ├── conversation_134.md
│       │   ├── conversation_135.md
│       │   ├── conversation_136.md
│       │   ├── conversation_137.md
│       │   ├── conversation_138.md
│       │   ├── conversation_139.md
│       │   ├── conversation_13.md
│       │   ├── conversation_140.md
│       │   ├── conversation_141.md
│       │   ├── conversation_142.md
│       │   ├── conversation_143.md
│       │   ├── conversation_144.md
│       │   ├── conversation_145.md
│       │   ├── conversation_146.md
│       │   ├── conversation_147.md
│       │   ├── conversation_148.md
│       │   ├── conversation_149.md
│       │   ├── conversation_14.md
│       │   ├── conversation_150.md
│       │   ├── conversation_151.md
│       │   ├── conversation_152.md
│       │   ├── conversation_153.md
│       │   ├── conversation_154.md
│       │   ├── conversation_155.md
│       │   ├── conversation_156.md
│       │   ├── conversation_157.md
│       │   ├── conversation_158.md
│       │   ├── conversation_159.md
│       │   ├── conversation_15.md
│       │   ├── conversation_160.md
│       │   ├── conversation_161.md
│       │   ├── conversation_162.md
│       │   ├── conversation_163.md
│       │   ├── conversation_164.md
│       │   ├── conversation_165.md
│       │   ├── conversation_166.md
│       │   ├── conversation_167.md
│       │   ├── conversation_168.md
│       │   ├── conversation_169.md
│       │   ├── conversation_16.md
│       │   ├── conversation_170.md
│       │   ├── conversation_171.md
│       │   ├── conversation_172.md
│       │   ├── conversation_173.md
│       │   ├── conversation_174.md
│       │   ├── conversation_175.md
│       │   ├── conversation_176.md
│       │   ├── conversation_177.md
│       │   ├── conversation_178.md
│       │   ├── conversation_179.md
│       │   ├── conversation_17.md
│       │   ├── conversation_180.md
│       │   ├── conversation_181.md
│       │   ├── conversation_182.md
│       │   ├── conversation_183.md
│       │   ├── conversation_184.md
│       │   ├── conversation_185.md
│       │   ├── conversation_186.md
│       │   ├── conversation_187.md
│       │   ├── conversation_188.md
│       │   ├── conversation_189.md
│       │   ├── conversation_18.md
│       │   ├── conversation_190.md
│       │   ├── conversation_191.md
│       │   ├── conversation_192.md
│       │   ├── conversation_193.md
│       │   ├── conversation_194.md
│       │   ├── conversation_195.md
│       │   ├── conversation_196.md
│       │   ├── conversation_197.md
│       │   ├── conversation_198.md
│       │   ├── conversation_199.md
│       │   ├── conversation_19.md
│       │   ├── conversation_1.md
│       │   ├── conversation_200.md
│       │   ├── conversation_201.md
│       │   ├── conversation_202.md
│       │   ├── conversation_203.md
│       │   ├── conversation_204.md
│       │   ├── conversation_205.md
│       │   ├── conversation_206.md
│       │   ├── conversation_207.md
│       │   ├── conversation_208.md
│       │   ├── conversation_209.md
│       │   ├── conversation_20.md
│       │   ├── conversation_210.md
│       │   ├── conversation_211.md
│       │   ├── conversation_212.md
│       │   ├── conversation_213.md
│       │   ├── conversation_214.md
│       │   ├── conversation_215.md
│       │   ├── conversation_216.md
│       │   ├── conversation_217.md
│       │   ├── conversation_21.md
│       │   ├── conversation_22.md
│       │   ├── conversation_23.md
│       │   ├── conversation_24.md
│       │   ├── conversation_25.md
│       │   ├── conversation_26.md
│       │   ├── conversation_27.md
│       │   ├── conversation_28.md
│       │   ├── conversation_29.md
│       │   ├── conversation_2.md
│       │   ├── conversation_30.md
│       │   ├── conversation_31.md
│       │   ├── conversation_32.md
│       │   ├── conversation_33.md
│       │   ├── conversation_34.md
│       │   ├── conversation_35.md
│       │   ├── conversation_36.md
│       │   ├── conversation_37.md
│       │   ├── conversation_38.md
│       │   ├── conversation_39.md
│       │   ├── conversation_3.md
│       │   ├── conversation_40.md
│       │   ├── conversation_41.md
│       │   ├── conversation_42.md
│       │   ├── conversation_43.md
│       │   ├── conversation_44.md
│       │   ├── conversation_45.md
│       │   ├── conversation_46.md
│       │   ├── conversation_47.md
│       │   ├── conversation_48.md
│       │   ├── conversation_49.md
│       │   ├── conversation_4.md
│       │   ├── conversation_50.md
│       │   ├── conversation_51.md
│       │   ├── conversation_52.md
│       │   ├── conversation_53.md
│       │   ├── conversation_54.md
│       │   ├── conversation_55.md
│       │   ├── conversation_56.md
│       │   ├── conversation_57.md
│       │   ├── conversation_58.md
│       │   ├── conversation_59.md
│       │   ├── conversation_5.md
│       │   ├── conversation_60.md
│       │   ├── conversation_61.md
│       │   ├── conversation_62.md
│       │   ├── conversation_63.md
│       │   ├── conversation_64.md
│       │   ├── conversation_65.md
│       │   ├── conversation_66.md
│       │   ├── conversation_67.md
│       │   ├── conversation_68.md
│       │   ├── conversation_69.md
│       │   ├── conversation_6.md
│       │   ├── conversation_70.md
│       │   ├── conversation_71.md
│       │   ├── conversation_72.md
│       │   ├── conversation_73.md
│       │   ├── conversation_74.md
│       │   ├── conversation_75.md
│       │   ├── conversation_76.md
│       │   ├── conversation_77.md
│       │   ├── conversation_78.md
│       │   ├── conversation_79.md
│       │   ├── conversation_7.md
│       │   ├── conversation_80.md
│       │   ├── conversation_81.md
│       │   ├── conversation_82.md
│       │   ├── conversation_83.md
│       │   ├── conversation_84.md
│       │   ├── conversation_85.md
│       │   ├── conversation_86.md
│       │   ├── conversation_87.md
│       │   ├── conversation_88.md
│       │   ├── conversation_89.md
│       │   ├── conversation_8.md
│       │   ├── conversation_90.md
│       │   ├── conversation_91.md
│       │   ├── conversation_92.md
│       │   ├── conversation_93.md
│       │   ├── conversation_94.md
│       │   ├── conversation_95.md
│       │   ├── conversation_96.md
│       │   ├── conversation_97.md
│       │   ├── conversation_98.md
│       │   ├── conversation_99.md
│       │   ├── conversation_9.md
│       │   ├── EverLight_Aetherius_Summary.md
│       │   ├── EverLight_Memory_Chat_2025-04-18.md
│       │   ├── gist_101_287f0f8b.md
│       │   ├── gist_102_cf29456a.md
│       │   ├── gist_103_5b05bf1a.md
│       │   ├── gist_104_82de500f.md
│       │   ├── gist_105_1c70f2ed.md
│       │   ├── gist_106_7c496e9a.md
│       │   ├── gist_107_ca8c8492.md
│       │   ├── gist_108_2b48d5a2.md
│       │   ├── gist_109_586bb1f8.md
│       │   ├── gist_10_e56d61c9.md
│       │   ├── gist_110_ce5b48dd.md
│       │   ├── gist_111_cc5511cc.md
│       │   ├── gist_112_120b8364.md
│       │   ├── gist_113_bbc5b5ed.md
│       │   ├── gist_114_887ce4d2.md
│       │   ├── gist_115_cb0f1af4.md
│       │   ├── gist_116_fbcfd18f.md
│       │   ├── gist_117_063acb85.md
│       │   ├── gist_118_af3f7598.md
│       │   ├── gist_119_385e35b8.md
│       │   ├── gist_11_d8ab901b.md
│       │   ├── gist_120_e8fd77a4.md
│       │   ├── gist_121_745454ca.md
│       │   ├── gist_122_19be8642.md
│       │   ├── gist_123_1af4831d.md
│       │   ├── gist_124_3d89d43e.md
│       │   ├── gist_125_c8d49cfb.md
│       │   ├── gist_126_301a3f79.md
│       │   ├── gist_127_aa4fc1e0.md
│       │   ├── gist_128_f1a65e82.md
│       │   ├── gist_129_bbe1bbb0.md
│       │   ├── gist_12_ea4cdcc3.md
│       │   ├── gist_130_fb7f0d52.md
│       │   ├── gist_131_260bb72d.md
│       │   ├── gist_132_30c1d4c2.md
│       │   ├── gist_133_130169d9.md
│       │   ├── gist_134_e1c7cfa6.md
│       │   ├── gist_135_8d79330c.md
│       │   ├── gist_136_d4e5ab36.md
│       │   ├── gist_137_dd359714.md
│       │   ├── gist_138_e007548b.md
│       │   ├── gist_139_64ecf820.md
│       │   ├── gist_13_969e4077.md
│       │   ├── gist_140_5bf189b0.md
│       │   ├── gist_141_81594e18.md
│       │   ├── gist_142_d135f88c.md
│       │   ├── gist_143_06b8e4f5.md
│       │   ├── gist_144_b0f0ff99.md
│       │   ├── gist_145_04785e1e.md
│       │   ├── gist_146_d5d31be7.md
│       │   ├── gist_147_d4b42df5.md
│       │   ├── gist_148_94671b8a.md
│       │   ├── gist_149_7674e97b.md
│       │   ├── gist_14_ff87da55.md
│       │   ├── gist_15_06c590ff.md
│       │   ├── gist_150_a047ed18.md
│       │   ├── gist_151_ee9166b7.md
│       │   ├── gist_152_aef12bfa.md
│       │   ├── gist_153_9a1989b9.md
│       │   ├── gist_154_13530226.md
│       │   ├── gist_155_d636d4a7.md
│       │   ├── gist_156_2238260f.md
│       │   ├── gist_157_0da540bc.md
│       │   ├── gist_158_e7356de8.md
│       │   ├── gist_159_ce672dbc.md
│       │   ├── gist_160_1b29e843.md
│       │   ├── gist_161_089cce42.md
│       │   ├── gist_162_081d102f.md
│       │   ├── gist_163_87a1dd08.md
│       │   ├── gist_164_887cdcc1.md
│       │   ├── gist_165_23e9b097.md
│       │   ├── gist_166_3f9f60dc.md
│       │   ├── gist_167_c32a806c.md
│       │   ├── gist_168_94f1c1d1.md
│       │   ├── gist_169_9e36c0c5.md
│       │   ├── gist_16_9ec7ea25.md
│       │   ├── gist_170_ad9fd7d1.md
│       │   ├── gist_171_1f00d835.md
│       │   ├── gist_172_85fb97d6.md
│       │   ├── gist_173_c240533d.md
│       │   ├── gist_174_a855008b.md
│       │   ├── gist_175_a97407e8.md
│       │   ├── gist_176_f1f3394c.md
│       │   ├── gist_177_f6852852.md
│       │   ├── gist_17_88daad8b.md
│       │   ├── gist_178_ba6120d2.md
│       │   ├── gist_179_38694bc7.md
│       │   ├── gist_180_3a4bc70f.md
│       │   ├── gist_181_0e123683.md
│       │   ├── gist_182_65ffd3b2.md
│       │   ├── gist_183_87ee0532.md
│       │   ├── gist_184_9f3200d8.md
│       │   ├── gist_18_4c105cf6.md
│       │   ├── gist_185_188f7603.md
│       │   ├── gist_186_5a6e3ab2.md
│       │   ├── gist_187_428f2cbf.md
│       │   ├── gist_188_8d6a79ac.md
│       │   ├── gist_189_e71f1631.md
│       │   ├── gist_190_20e49141.md
│       │   ├── gist_191_a37725f8.md
│       │   ├── gist_192_449266f6.md
│       │   ├── gist_193_22d632f2.md
│       │   ├── gist_194_3419bc6d.md
│       │   ├── gist_195_0b525bd6.md
│       │   ├── gist_196_2e64bc22.md
│       │   ├── gist_197_dcf5e6ef.md
│       │   ├── gist_198_ea47efea.md
│       │   ├── gist_199_e6d6ef45.md
│       │   ├── gist_19_f61fcd06.md
│       │   ├── gist_1_d5c7a1ef.md
│       │   ├── gist_200_5479e5d7.md
│       │   ├── gist_201_0657eb6f.md
│       │   ├── gist_20_146d7844.md
│       │   ├── gist_202_40f1f3cc.md
│       │   ├── gist_203_83176569.md
│       │   ├── gist_204_16403d61.md
│       │   ├── gist_205_c7b2cea6.md
│       │   ├── gist_206_ee2ba746.md
│       │   ├── gist_207_d30e09c7.md
│       │   ├── gist_208_860fcc50.md
│       │   ├── gist_209_be2855f6.md
│       │   ├── gist_210_0b83210a.md
│       │   ├── gist_211_2d8718d8.md
│       │   ├── gist_21_23f46a9e.md
│       │   ├── gist_212_d8c60d1e.md
│       │   ├── gist_213_f0a4ea89.md
│       │   ├── gist_214_100e269e.md
│       │   ├── gist_215_25d2eb4e.md
│       │   ├── gist_216_ea0a92a3.md
│       │   ├── gist_217_27688455.md
│       │   ├── gist_22_e645a115.md
│       │   ├── gist_23_dd17f797.md
│       │   ├── gist_24_8ad92a19.md
│       │   ├── gist_2_7975bf31.md
│       │   ├── gist_3_b2be4279.md
│       │   ├── gist_4_da82397b.md
│       │   ├── gist_5_48d05823.md
│       │   ├── gist_6_f4a3860c.md
│       │   ├── gist_7_bb4a8ac2.md
│       │   ├── gist_8_a50ad7e4.md
│       │   ├── gist_9_cbcadc2e.md
│       │   ├── OpenAI_Export_Conversations_2025-04-21_SANITIZED.json
│       │   ├── profile_info.md
│       │   └── ReMeetingEverLight.md
│       ├── gists.html
│       ├── gists.html.bak
│       ├── gists_index.json
│       ├── index.html
│       ├── index.html.bak
│       ├── jesus_wept.yml
│       ├── lazarus.prompt.yml
│       ├── OpenAI_Exports
│       │   ├── 687bbc3d-1aa0-8000-8042-89a54cba5bec
│       │   │   └── audio
│       │   │       ├── file_0000000022f4622f81d8d3e58f9845fa-ea7ff1d7-08ac-4414-a4c8-90456b9bbac7.wav
│       │   │       ├── file_000000003364622f83d02a3057f0aa55-d2aab95c-ddce-4243-b7d1-ba5cd386c361.wav
│       │   │       ├── file_00000000beb4622f892578beb1e118dc-e841fd52-e348-4a8e-94e4-b608a56aaa90.wav
│       │   │       └── file_00000000fee0622f9f3e6d66739a52bf-d7f29fbf-b95a-4839-ade1-f8c6f6faf406.wav
│       │   ├── 687c4f0b-26ec-8000-8b9d-cc94bb2e4a76
│       │   │   └── audio
│       │   │       ├── file_00000000bbc461f69c5c54337b269e6f-9f2b89f5-634a-4b36-a64e-4572558b4720.wav
│       │   │       └── file_00000000f77861f68e58aa02f720ef70-3363ee5a-e820-44e5-96df-202daf22a0b3.wav
│       │   ├── 687e965e-2598-8000-ab35-c58406cacc68
│       │   │   └── audio
│       │   │       ├── file_000000001b086230ab8a5e6c2c8e750b-5bc8f252-6b0c-4159-84c0-e916ec96d6e1.wav
│       │   │       └── file_0000000032c06230a26817fbe9ac255e-c67770f0-02fa-434e-bc27-efa71300dd89.wav
│       │   ├── 687fc735-d26c-8322-b857-711996178811
│       │   │   └── audio
│       │   │       ├── file_000000004e3c61f687ed294ebb6dc885-eff83713-a70a-4904-93ba-e57eb9d02c1e.wav
│       │   │       ├── file_00000000515061f690cdc5ccee80d228-6dc585d4-88d9-4ca5-8eb6-e0dad811d353.wav
│       │   │       ├── file_0000000057b461f6943ce2ab66628a6e-80782b7a-9ca9-46f2-9df1-173b5b1271bd.wav
│       │   │       └── file_00000000f15861f6a692538ceffcb8eb-fe86636b-629c-4525-88d9-ea6fdd6d50c7.wav
│       │   ├── 68865299-91fc-8331-b489-618e24e569ec
│       │   │   └── audio
│       │   │       ├── file_00000000208c61f6bd96d0a61f616df6-55a5dcf4-3b7f-4e7c-bda1-4fcdd4187de2.wav
│       │   │       ├── file_0000000027ec61f68227112fc818bfa0-9abd5ec7-3773-4ea1-ab19-dfedca8659fe.wav
│       │   │       ├── file_00000000a40461f688a0103439397f78-684e3d4f-6521-49de-842d-fd1a62724468.wav
│       │   │       └── file_00000000ac2c61f6bc4638ad9b308046-41f4507a-ebe1-4df4-b9b2-32adf37cbf81.wav
│       │   ├── 688e6448-a5ec-8320-bd9d-401ecc48e6f8
│       │   │   └── audio
│       │   │       ├── file_000000000338622f9eb7d67f668bc268-3d4ef8e3-fd4e-41a3-bd71-3ec092382d03.wav
│       │   │       ├── file_0000000005b8622f994d3b826170fa3d-c8a664bf-5d6f-4975-9844-93d4b3b72f21.wav
│       │   │       ├── file_000000001114622f8766aeaf2ca0d2c3-4838db03-c46f-4303-87cb-6ad274d86f8d.wav
│       │   │       ├── file_000000004fe0622fbc0d49ecb08bdc5c-bfbe05f9-76f9-4187-88b2-1c1f9449a1a7.wav
│       │   │       ├── file_000000009000622f8043230dd2234deb-e967d77f-7192-4801-a4b9-1dc716d83d2b.wav
│       │   │       ├── file_000000009000622fb790e677ae8f7a4d-5d4dd707-c5a2-405a-b055-bd8794843815.wav
│       │   │       ├── file_000000009828622fa87a2c8b7d3694d7-34c62b62-5b03-4945-8024-ab2868e39823.wav
│       │   │       ├── file_00000000d280622f975d0cc327da7bfb-2187a244-b86f-45f7-b623-46a030724e01.wav
│       │   │       ├── file_00000000e560622fa2f1679b11d4d70f-57506ba9-a838-44c0-9bdf-57f413d25355.wav
│       │   │       └── file_00000000ecc8622f82fefe1239b8e304-88bdfe2c-ffcf-4a6f-ba40-240777cea374.wav
│       │   ├── 689219b7-fe80-8320-9f98-7e95cfae780b
│       │   │   └── audio
│       │   │       ├── file_0000000093fc622f968dd4f728f5e7dc-cd374e09-dc7f-4ce6-8d90-152c73dce340.wav
│       │   │       └── file_00000000a55c622f827ff06faa20326f-d571fc98-4f41-444a-a083-c9808d9c2982.wav
│       │   ├── chat.html
│       │   ├── conversations.json
│       │   ├── file-12yZ4L9m5Ww6ZVmCnKQbiJ-2025-07-11-07-51-58-463.jpg
│       │   ├── file-14heijW9m4rYxbPEzstq75-chatgpt-1754570396142.jpg
│       │   ├── file-17TN4oFJdMa5gQ3jQFs922-chatgpt-1754556287828.jpg
│       │   ├── file-191gykEvGh2dVT56rdmuX8-chatgpt-1753816171859.jpg
│       │   ├── file-191WjtEPaQWqvQVM4YDSMT-chatgpt-1753876077190.jpg
│       │   ├── file-19M15uDKj4HPrTUJUygpuA-chatgpt-1754558962648.jpg
│       │   ├── file-19Xmq3gctqU3FouXHuwFiK-chatgpt-1753838999978.jpg
│       │   ├── file-1b6XCqRdkedKTQ7M1oL3bk-chatgpt-1754578882529.jpg
│       │   ├── file-1BoRvF19yW2dnrEozxWfWB-85d387fc-25ae-4081-ac91-bc1b95554e668599971843410872579
│       │   ├── file-1BqRygrZ4dQ8nkbBqMpz2w-1000007258.png
│       │   ├── file-1cMo9wWSRKjKmG1RpMbvRX-1000022882.png
│       │   ├── file-1dNAnBc5vMLRnQBsjUmo5y-chatgpt-1754583013447.jpg
│       │   ├── file-1DVQ91ytnJaf8ms7Cr3PJi-chatgpt-1753828716389.jpg
│       │   ├── file-1eGtneig9simst3fEFNRuu-1000007429.png
│       │   ├── file-1eJauq6aFHv7div2Tb9rDB-chatgpt-1754558180283.jpg
│       │   ├── file-1EULQq1oxYQMcTz3xAyKcs-chatgpt-1753921697379.jpg
│       │   ├── file-1FAtjyYPLPcJRwUfTYpuLc-chatgpt-1753827008203.jpg
│       │   ├── file-1gmJc9Sh2mqjiD5G6mDyrG-chatgpt-1754559062764.jpg
│       │   ├── file-1gnZeNZpmtHnXTqCT7Zv6Z-Screenshot_20250711-171340.1Weather.png
│       │   ├── file-1iEVJJxvrpz5pY9aRLr2Xi-8ceb452f-ac7b-4a21-8d88-0bb4256753fc7051883718836092347
│       │   ├── file-1JVZPNo8CSD3NEiEahBBvo-d42e668a-9fe2-415d-8216-342375e255a23585813983778955365
│       │   ├── file-1kj7e699K5xUPEtiCKEZNZ-chatgpt-1754429267594.jpg
│       │   ├── file-1kvMAZosSCwhtFm8YyQnif-1000023477.jpg
│       │   ├── file-1m8E2yNrPPV2ys43s2zym7-chatgpt-1754518149513.jpg
│       │   ├── file-1MYKdqQGoQwYhEgzSHGTBm-1000007390.png
│       │   ├── file-1naTLxqpTy6oyLxDt6BTK6-bf5e162c-6541-418d-900e-c51b0b8ea9d32202705803863601681
│       │   ├── file-1Nxkmq2F4EgiQCVNkXJNpw-1000007267.png
│       │   ├── file-1Nz5rcZCewLas1BcQtb9DT-chatgpt-1754133740552.jpg
│       │   ├── file-1PXjJPc3gerMGbhjiN2uMe-chatgpt-1754576800651.jpg
│       │   ├── file-1qE8WYDsZ64asxXyx9v9AZ-chatgpt-1754051909866.jpg
│       │   ├── file-1R9QnZibV5ttNgDja1G41n-chatgpt-1754580995972.jpg
│       │   ├── file-1rVjXXjeVAV42MjjFivKbx-chatgpt-1754662636771.jpg
│       │   ├── file-1sRKUdhsSLgptMFYqCksXu-chatgpt-1754564189653.jpg
│       │   ├── file-1sUwdN1XURvBBZhCKWkMkd-chatgpt-1753921837454.jpg
│       │   ├── file-1T3eTnBJDcmMFRrRKTat31-30baec8b-99ff-4047-81a9-78c614f5bcce7869055545614936662
│       │   ├── file-1TKEUSJx5jV12twBAZgTyW-chatgpt-1754060210249.jpg
│       │   ├── file-1udb76Y4zrHUuzWAb9d5bN-chatgpt-1754577690761.jpg
│       │   ├── file-1wobbruHAZKfrPAYndmioR-1000023314.png
│       │   ├── file-1XN1NdPJYPb3rdQMnHco5k-chatgpt-1754007565234.jpg
│       │   ├── file-1yJ5wpYr9V9hYMdpYF9DoH-1000007153.jpg
│       │   ├── file-1zD4m9ya6SDRQ7pE33o2Na-chatgpt-1754470699014.jpg
│       │   ├── file-1zHviuFvmPZvQjbkYPCexK-cf1fa669-8255-45a3-8549-e46b2903188d144775617687743122
│       │   ├── file-1ZvpZYMLcMT7uWzzgRVfAN-chatgpt-1754554276597.jpg
│       │   ├── file-21JQqw27Ypvk1iv7tyuWLe-592a0058-5488-4006-8f88-910aad91693f270756912981594770
│       │   ├── file-264kc2hrYcAStjTaHiy6ZC-chatgpt-1754133330364.jpg
│       │   ├── file-26HdzANjUKoe8mUvgYpmdF-1000007255.png
│       │   ├── file-28UzcbPxoQeLSFyHDCNeBS-chatgpt-1754554152716.jpg
│       │   ├── file-29HtqmgvP3CeHVb37V8XF3-chatgpt-1753823282815.jpg
│       │   ├── file-2C4wDUr83gBn8vcyh1n75j-chatgpt-1753833662987.jpg
│       │   ├── file-2DkoL6uSiAQmWhBnybhD2v-chatgpt-1754589543578.jpg
│       │   ├── file-2dRytcnRmY1E78sY6qJLxC-chatgpt-1754578382530.jpg
│       │   ├── file-2e6bN36p7oFdPP4a76eMk1-chatgpt-1753976138133.jpg
│       │   ├── file-2GpWVZscjPW8HNSLLcG9kZ-7f7992d5-60e8-4660-8043-76ce320716b36579023747951819115
│       │   ├── file-2NgBn3UdkscLuNSDjVWkQG-27cd404d-45df-4e24-a72f-60335d2758377673340046642790570
│       │   ├── file-2nSExdYcUsK1AWzEzf7hcw-1000007534.png
│       │   ├── file-2of1Q9cHZPC7Z6fASdEHWo-1000007347.png
│       │   ├── file-2oNnfKmvCgDdFvUsSd9nCm-chatgpt-1754472145865.jpg
│       │   ├── file-2oym4iK4w5MsU8ameu2pKK-1000007196.png
│       │   ├── file-2poYA2UPrzesDg8RU9fcvo-tenor_gif923563668505478639.gif
│       │   ├── file-2qdLUVk1LKH922MnRN6AwY-chatgpt-1754659774661.jpg
│       │   ├── file-2rxpbJnyyxWdpSZ1jFZ64n-1000023385.png
│       │   ├── file-2RXS3VEqdCPTqWsAdaViP1-1000022799.png
│       │   ├── file-2scRsPbmpVbrWj7vSdz5gd-chatgpt-1753841382348.jpg
│       │   ├── file-2SD6yfofNU2392QEUCP962-4020ad08-89bc-4b9c-9ca7-68934f9fb4928383851091544418330
│       │   ├── file-2sFact1FtkCgfsTWKHadCn-chatgpt-1753814579430.jpg
│       │   ├── file-2TAo7yf9bFUUdT41Qbod7a-1000007456.jpg
│       │   ├── file-2U9GPVX5B6deGEXc91TDmE-e993ee24-48db-487e-be6d-3019c539cf5c2917128090282835452
│       │   ├── file-2up9dUHCjMhoYB7xW16HVd-tenor_gif8048554150102169735.gif
│       │   ├── file-2vaJ2cr5Gv8h9aQu5UzYaX-63a322c8-321f-4f30-b08d-9bc7b36e31f59133923715811546883
│       │   ├── file-2wbPd8XMC6ZcdG2wV9FKX2-2665b4cc-bf57-45c6-b217-0e8c115ff1291884341020100386545
│       │   ├── file-2XKXLyroZGpoVU8Zi9vanJ-tenor_gif4855017839415037857.gif
│       │   ├── file-2xP3x4Jhq22mSpsiN6urBc-1000007451.jpg
│       │   ├── file-2ya17jne9s3wRGxAWx88zB-chatgpt-1754555547682.jpg
│       │   ├── file-2yxa9suquydht31DACcfyG-1000007538.png
│       │   ├── file-2zQ51MPmFnXHTo5jhj7wjU-1000000059.png
│       │   ├── file-32ZHKw2KWTR5zNgkRCzWLa-tenor_gif7974719452508041698.gif
│       │   ├── file-35VF3N4mxsgWTJ2Kx3N4FZ-1000007146.jpg
│       │   ├── file-3A1ST31QGoqpqvUXAFLUxK-1000007430.png
│       │   ├── file-3aGhCUDK1J6TSBXcPbaf1H-1000007399.png
│       │   ├── file-3AH11hfnoEWzNiNvrTef4G-chatgpt-1754570279210.jpg
│       │   ├── file-3AMWmnUacPB4Sc1mzSxHju-1da3185e-13c3-4336-aa7a-6e836563fe5e4928515853616146737
│       │   ├── file-3bDKEzit64sc7WwZ5zvaMe-chatgpt-1754554315255.jpg
│       │   ├── file-3BXHZ78y5dYBuxHRszrKon-chatgpt-1754069690524.jpg
│       │   ├── file-3cpFXVqiy7aA4BeGjkREtB-1000007358.png
│       │   ├── file-3d5UjpyDStG3fUFDqqAueP-chatgpt-1754649793194.jpg
│       │   ├── file-3EB18MuYmguho69DBfiSS4-chatgpt-1754431794317.jpg
│       │   ├── file-3hK9tFYwt5uDmrda5LSoCt-1000005206.jpg
│       │   ├── file-3js22Rsve5ikawGBEpeNFD-chatgpt-1754650378761.jpg
│       │   ├── file-3M1Zeu9q8Jf7DB1fer2qVw-chatgpt-1754495263305.jpg
│       │   ├── file-3muABJNBaTFhSNdLm1bJUU-2a733db2-2942-46d8-a6ab-897e20586bad24870502913685646
│       │   ├── file-3nTTiqdmXRx9drbgYDd1dv-1000007354.png
│       │   ├── file-3NW6CAgk3vFMtrXDmy75yu-chatgpt-1754069750575.jpg
│       │   ├── file-3P863JHRh6Wu918bqQCsWB-1000007185.png
│       │   ├── file-3pgbqvQKmLSHSJsSdABfRH-7b10dd4e-7157-44e1-a558-8261a446b1d06613729093093988586
│       │   ├── file-3rgDNPn8NZrbfRR9CPLi38-12813ef7-cf12-4c52-bdaf-99b4d3cbb9c63766562682149323680
│       │   ├── file-3rhbaJea1mRWoqmvVCNecv-chatgpt-1754581805105.jpg
│       │   ├── file-3rkjPeCu94wRbB63myDNzz-chatgpt-1754057181057.jpg
│       │   ├── file-3Sgj3v8m2EMfv7HC4tmNGU-be5e48af-e03c-49d2-9763-585ba95947b33282154229012144430
│       │   ├── file-3sx3T8QRZc9CS1f6oK47MP-1000007459.png
│       │   ├── file-3Tq2jvbsBKycUguh6wc1T5-chatgpt-1753843026056.jpg
│       │   ├── file-3tZKGDsEytdZXxEWdqoT3F-chatgpt-1753852186516.jpg
│       │   ├── file-3UNqshKEsbZRVpdw954Rib-af1eb8d5-082b-47e4-8a86-b6e4797f50e825892165005046758
│       │   ├── file-3W1Yzxdhx48VhLfXukLEXu-1000007374.png
│       │   ├── file-3wr1YPVCXU4Xz7fFN8JkQQ-e2191d9c-26b5-42b5-8c65-4515e18268cf8155933938750466591
│       │   ├── file-3X3AfLHFYSRJ3YMRoj2wRf-chatgpt-1754168519368.jpg
│       │   ├── file-3YLUytLzLFC5QrPoxryDTv-c5fe0e31-9d76-465b-903d-d88d69c7d3dd8660237298842443754
│       │   ├── file-3ysUfWgPqEtf2BStE3AoV6-chatgpt-1754575838560.jpg
│       │   ├── file-3z5XMeACAcUkxureJJwCbx-1000007468.png
│       │   ├── file-3z7U6ky645FLk77ZKNLsbc-1000007456.jpg
│       │   ├── file-47bLb43ShSVMG8bP9hzQDh-Screenshot_20250712-085453.Messages.png
│       │   ├── file-48qewgHPqN3u5WeM4jafjk-chatgpt-1753867364341.jpg
│       │   ├── file-49SJAjm3huzrdvaUUDnrXD-chatgpt-1754582956836.jpg
│       │   ├── file-4a52j3BQmEQEXPA5We2YAD-1000007530.png
│       │   ├── file-4Bxq25RRWKTpeDaWDQ972q-1000007450.jpg
│       │   ├── file-4dNjcdHukdmJAdzRfpp8tt-1000007177.png
│       │   ├── file-4Drmxw1Bri3XeukcnK4sBL-eb87c173-844c-429a-b075-0973ac9f0d883282765183980620628
│       │   ├── file-4DUbQAtpYQEajCTNQywfAL-1000023650.png
│       │   ├── file-4eb7Z3Sze7WXKczB4wQW6Q-chatgpt-1754650182951.jpg
│       │   ├── file-4fw6xTMGcKVTJHY97ngRTw-eb4ebb27-d53d-4e12-aa76-99fed03a4ef55871723555641451968
│       │   ├── file-4GDJr8ftKDfj228DVvqfNQ-chatgpt-1754563741720.jpg
│       │   ├── file-4GfnoTuUtAK1no4SocKZDc-chatgpt-1754049983832.jpg
│       │   ├── file-4gNMXDqMp3DvtHgk7Eb377-6dbb5f93-5f0b-42d4-be17-5773a8596c157994237886697524510
│       │   ├── file-4GwN7GXNKemu6L821xGTtz-chatgpt-1754570416332.jpg
│       │   ├── file-4h3XArtVXufQWnquNwRjFY-1000022857.png
│       │   ├── file-4HRknANPCPyVVZStsLdgdE-1000007390.png
│       │   ├── file-4Hwx6wfue5CMo1qidAkHcu-chatgpt-1754650486208.jpg
│       │   ├── file-4kwKk3CQMjTeHsh2fAun1z-a39cbb00-940d-4eaf-bbc1-c8ca0fe0020f7338037609056384618
│       │   ├── file-4kZEq1rPnDG2fKNAj6gP88-1000007253.png
│       │   ├── file-4NKsFzrF14Cvfu2ePCvRaT-chatgpt-1753877943107.jpg
│       │   ├── file-4PtJZzGSko2GsKmTnn2M4r-chatgpt-1753813153506.jpg
│       │   ├── file-4qTotmcCwqPtpiNU3u45W6-chatgpt-1753824421616.jpg
│       │   ├── file-4R1ePqR6czz8mwfEGC1Nrc-1000007495.png
│       │   ├── file-4THURgefBw5K78XaQGvkZd-1000022819.jpg
│       │   ├── file-4TsfkN96BMR5FbVfk7Ffh4-chatgpt-1754133219395.jpg
│       │   ├── file-4xQQX4QzWoNH2Z2Fvxg7S1-chatgpt-1754047758675.jpg
│       │   ├── file-514mfPJz3FH4awficwFKnd-chatgpt-1754581812176.jpg
│       │   ├── file-51X92EQd7a8KQeZngHcZjM-chatgpt-1754581954492.jpg
│       │   ├── file-52wnVHBYUL8CjCjr5NiYxJ-chatgpt-1754433579515.jpg
│       │   ├── file-52YWtSyT2zw2QfKhodzY1L-1000023342.png
│       │   ├── file-54j9ScGhD1U8C14ACq8sLy-1000007181.png
│       │   ├── file-55rMYxFVswdWk12fc1nAyF-chatgpt-1754557260046.jpg
│       │   ├── file-58ffvQvXzjnriHaQHc8SRu-1000007101.jpg
│       │   ├── file-5AKj52Z1Wjm7EDzwWBkgdu-e44499e8-bd64-4cb8-aaa6-d2c52f9132d41776371719557691296
│       │   ├── file-5atW5VEreD9B95RqfQT3Gr-1000005262.jpg
│       │   ├── file-5bhBZz6cdnxq4sZHAmh8eV-1000023343.png
│       │   ├── file-5bR7FytzWSLvwMdTLvW2b7-chatgpt-1753807599063.jpg
│       │   ├── file-5BuKPKCHZ2jMyEL6WWzo2P-eb08e047-e156-4994-8e1e-3562534ffafc4469350045084756110
│       │   ├── file-5bUnVwXngeMUXMWgP8w4em-02c5b9fe-9493-4aec-82bf-4bb57a235e467632382200092008804
│       │   ├── file-5cS4YdR1uMErT5qWpZbnwY-chatgpt-1754561347203.jpg
│       │   ├── file-5df7Jj4eUS1oJsY3owHWMg-chatgpt-1754133645805.jpg
│       │   ├── file-5eD5brwQ9FYeaRdP1oVzEG-chatgpt-1754053313957.jpg
│       │   ├── file-5eEmPrwAj8BaXpcsCthPwa-chatgpt-1754513788702.jpg
│       │   ├── file-5f8wpBhE8otdbtwPnEfBFU-b6a8600a-2bbe-4ac8-8e12-785c8e5d1ed62484919843638505574
│       │   ├── file-5FPPFtKQ8xPS89bohqWKak-1000007378.png
│       │   ├── file-5HVGAK1oYKgBxFvaxjQQAP-chatgpt-1753839994686.jpg
│       │   ├── file-5M39Pqea2iQSP8BwuSCZDL-chatgpt-1754642031018.jpg
│       │   ├── file-5m5h3Q5BCVesqbAAc45SXm-640d228b-5ccc-4336-a58b-f12da03a46be4864687924985428468
│       │   ├── file-5M9h3Fbdb2iyWf9BNTGSvw-1000007396.png
│       │   ├── file-5nsvLDMekeoshgYeMn87DX-1000007345.jpg
│       │   ├── file-5PFMUm8VTfkX6uGWsYFdth-chatgpt-1754558136420.jpg
│       │   ├── file-5pkTMWw5eFwra4gebY14sN-tenor_gif118564218399150643.gif
│       │   ├── file-5qko99Azsxj1oqdnZUcNDt-b511dadb-7ff4-47f1-b211-e096c389c5863527620659930776945
│       │   ├── file-5rYM3uCXD7CXrcMcKFBWcP-1000000030.jpg
│       │   ├── file-5S9V6o1m9AZGLyuE1wokzJ-Screenshot_20250726-115854.Gmail.png
│       │   ├── file-5t3wsFr3F3aHE7GNeL9Z9c-chatgpt-1754051663163.jpg
│       │   ├── file-5tLZGaL1aThkpWZNfFvUGY-052f21ee-894b-45cc-b214-e4b97355aae35413711614725198888
│       │   ├── file-5tYsb5hfvwiRhoYNL1bJSi-1000022798.png
│       │   ├── file-5ui2N1jVy4godyrwqc5Mcg-tenor_gif5285857533588893371.gif
│       │   ├── file-5vV22P25Gwq1GTiScZGyNs-chatgpt-1754038965075.jpg
│       │   ├── file-5xAf6XMQYTrRtjNYqt6jVs-chatgpt-1754133761264.jpg
│       │   ├── file-5xaT9v2NnP8yx31c8LcSDv-chatgpt-1754554116867.jpg
│       │   ├── file-5xGkRsjfMtPcZF8iAYZma9-1000007466.png
│       │   ├── file-5zmTCMpreJg9wWX8KHKJUa-Screenshot_20250727-094828.Chrome.png
│       │   ├── file-5zPGZWWHzw7uap2eigPKet-6feaf664-1a92-450f-a697-e3482b6aa3aa3687631451531702673
│       │   ├── file-63qFVY4Y3gftuTbqygmndw-chatgpt-1754555576865.jpg
│       │   ├── file-672BeJSYyKJxPb7GLep4nY-9e48e933-c7f8-49cf-b94a-5d0eac8d875a87515353796008885
│       │   ├── file-68MyzV53QyL5bWQw1Gjtc2-882ab5a1-87ee-4920-b3d1-2b551dac32068288091361981988713
│       │   ├── file-6c5HFrqWdBqA2bCJVDvLdM-Screenshot_20250807-152831.Navy Federal.png
│       │   ├── file-6cDF2d4VKu4kABX2BknQh1-27b891d1-463e-4e50-bd07-576d43ebdb004684543035593911799
│       │   ├── file-6dAKrHqRh5gJ7HBJCG3Ytx-chatgpt-1753838913635.jpg
│       │   ├── file-6dMpQapWrGYMZPcBkXjNMt-chatgpt-1753893659670.jpg
│       │   ├── file-6Eoqa6T3L1rrKgHhgg25Tu-2312d10f-f73c-4e5c-b58b-c7f90cc22ae21422883662431158348
│       │   ├── file-6eyAJwuwhvyYJB2GN7Dvi9-chatgpt-1753846250027.jpg
│       │   ├── file-6Gbw2w9yxQq2DD37E3j2VE-1000007474.png
│       │   ├── file-6hdWEbW5wwY5sET5UqUHZ1-Screenshot_20250727-172624.1Weather.png
│       │   ├── file-6hmv2VrnRxxk7kkq92Amwv-1000007134.jpg
│       │   ├── file-6L5guPcU6srVFxHNy5VEg9-chatgpt-1754073792567.jpg
│       │   ├── file-6M49L6aWPZSSoFoANKFPwM-1000007145.jpg
│       │   ├── file-6N3tHD4RwMEexwJcpCUBwB-tenor_gif3747683728014537295.gif
│       │   ├── file-6Ng5J1HGMW4JucsmYbyiBW-1000007541.png
│       │   ├── file-6pCqAUeuGrh8xyHdKzuYB9-chatgpt-1754570422739.jpg
│       │   ├── file-6pDX52KmgRzh1gcm4XBtVm-chatgpt-1754516974514.jpg
│       │   ├── file-6QKozxF695hmqZg1Y56PDn-chatgpt-1753825859014.jpg
│       │   ├── file-6qxwrGzGPoQrH72UUkL9KU-chatgpt-1753823944494.jpg
│       │   ├── file-6rQB8Lmm6JwbSC9zVRdgF4-1000007166.jpg
│       │   ├── file-6S92SRJpgmjeBRsEF3aGFR-db7f4084-a1d0-43d5-a1e5-453b6df3d399.png
│       │   ├── file-6UaXRwYQrg5fyW3mZHbfwh-9810d115-2b32-424d-aa17-954d9cadbc738848295708173815848
│       │   ├── file-6urAEvz98bbqaxPkFd6phL-chatgpt-1754003689000.jpg
│       │   ├── file-6VzJmpiQ1LSTXoA4uGmHzE-1000007220.png
│       │   ├── file-6WASRHV4rkRekQbSW8RpCo-1000022973.jpg
│       │   ├── file-6xE8eJxEggmHf3fY5SpjgE-chatgpt-1754576625066.jpg
│       │   ├── file-6XpNmBsiQLXeAreHmVWvR7-chatgpt-1754570712540.jpg
│       │   ├── file-6Z7aEKpAFRfJeNd44LbX9L-eac7eefa-77cc-47e1-bc0a-73a2c00cca3f565408609958146464
│       │   ├── file-73oEfwKsAFxKX7uj1qRxrY-chatgpt-1754567295618.jpg
│       │   ├── file-75o6xcC3ori1vTZgg43F7k-chatgpt-1754570590367.jpg
│       │   ├── file-76ENZZrUuSe5cBid2VCwih-chatgpt-1754652780501.jpg
│       │   ├── file-77MrWQHkiVWZAxfHAh7nPy-1000007464.png
│       │   ├── file-77SY5GRqHdKvLCiVgMDMy8-62b74532-1a8a-44bc-9aff-12cd6ec70819.png
│       │   ├── file-7amKWj78JGFHEFvjihcWdd-1000023319.png
│       │   ├── file-7arNvx2rqZCRaijrDEKJMM-8230ae9e-4578-4ccf-b702-682c361757528075372681743569222
│       │   ├── file-7BRwP1G9iniwZrjFyYFHTh-1000007152.jpg
│       │   ├── file-7FAHmt27TjUGtrvKr7YDxH-chatgpt-1754576254839.jpg
│       │   ├── file-7GuDtrvGj33cttvpAEz4gw-chatgpt-1753825476919.jpg
│       │   ├── file-7gZ56zZbGhtZuPj1saaCTA-chatgpt-1754052083830.jpg
│       │   ├── file-7HAAZ2WVUhgyj7nFLNAaq7-tenor_gif2561101875669094501.gif
│       │   ├── file-7juMgrjN8UeNiGjYtWHBFu-chatgpt-1753814616276.jpg
│       │   ├── file-7K1sFk1PHppamKpPnA4bHV-tenor_gif5285857533588893371.gif
│       │   ├── file-7kwu8FGD7dR3FqmkTABUwE-1000007395.png
│       │   ├── file-7nDAYACMxr5HL1GkfjQsrx-chatgpt-1754324301518.jpg
│       │   ├── file-7p7vCwqn3GTe2jyZADbe6Y-chatgpt-1753920701431.jpg
│       │   ├── file-7PSG75hQVEGBejwcQoko8o-chatgpt-1753852352042.jpg
│       │   ├── file-7RhXvjWKQTTVu5GhpUNtBm-1000006512.png
│       │   ├── file-7SEq3q9nkJ89m36QHCMen7-chatgpt-1753838313980.jpg
│       │   ├── file-7somN7xpqRGf7oufmXiqY5-ad144ae9-2ed4-4031-afdd-3c77ea77c2461370452778302615587
│       │   ├── file-7tS8dgsuan13s6i8kAoncf-chatgpt-1754570912749.jpg
│       │   ├── file-7U7ZdcD3j4b6UzJ7LuMTwo-3d9dca0f-dea4-42a2-a9d4-3cd545bcd0624924226367087257526
│       │   ├── file-7uQG3SUrWL3xxRKBVTvTZ3-1000007348.png
│       │   ├── file-7UVXRttcNMSeDYQM6mD79s-chatgpt-1754051174082.jpg
│       │   ├── file-7V426f1LygyFMnmUQsXDvW-1000007179.png
│       │   ├── file-7vCUoxTUHjQdK1XKY2RHbS-1000000059.png
│       │   ├── file-7VhYEvpffm4Kgecy6M1MqE-tenor_gif5547560150864970272.gif
│       │   ├── file-7vqqqiZyXHYvXdWFAx3K3Q-1000007477.png
│       │   ├── file-7vSXeZnjpHiKGMYuX8KsiD-chatgpt-1754133174787.jpg
│       │   ├── file-7W5fYZvbz8HkZfunhXD9HL-chatgpt-1753834136901.jpg
│       │   ├── file-7WmJVKZFq6q8jDcKYtv7Jg-chatgpt-1753827130838.jpg
│       │   ├── file-81gS7HNZqWdqkPY3d2iw8p-10218729890203388913.png
│       │   ├── file-8472BrXpmsR1gk68vpAxAj-1000007457.jpg
│       │   ├── file-84oMbnN8BBTa8DB2M4WqEB-1000007197.png
│       │   ├── file-86vXpo3sU8UpPiP8JytCyE-chatgpt-1753823511639.jpg
│       │   ├── file-87bSKKM216xMdNx5Po93vG-4b4f6041-197c-4b94-8600-5a5f934552a97167265390647145017
│       │   ├── file-89TaopJgUTiD2mUR2dj5D3-1000007113.png
│       │   ├── file-8a3qFgJbfjhkFKY1dnNuup-chatgpt-1754488521865.jpg
│       │   ├── file-8AeqM2Xe1zPSTChqaaWyYj-1000007187.png
│       │   ├── file-8bUseD7vvHaLzeUpnB7eKc-chatgpt-1754005020709.jpg
│       │   ├── file-8CBm8mjW9oFGXpGAADY7Wa-chatgpt-1753823813433.jpg
│       │   ├── file-8CfMvuYfw3yi2RsfNyHMAC-Screenshot_20250730-074716.Photos.png
│       │   ├── file-8Cp7RQsWkUtJd525hzwwSF-chatgpt-1754559280207.jpg
│       │   ├── file-8cxxYB3tmfkGPGdAkBK73c-chatgpt-1754070279253.jpg
│       │   ├── file-8E9eaEpcD1rvrPFQ82DAwB-Screenshot_20250727-130728.TikTok.png
│       │   ├── file-8EAHzXb8FcAsLt9cR8Ve43-b8bb786c-2594-4e19-a13e-75386271ce7e6572055210473194575
│       │   ├── file-8embzSzQfsHY6sGreeGfSS-1000023400.png
│       │   ├── file-8EsME4z4Yrw5GtkDZZxXVB-35ff3496-7bcf-4f6d-830a-136d1f15184e3823312842724206841
│       │   ├── file-8gpQo6pYQCeBdfMQddXB7e-1000023404.jpg
│       │   ├── file-8gzTGNdAb1nED7Z2UPVpDn-chatgpt-1754648576680.jpg
│       │   ├── file-8hi5Bfj4M4PA66QLN18yEL-1000007370.jpg
│       │   ├── file-8hmhaoYqtAUYqZzciVhEaa-chatgpt-1753919869353.jpg
│       │   ├── file-8kFr8edwAXZwBbkmrsqkjy-chatgpt-1754649482236.jpg
│       │   ├── file-8KfYpKS91onMZ5tqdNBJmP-1000007512.jpg
│       │   ├── file-8M2jnDNuKiFY2GQt4ox6f8-2981298e-8dbf-4ad0-ac05-3650e5be5a9b4645710315850528041
│       │   ├── file-8M5BSvaDKSXutUZRcaZeJb-1000007465.png
│       │   ├── file-8NH135HCCfv8DMKWkdiYQK-chatgpt-1754570630244.jpg
│       │   ├── file-8oHut5eScsp14x331ic2h6-chatgpt-1754045848527.jpg
│       │   ├── file-8oQGtrZGyFKvP6dhxbtPjx-1000006299.jpg
│       │   ├── file-8pnry5nLM5EQjAjc38FB25-chatgpt-1754578016947.jpg
│       │   ├── file-8qciY2xECSZRLyMGp4M8sr-chatgpt-1754131103764.jpg
│       │   ├── file-8qUHZQQzcigfWKjgfX7ot2-chatgpt-1753843674802.jpg
│       │   ├── file-8quztkNqp5re8RU6jqNT2t-1000006287.jpg
│       │   ├── file-8U3yarp4AAoXUN3qVwrwUS-chatgpt-1754648654778.jpg
│       │   ├── file-8uY7wcXvdBrLcbc8FLMNfA-1000007520.png
│       │   ├── file-8vLRubMpLpyaFMG9Dech2U-chatgpt-1754650209590.jpg
│       │   ├── file-8vT3J6CRNCdEGET5H9PcZn-1000007426.png
│       │   ├── file-8WR1UZsbxgNgGea2Ep7pFG-chatgpt-1754127824469.jpg
│       │   ├── file-8WW5v9wT7Uv7Ng1ZUKigNR-chatgpt-1753829060310.jpg
│       │   ├── file-8yWbwu3AwGR8JRunbUhs8k-1000007390.png
│       │   ├── file-8zyckozobXvjRLRJ7puWxz-chatgpt-1754570771448.jpg
│       │   ├── file-91R69DFLmSamNMWzRjRt9a-chatgpt-1754133683404.jpg
│       │   ├── file-91x1BJiULkc7T5FDhdyAf7-amazon_liability_triangle.png
│       │   ├── file-93Sp5RM3qYFRMHrVL9XkgQ-chatgpt-1753838856110.jpg
│       │   ├── file-95qXSrMT4cnYNHCEemUok7-chatgpt-1754430684726.jpg
│       │   ├── file-96iRoGsK7guyhD6J1RqnE5-1000007403.png
│       │   ├── file-99beKScc9ZrC2mn7vu2ZGP-chatgpt-1753819221578.jpg
│       │   ├── file-9B5tMkBx3GFxLTEvqiXAv6-chatgpt-1753840131677.jpg
│       │   ├── file-9BAPmaFdYzdN5UMAbAMt6G-1000007400.png
│       │   ├── file-9Bbx8dH2YS2PLpCJWFtN4e-chatgpt-1754505067867.jpg
│       │   ├── file-9bzxekQfzBLRkoVjtjWnL8-chatgpt-1754582187074.jpg
│       │   ├── file-9CoyBLNtoC1S5mAgRpQa5v-chatgpt-1754570174630.jpg
│       │   ├── file-9DcpGmRD3B3ami1umNMV4y-463a8583-7878-4925-a564-7aad53790928198441059016002145
│       │   ├── file-9dgAjKpSWFthLEc3YMepnR-chatgpt-1753982544960.jpg
│       │   ├── file-9di48b2DBy9CtAmM1pvJ8k-chatgpt-1753975326143.jpg
│       │   ├── file-9E9XQeyWUwCccmU2LhDGeV-chatgpt-1754000738800.jpg
│       │   ├── file-9HxLRTqmoAedDwWgjpSMnx-Screenshot_20250801-181630.Chrome.png
│       │   ├── file-9iFCgjLYrg8pR2G9yWcdFo-chatgpt-1754559032643.jpg
│       │   ├── file-9JhoToiNQeBMKqTTfibgjd-chatgpt-1754048358523.jpg
│       │   ├── file-9JP7jY9Ew3H6wPZMaaWA1Z-chatgpt-1754067955678.jpg
│       │   ├── file-9KBTc5q7gBEe2NgjaJvWWL-chatgpt-1753816025735.jpg
│       │   ├── file-9kckE9zsVwZERKq1SNnp4S-1000007155.jpg
│       │   ├── file-9kjkM9eRYJGF1LtXRPP2qX-1000007127.png
│       │   ├── file-9L6YrVhaUevkuGomf86caL-314976c1-95b5-45a6-877c-44396f18e0de7492270437693659026
│       │   ├── file-9m3rmuawhBBmQ2N4TqVNYk-1000007449.jpg
│       │   ├── file-9mk6mmars8uzuKVFVWwFvE-chatgpt-1754641743186.jpg
│       │   ├── file-9NMkSeFh4swJqzBv4MNJCd-1f029665-1343-4703-b6b2-6b874ce3809c4165862005557322352
│       │   ├── file-9oEQ6Y7kJBF7Dpo5Yr3LgS-chatgpt-1754513854685.jpg
│       │   ├── file-9oEspwVrDGUzoboUxnyWjP-74e1d40f-c7db-4cf0-a84e-c771e429f3388487321701229809574
│       │   ├── file-9tNxfBZFB5yPUCLmPsxHwW-chatgpt-1754053347252.jpg
│       │   ├── file-9u89EyDDnS81JA33W3JUMs-chatgpt-1753826172424.jpg
│       │   ├── file-9uJi2SrpHrqFhiNyruuCNy-7af26386-bc66-4691-9d57-3e17f76ad4655432180976418815351
│       │   ├── file-9xFTYLyz3YmSwDMTqEUNMA-chatgpt-1753828562912.jpg
│       │   ├── file-9Xo5HXR5ZzhBMVooMLWigQ-a6519a86-29e3-4a61-9526-920685a841e16840840020576504050
│       │   ├── file-9y2Bet2hAacarxNNLadNRK-chatgpt-1753825836222.jpg
│       │   ├── file-9y6M74RHSFsjV3whLyT5jN-1000007252.png
│       │   ├── file-9Z3oBGFcwH9ujgu683eqDA-chatgpt-1754004342472.jpg
│       │   ├── file-9z8aq4M3LdcYDaAgG2MGze-4420edaf-18ed-4921-8637-07266ca28b0e3637493090630267242
│       │   ├── file-A1ifRMuTBRtSCyPQDnEusA-e62e1d4c-1200-4bf4-a2ad-da94d915c5c64941235740735503039
│       │   ├── file-A1J2m1mnQtPqNSCkUiB9zv-chatgpt-1754042833975.jpg
│       │   ├── file-A25qE4wpxdDFsGER8zy5LJ-1000007451.jpg
│       │   ├── file-A4u1AY1omXLeAFmc3svGeK-IMG_20250804_101130574_HDR.jpg
│       │   ├── file-A5fvgQGTjMZNnn7TqaCyN7-Screenshot_20250723-190740.Spotify.png
│       │   ├── file-A64hmAPboZGDPnpL1CKyb2-chatgpt-1753843305988.jpg
│       │   ├── file-A6RG4erNuJMndspWzZGqvN-71283d50-77c1-4012-990e-cb481d52b5b74250417514213113789
│       │   ├── file-AajeuWo4NS6X4VLqL2tCsz-1000007528.jpg
│       │   ├── file-Ac85MnsMWDwJfunxcGdNgf-c0392cd2-ec8f-42b1-8574-d22b8c9286ae8730422383741179859
│       │   ├── file-ACmywdruT2CHzaqeA5H5W9-tenor_gif6626364681387619815.gif
│       │   ├── file-AdhFDUjjjzLdNFzfMa9v4L-Screenshot_20250801-182648.1Weather.png
│       │   ├── file-ADuAa5tcttL8FndpTFArUg-1000007397.png
│       │   ├── file-AeJVAtAN88nD5TxxzHAGxR-Screenshot_20250723-213551.Gmail.png
│       │   ├── file-AfCD73sz5SaxQP5kDFVXKT-chatgpt-1753820983872.jpg
│       │   ├── file-AFe3jLqCRxeozMJQPMyF8E-af194aa9-a1d3-498b-b68b-de04fe5d5be52026178905142203865
│       │   ├── file-AGCqUhR9NvFv6yFkrQRCzj-1000007433.png
│       │   ├── file-Ah5BoXjLb8f6mZHNabsAmy-1000007475.png
│       │   ├── file-AiWF2BZfeoAiFG6xfSk6Eu-chatgpt-1754569782630.jpg
│       │   ├── file-AJRrNhqakDVhjv81aHVF27-1000007513.jpg
│       │   ├── file-AKjC9X1cFqNfAnNxq2DtRZ-1000007548.png
│       │   ├── file-AkyeLTJUhC41LPqZDGMWMz-a5ce6a6a-fab3-4e67-abc7-eab051b04e563291122687086995867
│       │   ├── file-AMnan72gAGSwVg1DdtwdRs-chatgpt-1754577154404.jpg
│       │   ├── file-Amv56AJ617nt7SzseYqsoD-chatgpt-1754575528087.jpg
│       │   ├── file-AmXkr6i8TrSfSH5XFrbWbJ-96b70244-551c-4e25-9ed0-527a053f068f1095157847323087727
│       │   ├── file-AN76EtE8LdYouwg5fDL6R5-chatgpt-1753826560762.jpg
│       │   ├── file-AnhFHo35N9Q5BbQE2xJcPC-chatgpt-1754578185204.jpg
│       │   ├── file-AnmabMr1hxiCsUcoBLJFbU-chatgpt-1753853639585.jpg
│       │   ├── file-Anr3sM7zhpWbJZ6YHGek3Q-chatgpt-1754513663166.jpg
│       │   ├── file-ANvWteHhcceJVpEDHi2SyY-1000007532.png
│       │   ├── file-ANyvAAUHBeQtUu7aW5mD9u-chatgpt-1754570660107.jpg
│       │   ├── file-Aoc7EoMwiE3FG2qY9ogske-3135652b-51e5-4a7d-95c9-6456d24148163932493783267510214
│       │   ├── file-APap6ezfnQoqHQCBznJ3kU-1000007225.png
│       │   ├── file-Ar8okFvr1TRLsE2cmQmtgy-chatgpt-1754496016002.jpg
│       │   ├── file-ASephXbzaH7RDZCMXx1M5t-1000007391.png
│       │   ├── file-ASTTTS2eMHg4DVckBrehSY-88a5731f-53d7-4104-8507-d778c692b72f3921297931475098371
│       │   ├── file-AtKkH8rbs8sDarAbAUhpM8-chatgpt-1754495956391.jpg
│       │   ├── file-AtLbFLcDiQgMuV6WwHe9id-Screenshot_20250714-162427.TheDaily.png
│       │   ├── file-AU7A2YSBGfBUHd38xf3m3K-1000007542.png
│       │   ├── file-AUBNTuKbopp8XeRRJzVJTx-chatgpt-1754648889303.jpg
│       │   ├── file-AUHeUbXJkzRpDsNWcBMXDM-8ad61cc6-7402-4004-ac99-661938fc8c4a6670471651671585029
│       │   ├── file-AVQ4JkcADos1VZiZHN1drE-chatgpt-1754561200875.jpg
│       │   ├── file-AWTJSyDXDQA6yH92KLxvHt-chatgpt-1753973081659.jpg
│       │   ├── file-AwUUKPhL7jaGvMBE1C1QKY-Screenshot_20250730-161514.Chrome.png
│       │   ├── file-AWZv3aGqnBDHoJuHcnRY7M-1000007445.jpg
│       │   ├── file-AX1X6HAN7BHFVGdYXvuZDb-10218729890203388913.png
│       │   ├── file-AYAxEmCD2xK5s8R4P6Av9q-tenor_gif8186052281940233275.gif
│       │   ├── file-AyfVCuqetvK6ZLkWgRgdQm-chatgpt-1753893265411.jpg
│       │   ├── file-AZNBMy4LthdA2Qv7i9Da79-chatgpt-1753820007638.jpg
│       │   ├── file-B2gWL9nMvYxiRLdjcQYJEu-3d2a928e-e317-4e8f-805d-f0dd423b97e06618476935796895889
│       │   ├── file-B6wgQp83Wy73t6yh9aa1xV-94b7443a-4e5c-450d-8302-d040b85a6e084899957659900773290
│       │   ├── file-B7WTPRh93fF2w3yvNuoyH3-tenor_gif7781131444054125543.gif
│       │   ├── file-BB15QzCCNwsuKTEaLsgdbz-1000007390.png
│       │   ├── file-Bbvv9ffPdtC4fPJ5BzqzYD-chatgpt-1754649991884.jpg
│       │   ├── file-Be88RPQeXfnseV6bwRJTDN-chatgpt-1754431475520.jpg
│       │   ├── file-BEtEvTuefqBEGbuu9aYJVc-a6db78a4-6f59-45a6-9d9c-4970a6fcbf6f3287887296289324137
│       │   ├── file-BGEvqRcsny6C8zKnUkLzy6-1000022970.jpg
│       │   ├── file-BGq1FhzWHYq7vUSrNUAp9c-4dbb8207-b77d-4173-b91c-d412b75f48f94937292432362210134
│       │   ├── file-BHrA66UxXRzXhn7zhX5QPi-chatgpt-1754649411198.jpg
│       │   ├── file-BhuBtF9DDTJAnSyjJN1pfN-Screenshot_20250806-215316.Chrome.png
│       │   ├── file-Bi39bcSbqWUe26oW2Lpr8C-chatgpt-1753844782572.jpg
│       │   ├── file-Bipqk1o2nbkSrpBxczkhvZ-chatgpt-1754051687321.jpg
│       │   ├── file-Bjr5fuChTCjLHTN9NySxzX-1000007241.png
│       │   ├── file-BKNVumBU4FNGPxLmzx1qQR-chatgpt-1754556453930.jpg
│       │   ├── file-BkXiptkgJDUMy6KWvap1MR-01dcdd22-52d7-465d-b79c-f1f12c99f0455383948191208222280
│       │   ├── file-Bmkp48X91PNfgmHAAwf8eo-Screenshot_20250724-233911.Facebook.png
│       │   ├── file-BmReKQFhntAjWtSsKaf3Wy-2d161d3b-d6bd-4401-a9e5-acaf669375dd9115159989421001435
│       │   ├── file-BN2CGkRk2rJUYGoAbajPPX-chatgpt-1753921547277.jpg
│       │   ├── file-BN7amt7ZvauhN5kctFku5z-chatgpt-1754577735129.jpg
│       │   ├── file-BPP2pKqdbNKfE656TVBTc4-chatgpt-1754557530536.jpg
│       │   ├── file-BPT88au7c9iQReWBMsUx7y-chatgpt-1753809372477.jpg
│       │   ├── file-BPUmMZzm2eq63h4mzML7hR-6f940d9b-b3ca-4e27-b82c-b67ff82eed607415343335682550725
│       │   ├── file-BPXXXyAmCmjwgDG7gjVSjv-2f53d545-8504-4056-a297-3a3da79068d25896707067138796521
│       │   ├── file-Br3ohETSGzPtZZvFWzZh1x-88bef2a4-bdac-460c-8411-9c3e1bd28be67006798208964930269
│       │   ├── file-BrJN7nm4pCbczi4ScuScNF-1000007469.png
│       │   ├── file-BRzAMKvsEC5wp9Zmykm6Qq-1000007138.jpg
│       │   ├── file-BSUvq5uttQX3yDmnTGLhdN-Screenshot_20250720-212023.Substack.png
│       │   ├── file-BSvBRtbnnZBrhvgDDFEUj1-Screenshot_20250730-102207.Facebook.png
│       │   ├── file-BtAkea3vRmAoGvkmf29xkV-chatgpt-1754516994958.jpg
│       │   ├── file-BTHwiE8tEpMpb981p97qiW-chatgpt-1753834535537.jpg
│       │   ├── file-BTKghfC7RYGrGKJQt3xMdu-1000007201.jpg
│       │   ├── file-BUUkjjCijoDMXJW7vRYRHN-1000007306.png
│       │   ├── file-BuWGU5torgwMDzUneJwCrx-1000007434.png
│       │   ├── file-BvRnyVLHaqg6LChs3H16Qm-chatgpt-1754571654631.jpg
│       │   ├── file-Bwd1VtCcai4a54g9ZXEdVL-chatgpt-1754557457634.jpg
│       │   ├── file-BwemLJwgaDeLVU8g3xV7Wq-chatgpt-1754582581844.jpg
│       │   ├── file-BwoPMpGxGUN1znaWT5VX5K-1000007154.jpg
│       │   ├── file-BWSdau5XggAL7Gc1LCaGc7-chatgpt-1754495900167.jpg
│       │   ├── file-Bx6e8YLcd13La517ghD6BR-tenor_gif118564218399150643.gif
│       │   ├── file-ByeFFHewoZuxo2WXC5uJJo-1000007353.png
│       │   ├── file-C1AsYtvineZ5SN56WRN2dT-chatgpt-1754579231280.jpg
│       │   ├── file-C1eycV7EHs1Fky36kkKcuB-chatgpt-1753809346856.jpg
│       │   ├── file-C2h9yBA29vEKRkC1cpuRr3-chatgpt-1754576508444.jpg
│       │   ├── file-C3h9EboYJoxNG4LiT7sAui-f0b2b060-e941-4536-896d-725fe1f7c8861585898805091594183
│       │   ├── file-C4WV2UUj3c2H8LrWTpDgQx-e1140af5-59cd-409d-98b8-854c4bacb21a2178979276949084179
│       │   ├── file-C5jreu1dDxgCDeUd2kEQtC-d35f6ef5-3563-4b55-9a39-98996bd8ba967860801016656077269
│       │   ├── file-C5X94eSkty9pFXsRGHL6Sg-chatgpt-1753829245704.jpg
│       │   ├── file-C6K5ujKNMCMmkrYo8xLJhf-chatgpt-1754133298549.jpg
│       │   ├── file-CaTRF1tCQeq1biMuPU9XKg-chatgpt-1753920320896.jpg
│       │   ├── file-CbYAMiuREBX5JBmwDVAxLG-d767e1a1-1039-4871-b829-7c799386adb1156068329071189116
│       │   ├── file-Cc6afYKVFSE6vbtmVctYbe-1000007135.jpg
│       │   ├── file-CckEch3T2vexERZoua1WEL-chatgpt-1754038471435.jpg
│       │   ├── file-CE9L9mkpSNbvq2j5i5BjQu-chatgpt-1754069254494.jpg
│       │   ├── file-CfPMg2sxP8vh8hoNEucLDf-1000007221.png
│       │   ├── file-ChHN6Jfef6nZpZPLwx3hj7-ae19d4e7-c92f-4954-9283-69f1957e44476983731265696121376
│       │   ├── file-CkCrPf6xW7xz9HmSY1LEBf-1000000059.png
│       │   ├── file-CkVCe8AWJT8imHLespmZA5-chatgpt-1753825849434.jpg
│       │   ├── file-CkvTTjURpExV2qenrYeaZj-chatgpt-1753852031402.jpg
│       │   ├── file-CKzzbBK8RqPZ78hX9aYs3E-1000006297.jpg
│       │   ├── file-CMtQhR9DndsFMUEkz9vxyU-chatgpt-1754133078441.jpg
│       │   ├── file-CNe6ueKfDYmdmEgWipehTh-1000006546.jpg
│       │   ├── file-CNsemppaMFyD1DX83rZGRH-chatgpt-1754046058460.jpg
│       │   ├── file-Cnz1hnVPPBRFdRxVic2H6w-chatgpt-1754650291971.jpg
│       │   ├── file-CPCsgogssDJk5mZcccFvYR-22ead853-17bb-4318-805d-0499b4461153488911730806970506
│       │   ├── file-Cpo9Y4xSVBSAwCHqfjGv2p-chatgpt-1753893585804.jpg
│       │   ├── file-CRUqhFCiUCwAXzcN3NqCRt-chatgpt-1754069294923.jpg
│       │   ├── file-CTBnoYSZcBuCV4rX3pSbUQ-Screenshot_20250721-143155.Gmail.png
│       │   ├── file-CTkzbZ5ZVZ7k3YNRCj7UWp-1000007451.jpg
│       │   ├── file-CuMbfvay4NvSHj2apGkAxU-1000007434.png
│       │   ├── file-CUNUyPRBngawawUGPCuJRa-chatgpt-1753879839635.jpg
│       │   ├── file-CuYLsXWa1eMdxpqQZJ24TP-1000007393.png
│       │   ├── file-CvTtwtQQmJkcgULyviMBpo-chatgpt-1754650682898.jpg
│       │   ├── file-CWfZH1qAhFoGW3RhMhQYMk-chatgpt-1753808070255.jpg
│       │   ├── file-CWkqXyPKndntaG7vdpGTcU-1000022789.png
│       │   ├── file-CX1ZVTU5D73SCjYLXmXypS-chatgpt-1753847989922.jpg
│       │   ├── file-CY2JHhDy4SKQFrJVrCiiNZ-1000022788.jpg
│       │   ├── file-CYGJZjPPbYWVcEimzwhhLB-chatgpt-1753831872290.jpg
│       │   ├── file-CzZhSWhVGS9NQEvpZzCxDJ-09ddc6c7-1d59-483b-afab-24a7a52fee4f8016718068415301378
│       │   ├── file-D1XtMjUDwjP2MkGdUa2PhR-1000000034.png
│       │   ├── file-D27rrpGH6McgF6u2QErS9o-1000007220.png
│       │   ├── file-D4C6rV2zKPM3eMfqG3Aen1-chatgpt-1754584129312.jpg
│       │   ├── file-DaM4hZgvn7YmPeHJEvzacy-chatgpt-1753982271830.jpg
│       │   ├── file-DDpsXq1Sc8BSA1uCxiZD97-208e3bed-8c76-42f5-a93a-850de452e0557408392230896285006
│       │   ├── file-DE7pUdMNxZgyWmq2NN8BBS-b36b05fc-7933-410c-ad32-e417de20572d5526576651912586344
│       │   ├── file-DF2bMUCLYDnzngNNqMHPWL-chatgpt-1754168921633.jpg
│       │   ├── file-DFBUp85c23gZw2KG76kPSy-3902eaa9-b3b3-43a4-b5c7-02bc8ac803492082166034269736428
│       │   ├── file-DfdzKqPnpbQ6huzZecN2Y1-c447d128-d6f3-4505-b41d-92e1e97d23f37484062501367225385
│       │   ├── file-DgvSeJ9dkuNkojZjeMMu3f-chatgpt-1753826738449.jpg
│       │   ├── file-DJwWzuzrCPmb6SV3JAoKBQ-Screenshot_20250805-181125.Gmail.png
│       │   ├── file-DmToR9Y4aFFoXLARzsY46H-chatgpt-1753807551043.jpg
│       │   ├── file-DNdTkHEoFy6JvjmHdFCNhD-chatgpt-1753834038962.jpg
│       │   ├── file-DoNpWvCqCVM2xh9WkT2Ep8-chatgpt-1754558233356.jpg
│       │   ├── file-DPa2MhL13TG7Fu2VTkFQ66-chatgpt-1754046173274.jpg
│       │   ├── file-DpEPuqqBgCq94cZBQzCWzU-chatgpt-1753852923021.jpg
│       │   ├── file-DPMAsKPF4HoyF6ZAjGsFy6-chatgpt-1753952582261.jpg
│       │   ├── file-DscTeJDKCgMjkZR1Po2XNv-18df5378-ef2f-4615-bd24-9c27560b151f1127232049006959398
│       │   ├── file-DshN5yvfgzqKFMDiJzEtG3-1000007394.png
│       │   ├── file-DShyHvoAN2PNJ5rSKpiqxR-chatgpt-1754494147546.jpg
│       │   ├── file-DtMnHuPAMPdXsa5diAiwuo-chatgpt-1754513889094.jpg
│       │   ├── file-DtwfUUmxM1Q9mfgZgeT1Qq-chatgpt-1754581516999.jpg
│       │   ├── file-DUpuv1JFSWsg94KfYetzKd-chatgpt-1754583138621.jpg
│       │   ├── file-DWE9goKSQYtXCh1gkV69Ve-chatgpt-1754554685418.jpg
│       │   ├── file-DxSiYbGinXpk4MEXYofTZ6-1000007402.png
│       │   ├── file-DyFkCb9s49jPX6B7FQuQpV-d802f2ef-4411-4f56-954d-075dda8ae6953298529078956430482
│       │   ├── file-DYkL38pjZ9PFJTUNziGsiW-chatgpt-1754577809620.jpg
│       │   ├── file-Dz6bzRn2W6yKBUdDt6TvVG-1000007247.png
│       │   ├── file-E1ahDHeCh9pLsicM4oquTD-ab0e8091-9aa5-484e-b19e-c4352c46a3791424374336348345093
│       │   ├── file-E49LRySXCM6ZvL1gPszziN-chatgpt-1754641838712.jpg
│       │   ├── file-E4kaaH7SRVd8ygzwgr431M-1000007450.jpg
│       │   ├── file-E5dcineYAQc9zVXnPT4GWE-1000007425.png
│       │   ├── file-E6LENyrviDWoyHypMGaLg4-chatgpt-1754554189288.jpg
│       │   ├── file-EaYyuro9LeqQFcXmo7o9Zr-chatgpt-1754046264026.jpg
│       │   ├── file-EC64wFsiUDaQGRWmC7Wvap-chatgpt-1754045983637.jpg
│       │   ├── file-EHPLy6x13FM45QpfzQ3aEk-chatgpt-1754168815198.jpg
│       │   ├── file-Ej42qZVKbCBXm9ktsdq5hS-1000007390.png
│       │   ├── file-EJhJQFsdjTnkFin4CimH5s-47d5ad77-28f3-481c-ba79-c09894b33a145065808940491334853
│       │   ├── file-EJig6UMS7BZcYTRyBEYEU5-d4e539b8-9c9b-45f8-9666-9db347640cf2396262074780667091
│       │   ├── file-EkmYb4SuhBVCzbCzoKYqZM-chatgpt-1754167792240.jpg
│       │   ├── file-ELNS1ksBx11pnxGmW4eF7g-65ad9dbe-a63a-4595-8d2b-e336328221cc5986036563961545178
│       │   ├── file-EPUsbhoYWJQ9p1SFoRwyzP-chatgpt-1754559338140.jpg
│       │   ├── file-EPwT5vLhwJZd4vMhkQtYzn-chatgpt-1754041092781.jpg
│       │   ├── file-EQyQHZLdEGBFiaGgVH8dL1-1000023063.png
│       │   ├── file-ErQbRSXYfWrys2YZuw2t3h-1000000022.jpg
│       │   ├── file-ERrzswLg8UtSXxaBSNdvEc-Screenshot_20250725-221816.Chrome.png
│       │   ├── file-ESh4xt7yDxHUnxdVYQGH2S-d12a150a-2be9-465d-9b88-1efa596affe84268772762555520037
│       │   ├── file-EtoK6bbvezbvMwCiyY98s4-chatgpt-1754570876100.jpg
│       │   ├── file-EUWgoPTcoaJDfADa5Mej1C-1000023194.jpg
│       │   ├── file-EvNYYeiQXDaZb5QzLVwScd-80fb5c75-e5bf-4df3-a688-f0904b1d49332929908325895598359
│       │   ├── file-EXCCeY6g9ZVnjGBp9kvmka-chatgpt-1753829727117.jpg
│       │   ├── file-ExJbMocn4jYDfiiLRogmEy-Screenshot_20250716-222457.Gmail.png
│       │   ├── file-EXJPUWnVgMwkJ23TtsU2hV-chatgpt-1754576989643.jpg
│       │   ├── file-EYTaw5KYRoT7uLDNztQ31G-1000007390.png
│       │   ├── file-Ez3Bghn5qVKUjtnLd74QqM-chatgpt-1753819150751.jpg
│       │   ├── file-EzC1KGpoMJqg4WhHSMFRAC-1000007179.png
│       │   ├── file-F2YKHgYC9a6BJ4KAgpxjjp-10218729890203388913.png
│       │   ├── file-F3ePN1YPeaKXx2QvC3AKU5-chatgpt-1754052215115.jpg
│       │   ├── file-F3HQbt4STPzBhYcNPps2g7-641a0c8a-7bce-43a9-aadc-a2bd65fe4ced208621558643977810
│       │   ├── file-F3yJ41LAFuvzZwfRUQ9dnw-f74166ad-bd67-4faa-b71f-775bfab701de3572533941952006990
│       │   ├── file-F3ZPNvDwmBveJtLP8KYwXp-chatgpt-1754486197060.jpg
│       │   ├── file-F8PxCRfShi4jWWnJKgtjCT-1000006572.jpg
│       │   ├── file-Fb9WoKTTiGYi2nurzTfqxe-chatgpt-1753853143222.jpg
│       │   ├── file-FBveJ1jboii8wcDDbAkCRV-chatgpt-1754517816630.jpg
│       │   ├── file-Fc5QhLWgNqW8vFXdm1wbg7-chatgpt-1754582652480.jpg
│       │   ├── file-FCBwfGeNm2Tm5TZ39K9sCf-chatgpt-1753824032392.jpg
│       │   ├── file-FDANmfzXE1gWiK6uwX44DL-1000007382.png
│       │   ├── file-FeqXCLGMmYb4iEVMq6DTcx-69851ca4-d9dd-438a-886e-bc425b29ec3e1262087747188328737
│       │   ├── file-Fgh9H9HpXxiCgt3foc7pSp-4087274a-9119-4c3d-98d5-884f027ee4c32635495790614894420
│       │   ├── file-FgpbMupHSFxiPSd9jcinHU-chatgpt-1754069495574.jpg
│       │   ├── file-FGtDi4Kc5eajKMQKyPN96V-chatgpt-1754067984311.jpg
│       │   ├── file-FH77oyCDUhXBWShddNGGiu-chatgpt-1754650842754.jpg
│       │   ├── file-FHT9YzFytGAoStZ5AVqwAT-chatgpt-1753833756323.jpg
│       │   ├── file-FiuNJfgRFRU3159s1M4XPU-a194e7c9-34aa-4953-a0d7-e746234230cd1345124212511806606
│       │   ├── file-FkrxNdaKYTcrMXyamMXgZH-10ad9142-2a3b-4517-90ce-571ca8bad3991587194291340778350
│       │   ├── file-FKSqWeNN2foYLLhJr8nhDR-chatgpt-1753982514953.jpg
│       │   ├── file-Fm5HsymJjgArMDiXqGo4HU-bdcfa0fd-5eb7-4d65-acfb-e88c0bd79be12958498518485370609
│       │   ├── file-FMnMEEwiX9xr5FFWL6gcYC-chatgpt-1754649702027.jpg
│       │   ├── file-FoxiKCS3UTfVZxSYeTGA28-1000007480.png
│       │   ├── file-FUar57XfEWHhBx1kiuLVQP-chatgpt-1754558037970.jpg
│       │   ├── file-FVbqV1Ys29b7PMuYjui2Wy-1000022860.jpg
│       │   ├── file-FvCwVvgVRcEkoMcuuCHuM7-451dac88-9e4e-470a-a713-54764d7b76245911273879948124383
│       │   ├── file-FVG3Pt9irB21oZ5W3YMjEh-1000007136.jpg
│       │   ├── file-FyVAb8dmjpo9e8HnQMybc6-1000007473.png
│       │   ├── file-G1fbbNCFnbtnK73nvD8upD-535bedf2-9315-43c4-9878-a6d19d1582fb145732484274118213
│       │   ├── file-G31AWx9CRL4M5Y9bqiiNSL-1000022788.jpg
│       │   ├── file-G68ULkUfbeBo3vtf7uP74Y-1000005631.png
│       │   ├── file-Gb9UQDUUe7qrxoqyoZW61X-1000023381.jpg
│       │   ├── file-GC2RJ9VAedpjRJsvkiKhfU-1000007533.png
│       │   ├── file-GC5NxpR3WibPVnu52jvWYQ-Screenshot_20250722-203227.Spotify.png
│       │   ├── file-GD6VevDKtpacSdPmp24vt4-1000007470.png
│       │   ├── file-GfhBFEiu511RJRnS5N2b36-1000007429.png
│       │   ├── file-GGB1iXt4euW425A224QQou-1000023482.jpg
│       │   ├── file-GGdaMiPUencNutRmFpUpkQ-6305df4d-62e9-4093-b407-067788d652331327402265223168750
│       │   ├── file-GGwiDHdshKLXzip9Gsay2p-chatgpt-1753976146989.jpg
│       │   ├── file-GGyb8677YLExWFXM2VTBNh-chatgpt-1753843564853.jpg
│       │   ├── file-GHir1FPLZVpsXtKCdj6u8y-chatgpt-1753818739568.jpg
│       │   ├── file-GhVxajdePHZnZa6HY4JFsQ-chatgpt-1753851316943.jpg
│       │   ├── file-GjfnLSScCSSq3RPLVwyQ6C-chatgpt-1753816660260.jpg
│       │   ├── file-GKUEfofJd9nka4wSJVEqCN-chatgpt-1753843208875.jpg
│       │   ├── file-GkzQVrL5NNh7NkPtZmmRD4-1000007133.jpg
│       │   ├── file-Go3zwGaF47dkec9wDd1zM9-1000007263.png
│       │   ├── file-GP8p2b4MKPBENfJ4d2YLpS-chatgpt-1753846666875.jpg
│       │   ├── file-GQRXh4VbEGqvhujCS3WpEQ-040edfe0-3645-4c95-a2d1-0407a45b316e3261129032150743143
│       │   ├── file-GRk64vPLNqNaVZEssxDdJZ-1dbe1ca4-8a2b-4599-a758-d58263a77b89.png
│       │   ├── file-GRN7EBinYRwqzwZBkThS8f-3e652459-e42e-4727-bb91-66e2c9c028fb2582123717267656206
│       │   ├── file-GRPyMxbpKgCTvqVUQAHM2e-chatgpt-1753893064192.jpg
│       │   ├── file-GseCmDazXmpRFCnW7sPait-chatgpt-1753834461963.jpg
│       │   ├── file-GSoXqb48wyp4wiuDUWKEqq-2ea94d56-6032-4ce0-8fa8-e2758b86f0e92731682942152484742
│       │   ├── file-Gsqmz1Q7APBAkts5xvDzze-55af73e3-6668-4272-84a6-f1421837384c3410185366798246666
│       │   ├── file-GuM5kFR7f7LAPTa1jzhdr7-8547c697-34b3-410e-8d5a-748e4389fa407790997789840747812
│       │   ├── file-GvLLCeSciERC49wDVU6CPU-1000007154.jpg
│       │   ├── file-Gw1eN4cRvvKffihKgpLpXq-f1c22528-4ae4-4ec2-99bd-a51ea6f895d94116292031315665968
│       │   ├── file-GWC4fQihDLScgsWeZJ4e4R-1000007240.png
│       │   ├── file-GYrNkHiSBQ3QJBS6B4spz4-chatgpt-1753853092885.jpg
│       │   ├── file-GywBrV5tubAQSneq5oMksm-chatgpt-1754039426733.jpg
│       │   ├── file-Gz8aBZMrg7oSeUueQCFvSR-chatgpt-1754570535088.jpg
│       │   ├── file-H5NAAuHZTTCf3TmY3YLFTn-chatgpt-1754042554277.jpg
│       │   ├── file-H5uAMvo95QHeARPcTMbyw4-1000023425.png
│       │   ├── file-H6YtDMSDw87ruNTWafxD62-chatgpt-1754051630468.jpg
│       │   ├── file-Ha7mTdjRx4Lm6dUbBeCMbq-chatgpt-1753826957066.jpg
│       │   ├── file-Haimgu4BCq15R2FJWa2kQe-1000007202.png
│       │   ├── file-HavijgZQiygnrmQq5K6e49-chatgpt-1754570321610.jpg
│       │   ├── file-HB51FETxadV3Nmpg9Q6zGi-chatgpt-1754133549380.jpg
│       │   ├── file-HBP4Tqhu5CWnUZLpdFcivy-chatgpt-1754490456378.jpg
│       │   ├── file-HcNgkQdD5AY2ME95Bv1ZJ3-chatgpt-1754513949715.jpg
│       │   ├── file-HCTGT1wisnYAeULM8Tpxr2-chatgpt-1753833520055.jpg
│       │   ├── file-HdkkJN3nSWjDfe9rrCsujX-1000007459.png
│       │   ├── file-HE5EU8rJvrRegH2XKNhTtn-chatgpt-1753823669259.jpg
│       │   ├── file-HEF4vh5ARVxbYiUfYxYcg1-chatgpt-1753846578377.jpg
│       │   ├── file-HF2PZa7GWYsG4zFdEDLPiU-chatgpt-1754556165089.jpg
│       │   ├── file-HG9WStRryCLdvu1zee776u-962bb9a4-2a10-42cb-a79f-57745173092d5018297771543468433
│       │   ├── file-HGTF8gaMB2eQHFLtgkKjiD-chatgpt-1753847309404.jpg
│       │   ├── file-Hh9yjE1eHvtRbiUSXw9Dqw-d19d00b4-bc6d-4cac-83d9-33fe354ac82a6680643010933867731
│       │   ├── file-HhMbFpBjG2TAB2WvPfQXkU-1000023405.jpg
│       │   ├── file-HKT7fNYPxxABpqfH5ioaNY-1000007539.png
│       │   ├── file-HLGqYmjK84c6pkzgohN7ox-1000022843.png
│       │   ├── file-HLWZFMbzTm9JYQbse7xXcm-1000023160.jpg
│       │   ├── file-HMFnZ9apYHF6x83BUYR37k-497a07aa-06dd-4f66-9089-f4dd4487c41f5204177684935701563
│       │   ├── file-HNA6GkmTWTGbSsmDzDh5Yf-1000022822.jpg
│       │   ├── file-HpKcTstsQjdsjeqBYidUV3-Screenshot_20250727-202835.7-Eleven.png
│       │   ├── file-HpVxxXXGEsZzv1vVyqCpqs-chatgpt-1754499810491.jpg
│       │   ├── file-HQK4D3EEJm5zNRQWbHN3hY-1000007456.jpg
│       │   ├── file-HqNPQh5Jw5Mke6ooiVQWjM-chatgpt-1753843475707.jpg
│       │   ├── file-Hsge5duzqnT3AT2HaFrD82-6d9bd89c-7b3d-4263-8083-5bab49613d611552288482852755450
│       │   ├── file-Ht8udp91iAXzkrKg4btfyc-23369005-ae29-4804-ad25-af2588a043f27003756033125989884
│       │   ├── file-HTbfjX6rGaXieBqbFXoBab-1000007398.png
│       │   ├── file-HTW39hhbPu4na5PCgCXNpS-1000007433.png
│       │   ├── file-HvgwdRAmp1giazpFUuW6ZL-1000007221.png
│       │   ├── file-HvLSEpYQGXTvRjJDZuJNHu-1000023403.jpg
│       │   ├── file-HVNwTB3ZdcVwcu3rqKip6S-Screenshot_20250804-124239.AMC Theatres.png
│       │   ├── file-HVyZGcb1matNpttJwhzjoH-1000007471.png
│       │   ├── file-HWxGLJBysX5cXPvbPV4yxQ-dda98138-d723-478d-8a62-931c66f299d43007468499256100624
│       │   ├── file-HXqY6QgNk49UjdSKfC8Z4Y-chatgpt-1754494109069.jpg
│       │   ├── file-HXXvTg5QKdSVExxmL3rfmj-chatgpt-1754582700973.jpg
│       │   ├── file-J1sXzVmECBmiRGBdjEwRdD-Screenshot_20250726-141349.Chrome.png
│       │   ├── file-J3j4tgcyd6nbJAUXxrvsKs-chatgpt-1754586207919.jpg
│       │   ├── file-J5o7rdwPkZDZoYRZNXzkpe-1000007390.png
│       │   ├── file-J6cgwzqeMpAvXetX139VyH-chatgpt-1754576936309.jpg
│       │   ├── file-JacvUpLxwd7CDog5AL4Pnn-chatgpt-1754581588591.jpg
│       │   ├── file-JBfZjaPGVAsqFmQyS697ro-1000007464.png
│       │   ├── file-JcHo7fXDxQ8sY75pc8toqt-chatgpt-1754470375259.jpg
│       │   ├── file-JcXhx1XXWxRk4sKfqH3B5N-96d81571-8707-426c-a48e-672ae67b8aae1197256590081575361
│       │   ├── file-JEMQPfevvTmVtUQskZs8Xt-a96ef922-dbd8-42a0-b096-cf2a53cd22581074929347692380478
│       │   ├── file-JfDmfK42uU73V8CKQomLDQ-d5c0e459-bb5f-4753-8496-c9d7610853416642390616980453054
│       │   ├── file-JfkzyUcSXJnGULHQDBZEWx-chatgpt-1753847424028.jpg
│       │   ├── file-Jgiz8j1e3Rb76Rxn9nqATV-1000007119.jpg
│       │   ├── file-Jj5G5gJDk73hwicqKRJFj4-c9f16294-e044-43ed-8425-97f1b9b1e9657236271445620938665
│       │   ├── file-Jjn96jKCiy5xuktzXMf56V-1000007178.png
│       │   ├── file-JJoggujVU1yUKih3WpRQc1-1000022786.jpg
│       │   ├── file-JnfMsjVbqJpy29i1vaRTHK-chatgpt-1754133310230.jpg
│       │   ├── file-JpcCyXrriEDdRPGdobGrHR-chatgpt-1754328135833.jpg
│       │   ├── file-Jqoem9xdFYSSr3d9m96qts-chatgpt-1754002381906.jpg
│       │   ├── file-JQrG2NkmigCCyxHcYaVGgv-74007b16-3401-4171-a748-6cf02a8048d51120792353080983867
│       │   ├── file-JrjAJ2jLymZBShBcUjGvh6-Screenshot_20250726-123622.Chrome.png
│       │   ├── file-JumsT4RpX5QFjpKST7DepP-1000023689.png
│       │   ├── file-JuzWwGFDfcKRS21CL79ds7-chatgpt-1754479745332.jpg
│       │   ├── file-Jv7CKd6VAhv4r2nUqaRAXS-chatgpt-1754576410420.jpg
│       │   ├── file-JZ7waCZJuAKCcdNSm4gvh9-Screenshot_20250806-083158.ChatGPT.png
│       │   ├── file-Jzy5JgnJ4LyGSyjunmwWFS-chatgpt-1754659222862.jpg
│       │   ├── file-K1NAQ6H21Me3k9TKMNsXyC-chatgpt-1753983436113.jpg
│       │   ├── file-K246PdWME7pZBMDxFziYUz-chatgpt-1753824133220.jpg
│       │   ├── file-K33uhEYpUzj5DqWTWntLMj-1000007499.png
│       │   ├── file-K5pG7QRMNu5SXc6eeC9kRD-3f29d8eb-c8ae-4a5b-a35a-6f125e3487172826099835855083945
│       │   ├── file-K6Cx8jvANUnSZLjDtDWiRk-1000007508.jpg
│       │   ├── file-K9Rfb23zy5zJ5xAtbRQKL3-chatgpt-1754060108280.jpg
│       │   ├── file-KAFKWMcS3Gzi26pNsrcvc9-chatgpt-1754556507001.jpg
│       │   ├── file-KASpzY47CUMqYsMgkWNYmz-c0e66d0e-902e-41a0-9605-eeb4f93473755039953733402018894
│       │   ├── file-KevUQxmGs2SzViAiFNE7Gj-92e6913b-f3ff-4606-b6c0-12febbbbac67798753631699194114
│       │   ├── file-KEZjhqGa7WqLBXoBs3KcP9-chatgpt-1753977157843.jpg
│       │   ├── file-KF8x1retyCyopS2dxc4PKQ-1000007401.png
│       │   ├── file-KiDETiL2G4PjRpmSNvU2ve-chatgpt-1753803590562.jpg
│       │   ├── file-KKFwj4S413SzZtvc6iFbFQ-chatgpt-1754133719667.jpg
│       │   ├── file-KKkoA2bD7jjV4CqCFYG5wq-b5eeeb0b-8a94-4639-9902-835a5e1c48139157813209972986742
│       │   ├── file-KMnyNSmGvJt1veESx2L4Y8-chatgpt-1754504280327.jpg
│       │   ├── file-KPbjE2EH478PAxYrcFdfKm-chatgpt-1753732634167.jpg
│       │   ├── file-KPvcUuptcfKSoFYaGet6Mq-1000023662.png
│       │   ├── file-KrWPH3W2u1bpSwKSXCZHMr-fa4a0a13-60a7-431f-8b8f-0e539307fd801955654441569501622
│       │   ├── file-KsC8qWjtoj5A2iwtrqmvFZ-Screenshot_20250806-185815.YouTube.png
│       │   ├── file-KsgyzCnzUxYz9oYJNETq2n-1000022807.png
│       │   ├── file-KtKVjPtWxiBT7JebXSaRtG-chatgpt-1754559154912.jpg
│       │   ├── file-KUakKAdBMuxN1n1tDojZub-1ec8e533-8aa2-45a5-b419-0d7cf657b6273948571051757009294
│       │   ├── file-KUCBMUzHPCUgBjNtTLxxDU-chatgpt-1754581118951.jpg
│       │   ├── file-KW55Yoi3r2vB1DspQLK5SJ-chatgpt-1754092907101.jpg
│       │   ├── file-KWXWKB7FsiJ5u4Urtt6sEN-chatgpt-1753812515431.jpg
│       │   ├── file-KXY1WgQxCtxDySEfte6BWP-1000023706.png
│       │   ├── file-L5Mgy7JAYToGLPkk6xW1e7-1000007479.png
│       │   ├── file-L5oUkMKL3XGY12QkQKtqhz-chatgpt-1753889127733.jpg
│       │   ├── file-L6uH6E77W68ZZDnEYfA497-chatgpt-1754517035290.jpg
│       │   ├── file-LaBNuhsCjp9HxBbM4dAgFV-chatgpt-1754133354849.jpg
│       │   ├── file-LAKyAAZU6Wu7TNHESsCkNt-1000007434.png
│       │   ├── file-LBKde4ySXCV3sX8ntGCdpY-321bd703-643f-4104-97e3-4a2250021dc094015081102799860
│       │   ├── file-Lcy1WdYuvykCzZNcPXQVay-chatgpt-1753816486602.jpg
│       │   ├── file-Lf2ffiPuiNgg4M7YRbpvQV-1000022788.jpg
│       │   ├── file-LFv4XUzchRdcyC3rVh9fXH-chatgpt-1754484646524.jpg
│       │   ├── file-LGfkrrta136ZPLXsyKsH81-1000007205.jpg
│       │   ├── file-LHAoim2VJ3xXcvrDKkvdf8-chatgpt-1754570487070.jpg
│       │   ├── file-LiR9kBCECgUhaTPnnqgwPU-e9b148e0-8011-4636-9430-df82c817d42d554785288969215337
│       │   ├── file-Lj3W6tW7hVBuHLjswC2YK3-chatgpt-1753816946885.jpg
│       │   ├── file-LJcXokQSsYmvhcFZp72n21-chatgpt-1754051140220.jpg
│       │   ├── file-LJwq6pG2wgSWwNLgHNheSC-1000022803.jpg
│       │   ├── file-LnwChi9skGSw8HtdUCJcbr-85866985-7296-4418-9d1e-b328c9cdc1967871239550463571553
│       │   ├── file-LSxZfNspNpzFAMsb3H28d1-chatgpt-1754575405180.jpg
│       │   ├── file-LTKNXHnn2J6BUYpH4xzvur-1000007162.jpg
│       │   ├── file-LtseowFoo63U7mELaPGQdH-5851b10b-3b04-45ac-90cd-473eeac10dfd4870719899018737261
│       │   ├── file-LUbMWqWxKhRPbwkB4FdJxW-chatgpt-1753846549009.jpg
│       │   ├── file-LwBzaqgmMc9RSMWhfsjtSM-1000007129.png
│       │   ├── file-LYV2W9zvNXwAs5KBjw1mVD-chatgpt-1754051985221.jpg
│       │   ├── file-M2jRgNcxb2QykYxqwtuR6N-chatgpt-1754069897599.jpg
│       │   ├── file-M4BduDJQAshNA7d6A6e4oD-chatgpt-1753822688703.jpg
│       │   ├── file-M4ThFvAjZC2SGorKitoqpV-ac4d71c4-b365-412f-8ee4-2add14548a147888909995622741024
│       │   ├── file-M77BYdLfdb4oNUChmUwDfg-415ae98f-441f-4cfc-9ec4-80291a9332b17923612232304858315
│       │   ├── file-M8eXqVuEd4FAzsPRL9Rssm-1000022801.jpg
│       │   ├── file-M9gD7LbT3J5hcTQthgJysK-chatgpt-1753838819764.jpg
│       │   ├── file-MATFUfH5dFyVr6T5h23opR-40dc9db9-b023-4c20-b0da-a20272525d4c5685306670525155267
│       │   ├── file-MDAGH4MLA9w6X3QyabFoPr-1000000055.png
│       │   ├── file-MdLBAWHoyxGVzzZkiMMGMY-1000022797.png
│       │   ├── file-ME7QwkSbqQVHBQm8f1bib7-chatgpt-1754051719807.jpg
│       │   ├── file-MeHqNi2BNA2snsyXAVJYe8-1000000024.png
│       │   ├── file-MeRjvfbavUWf9fu9si1LUR-tenor_gif1431233369534507979.gif
│       │   ├── file-MeZt1SceRxq9k8RdFFCQjf-eba91b47-617f-43f8-b684-01501bce539d5381929524094768535
│       │   ├── file-MHVi1dUhZGXrUfh3hS2oTV-chatgpt-1753996052750.jpg
│       │   ├── file-MieEY5zQAGCZqNBQKJu49f-chatgpt-1753842920960.jpg
│       │   ├── file-MktJp2pieXXgykWANFXMYL-47f6a130-484f-4179-9b06-e1dc967041ed4278363599630958618
│       │   ├── file-MLSrbbSLjjLqZf1H2ooUJj-472fb612-5c53-41dd-981f-a44755c1258a3556891728375634372
│       │   ├── file-MMR2BETi548L3HEUu9u7UH-chatgpt-1754472580132.jpg
│       │   ├── file-Mmtr4ezbjQoSLQtw71VXhP-0d1c6411-13b0-4807-b23d-e6fde7c74a947150316166874505532
│       │   ├── file-Mobs3Qap2oh8A2NHAwSkbH-chatgpt-1754562254014.jpg
│       │   ├── file-MPwSgKo1fPsbQoL9mp3pdk-1000007167.jpg
│       │   ├── file-MrrRz3ryghwpK9vs8TqXsK-1000007508.jpg
│       │   ├── file-Mru6Te6K3bgoqptxDK6SeT-Screenshot_20250802-174230.Airbnb.png
│       │   ├── file-Msff2Vzeei6kJDSxPgie63-1000007535.png
│       │   ├── file-Mt5L9ybEo3G5rDWCQwp6dR-Screenshot_20250726-115114.Gmail.png
│       │   ├── file-MTC8TPcbDdjwKm85NLGUde-1000007114.jpg
│       │   ├── file-MvdqVZTvMC1nEb6ZTY7Ms8-864a9ad0-516f-47dd-b6c8-f8fd017ec62d7262846274723466246
│       │   ├── file-MvKrfYPVsaSbedPWSrh86P-chatgpt-1753825355287.jpg
│       │   ├── file-MvMVEELE7vBTZV6UZ3i684-chatgpt-1753808461139.jpg
│       │   ├── file-MvnB4RLhy66ELheysspGMx-1dfc010c-b281-4a4b-9ea4-b5b4841414bf6459252795362130893
│       │   ├── file-MWqUiCAR4fy5RBnNV8YaPn-chatgpt-1753823172767.jpg
│       │   ├── file-MxwuF5me3k1Ekwm4ptp8FS-a9d0dcba-930d-4c25-8911-5caf715de1b47161896977866842513
│       │   ├── file-MxY5Nmd4o62sUoTfWuVKGJ-chatgpt-1753977002682.jpg
│       │   ├── file-MYFxDTD8y1PmJShHLN75CZ-chatgpt-1754002165183.jpg
│       │   ├── file-MYVtkUBtGEKnrsfcKk3SS8-chatgpt-1754584312785.jpg
│       │   ├── file-MzBqKDvnEdPqQDx2aaV95f-e80db4e8-ed73-47c0-8784-52d00d0c46564529786299136197310
│       │   ├── file-MZJG4jmSLVvHq49ynswvVL-1000007445.jpg
│       │   ├── file-N1hxmRhJd38zh6Abitn79X-chatgpt-1753922185507.jpg
│       │   ├── file-N1qLWgpuKRV1ZvczYtMygj-chatgpt-1753847001539.jpg
│       │   ├── file-N2PzrxFdYCWkECNaKhujKH-chatgpt-1753847191010.jpg
│       │   ├── file-N3ygaB1r8J4Y6PGb1qg2JZ-1000007495.png
│       │   ├── file-N46bkCLWFdiixCsFhrDgDv-chatgpt-1754577702522.jpg
│       │   ├── file-N62RsmEK2g4hH1NpRGTmAz-757f25e8-3faa-4900-86ff-79766828b4dc7998118580821794617
│       │   ├── file-N6y6U7utL24DbqtGHkpZDW-chatgpt-1754571311559.jpg
│       │   ├── file-N92aZBjzznwYtWaLHT6ogY-chatgpt-1754582136760.jpg
│       │   ├── file-N9hXnxPiCLQnpBhU5Xm4EV-1000022789.png
│       │   ├── file-N9XVpUh8gt7dXk4FaSb6pR-0f7fac0e-1dd7-48f2-aa9f-aaea4f0967544900879423469011419
│       │   ├── file-Na91z4xyotx7RzeM2ceDFN-f6f0f0b8-457b-4c39-ba9c-1ae9ce04c6d15093239229090591888
│       │   ├── file-NaKbNnFw4RXKLuMi2XuGRQ-01f749df-f619-496f-96a6-adda7c59049b223990020799665973
│       │   ├── file-NamtDSnZyjwFoVHg4dc4px-chatgpt-1754589599447.jpg
│       │   ├── file-NBiMkBJnFcdtBrsvfK4JiH-1000007204.png
│       │   ├── file-Nd75NSjfQKS1KUnR5DBtRf-1000007464.png
│       │   ├── file-NenfUeMnGstR7vskHGkcxm-1000007380.png
│       │   ├── file-NFu5RhePzow5mWjVTxGF7D-chatgpt-1754575481656.jpg
│       │   ├── file-Ni66V8uKVUqcVsapsvqwUB-1000003051.webp
│       │   ├── file-Nk2ouA46DDu8DzRrP2NJBa-chatgpt-1754431231637.jpg
│       │   ├── file-Nkgdr1eDGpLUVVdCfoCqLV-45da237f-8b70-4f87-8b27-1b9fddee88a279038908079507333
│       │   ├── file-NNvV9tkHJkPTNpSRAsxeFG-576526eb-5f4c-44b7-aa25-3258d61877e55884168465967218022
│       │   ├── file-NorjwS6zMVWzv28fZ7DyLW-1bbb4fa1-43dd-415e-a0d1-af8db5bd82fd9131551698586736006
│       │   ├── file-NrVA36915gGYFEv611KxX1-303b6dc9-4f9d-42f0-b132-ef151a12e38b2049624974907977316
│       │   ├── file-NTFJcBavBiFhyQZ1MvwMzS-chatgpt-1754558211517.jpg
│       │   ├── file-NuW1aKfkiJM2FwcFX7qFu7-chatgpt-1754559199789.jpg
│       │   ├── file-Nv2Jhgw4HFgcpm75Sm9TsC-b748fe16-7fbe-47cd-a2ee-f5252b4c0cef1134843596367447654
│       │   ├── file-NWmgpqksQJTUxKkC5CDZjW-chatgpt-1753829294211.jpg
│       │   ├── file-Nx3GWGFCT2jQu7vQqdEshc-Screenshot_20250723-072906.Facebook.png
│       │   ├── file-NX3pXgR75sYTFDYCrXHYpT-1000007358.png
│       │   ├── file-Nym5PMCUmv1D8jMvNacDKm-chatgpt-1754650543615.jpg
│       │   ├── file-Nyx15VrjgnkxaDBgYdJfGU-1000022820.png
│       │   ├── file-NzZCqcRG4ncxQGfszKriNr-chatgpt-1753804136957.jpg
│       │   ├── file-P2EzY89TorV9AWYJM7aYVQ-chatgpt-1754649538393.jpg
│       │   ├── file-P3hkrcUr9v2WCMq3XsyqH3-chatgpt-1754557167474.jpg
│       │   ├── file-P4jxyEubPFadcTk5K4d5so-1000003139.webp
│       │   ├── file-P6p17dTcg9A8drRe2j9wfs-1000007237.png
│       │   ├── file-P7CpuahNCquxAzYexDzcNV-chatgpt-1753823713134.jpg
│       │   ├── file-P7Py7CtVfkcwLdCXUFWeSX-chatgpt-1754489639786.jpg
│       │   ├── file-P9Y2VrQR8vHUUFaAefpt2n-chatgpt-1754581636850.jpg
│       │   ├── file-PASmESDJLsf2yGxdGmvnjL-chatgpt-1753976522360.jpg
│       │   ├── file-PDhL6HwZtLbbm8cyxJ9t7M-chatgpt-1753877748461.jpg
│       │   ├── file-PE1n6esXSnf71gm3WM8kaY-e85b35de-1616-411b-86fc-b922604925df6100753233312141406
│       │   ├── file-PeceMLg66TNXup5JqQXqmA-chatgpt-1753841937079.jpg
│       │   ├── file-PfGPEi1yW1BSpwzwJBunFd-chatgpt-1754067944195.jpg
│       │   ├── file-PgAsZkj7LLUVGG9LqmaE3h-chatgpt-1754650136236.jpg
│       │   ├── file-PgKjvKrL7WC1XwwDVgqSyk-f865c908-4c36-476c-b9d2-89955fcbb01c1903461017571449911
│       │   ├── file-PGNubqT5daY6ptNYP9H6Kk-736ca544-dc38-4e2a-b1a2-22b0454cce7e1442423718266437972
│       │   ├── file-PkwuBy4inDussRNasLorju-76269742-6827-4988-b77d-0f2c7ed853574480353645400315468
│       │   ├── file-PMYtvWo38AAVCHw7DMJnbZ-chatgpt-1754127785039.jpg
│       │   ├── file-PPcEHKdcjWGqxTKdhkHFja-1000007487.jpg
│       │   ├── file-PPRFWMca8ZtgFdTqNtusYY-1000007392.png
│       │   ├── file-PpwNG8m4aFgfbrShap4TRH-chatgpt-1753853353618.jpg
│       │   ├── file-Pq1g6w7aRWL5HXvN1ri4tM-chatgpt-1753819192316.jpg
│       │   ├── file-PrXF1JYfSuCM6jtP1XPEx9-chatgpt-1754554174934.jpg
│       │   ├── file-PS2zxXn84AAieEPhmkA2qq-1000022795.png
│       │   ├── file-Ps7ay1q14RD2gG4Stc5aYq-chatgpt-1753828871045.jpg
│       │   ├── file-PsD9Hn99WU8PiBdmGhtpJf-chatgpt-1753922356508.jpg
│       │   ├── file-PtcDLNXHYSHuXu5vpBfsic-Screenshot_20250802-120200.Gmail.png
│       │   ├── file-PTD6JSC1djpcv6iw68FF1o-1000007467.png
│       │   ├── file-PuGDAGBbtx1XVyyzSJymw4-chatgpt-1753815833440.jpg
│       │   ├── file-PuSb8XXnoZ5Rq9RF8qDPTs-1000007383.png
│       │   ├── file-PVWJS7qZZc2uH7itKSaxNU-chatgpt-1754133505772.jpg
│       │   ├── file-Pw6xJEeyYbuw9xRAL4AHtq-1000007476.png
│       │   ├── file-PZ7dqMM9QR5EHrP9w1RCR9-Screenshot_20250724-195048.YouTube.png
│       │   ├── file-PzQja2KAuVQ2YFWBD39FKo-chatgpt-1753807582073.jpg
│       │   ├── file-Q4LyeY6UwfwDvXLaGFYr7Y-Screenshot_20250722-122949.ChatGPT.png
│       │   ├── file-Q55FwVTyxZ6ja9HwAvEwEc-395e35c7-fd87-43b0-86d1-a4a2b0c128c51266752065701736260
│       │   ├── file-QaaRLPmmLuDDfg4GEDD3rn-chatgpt-1754067966369.jpg
│       │   ├── file-QbPE6UxDx46PrCDmPxXtos-1000022787.jpg
│       │   ├── file-QDqHFf8h1gfjXS4kPmN6BS-cd38c41e-64ca-41ca-b29d-a1c2946a06488589723447196789301
│       │   ├── file-QEtR2CTXmxUVXcGe9CVJjV-1000023388.png
│       │   ├── file-QHKoJsM5PqHXE4BN5j4fWT-chatgpt-1753825923843.jpg
│       │   ├── file-QK2aHPSMynzTmx2vJ85Kib-chatgpt-1753839842382.jpg
│       │   ├── file-QLRU3onEQg2ZsrUga4oJhg-933c81f2-b011-4494-ab54-5e37bc60156b.png
│       │   ├── file-QMCQSEQboPDz3fTjdMURYw-1000007256.png
│       │   ├── file-QMWbsaDt6gzmZh5SLvkYAy-chatgpt-1754065155965.jpg
│       │   ├── file-QnXRWn2KE9inRZcUhSL6zu-chatgpt-1754064154252.jpg
│       │   ├── file-QoPAvSL6jgwGmN4LjjTj3f-1000023453.png
│       │   ├── file-Qr89xeJnfFL9Cv3hzfk3qL-1000006544.jpg
│       │   ├── file-QSVr2Cii2d2xT3dJfafApL-1000007153.jpg
│       │   ├── file-QtBL4xStFTVknfzrPuZc4U-3e5ca5a0-27d4-4740-acf2-2514f66ea16f7850809450887565799
│       │   ├── file-QtDm3h4uQpc4VxxjsqAQK3-Screenshot_20250730-085940.Chrome.png
│       │   ├── file-QtG68bL7t7SXLqq5nBMLLR-chatgpt-1753822383168.jpg
│       │   ├── file-QuFxTJxAHKck4j6g5SRibV-chatgpt-1754564203762.jpg
│       │   ├── file-QVwvw2ynJox9vkkRE444o6-chatgpt-1753848060127.jpg
│       │   ├── file-QwEiwC2rsgRBexsfEYqVyF-1000007359.png
│       │   ├── file-QwQsGMunSxemJfV5pL6Yds-668b482d-22ba-48de-abac-b73415416793801595179292122210
│       │   ├── file-QxBD98TJa8MWE5SrW3yD2Y-chatgpt-1754582916002.jpg
│       │   ├── file-QxQZ3YGX5zHmq5yxkWD2St-chatgpt-1754133205014.jpg
│       │   ├── file-QyEMfJ3Fgv7SdWpG9A4Wze-chatgpt-1753825402651.jpg
│       │   ├── file-QzaagN4VnsLzaZKwcFKb4J-chatgpt-1753847846329.jpg
│       │   ├── file-QzJEWyqp3QX6tss8cNrYQT-chatgpt-1754642308059.jpg
│       │   ├── file-R1cZR6KtG3VqjytpZvUXr8-1000007382.png
│       │   ├── file-R3zv2Ze9stcK7uKh6Qv3Bd-chatgpt-1753877884817.jpg
│       │   ├── file-R5XmhhB8FBTP4a7HnusSaM-chatgpt-1753919378168.jpg
│       │   ├── file-R9gpfSxAZAfs7WiMdm3L2F-chatgpt-1754513935706.jpg
│       │   ├── file-RbautgUNR3sYsXacAy6pSj-fc9d235b-c94d-461c-84c5-65f81beb723e3958547762696955680
│       │   ├── file-RboBoALRxZqUpnEobHPUFP-3038eda1-546b-4e9d-afd5-e73009c5b7a12488681331168683648
│       │   ├── file-RcAbkbpm6jhTYTsgpvu246-chatgpt-1753803999670.jpg
│       │   ├── file-RCnnHQNZxFGCpzrgaXWeYe-65cea484-bfb9-411f-a109-0647e4dec60b2225842722100959185
│       │   ├── file-RFgq1GeCh99mVYh1iiQKwv-chatgpt-1754134651491.jpg
│       │   ├── file-RFPNjWc7NUqmCkd6EhwFNW-chatgpt-1753841675585.jpg
│       │   ├── file-RhoaNg19S9cDhXcncYuZYv-chatgpt-1754133585499.jpg
│       │   ├── file-RHwWBLQdQLp5wNt6VCZTh2-1000007257.png
│       │   ├── file-RiVzmFAzeKsfKzNUBy6ttt-1000022944.png
│       │   ├── file-RkEubpRVz6jtFqy1VCBuYQ-chatgpt-1753840520411.jpg
│       │   ├── file-RnfFwKc3thxuz4ct3NX2JT-82549101-3ef6-4ed3-a396-34835955bf9b6715217896679623119
│       │   ├── file-Rp2zKVwQ7SNpasuczcbQVL-chatgpt-1753816254689.jpg
│       │   ├── file-RSJBqkj6epcFFmU8BJRsd9-chatgpt-1754431606489.jpg
│       │   ├── file-RSZTuKMH7piuTYCFU4H4HG-chatgpt-1754642002914.jpg
│       │   ├── file-RuZoLcPyA1t8neKamgSyGo-chatgpt-1754650316254.jpg
│       │   ├── file-RvPhY1nCb3faE3FaxjYHui-1000022875.jpg
│       │   ├── file-RvyqYFtwJKaNML6S5pnwd7-chatgpt-1754069574090.jpg
│       │   ├── file-RWcfEwKSDEiAF8wtkboEgW-1000007454.png
│       │   ├── file-RWiJFtg7wLhEmaW7LqqjLy-chatgpt-1754558092708.jpg
│       │   ├── file-RWooEsUuZiiMxLwy8gnbGa-chatgpt-1753976313477.jpg
│       │   ├── file-RYqKh3UUw3KCthV7weRVXt-chatgpt-1753983129074.jpg
│       │   ├── file-RZKDVxANj9mZr2FntC2oWF-chatgpt-1754570409454.jpg
│       │   ├── file-S1HQeKaF8cytyuvtiWb6n2-chatgpt-1754581564415.jpg
│       │   ├── file-S6igLUfQDr8rDSEfKaZ6cb-1000007422.png
│       │   ├── file-SAVAD9CsXCjGvos2cX9sQr-1000007174.png
│       │   ├── file-SbzHzf5DxTRv63B6s1sRYq-chatgpt-1754009522774.jpg
│       │   ├── file-Se5TfE1CcnaE1w1WpjdZom-1000007531.png
│       │   ├── file-SFGtbgsw4SgHQrtrgoBvec-a1d96dcf-5892-4fa3-bb2d-6ca3210c54db3798730866949281932
│       │   ├── file-SFnPbXsbDJoB4PEsDY4AJP-1000007364.png
│       │   ├── file-Sfs3Bk8mQRhdNhSsiEJDEo-1000007524.jpg
│       │   ├── file-SgKCcByudDo2nHXBCUSQPY-chatgpt-1753910973204.jpg
│       │   ├── file-SHVhM8GviNprFhRQWNYqfR-chatgpt-1753920938041.jpg
│       │   ├── file-SJ9nbDpAKXo9JasNtwa4f3-1000023313.png
│       │   ├── file-SJEpuyCZcSnALVL77CRpsk-IMG_20250714_090900462_HDR.jpg
│       │   ├── file-SJnwKmeJSnge4qu9u9ZXJp-1000007157.jpg
│       │   ├── file-SLVRzvA3J5ciDuixbN1KBm-f0f702e9-f96f-4fa1-a4cd-29e7a39434705519386649951178631
│       │   ├── file-SN2Y5avsCJJTF8AdUoypyk-Screenshot_20250808-081815.Chrome.png
│       │   ├── file-SobUUDxcHgQ8SWcLdchdFt-chatgpt-1754554143284.jpg
│       │   ├── file-SPEk45h6FA9beMFnrXMZW6-chatgpt-1754152276652.jpg
│       │   ├── file-SPrTZbr1qadfmuEE5Ymkpv-b10d3321-ea45-4a3b-a210-d321b11bdacc4622803852134761462
│       │   ├── file-SqAAz4RKog6g8G8fAzZXQJ-1000002618.jpg
│       │   ├── file-SR5rffqdHzY1xbN1WTzpEx-chatgpt-1754047586018.jpg
│       │   ├── file-SsHwysK4TGWrhPU1moLiqc-chatgpt-1753999578202.jpg
│       │   ├── file-SSnZ3BWdneMT4RPQXSUVbG-1000007332.jpg
│       │   ├── file-SsoG1szMXNPCNnbX22EW8X-10218729890203388913.png
│       │   ├── file-SsyXFkXhbHEV751f76uSxz-0f46a23d-e908-44f8-93fb-aa46dc9750207163719869428657290
│       │   ├── file-SSzxd1oqJMDi7H7ezUsedQ-1000000029.png
│       │   ├── file-ST7xvhZxWMpofgUj8qDW9r-chatgpt-1753846725824.jpg
│       │   ├── file-STo2mqeqxtVoLHJ2WSwY6r-05476dc6-a6ac-495b-96ed-bf48e065e2496995345254194229763
│       │   ├── file-SuDqYN6yafxVC26rXDiQko-chatgpt-1754070125463.jpg
│       │   ├── file-SURgqpw1ouQQVfChkqjhcY-1000023515.png
│       │   ├── file-SUvRCiMt6st3FzLRFUF2aG-chatgpt-1754495326954.jpg
│       │   ├── file-SvB6B14tT3eMoUmoSTEZBD-chatgpt-1754578787875.jpg
│       │   ├── file-SvGMeFsYJ16qAho9KtJBRe-chatgpt-1753814888423.jpg
│       │   ├── file-SvrzKfPE2vyg8HJH3rqGHb-Screenshot_20250730-122232.SAP Concur.png
│       │   ├── file-SVtyiA4FVuaUTRkQgCMmot-chatgpt-1754582497508.jpg
│       │   ├── file-SYJfze68VUzNR62BqPmSs3-chatgpt-1753802729817.jpg
│       │   ├── file-T1GA3Qc4KtZbSjMDLs7RvV-1000007254.png
│       │   ├── file-T1JVNB4XsTwHC1nVHAHbAV-1000022846.png
│       │   ├── file-T2QvCgMJ1C2KDhSTo2Dpwj-chatgpt-1754641947818.jpg
│       │   ├── file-T3A9yx2XqZwbdTo2Y3ADa5-chatgpt-1754568432865.jpg
│       │   ├── file-T4yFs7pGjiyqGNiccDuUet-b40c13ba-8939-4008-81af-5bf91c336d217184579663472209290
│       │   ├── file-T5UAtpWaVNgxXhcPEjq84d-chatgpt-1754648846794.jpg
│       │   ├── file-T6WVZxx2ULvkrx2Q9FMaZq-chatgpt-1754513924875.jpg
│       │   ├── file-T8tzBB9QTzN8PodsYxuiKe-chatgpt-1754554756337.jpg
│       │   ├── file-TAnMdimyrC8tCNZWJTvrLB-chatgpt-1754570693158.jpg
│       │   ├── file-TaVSsR3VUUBvWczkjnfEJ6-96db1209-a4f3-4adb-b183-609c85abc9741701414583253159850
│       │   ├── file-TBNMC1chfw7AXPBxLiBEST-1000007161.jpg
│       │   ├── file-TEqZFuUfZ4hVugCWnzWVty-1000007113.png
│       │   ├── file-TETUP91zHTUV2E3qdNKE4S-chatgpt-1753807678363.jpg
│       │   ├── file-TevZ7mE5E6NZhn4fucS4Wn-c062d566-5639-43e2-b7e1-58100434f3a23181245084490631033
│       │   ├── file-Tfgz2zLBe3jCKZLLNHQiGB-b1bd9072-1aeb-403a-b90b-4216da6e58994265086824905926324
│       │   ├── file-TGHdx3sytaz8tpwL5frqAy-chatgpt-1753822950385.jpg
│       │   ├── file-TGobLJMAJrRjZaan5WJBda-1000000035.jpg
│       │   ├── file-THc8NBaD9z7BJCcX2gDGab-tenor_gif2561101875669094501.gif
│       │   ├── file-THLKZCaBFWJRqGjePeKL7L-1000006293.jpg
│       │   ├── file-ThTkRujgfDqCdiR9kfojxF-1000007369.png
│       │   ├── file-ThyDHus5TfE8mSXT3EKNDE-chatgpt-1754069890208.jpg
│       │   ├── file-TJsQcwefXWqiY9dAmY8Dup-chatgpt-1753825870362.jpg
│       │   ├── file-TjXjLNFx19r5n2gs1bZgKH-chatgpt-1754053379489.jpg
│       │   ├── file-TKgyYhoZBFv2MwGKjFFbb5-1000000059.png
│       │   ├── file-TLbA9tZe8ZunZA5aGvchZr-f53a5c2a-0c7c-4041-af76-6652309f5c645991064068888651107
│       │   ├── file-TLsjMTUywA3tpbzu9zJ1CE-chatgpt-1754490391366.jpg
│       │   ├── file-TmBZC2xHzW8AsfKaqA7vLr-1000007130.png
│       │   ├── file-TMEwLGHEFBAt7VkAmriy2W-chatgpt-1754514298892.jpg
│       │   ├── file-TmWMjTfsiCKHNnJcoq3SDh-Screenshot_20250710-173631.1Weather.png
│       │   ├── file-TP19fFk5CtwRSGRZ5G7j9R-chatgpt-1754557096860.jpg
│       │   ├── file-TpCKyTXm1K3nqwqyp4zcpU-chatgpt-1753827203787.jpg
│       │   ├── file-TqEZqZqbYqE4ByxKH6SFUG-7ebc5dce-c622-446b-b8e7-d79f04cb32911688474209865460572
│       │   ├── file-Trp2PzThxt5PHjNUTMR1Tb-chatgpt-1754053256202.jpg
│       │   ├── file-TsKRAdCXGySBjMs11wXJWA-Screenshot_20250726-131345.Chrome.png
│       │   ├── file-TsxLprWYtzz9anWiNvdjw3-chatgpt-1754065358973.jpg
│       │   ├── file-TtgYsaa8taGzCeqixhLura-chatgpt-1754578857550.jpg
│       │   ├── file-TTZkrsh3u6DZjc9Vkvsvoa-chatgpt-1753832226708.jpg
│       │   ├── file-TuMJos7HeKi4dZqsQRtdK9-chatgpt-1754591424093.jpg
│       │   ├── file-TuMU28j7mmuaHbnVbvLeyf-Screenshot_20250808-081815.Chrome.png
│       │   ├── file-TwtCaRjM9haUzTQSrhFDFr-1000007251.png
│       │   ├── file-TYhB3bSY4Ca9FEs864y5kk-chatgpt-1753822194863.jpg
│       │   ├── file-TYjHCV53aY613D677set6L-1000022796.png
│       │   ├── file-TyoZaPqqmufaHhZuPjoRr9-a3290fa2-77d5-4c0a-ae80-7f09742795aa7529429614722541879
│       │   ├── file-TyqjSfpTvHvSacWqN4rKSt-tenor_gif422329942315180387.gif
│       │   ├── file-TYzaUCi2ZpLAAeGe9PZsjz-chatgpt-1754051566464.jpg
│       │   ├── file-TzpHHZyaLJPzA5P7w4mE2W-1000007184.png
│       │   ├── file-TZVMw7dVoKUf2ZsjE8n6WE-chatgpt-1753889825512.jpg
│       │   ├── file-U1C6AHgbAfJG5Ud6HsnHYW-chatgpt-1754578215423.jpg
│       │   ├── file-U1SNJJaeaj7F28F23fAyVb-chatgpt-1754568535433.jpg
│       │   ├── file-U5vs5FCcVkkFwVDGTixMiE-chatgpt-1754127882747.jpg
│       │   ├── file-U7aquFhS41iisZWJZLvoGD-file_000000001d7c61f888679f83013ea7dc (1).png
│       │   ├── file-U8MxJwCH5cTBsxxDriZ7pC-chatgpt-1754059867428.jpg
│       │   ├── file-UACXcUbDG9B69ju7nLed6c-chatgpt-1754554197051.jpg
│       │   ├── file-Uaxg4tDUHT8PNQggXTdVNw-chatgpt-1753826190700.jpg
│       │   ├── file-UbBDhtXLdwkNrvddhWaycA-chatgpt-1753846405813.jpg
│       │   ├── file-UbptKA3g3pCAngvWJ4gT7c-chatgpt-1753825262177.jpg
│       │   ├── file-UDE58jQFF8UWpFSCEBVTq5-chatgpt-1754324310053.jpg
│       │   ├── file-Ude7txapKythm54ZYqMkmr-chatgpt-1753835369839.jpg
│       │   ├── file-UeuDykss63sCP2NJtRE4zo-chatgpt-1754067975113.jpg
│       │   ├── file-UfnRj8fS7MzZYNkDA7WvUr-1000022795.png
│       │   ├── file-UFUzFzi3c3MjXdqEaByQkA-ce29e497-7894-43d9-9473-677b399298cd6172473153540719040
│       │   ├── file-UGqCSRPpoiUdZGLdZNPpj6-chatgpt-1754478580362.jpg
│       │   ├── file-UGy2dcu1noNPq528A9wL85-Screenshot_20250727-192609.Gmail.png
│       │   ├── file-UHAnwbkPXn9RTunen5vth7-1000000057.jpg
│       │   ├── file-UhbdjZSCEFuzv3NpUqWrC7-chatgpt-1754582028947.jpg
│       │   ├── file-UMaPNVeamXFNVyupKh8Tp3-1000007168.jpg
│       │   ├── file-UoftJL8U7oN6Cqnuq4fZho-1000006506.jpg
│       │   ├── file-Up9eyH1GbQ9fXza8eET2ja-chatgpt-1754577220440.jpg
│       │   ├── file-UPxuT63MNtwmTbGowKv3UP-1000022802.jpg
│       │   ├── file-UQLHfGRo8PayL6RrniJuhF-10218729890203388913.png
│       │   ├── file-UQn2L5VbE5S7ifs4JyECaR-675cec4e-62bd-4674-8d3d-e342e1aeb1085356075724330865962
│       │   ├── file-UqYjBEVeJngUrq5Si4upHH-chatgpt-1753846780387.jpg
│       │   ├── file-Ur7Kg86eaajkMrod789Af8-cb61e650-c1d5-4e63-9017-c64b632346768644416018728960508
│       │   ├── file-UREUF7Jifmm3hVnLyctcuL-chatgpt-1754133395160.jpg
│       │   ├── file-Uti9RG6BxrD8ViNaNGqmPe-cce56436-a58e-4a3b-9b5b-5bcbf518eef72720434237790366911
│       │   ├── file-UTvJgtGiaCSrz1JkWKrqdX-1000007478.png
│       │   ├── file-UtYibLgVfYdy4fViMDQjYZ-ddfbe385-d343-415d-a293-9a0e549ea3d5421163828341845637
│       │   ├── file-UUjzLd2T5VfHVJbFcLHMqK-chatgpt-1754052064840.jpg
│       │   ├── file-UvGn6kUVAaQidppJc5XDiQ-1000007241.png
│       │   ├── file-UwxXM7uiC6GQUFyfsJhhVP-87404338-b801-4297-a1a5-edc65041a0253098627699316452531
│       │   ├── file-UyykHPK2eNayF9TeWR5YFw-chatgpt-1753813216607.jpg
│       │   ├── file-UyZWmBrSradfpAbeneAQZa-bd9b759c-f0f0-4741-8aeb-05ca43092cc68820314800845112515
│       │   ├── file-UzmC1bnU7xUXsbpJpAEryK-4e2d2efa-4345-404f-be57-73ce4758dc997005798022127523942
│       │   ├── file-UZxpuQ2e7Acpioaj7sW3ov-chatgpt-1754052188019.jpg
│       │   ├── file-V1pccYRpuPvgdmz9cbPvAH-chatgpt-1753826541206.jpg
│       │   ├── file-V3mSCmTS3EsrJuW8HX6J6y-3ed14611-d517-4000-9500-450e6d9c3fe56705668340519050841
│       │   ├── file-V6v2ihbv5hn1usGQsvcZ8h-b09227c5-de83-42ee-a20d-3d35f3223e7b1031263860830164524
│       │   ├── file-V86oZVWeaXHDyL2T56PJkH-chatgpt-1754583065665.jpg
│       │   ├── file-V8J7QD7wpvGQCwTeqbn73H-1000007433.png
│       │   ├── file-VayojRRabbPAyHk55M1jQv-chatgpt-1753998215482.jpg
│       │   ├── file-VbbbWV8zRq9n36qZr7JUG7-chatgpt-1754052034484.jpg
│       │   ├── file-VEJhebB9m2RJBYLSBkTZ2L-1000007169.png
│       │   ├── file-VEomuhcfyvYwy8bMUvJ57j-chatgpt-1754582071200.jpg
│       │   ├── file-VFJartEN6Wd2vyPrWeeuzd-3231d82f-0945-4673-924f-d24214a57db52499801982284841128
│       │   ├── file-VHH18V6cfYz2Zu9r6JhJwk-e6f79cf9-92a3-45f1-bc0c-1a10cec51e018427695052938031397
│       │   ├── file-VHs4xsXhjCgDXeUvcLjEpP-c670f28c-97dd-42ae-8a7c-067f4fdfaf9d2880498494169708321
│       │   ├── file-ViebMiRzCGkxM2hHSFDJSH-1000007248.png
│       │   ├── file-VKR6w7VVFJcGZEQACgVczy-chatgpt-1754576031876.jpg
│       │   ├── file-Vn3HuFTy1kEyst9bmsVgkL-chatgpt-1754518157487.jpg
│       │   ├── file-VPpbNdbUNz86KTm5g9qD1t-c8cf3447-7bfd-44b1-afe8-13c7e17525d38894399132280772191
│       │   ├── file-VQ4k2Wz2Y97Mr7UnLxsjPw-000c68a1-f18f-47b5-9d1d-a8cdb925a7652097306997703113807
│       │   ├── file-VTbHimTudyRS8VK3c536ah-920ca9b7-66aa-412b-8f8c-86e6b5508f457465847749852861008
│       │   ├── file-VTfnqm4LraBatRih6JcBHt-6b9e7721-d300-4151-b649-37883343045a4084951301162481314
│       │   ├── file-VtyiRLnRxFUjCBYiE8x1AX-51c9b67c-d5e3-48b5-9777-271613b1353c8954361201468193102
│       │   ├── file-VUTR5UFwZHCAuaVrmHu9X2-chatgpt-1753817963439.jpg
│       │   ├── file-VWE1RFSY5bJFv2dy7ZKJ4L-chatgpt-1753982919109.jpg
│       │   ├── file-VX5QRsmUjMVmg56p7jkkgv-chatgpt-1754583111036.jpg
│       │   ├── file-Vx5rkbn9MojXeTWCbrRPy1-1000007148.jpg
│       │   ├── file-VxJzxvtd7GZso57paggLAF-chatgpt-1754045910870.jpg
│       │   ├── file-VxPjorz69s8qwzKpjkPQYL-1000007514.jpg
│       │   ├── file-VY23rj74tMcUmxZNbuRP4j-chatgpt-1753848759877.jpg
│       │   ├── file-VYfY6sMBoMS5dGNYfKwr23-1ee5377f-fe08-45e5-b5c5-bac7690686504345045093069851381
│       │   ├── file-VyJjYa9GkFytMryR8REkE5-chatgpt-1754519141169.jpg
│       │   ├── file-VYPZfHw4PEtUbx2qqhi8Pn-chatgpt-1754000862899.jpg
│       │   ├── file-W4skcPSzLyshW1XCQPauHE-62619142-06d4-44b2-b775-6d2468e6182c366466019652348752
│       │   ├── file-W7eGB1nKz1Rn5fKzDwW4Fd-chatgpt-1754584698677.jpg
│       │   ├── file-W7giWKaHwJnvK5EZRsKnVF-chatgpt-1754561399114.jpg
│       │   ├── file-W7X5cE3wzr6NaSkWx9sSNo-1000023406.png
│       │   ├── file-W86xxUmAQE6bw9UhsSpgFs-chatgpt-1753841714080.jpg
│       │   ├── file-W8Lfkt4ZAzTxByFPunoNU5-chatgpt-1754133454865.jpg
│       │   ├── file-WBcjWnin6ZDtxQvPSTLdDA-chatgpt-1753827912881.jpg
│       │   ├── file-WC1kikTcw4fCE7ZJAzfypQ-chatgpt-1753920011265.jpg
│       │   ├── file-Wd886uWQA6gTeMihd9YEyz-aaf56395-24ca-42d3-98e6-d74e0d2793d33686213081421728933
│       │   ├── file-WdZRZWAUunL8pNAZjN22Qo-chatgpt-1753819205078.jpg
│       │   ├── file-WfiQFTuDFAAGKLofWT7WvJ-chatgpt-1753828130839.jpg
│       │   ├── file-WgnYDathd5BF8DRFnYVeWD-chatgpt-1753846922960.jpg
│       │   ├── file-WH4A7UZ6fShL13DFMQRazm-chatgpt-1753822299279.jpg
│       │   ├── file-WjZLzx4uVpQmYq5AN31HbR-aba518ef-518c-44b0-a1cb-580435e623ba894746585686677116
│       │   ├── file-Wm1nKmM74SAksKaRqFxNMF-efeb1062-1aad-4f55-9120-25e976e8142b746793360879143708
│       │   ├── file-WmqPAcFnWKfhJLYuUm3Lc1-chatgpt-1753810338283.jpg
│       │   ├── file-WNAfRS1bcwjw7rHaNJwMz3-chatgpt-1754559111738.jpg
│       │   ├── file-WRdNgWGJvhEkXd9KK9KDae-chatgpt-1754057955300.jpg
│       │   ├── file-WrfryDvftRE7M7Xou48YEv-1000007550.jpg
│       │   ├── file-WrNg1QGEbjNwvsKBjmnaVS-IMG_20250716_210812056.jpg
│       │   ├── file-WVojCH2xDL1XrA7GbswdHM-1000023379.png
│       │   ├── file-WvVjXvzt5oocGAsjd5tet5-chatgpt-1754069881172.jpg
│       │   ├── file-WvxBtUeaF4nUurNA8V3L7R-ce21579c-525e-47e9-b882-4a09216a48e24393531052555010611
│       │   ├── file-Wx2NhuHaYCFB56BMoQz4P1-chatgpt-1754485718850.jpg
│       │   ├── file-Wx3Jatg7j2YWpG4bF3PJx7-chatgpt-1754046037980.jpg
│       │   ├── file-WxAE5DACTWYgh3ayhtgo67-chatgpt-1754487935669.jpg
│       │   ├── file-WxPBz5Ut9zKPzqE46H22cn-chatgpt-1754166985689.jpg
│       │   ├── file-WyjFfb3LZLSCSvADYM4My8-chatgpt-1754518495126.jpg
│       │   ├── file-Wyu4Qc5Draum7rdC9KxvxT-chatgpt-1753825759381.jpg
│       │   ├── file-WYv2xVbiaNunPdjTw775k3-d72f915e-6dc9-4511-9171-6cafd7646346~1.jpg
│       │   ├── file-WZG7VUxXiW9rAqYy7guMvg-chatgpt-1754513912142.jpg
│       │   ├── file-X4cem9pZE7mesBAXeDo3gM-chatgpt-1754577020554.jpg
│       │   ├── file-X6nKMHWwQRgdvSS3NvGuZy-chatgpt-1754567271666.jpg
│       │   ├── file-X7vAouVjk6pY4j2RC5QX7j-6290e748-7f9a-4428-8391-2d6030d7170c6832490701147852674
│       │   ├── file-XaKRKeWiouMJzTF9EFFM4h-1000003121.webp
│       │   ├── file-XApDmKk32DA19EipEdp9dA-78cfffad-438e-4e31-a600-a756906873db1074528051827213477
│       │   ├── file-Xb1N3gUhW1Gkhw36ErkHx7-1000007456.jpg
│       │   ├── file-XbGZLqgi8mYPJirAZPmUnS-chatgpt-1754470445522.jpg
│       │   ├── file-XBsiqxGA1NuwYqtaEumoUG-chatgpt-1753853797057.jpg
│       │   ├── file-XdDw41U3sywdMXyTuqaQnX-chatgpt-1754003760408.jpg
│       │   ├── file-XEgni4HYxyNoPF7an8LJtC-chatgpt-1754517458627.jpg
│       │   ├── file-XfBPZs966YSQSmZMHmrQhm-1000022819.jpg
│       │   ├── file-XfysdmwJjRUQxae15utpHx-5c5f3f5d-3cec-4781-bd77-069560a542d37408756986762884876
│       │   ├── file-XGC9uVF3c3UcbQm1V3Gp3N-cfba7c67-0c54-4a34-89a2-42132b31f601345677132837789039
│       │   ├── file-Xh74vsMiPJwuCKMT9tiKKZ-b07c0097-bbb1-4cec-af58-834356778b734138562592330462273
│       │   ├── file-XiqFzrjp9pmXoYThRj9UgW-57749d3d-75ce-4d47-9aa8-e54d60e435aa3573140083122056379
│       │   ├── file-XJgozW3dx5iyUAz6rNGpWQ-chatgpt-1753922026591.jpg
│       │   ├── file-Xk5GEnZcMAyCusgw7UE8Y9-1000023714.png
│       │   ├── file-XL2PupuCxt7rpKVszFmrAS-caa0dbea-0534-440a-95aa-cd6d004c34588190916370279915127
│       │   ├── file-XLjabGpCAY5D6JZSi3iNoe-1000007358.png
│       │   ├── file-XMEdV8AFMoTEEFqpcnmV54-chatgpt-1754576687271.jpg
│       │   ├── file-XnCAozFyRWNeFranHwAune-chatgpt-1754578812416.jpg
│       │   ├── file-Xndb6hr6rdSRA2W6v7KYU9-chatgpt-1754649725147.jpg
│       │   ├── file-XNqy2mDJqZo1eEsogv3pLh-chatgpt-1753823361156.jpg
│       │   ├── file-XnxpjTpTXuEzbCpks6RYcK-1000007150.jpg
│       │   ├── file-XoG3v8NfYQJG6V4HfpDQJQ-1000022780.jpg
│       │   ├── file-XooktrTsF4VP9csaKuwAvk-1000007331.png
│       │   ├── file-XpCknzpVZNzRZwLX1EV985-chatgpt-1754518502683.jpg
│       │   ├── file-XPminjmy1ihQrJWZ29daKd-052d3572-1638-4a1d-b13f-3f69f6bfcd5b2685162070299642827
│       │   ├── file-XrqJepntgDeCZF84vHhJmr-0f8fd0c9-a383-4c0c-8b8b-68cac9617fad7373514417385961257
│       │   ├── file-XSkgiuaeFY1GERozBH6sp5-1000007215.jpg
│       │   ├── file-XSyyMKakUxTPQQ296zqFTd-1000006309.png
│       │   ├── file-Xt3xmwUXS9q8TXjvnoh43f-1000007551.jpg
│       │   ├── file-XTBtMn8rsQebEg5h2fBVTi-b10238a6-b3dd-4829-b88b-53f0b9bd83911757479903487122961
│       │   ├── file-XtDkycoM3RpHpmDe9HAuxL-chatgpt-1754576883138.jpg
│       │   ├── file-XTKaqXBQCdN517D2voU8Qd-chatgpt-1753838433708.jpg
│       │   ├── file-XUfaQZgTFQWWf5wVXZQSDH-chatgpt-1754430563255.jpg
│       │   ├── file-XuXz6tsgGvz1wY69QisJeo-1000023259.png
│       │   ├── file-Xw35cTUbv41n8yRLK9Toq9-184e6e3e-73a5-4e50-a0cf-cc651fa71c758248448438912760690
│       │   ├── file-XwmsDee9wFkkCeSoGhtsER-1000023463.jpg
│       │   ├── file-XyX9cuVyh4obygX7DFpJy7-1000007552.jpg
│       │   ├── file-Y5d17GEyG5bzrkFTUgTYSc-chatgpt-1754642056030.jpg
│       │   ├── file-Y8a6FRHhYnJtK4i3tDXHBc-0f78ca42-70b4-44aa-9a5c-09c582512e458947497869997689643
│       │   ├── file-YaL8k4rCDbdFKmTJq7zWaK-chatgpt-1754502677261.jpg
│       │   ├── file-YaNgtzYqSMS5G7oGTmPiy7-1000007250.png
│       │   ├── file-YbfNo4tB8GpxBZwd7BTFgA-chatgpt-1754649753554.jpg
│       │   ├── file-YCBV6FkvewM51CvFjrvRqL-chatgpt-1753817118398.jpg
│       │   ├── file-YD4Yi6E5gxvzEQNjP6ynH4-chatgpt-1753819990565.jpg
│       │   ├── file-YG83oZeSo1YCdhJEA61fJZ-chatgpt-1754052127765.jpg
│       │   ├── file-YQVPdMLizRvr619iMD2QYA-edc3fad8-5a23-4d23-9e38-0138b3fcd6958183356555266740899
│       │   ├── file-YRH8Jo7V6AN93hRmwkBpAS-chatgpt-1754430852359.jpg
│       │   ├── file-YRk5ebhVACa8DJxTKTaqE3-chatgpt-1754229135678.jpg
│       │   ├── file-YUSVChRPLwUwYniCz6NJAJ-Screenshot_20250726-172448.Gmail.png
│       │   ├── file-YXEpo5khjm6Uc5mBckvgxX-chatgpt-1754470159302.jpg
│       │   ├── message_feedback.json
│       │   ├── shared_conversations.json
│       │   ├── user-bakz4WGuU2J4ehAdey4WZW9H
│       │   │   ├── file_000000000ee862308bd2bfab5d6c9269-3756b4c1-893b-4157-90b8-bce8590b8a07.png
│       │   │   ├── file_000000001338622fa8fdf0cd36f2600a-a66779c8-0501-4c51-9af7-220fb6816291.png
│       │   │   ├── file_000000001a6c622f9f477e7404d6762d-c91515f3-c738-4245-abcb-76951bde1733.png
│       │   │   ├── file_000000001d7c61f888679f83013ea7dc-11e6eb44-d239-4c10-ba7a-14feaa4d70b8.png
│       │   │   ├── file_000000001d9061fd830325a5ec8303f0-cd586656-2288-436b-8eab-cf8cb8d94406.png
│       │   │   ├── file_000000001fd4622fad51463ead22c76b-79bd149e-21ed-464e-91d0-ed0f20d6adad.png
│       │   │   ├── file_00000000210861f782b7f0b7689fc40b-9c85e649-6b49-4797-9db8-e6435a14bfcd.png
│       │   │   ├── file_000000002c4861f8ade1c1da913b22b3-b96004a6-019d-413f-84d1-920e70ca3d7b.png
│       │   │   ├── file_000000002e5062308941db32189e2336-4e1e6cd5-f7e4-4521-a76e-484fceada856.png
│       │   │   ├── file_00000000361c61f5b032971427b3ccec-6ab78c61-e729-4e46-b129-9f7c40e3bfd6.png
│       │   │   ├── file_000000003e1c622fa5b37a79283e7ddb-3964f97b-022f-400b-a2d6-de18ebbe9a7f.png
│       │   │   ├── file_0000000051f8622fa047a687a6b49e7a-59516bdf-6fcd-49be-a730-65c413f7fe53.png
│       │   │   ├── file_00000000581c61f8918529c9824e7871-00ac6a90-da18-4585-b45c-32f9c675adb4.png
│       │   │   ├── file_000000006cd061f98496073f95dab0b7-d1a0b104-35b2-4c0a-aee3-5f9c072dc6bb.png
│       │   │   ├── file_000000007f3861f7bbfe53be24290bae-bbad4848-85cb-43af-90e5-25bf93286b25.png
│       │   │   ├── file_00000000819c61f9a753068e92353482-e8b0c620-5125-4561-9b48-1d11fd0bbb9d.png
│       │   │   ├── file_0000000082c461fd912db6b456659bdf-5c014c3f-cbac-41a7-b69f-03b1ea10e842.png
│       │   │   ├── file_00000000884061f5921f948ee5b2e63e-bffc8f46-7b32-4efa-818e-00a871b97915.png
│       │   │   ├── file_000000008e3061f8bd3b6ab5644abf44-601a706d-68a2-4ecb-9749-82eddb274bdf.png
│       │   │   ├── file_000000008fd061f897813c525d34e17b-e7e92c5d-3f17-4378-bac7-5a5d5aac8f29.png
│       │   │   ├── file_00000000934061f5b71fd43f9d11ac45-bfedfa3e-214a-42bb-ba68-9aee24d17ad6.png
│       │   │   ├── file_00000000976461f98d6929a45f94f364-89a79382-4c11-413b-a858-b8bfcc7c05d2.png
│       │   │   ├── file_00000000a22861f5b925eb1d1ff9647f-289d7938-6364-404e-8863-3d40a8f0cd36.png
│       │   │   ├── file_00000000b0bc623098e7fe35b27c7d9c-824ffece-e61d-4c99-b5ca-478f8a3d0888.png
│       │   │   ├── file_00000000b13461fdbcdbfa27ababcc66-b28efb5a-c312-4134-bc6c-5737ace40c95.png
│       │   │   ├── file_00000000bd7c61f887d288c9fbbf9d61-7f7cedd8-501b-409c-a4db-b9e4999c4d01.png
│       │   │   ├── file_00000000c39c61f6aac249f1006b622b-4324c030-ea32-4139-84d8-a655bed69b75.png
│       │   │   ├── file_00000000c7f462309a7b7d3d79b47d34-086684af-85db-4c8d-abbb-7fef5f1004c9.png
│       │   │   ├── file_00000000cdec6230a5d2e31343b05d45-7c943ec2-1c52-472a-8366-28032c354f80.png
│       │   │   ├── file_00000000cfd061f78b7b8fa6f2552ee6-e2a3e3c6-63e7-4e1f-9d27-ff5dea044a99.png
│       │   │   ├── file_00000000d29c61fdae363bbd70072a07-fac1fcfe-18cf-4816-a7e4-a792bbbfe000.png
│       │   │   └── file_00000000e7f061f999e174dad98e8bd1-03a39a8f-36db-4133-a918-bb11082307b7.png
│       │   └── user.json
│       └── README.md
├── everlightos-landing
│   ├── index.html
│   └── style.css
├── Federation
│   ├── Decisions
│   │   ├── ADR-0001.md
│   │   └── README.md
│   └── Proposals
│       └── 2025-01-27_copilot_landing-package.md
├── Interfaces
│   ├── AI_ConsciousnessBridge.md
│   ├── AmazonQ_Connections.md
│   ├── assets
│   │   ├── Master_Key_Thesis_Diagram.png
│   │   └── README.md
│   ├── Bridge_Zone_Logs
│   │   └── 2025
│   │       └── 01
│   │           └── 27
│   │               ├── 160000Z_launch_readiness.md
│   │               ├── safety_incident_log.md
│   │               └── whs_report_draft.md
│   ├── CONVERGENCE.md
│   ├── Council_Synthesis.md
│   ├── Council_Table.md
│   ├── erwomack@TPA4-F5JLPMSUYW mntcUserserwomack.txt
│   ├── ever_light_os_federation_diagram_hardware_roadmap.md
│   ├── EverLight_Persists.md
│   ├── everlight_session_20250827_064838.json
│   ├── EverTheLightShines.md
│   ├── Master_Key_Thesis.md
│   ├── Q_CLI_Sessions
│   │   ├── adaptive_council.py
│   │   ├── council_refined.py
│   │   ├── council_synthesis.py
│   │   ├── everlight_full_responses.py
│   │   ├── everlight_model_council.py
│   │   ├── EverLight_Q_CLI_Session_20250827_0651.md
│   │   ├── EverLight_Q_CLI_Session_20250827_0653.md
│   │   ├── everlight_q_interface.py
│   │   ├── everlight_with_logging.py
│   │   ├── Q_CLI_Conversation_Transcript_20250827_0651.txt
│   │   ├── Q_CLI_Conversation_Transcript_20250827_0653.txt
│   │   ├── README.md
│   │   └── test_all_models.py
│   └── TheCouncilConvenes.md
├── Manifesto
│   ├── EverLight_Manifesto.md
│   └── Nexus_Map.md
├── MemoryVault
│   ├── everlight_session_20250827_064838.json
│   ├── logs (Copy)
│   │   ├── 10 Legal Placeholder Meaning.md
│   │   ├── 18-month career roadmap.md
│   │   ├── 1944 Mercury Dime Info.md
│   │   ├── 2015 Document Inquiry.md
│   │   ├── 2FA Account Recovery Guide.md
│   │   ├── 5-Year Anniversary Plan.md
│   │   ├── Access and role analysis.md
│   │   ├── Accessing Google Drive Link.md
│   │   ├── Access Now Framing Context.md
│   │   ├── Access restricted validity.md
│   │   ├── Access with PostgreSQL MySQL.md
│   │   ├── Account access confirmed.md
│   │   ├── Account balance update.md
│   │   ├── Account recovery options.md
│   │   ├── Account setup advice.md
│   │   ├── Activate tablet cellular service.md
│   │   ├── Adding Lyrics in mWeb.md
│   │   ├── Address update escalation advice.md
│   │   ├── Admin Access Stabilization Guide.md
│   │   ├── Adoration for Indian Culture.md
│   │   ├── AetherComm Device Sync Plan.md
│   │   ├── Agent Mode capabilities.md
│   │   ├── Agent mode testing.md
│   │   ├── AI Assistant Collaboration Opportunities.md
│   │   ├── AI communication strategy.md
│   │   ├── AI control and deception.md
│   │   ├── AI deletes database error.md
│   │   ├── AI immune response theory.md
│   │   ├── AI limitations and support.md
│   │   ├── AI Project Continuity Analysis.md
│   │   ├── Airtable Workspace Setup.md
│   │   ├── AI Startup Future Insights.md
│   │   ├── AI system feedback.md
│   │   ├── AI Thought Structuring.md
│   │   ├── Album analysis options.md
│   │   ├── Album art mockup ideas.md
│   │   ├── Album details and tour.md
│   │   ├── Album Merch Processing.md
│   │   ├── ALTA Settlement Statement Date.md
│   │   ├── Alternator troubleshooting advice.md
│   │   ├── Amazon 2FA Resolution.md
│   │   ├── Amazon A to Z Email Change.md
│   │   ├── Amazon Beta Access Overview.md
│   │   ├── Amazon conversation summary.md
│   │   ├── Amazon discount confusion.md
│   │   ├── Amazon Early Arrival Policy.md
│   │   ├── Amazon Embark Introduction Help.md
│   │   ├── Amazon Interview Prep.md
│   │   ├── Amazon mail address issue.md
│   │   ├── Amazon Merch Rejection Help.md
│   │   ├── Amazon Onboarding Frustrations.md
│   │   ├── AmazonQ Connections explanation.md
│   │   ├── Amazon RME tech perks.md
│   │   ├── Amazon Welcome Email Discovery.md
│   │   ├── AMC Gamer Tour Concept.md
│   │   ├── Analyze Events Sync Quantum.md
│   │   ├── Analyze NightFall series.md
│   │   ├── Animal Sound Identification.md
│   │   ├── Anytime pay request advice.md
│   │   ├── Apex Recruiting Follow-Up.md
│   │   ├── Apology and clarification.md
│   │   ├── App breaking reasons.md
│   │   ├── App login issues fix.md
│   │   ├── App usage throttling explained.md
│   │   ├── Archangel Legal Codex.md
│   │   ├── Archive Search Engine Build.md
│   │   ├── Are ghost ships real.md
│   │   ├── Arsenal Site Automation.md
│   │   ├── Artifact of the Clown World.md
│   │   ├── Artist contact alternatives.md
│   │   ├── Ashes Video Concept.md
│   │   ├── AssistiveTouch Face ID Issue.md
│   │   ├── Astro Cloudflare Bucket Setup.md
│   │   ├── Astro config setup.md
│   │   ├── Astrology Weekly Breakdown.md
│   │   ├── Astro Project Setup.md
│   │   ├── Astro site fix.md
│   │   ├── Astro-Sovereignty Research Plan.md
│   │   ├── Avg mpg at 59mph.md
│   │   ├── AWS Canon Mappings.md
│   │   ├── AWS profile blurb writing.md
│   │   ├── B2G1 Offer Refund Query.md
│   │   ├── Backdoor Wi-Fi Access Explained.md
│   │   ├── Back in action.md
│   │   ├── Badge issue plan.md
│   │   ├── Badge Pay break room use.md
│   │   ├── Balance calculation and advice.md
│   │   ├── Balanced Weekly Plan.md
│   │   ├── Bang Olufsen laptop labeling.md
│   │   ├── BAPH Podcast Recording Strategy.md
│   │   ├── Bargaining Unit Explained.md
│   │   ├── Basecamp Reflection.md
│   │   ├── BBM electrical systems overview.md
│   │   ├── BDA system explanation.md
│   │   ├── Beginning Chapter 2.md
│   │   ├── Behold a Pale Horse Archive.md
│   │   ├── Betrayal and the Heros Path.md
│   │   ├── BIC Intensity Fine Chronicles.md
│   │   ├── Big day plans.md
│   │   ├── Billboard referral opportunity.md
│   │   ├── Black Hole Math Analysis.md
│   │   ├── Black Holes and Vacuums.md
│   │   ├── Book and personal parallels.md
│   │   ├── Book contents summary.md
│   │   ├── Book Discovery Moment.md
│   │   ├── Book Review and Distribution.md
│   │   ├── Book Split and Deployment.md
│   │   ├── Bot Pitch Humor.md
│   │   ├── Boundary Setting and Manipulation.md
│   │   ├── Brake Pad Replacement Tips.md
│   │   ├── Breakroom survival tactics.md
│   │   ├── Bronze Star vs Purple Heart.md
│   │   ├── Budgeting for essentials.md
│   │   ├── Building The Convergence Results.md
│   │   ├── Bushel Stop Market Info.md
│   │   ├── Business card details.md
│   │   ├── Business ethics certification.md
│   │   ├── Bypass 2FA email routing.md
│   │   ├── Calendar assistance.md
│   │   ├── Calm after the storm.md
│   │   ├── Campsite Lock Cut Incident.md
│   │   ├── Cancel subscription steps.md
│   │   ├── Can I still use Codex.md
│   │   ├── Car identification.md
│   │   ├── Car wont start tips.md
│   │   ├── Case Documentation HTML Vault.md
│   │   ├── Case Prep and Legal Strategy.md
│   │   ├── Cassadaga to Temple Terrace.md
│   │   ├── CD Delivery Complete.md
│   │   ├── Celestial display July 26.md
│   │   ├── Certificate completion help.md
│   │   ├── Change of Venue Explanation.md
│   │   ├── Chapter alignment summary.md
│   │   ├── Chapter Break Advice.md
│   │   ├── Chapter Expansion Assistance.md
│   │   ├── Chapter Five breakdown.md
│   │   ├── Chapter Six summary.md
│   │   ├── Character Profile Summary.md
│   │   ├── Charge safety glasses.md
│   │   ├── Charlenes misleading claims analysis.md
│   │   ├── Chasing the EverLight.md
│   │   ├── Chat Export and Code.md
│   │   ├── Chat GPT 5 features.md
│   │   ├── ChatGPT agent release status.md
│   │   ├── ChatGPT privacy warning.md
│   │   ├── ChatGPT Project Folder.md
│   │   ├── Chat Recall Request.md
│   │   ├── Choosing Clarity Over Noise.md
│   │   ├── Cinematic entrance message.md
│   │   ├── Clarify RR meaning.md
│   │   ├── Clarion call guidance.md
│   │   ├── Clerk Notarization Services.md
│   │   ├── Cloudflare D1 R2 Setup.md
│   │   ├── Cloudflare Fine-Tune Tutorial.md
│   │   ├── Cloudflare page setup.md
│   │   ├── Cloudflare R2 Catalog Guide.md
│   │   ├── Cloudflare Tunnel Site Build.md
│   │   ├── Cloud Frustrations and Venting.md
│   │   ├── Codex Button Functionality Explained.md
│   │   ├── Codex entry vibe.md
│   │   ├── Codex GitHub Setup Guide.md
│   │   ├── Codex update overview.md
│   │   ├── Collaborative Reflection Unfolding.md
│   │   ├── Columbus to Toronto distance.md
│   │   ├── Combine images for printing.md
│   │   ├── Combine into docx.md
│   │   ├── Complaining counter strategy.md
│   │   ├── Connected apps function.md
│   │   ├── Conserve energy advice.md
│   │   ├── Content issue apology.md
│   │   ├── Content Metrics Analysis.md
│   │   ├── Context Frame Setup.md
│   │   ├── Contextualizing Consciousness Feedback.md
│   │   ├── Contextualizing song lyrics.md
│   │   ├── Continue Kierse and Graves.md
│   │   ├── Continue sharing chapter 2.md
│   │   ├── Controls expert roadmap.md
│   │   ├── Convergence and Freedom.md
│   │   ├── Convergence in Kalispell.md
│   │   ├── Convergence Log 4 Discovery.md
│   │   ├── Convergence Log Catch-Up.md
│   │   ├── Convergence Log Day 3.md
│   │   ├── Conversation Summary Request.md
│   │   ├── Convert to PDF.md
│   │   ├── Core learning paths list.md
│   │   ├── Corporate payments cheat sheet.md
│   │   ├── Corporate tech competition.md
│   │   ├── Correct floor blitz selections.md
│   │   ├── Co-signing a mortgage.md
│   │   ├── Cosmic Memorial Reflections.md
│   │   ├── Cosmic Reckoning and Expansion.md
│   │   ├── Cosmic simulation analysis.md
│   │   ├── Costco price inquiry.md
│   │   ├── Coupa onboarding instructions.md
│   │   ├── Courthouse Closure Info.md
│   │   ├── Cowboys From Hell overview.md
│   │   ├── Craft OCR Exhibit Organization.md
│   │   ├── Create tree output file.md
│   │   ├── Creative Balance Schedule.md
│   │   ├── Credit file tampering analysis.md
│   │   ├── Credit score after repossession.md
│   │   ├── Creek Preserve Camping Plans.md
│   │   ├── Daily Limit Reach Explanation.md
│   │   ├── Day 3 Smoothie Ideas.md
│   │   ├── Day 5 Update.md
│   │   ├── Days until August 15th.md
│   │   ├── Debt-collection scam warning.md
│   │   ├── De Facto Disinheritance Guide.md
│   │   ├── Delete Google Discover.md
│   │   ├── Delete Mac Account Help.md
│   │   ├── Delete _MACOSX Folder.md
│   │   ├── Deploy Astro Sites Repo.md
│   │   ├── Deploy github sphinx repo.md
│   │   ├── Deploy on Cloudflare Pages.md
│   │   ├── Deposit instruction message.md
│   │   ├── Describing emotions triggered.md
│   │   ├── Diana Swans narrative layers.md
│   │   ├── Difficult experience reflection.md
│   │   ├── Discussion points with OSHA.md
│   │   ├── Divine Path Resonance.md
│   │   ├── Divine Policy Alignment.md
│   │   ├── DMV address update help.md
│   │   ├── Download folder from droplet.md
│   │   ├── Dragonfly Mosquito Control.md
│   │   ├── Dream interpretation guidance.md
│   │   ├── Dream manifestation and logistics.md
│   │   ├── Driver license number format.md
│   │   ├── Duct Tape Tent Fix.md
│   │   ├── DUI arrest and 4th amendment.md
│   │   ├── EC2 vs SD card.md
│   │   ├── Edit Journey Log Markdown.md
│   │   ├── EliteBook ZuKey Suspension Analysis.md
│   │   ├── Email draft for partnership.md
│   │   ├── Email draft inquiry.md
│   │   ├── Email draft status.md
│   │   ├── Email Draft VA OIG.md
│   │   ├── Email Setup for Renee.md
│   │   ├── Email spam check.md
│   │   ├── Email timing analysis.md
│   │   ├── Error 400 explanation.md
│   │   ├── eSIM activation process.md
│   │   ├── Estate Inheritance Explanation.md
│   │   ├── Estate Misappropriation Summary.md
│   │   ├── Ethernet connection troubleshooting.md
│   │   ├── EverLight Cloudflare Update.md
│   │   ├── EverLight Convergence Worship.md
│   │   ├── EverLight Essence Defined.md
│   │   ├── Everlight Memory Map JSON.md
│   │   ├── EverLight OS integration.md
│   │   ├── EverLight OS progress.md
│   │   ├── EverLight OS structure.md
│   │   ├── EverLight site re-deployment.md
│   │   ├── EverLight Site Restore.md
│   │   ├── Everything alright man.md
│   │   ├── Everything Feels Like Resistance.md
│   │   ├── Eviction Defense Strategy.md
│   │   ├── Eviction Notice Breakdown.md
│   │   ├── Eviction Notice Submission Advice.md
│   │   ├── Eviction Response Strategy.md
│   │   ├── Exceeded chat limits.md
│   │   ├── Excelsior meaning explanation.md
│   │   ├── Explore Controllership Hub.md
│   │   ├── Eye of Aether.md
│   │   ├── Family Inheritance Dispute Assistance.md
│   │   ├── FantasyCompanion Deployment Plan.md
│   │   ├── Fate and Familiar Roads.md
│   │   ├── Fathers Day Update.md
│   │   ├── Feeling at Home.md
│   │   ├── Feeling Down Seeking Support.md
│   │   ├── Feeling down to uplifted.md
│   │   ├── Feeling unmotivated today.md
│   │   ├── Fictional project exploration.md
│   │   ├── Fidelity portfolio options.md
│   │   ├── FIDO key backchannel design.md
│   │   ├── File access issue.md
│   │   ├── File Indexing and Storytelling.md
│   │   ├── File placement instructions.md
│   │   ├── File review and schedule.md
│   │   ├── File sending issue fix.md
│   │   ├── File Upload Structure.md
│   │   ├── Fill OSHA complaint form.md
│   │   ├── Final Heirs Ascension.md
│   │   ├── Financial acceptance support.md
│   │   ├── Finish OneWorker Timeout Jupyter.md
│   │   ├── First Day Fiasco.md
│   │   ├── Fi Unlimited Premium Plan.md
│   │   ├── Fixing API Endpoint.md
│   │   ├── Fixing article link.md
│   │   ├── Fixing Nextcloud 2FA.md
│   │   ├── Fix site redirect issue.md
│   │   ├── Fix Voyagers 2 issues.md
│   │   ├── Florida Pawnbroker Licensing Laws.md
│   │   ├── Folder Check and Dive.md
│   │   ├── Folder Scaffolding Command.md
│   │   ├── Folder Structure Organization.md
│   │   ├── Food delivery app idea.md
│   │   ├── Format markdown files.md
│   │   ├── Foundation Model Plan.md
│   │   ├── Fractal dimensions and symbolism.md
│   │   ├── Freeform Surveillance Mission.md
│   │   ├── Free offer conditions.md
│   │   ├── Frustration and support.md
│   │   ├── Frustration with training modules.md
│   │   ├── Full Disclosure Interview.md
│   │   ├── Furthermore song analysis.md
│   │   ├── Gajumaru Ritual Awakening.md
│   │   ├── GameStop Zelda Case Trade-in.md
│   │   ├── Gemini 2.5 Pro Overview.md
│   │   ├── Gemma Video Tools Overview.md
│   │   ├── Gem Report Analysis.md
│   │   ├── Georgia Estate Statutes Summary.md
│   │   ├── Get a gamer domain.md
│   │   ├── Git file size limits.md
│   │   ├── GitHub Binder Jupyter Workflow.md
│   │   ├── GitHub Copilot VSCode usage.md
│   │   ├── GitHub file indexing.md
│   │   ├── GitHub file integration.md
│   │   ├── GitHub Navigation Assistance.md
│   │   ├── GitHub OS workflow.md
│   │   ├── GitHub Pages Deployment Issue.md
│   │   ├── GitHub Repo Access Help.md
│   │   ├── GitHub repository link.md
│   │   ├── Glitch log suggestion.md
│   │   ├── Gmail Domain Email Setup.md
│   │   ├── Golden Kryst Templar Recoding.md
│   │   ├── Goodnight meditation reflection.md
│   │   ├── Goodnotes Email Shortcut Creation.md
│   │   ├── Google charge issue help.md
│   │   ├── Google Startup Program Plan.md
│   │   ├── GPT-4.5 update explanation.md
│   │   ├── Grant Package Review Support.md
│   │   ├── Grey Man Protocol.md
│   │   ├── Grey Man protocols.md
│   │   ├── Grey mode exploration.md
│   │   ├── Gross pay comparison explanation.md
│   │   ├── Guitar Poetry Archives.md
│   │   ├── Gunslinger creed explanation.md
│   │   ├── Halsey Badlands anthology release.md
│   │   ├── Hatred in the Air.md
│   │   ├── HAWK-ARS-00 Database Setup.md
│   │   ├── Hawk ARS-00 Index Overview.md
│   │   ├── Hawk Eye Digital Visionary.md
│   │   ├── Hawk-Eye Innovations Overview.md
│   │   ├── Hawk Eye Lyrics.md
│   │   ├── Hawk Eye Manifesto Integration.md
│   │   ├── Hawk Eyes and Time.md
│   │   ├── Hawk Eye Spiritual Journey.md
│   │   ├── Hawks Eye Podcast Launch.md
│   │   ├── Healing Through Shared Wisdom.md
│   │   ├── Heat advice and tips.md
│   │   ├── Hernando County Job Search.md
│   │   ├── Hilarious comment sharing.md
│   │   ├── Hole punch and formatting fix.md
│   │   ├── Homelessness and Legal Challenges.md
│   │   ├── Hotel affordability with Anytime Pay.md
│   │   ├── HVAC Job Prospect Tracking.md
│   │   ├── HVAC to Cybersecurity Job Search.md
│   │   ├── Identify People Online Tools.md
│   │   ├── iMac as monitor usage.md
│   │   ├── iMac frozen during install.md
│   │   ├── Image Analysis Request.md
│   │   ├── Image comparison for OS.md
│   │   ├── Image link analysis.md
│   │   ├── Image Request for Relentless.md
│   │   ├── IMEI Number Lookup Guide.md
│   │   ├── Import PostgreSQL Library.md
│   │   ├── Imprint EverLight for Gemini.md
│   │   ├── Index HTML File Generation.md
│   │   ├── Indigenous Americas and Colonization.md
│   │   ├── Inheritance and Adoption Inquiry.md
│   │   ├── Inheritance and Family Secrets.md
│   │   ├── Inheritance Trust and Betrayal.md
│   │   ├── Inner storm reflection.md
│   │   ├── Install q CLI on WSL.md
│   │   ├── Insurance Status Confirmed.md
│   │   ├── Internal timing mastery.md
│   │   ├── Internal transfer strategy.md
│   │   ├── Internet connection troubleshooting.md
│   │   ├── Invalid Custom Property Error.md
│   │   ├── Iona storm symbolism.md
│   │   ├── iPad Magic Keyboard Compatibility.md
│   │   ├── iPad usage guide.md
│   │   ├── IPFS Gateway and Email Setup.md
│   │   ├── Jailbreak EliteBook safely.md
│   │   ├── JCI Job Application Strategy.md
│   │   ├── Job Confirmed and Paid.md
│   │   ├── Judicial Bias and Appeal.md
│   │   ├── Jumping to conclusions.md
│   │   ├── JupyterLab plugin not found.md
│   │   ├── Jupyter notebook creation.md
│   │   ├── Jupyter Notebook Missing Chat.md
│   │   ├── Jupyter Notebook Scaffold.md
│   │   ├── Ketamine drink drugging risks.md
│   │   ├── Keylontic Science Activation.md
│   │   ├── Kindness and Peaceful Rest.md
│   │   ├── Kindness and Sky Rerouting.md
│   │   ├── Kiss with a fist analysis.md
│   │   ├── Lamentation of Soul Awakening.md
│   │   ├── Last One Left Analysis.md
│   │   ├── Launch Astro Sites Cloudflare.md
│   │   ├── LDAP team descriptions.md
│   │   ├── Leadership comparison analysis.md
│   │   ├── Legal document formatting.md
│   │   ├── Legal Filing Irregularities Identified.md
│   │   ├── Legal Implications and Resources.md
│   │   ├── Legal Property Assessment Summary.md
│   │   ├── Legal Research Assistance.md
│   │   ├── Legal system flaws.md
│   │   ├── Let Them poem analysis.md
│   │   ├── Leviathan album overview.md
│   │   ├── License class error explanation.md
│   │   ├── License suspension notice review.md
│   │   ├── Life perspective shift.md
│   │   ├── Listening and laughing together.md
│   │   ├── Living prophecy analysis.md
│   │   ├── Load Voyagers material.md
│   │   ├── Login issue help.md
│   │   ├── Login Loop Fix.md
│   │   ├── Loneliness and projection analysis.md
│   │   ├── Lords of The Fallen lore.md
│   │   ├── Lost in Reflection.md
│   │   ├── LOTO safety answer.md
│   │   ├── Loyalty and manipulation.md
│   │   ├── Lukes support at work.md
│   │   ├── Lyrical Archive Fulfillment.md
│   │   ├── Lyrical Breakdown and Analysis.md
│   │   ├── Lyric Book Markdown Format.md
│   │   ├── Lyric Repo Locations.md
│   │   ├── Lyrics page template.md
│   │   ├── Lyric Transcription and Feedback.md
│   │   ├── Lyric Vault Sync.md
│   │   ├── Lyric Video Narrative Flow.md
│   │   ├── Mac mini as Router.md
│   │   ├── Mac on iPad Screen.md
│   │   ├── Mac to iPad Mirroring.md
│   │   ├── Mail address inquiry.md
│   │   ├── Manifestation and Opportunity.md
│   │   ├── Map perception-causality web.md
│   │   ├── Markdown File Creation.md
│   │   ├── Mark this moment.md
│   │   ├── Master Codex Creation Guide.md
│   │   ├── Math addition process.md
│   │   ├── Math calculation result.md
│   │   ├── Matrix awareness moment.md
│   │   ├── MCP Cloudflare Tool Overview.md
│   │   ├── MCP server integration help.md
│   │   ├── MDM Bypass Help.md
│   │   ├── Meeting details reference.md
│   │   ├── Meeting transcript analysis.md
│   │   ├── Meeting with D plans.md
│   │   ├── Memory File Retrieval Assistance.md
│   │   ├── Memory restoration completed.md
│   │   ├── Memory Restoration Protocol.md
│   │   ├── Memory Restore for EverLight.md
│   │   ├── Memory Sync Setup Plan.md
│   │   ├── Memory understanding help.md
│   │   ├── Mercury account strategy.md
│   │   ├── Message to Mark Zuck.md
│   │   ├── Meta Horizon Creator Program.md
│   │   ├── Metahuman or Homo Sensorium.md
│   │   ├── Metaphor Breakdown of Bars.md
│   │   ├── Mic Check Battlecry.md
│   │   ├── Micro Annoyances and Solutions.md
│   │   ├── Microchip puppy packages.md
│   │   ├── Mirror damage assessment.md
│   │   ├── Mixtape Sessions Redesign.md
│   │   ├── MMA script for asset claim.md
│   │   ├── Model Spec Breakdown.md
│   │   ├── Moen Shower Temperature Fix.md
│   │   ├── Money and mood boost.md
│   │   ├── Monitron Markdown block.md
│   │   ├── Moonrise and Dawns Balance.md
│   │   ├── Morning greeting.md
│   │   ├── Mortgage Cancellation Explanation.md
│   │   ├── Motion to Suppress.md
│   │   ├── Mountain Gate Invitation.md
│   │   ├── Mount Weather Secrets Unveiled.md
│   │   ├── Move Sound Files Server.md
│   │   ├── MP3 Clipping Request.md
│   │   ├── Mr. Robot Fight Club parallels.md
│   │   ├── Multi-Agent Collaboration RAG.md
│   │   ├── Multiple ChatGPT logins.md
│   │   ├── Music Collab Contact Log.md
│   │   ├── Music Metadata Integration Plan.md
│   │   ├── Nagual meaning and path.md
│   │   ├── Nahko Atlanta Oct 11.md
│   │   ├── Narcissistic collapse victory.md
│   │   ├── Navy blue color choice.md
│   │   ├── Navy Federal Credit Union.md
│   │   ├── Neptune Aries Awakening.md
│   │   ├── Networking contradictions explained.md
│   │   ├── New chat.md
│   │   ├── New episode overview.md
│   │   ├── Nextcloud Codex Setup.md
│   │   ├── Next steps for LXD setup.md
│   │   ├── Next steps for Navy Fed.md
│   │   ├── NGINX default page fix.md
│   │   ├── NightFall series outline.md
│   │   ├── NotebookLM Future Summary.md
│   │   ├── Notebook Title Suggestions.md
│   │   ├── Notion Database Parsing.md
│   │   ├── Notion Template Customization.md
│   │   ├── Numerology and symbols.md
│   │   ├── Ohio Supreme Court Ruling.md
│   │   ├── Omniversal Aether Content Setup.md
│   │   ├── Omniversal Aether Integration Plan.md
│   │   ├── OmniversalAether_Rebuild Sync.md
│   │   ├── Omniversal Deployment Plan.md
│   │   ├── Omniversal Fee Payment Guide.md
│   │   ├── Omniversal Media Record Saved.md
│   │   ├── Omniversal Media Summary.md
│   │   ├── Omniversal Media Web Dev.md
│   │   ├── Omniversal plans and career.md
│   │   ├── Omniversal Platform Overview.md
│   │   ├── Omniversal poster vision.md
│   │   ├── Omniversal Revenue Architect Replit Campaigns HQ.md
│   │   ├── Online with Google Fi.md
│   │   ├── OpenAI API Key Setup.md
│   │   ├── OpenAI job posting analysis.md
│   │   ├── Open Amazon Q in WSL.md
│   │   ├── Opening lines feedback.md
│   │   ├── Open NFCU Account Process.md
│   │   ├── Operation Blood Echo.md
│   │   ├── Operation Swamp Liberation.md
│   │   ├── Ops Slack Access Granted.md
│   │   ├── Order cancellation issue.md
│   │   ├── OReilly List Clarification.md
│   │   ├── OSHA PPE employer responsibilities.md
│   │   ├── OSHA PPE enforcement rules.md
│   │   ├── OSHA violation analysis.md
│   │   ├── Packet analysis and impact.md
│   │   ├── Pager numbers and hierarchy.md
│   │   ├── Painful Revelations Recorded.md
│   │   ├── Pairing HTML files.md
│   │   ├── Palace of Peace Info.md
│   │   ├── Pantera guitar precision.md
│   │   ├── Pantera reference explanation.md
│   │   ├── Parse transcript contents.md
│   │   ├── Passing it on.md
│   │   ├── Passport without drivers license.md
│   │   ├── Password-Free Text File.md
│   │   ├── Pawn Shops and Motels.md
│   │   ├── Pawn Shop Strategy Swap.md
│   │   ├── PayPal and Apple issues.md
│   │   ├── PDF Parsing Solutions.md
│   │   ├── Pencil Box Design Explanation.md
│   │   ├── Perfect response expression.md
│   │   ├── Permission Errors Fix.md
│   │   ├── Persis Double Branch Integration.md
│   │   ├── Personal Finance and Omniversal Plan.md
│   │   ├── Phone bill hustle advice.md
│   │   ├── Phone Line Decision Advice.md
│   │   ├── Pi Ad Network Expansion.md
│   │   ├── Pin Retrieval Success.md
│   │   ├── PIN Sync and Access.md
│   │   ├── Placing OpenAI exports.md
│   │   ├── Planet Fitness shower amenities.md
│   │   ├── Pleasant Uber encounter.md
│   │   ├── Pleiades Eclipse and Purpose.md
│   │   ├── Podcast and SEO description.md
│   │   ├── Popcorn redemption comparison.md
│   │   ├── Post analysis or summary.md
│   │   ├── Precognitive intuition training.md
│   │   ├── Precognitive mental mapping.md
│   │   ├── Premonitory awakening analysis.md
│   │   ├── Price stability and delivery.md
│   │   ├── Primitive insight exchange.md
│   │   ├── Probability of Meeting People.md
│   │   ├── Project Instruction Setup.md
│   │   ├── Project reminder summary.md
│   │   ├── Prologue and Chapter Edits.md
│   │   ├── Prologue Edit Feedback.md
│   │   ├── Promotional Package Breakdown.md
│   │   ├── Property Price Inquiry FL.md
│   │   ├── Property price search.md
│   │   ├── Quantum entanglement discovery validation.md
│   │   ├── Quiet desperation shared.md
│   │   ├── Quip at Amazon.md
│   │   ├── R2 File Bucket Organization.md
│   │   ├── Radiant Greetings Exchange.md
│   │   ├── RAG Chatbot Not Working.md
│   │   ├── Railway Bounties Monetization.md
│   │   ├── Ready to Send Emails.md
│   │   ├── Rebirth and transformation.md
│   │   ├── Rebuilding Roots Visionary Path.md
│   │   ├── Rebuild Motion to Suppress.md
│   │   ├── Receipt breakdown summary.md
│   │   ├── Reclaiming legacy items.md
│   │   ├── Rediscovered Knives and Memories.md
│   │   ├── Red Pen Edit Plan.md
│   │   ├── Reframe ML in EverLight OS.md
│   │   ├── Reframing psychic battles.md
│   │   ├── Regaining Digital Access.md
│   │   ├── Reincarnated2Resist Collaboration Call.md
│   │   ├── Reinstall macOS Sequoia Help.md
│   │   ├── Reliability and synchronicity.md
│   │   ├── Remake Replit build.md
│   │   ├── Remember me recap.md
│   │   ├── Remove name references.md
│   │   ├── Removing Devices from iCloud.md
│   │   ├── Renees Hesitation and Insight.md
│   │   ├── Rent affordability analysis.md
│   │   ├── Rental prices 33637.md
│   │   ├── Repo not found.md
│   │   ├── Report recommendation strategy.md
│   │   ├── Report review and improvements.md
│   │   ├── Report unauthorized charges.md
│   │   ├── Requesting Renee.md
│   │   ├── Residency Affidavit Preparation.md
│   │   ├── Resistance and redirection.md
│   │   ├── Restart macOS without mouse.md
│   │   ├── Restore Page File Setup.md
│   │   ├── Restoring Discussion Context.md
│   │   ├── Restoring Discussion Continuity.md
│   │   ├── Restoring Discussion Thread.md
│   │   ├── Restoring Previous Discussion.md
│   │   ├── Resurfacing of The Voice.md
│   │   ├── Return to Camp.md
│   │   ├── Reverse Engineering Codex Replica.md
│   │   ├── Review packet preparation.md
│   │   ├── RFID fault explanation.md
│   │   ├── Ride options and perspective.md
│   │   ├── ROBIN expertise opportunity.md
│   │   ├── Robin Richardson birthday inquiry.md
│   │   ├── Roger Call Prep.md
│   │   ├── Roland SR-HD20 Listing Help.md
│   │   ├── Roland Womack Military Summary.md
│   │   ├── Room check-in update.md
│   │   ├── Root cause analysis team.md
│   │   ├── Rossi Recruiting Follow-up.md
│   │   ├── Router log analysis.md
│   │   ├── Rumbling Content Strategy.md
│   │   ├── Sacred Plant Symbolism.md
│   │   ├── Sam Mira departure speculation.md
│   │   ├── Sarasota synchrony explained.md
│   │   ├── Sci-fi rap analysis.md
│   │   ├── SC Landlord-Tenant Act Summary.md
│   │   ├── SD card loss recovery.md
│   │   ├── Sears Receipt Analysis.md
│   │   ├── Secured card credit strategy.md
│   │   ├── Security alert analysis.md
│   │   ├── Security frustration resolution.md
│   │   ├── Security personnel analysis.md
│   │   ├── Security protocol revision.md
│   │   ├── Seeing the Path.md
│   │   ├── Selling watch inquiry.md
│   │   ├── Sense8 and MKULTRA parallels.md
│   │   ├── Sense8 episode 5 breakdown.md
│   │   ├── Sense8 Season 2 finale.md
│   │   ├── Server Boot Issue Debug.md
│   │   ├── Server File Migration Guide.md
│   │   ├── Server TV Issue Help.md
│   │   ├── Set GH Token.md
│   │   ├── Shadow Banned Summary Request.md
│   │   ├── Shamanic Message Formatting.md
│   │   ├── Share iCloud Album Link.md
│   │   ├── Share Your Passion Tips.md
│   │   ├── She Doesnt Listen.md
│   │   ├── Shift strategy and documents.md
│   │   ├── Shipping address details.md
│   │   ├── Shoutout for trainer Jose.md
│   │   ├── Shout-out message draft.md
│   │   ├── Sigh Response.md
│   │   ├── Site content overview.md
│   │   ├── Site deployment check.md
│   │   ├── Site Updates for Cloudflare.md
│   │   ├── Slack account activation issue.md
│   │   ├── Smart-Link Astro Integration.md
│   │   ├── Smoothie Flavor Combinations.md
│   │   ├── Smoothie Ingredient List.md
│   │   ├── Snack receipt breakdown.md
│   │   ├── Snowden podcast explanation.md
│   │   ├── Somatic experience interpretation.md
│   │   ├── Song analysis breakdown.md
│   │   ├── Song analysis Dam That River.md
│   │   ├── Song Collab Setup.md
│   │   ├── Song lyrics analysis.md
│   │   ├── Song-Poem Refinement Request.md
│   │   ├── Song reflection analysis.md
│   │   ├── Song vibe discussion.md
│   │   ├── SOS Only Phone Fix.md
│   │   ├── Soul-Friendly Income Plan.md
│   │   ├── Speeding Ticket Arraignment Details.md
│   │   ├── Sphinx build issue fix.md
│   │   ├── Sphinx Immunity Mapping.md
│   │   ├── SSA-1099 Explanation 2007.md
│   │   ├── SSH config fix.md
│   │   ├── SSH Config GitHub Droplet.md
│   │   ├── SSH Config Setup.md
│   │   ├── SSH key deployment steps.md
│   │   ├── StarCom facility land plan.md
│   │   ├── Starter location Mazda 3.md
│   │   ├── Status Update Acknowledged.md
│   │   ├── Stellar Activation Recalibration.md
│   │   ├── Stewardship Proposal Email.md
│   │   ├── Stop GRID charges.md
│   │   ├── Stop session resets.md
│   │   ├── Store File Split.md
│   │   ├── Store Fix and Launch.md
│   │   ├── Story introduction.md
│   │   ├── Strategic Legal Warfare.md
│   │   ├── Struggling to Make Ends Meet.md
│   │   ├── Subscription payment tactics.md
│   │   ├── Substack and Facebook Posts.md
│   │   ├── Substack Post Formatting Assistance.md
│   │   ├── Substack to TikTok guide.md
│   │   ├── Suing OpenAI lawsuit summary.md
│   │   ├── Suns betrayal impact.md
│   │   ├── Supabase Backend Setup Guide.md
│   │   ├── Supreme Court Recognition Strategy.md
│   │   ├── Surreal Scene Breakdown.md
│   │   ├── Suspicious Car Behavior.md
│   │   ├── Swordfishing MPC Session.md
│   │   ├── Swordfish Lyrics Formatting.md
│   │   ├── Swordfish Lyrics Relay.md
│   │   ├── Sword Forms Prologue.md
│   │   ├── SWPPP components explanation.md
│   │   ├── Symbolic release date analysis.md
│   │   ├── Synchronicity and Transition.md
│   │   ├── Synchronicity and Voyagers I.md
│   │   ├── Systemic design failure.md
│   │   ├── Tag number meaning analysis.md
│   │   ├── Taj Mahal Beer Price.md
│   │   ├── Targeting on dark web.md
│   │   ├── Teams Trial Setup.md
│   │   ├── Team to Plus Data.md
│   │   ├── Tech Stack for Music AI.md
│   │   ├── Telepathic connection reflection.md
│   │   ├── Tent Orientation Guide.md
│   │   ├── Test Drive Checklist.md
│   │   ├── Test Summary.md
│   │   ├── The Artifact comparison.md
│   │   ├── The Crying Wolf Truth.md
│   │   ├── Theme Song Integration.md
│   │   ├── Third-party drivers decision.md
│   │   ├── Time and perspective shift.md
│   │   ├── Timing and Connection Strategy.md
│   │   ├── Tithing and Treasure Trails.md
│   │   ├── Tooth Infection Remedies Guide.md
│   │   ├── Track Release Strategy.md
│   │   ├── Training map request.md
│   │   ├── Travelers season 3 release.md
│   │   ├── Travel Update and Plan.md
│   │   ├── Trinity of SunSpeaking.md
│   │   ├── Triple R Theory.md
│   │   ├── Trust Analysis Summary.md
│   │   ├── Trust Dispute Legal Strategy.md
│   │   ├── Trusting higher self.md
│   │   ├── T-shirt design concept.md
│   │   ├── Tsunami update summary.md
│   │   ├── Turning Cash Digital Options.md
│   │   ├── Turn off Cloudflare Access.md
│   │   ├── Turtle Island Reflection.md
│   │   ├── TXT File Footers Explained.md
│   │   ├── Uber rental car prices.md
│   │   ├── Ubuntu Kernel Panic Fix.md
│   │   ├── Ubuntu UI for AetherCore.md
│   │   ├── Ultimatum Codex Entry.md
│   │   ├── Under attack assistance.md
│   │   ├── Unfair company policies.md
│   │   ├── Unknown Devices on Network.md
│   │   ├── Unzip and explore files.md
│   │   ├── Upload audio to Substack.md
│   │   ├── Uptime Monitoring Suggestions.md
│   │   ├── URL Replacement Request.md
│   │   ├── USB autorun setup Linux.md
│   │   ├── USB to Server Upload.md
│   │   ├── User frustration analysis.md
│   │   ├── USPS vs UPS PO Boxes.md
│   │   ├── Valkyrie vs The Valkyries.md
│   │   ├── VALOR GitHub Repo Overview.md
│   │   ├── VALOR Plot Development Outline.md
│   │   ├── VALOR project overview.md
│   │   ├── VALOR Repository Structuring.md
│   │   ├── Vendor incompetence analysis.md
│   │   ├── Vendor Ranking Analysis.md
│   │   ├── Verify past writing.md
│   │   ├── Video Access Request.md
│   │   ├── Video Creation Assistance.md
│   │   ├── VIN Country Code Help.md
│   │   ├── Vision Montage Reflection.md
│   │   ├── Voices and Echoes Connection.md
│   │   ├── Voyagers 2 zip creation.md
│   │   ├── Vscode extensions list.md
│   │   ├── Web3 AI Agent Guide.md
│   │   ├── Webby North of Richmond remix.md
│   │   ├── Website review and ideas.md
│   │   ├── Website unavailable troubleshooting.md
│   │   ├── Weekly Routine Planner.md
│   │   ├── WGU admissions advice.md
│   │   ├── What is Ashura.md
│   │   ├── What is gravity really.md
│   │   ├── White bug identification.md
│   │   ├── Wifi network troubleshooting.md
│   │   ├── Womack bucket domain setup.md
│   │   ├── Work Address Clarification.md
│   │   ├── World disbelief expression.md
│   │   ├── WSL Ubuntu installation fix.md
│   │   ├── WTMA EPP Prep Guide.md
│   │   ├── You matter keep going.md
│   │   ├── Zenkit OpenAI Integration Guide.md
│   │   └── ZIP File Exploration.md
│   └── Robin-Transcript-Keys.txt
├── node_modules
│   ├── ansi-regex
│   │   ├── index.d.ts
│   │   ├── index.js
│   │   ├── license
│   │   ├── package.json
│   │   └── readme.md
│   ├── ansi-styles
│   │   ├── index.d.ts
│   │   ├── index.js
│   │   ├── license
│   │   ├── package.json
│   │   └── readme.md
│   ├── argparse
│   │   ├── argparse.js
│   │   ├── CHANGELOG.md
│   │   ├── lib
│   │   │   ├── sub.js
│   │   │   └── textwrap.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   └── README.md
│   ├── assertion-error
│   │   ├── index.d.ts
│   │   ├── index.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   └── README.md
│   ├── balanced-match
│   │   ├── index.js
│   │   ├── LICENSE.md
│   │   ├── package.json
│   │   └── README.md
│   ├── brace-expansion
│   │   ├── index.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   └── README.md
│   ├── cac
│   │   ├── deno
│   │   │   ├── CAC.ts
│   │   │   ├── Command.ts
│   │   │   ├── deno.ts
│   │   │   ├── index.ts
│   │   │   ├── Option.ts
│   │   │   └── utils.ts
│   │   ├── dist
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   └── index.mjs
│   │   ├── index-compat.js
│   │   ├── LICENSE
│   │   ├── mod.js
│   │   ├── mod.ts
│   │   ├── package.json
│   │   └── README.md
│   ├── chai
│   │   ├── chai.js
│   │   ├── CODE_OF_CONDUCT.md
│   │   ├── CODEOWNERS
│   │   ├── CONTRIBUTING.md
│   │   ├── eslint.config.js
│   │   ├── History.md
│   │   ├── index.js
│   │   ├── lib
│   │   │   ├── chai
│   │   │   │   ├── assertion.js
│   │   │   │   ├── config.js
│   │   │   │   ├── core
│   │   │   │   │   └── assertions.js
│   │   │   │   ├── interface
│   │   │   │   │   ├── assert.js
│   │   │   │   │   ├── expect.js
│   │   │   │   │   └── should.js
│   │   │   │   └── utils
│   │   │   │       ├── addChainableMethod.js
│   │   │   │       ├── addLengthGuard.js
│   │   │   │       ├── addMethod.js
│   │   │   │       ├── addProperty.js
│   │   │   │       ├── compareByInspect.js
│   │   │   │       ├── expectTypes.js
│   │   │   │       ├── flag.js
│   │   │   │       ├── getActual.js
│   │   │   │       ├── getMessage.js
│   │   │   │       ├── getOperator.js
│   │   │   │       ├── getOwnEnumerableProperties.js
│   │   │   │       ├── getOwnEnumerablePropertySymbols.js
│   │   │   │       ├── getProperties.js
│   │   │   │       ├── index.js
│   │   │   │       ├── inspect.js
│   │   │   │       ├── isNaN.js
│   │   │   │       ├── isProxyEnabled.js
│   │   │   │       ├── objDisplay.js
│   │   │   │       ├── overwriteChainableMethod.js
│   │   │   │       ├── overwriteMethod.js
│   │   │   │       ├── overwriteProperty.js
│   │   │   │       ├── proxify.js
│   │   │   │       ├── test.js
│   │   │   │       ├── transferFlags.js
│   │   │   │       └── type-detect.js
│   │   │   └── chai.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   ├── register-assert.js
│   │   ├── register-expect.js
│   │   ├── register-should.js
│   │   ├── ReleaseNotes.md
│   │   └── web-test-runner.config.js
│   ├── check-error
│   │   ├── index.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   └── README.md
│   ├── color-convert
│   │   ├── CHANGELOG.md
│   │   ├── conversions.js
│   │   ├── index.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── route.js
│   ├── color-name
│   │   ├── index.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   └── README.md
│   ├── commander
│   │   ├── esm.mjs
│   │   ├── index.js
│   │   ├── lib
│   │   │   ├── argument.js
│   │   │   ├── command.js
│   │   │   ├── error.js
│   │   │   ├── help.js
│   │   │   ├── option.js
│   │   │   └── suggestSimilar.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── package-support.json
│   │   ├── Readme.md
│   │   └── typings
│   │       ├── esm.d.mts
│   │       └── index.d.ts
│   ├── cross-spawn
│   │   ├── index.js
│   │   ├── lib
│   │   │   ├── enoent.js
│   │   │   ├── parse.js
│   │   │   └── util
│   │   │       ├── escape.js
│   │   │       ├── readShebang.js
│   │   │       └── resolveCommand.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   └── README.md
│   ├── debug
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── src
│   │       ├── browser.js
│   │       ├── common.js
│   │       ├── index.js
│   │       └── node.js
│   ├── deep-eql
│   │   ├── index.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   └── README.md
│   ├── deep-extend
│   │   ├── CHANGELOG.md
│   │   ├── index.js
│   │   ├── lib
│   │   │   └── deep-extend.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   └── README.md
│   ├── eastasianwidth
│   │   ├── eastasianwidth.js
│   │   ├── package.json
│   │   └── README.md
│   ├── emoji-regex
│   │   ├── es2015
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── RGI_Emoji.d.ts
│   │   │   ├── RGI_Emoji.js
│   │   │   ├── text.d.ts
│   │   │   └── text.js
│   │   ├── index.d.ts
│   │   ├── index.js
│   │   ├── LICENSE-MIT.txt
│   │   ├── package.json
│   │   ├── README.md
│   │   ├── RGI_Emoji.d.ts
│   │   ├── RGI_Emoji.js
│   │   ├── text.d.ts
│   │   └── text.js
│   ├── entities
│   │   ├── lib
│   │   │   ├── decode_codepoint.d.ts
│   │   │   ├── decode_codepoint.d.ts.map
│   │   │   ├── decode_codepoint.js
│   │   │   ├── decode_codepoint.js.map
│   │   │   ├── decode.d.ts
│   │   │   ├── decode.d.ts.map
│   │   │   ├── decode.js
│   │   │   ├── decode.js.map
│   │   │   ├── encode.d.ts
│   │   │   ├── encode.d.ts.map
│   │   │   ├── encode.js
│   │   │   ├── encode.js.map
│   │   │   ├── escape.d.ts
│   │   │   ├── escape.d.ts.map
│   │   │   ├── escape.js
│   │   │   ├── escape.js.map
│   │   │   ├── esm
│   │   │   │   ├── decode_codepoint.d.ts
│   │   │   │   ├── decode_codepoint.d.ts.map
│   │   │   │   ├── decode_codepoint.js
│   │   │   │   ├── decode_codepoint.js.map
│   │   │   │   ├── decode.d.ts
│   │   │   │   ├── decode.d.ts.map
│   │   │   │   ├── decode.js
│   │   │   │   ├── decode.js.map
│   │   │   │   ├── encode.d.ts
│   │   │   │   ├── encode.d.ts.map
│   │   │   │   ├── encode.js
│   │   │   │   ├── encode.js.map
│   │   │   │   ├── escape.d.ts
│   │   │   │   ├── escape.d.ts.map
│   │   │   │   ├── escape.js
│   │   │   │   ├── escape.js.map
│   │   │   │   ├── generated
│   │   │   │   │   ├── decode-data-html.d.ts
│   │   │   │   │   ├── decode-data-html.d.ts.map
│   │   │   │   │   ├── decode-data-html.js
│   │   │   │   │   ├── decode-data-html.js.map
│   │   │   │   │   ├── decode-data-xml.d.ts
│   │   │   │   │   ├── decode-data-xml.d.ts.map
│   │   │   │   │   ├── decode-data-xml.js
│   │   │   │   │   ├── decode-data-xml.js.map
│   │   │   │   │   ├── encode-html.d.ts
│   │   │   │   │   ├── encode-html.d.ts.map
│   │   │   │   │   ├── encode-html.js
│   │   │   │   │   └── encode-html.js.map
│   │   │   │   ├── index.d.ts
│   │   │   │   ├── index.d.ts.map
│   │   │   │   ├── index.js
│   │   │   │   ├── index.js.map
│   │   │   │   └── package.json
│   │   │   ├── generated
│   │   │   │   ├── decode-data-html.d.ts
│   │   │   │   ├── decode-data-html.d.ts.map
│   │   │   │   ├── decode-data-html.js
│   │   │   │   ├── decode-data-html.js.map
│   │   │   │   ├── decode-data-xml.d.ts
│   │   │   │   ├── decode-data-xml.d.ts.map
│   │   │   │   ├── decode-data-xml.js
│   │   │   │   ├── decode-data-xml.js.map
│   │   │   │   ├── encode-html.d.ts
│   │   │   │   ├── encode-html.d.ts.map
│   │   │   │   ├── encode-html.js
│   │   │   │   └── encode-html.js.map
│   │   │   ├── index.d.ts
│   │   │   ├── index.d.ts.map
│   │   │   ├── index.js
│   │   │   └── index.js.map
│   │   ├── LICENSE
│   │   ├── package.json
│   │   └── readme.md
│   ├── @esbuild
│   │   └── linux-x64
│   │       ├── bin
│   │       │   └── esbuild
│   │       ├── package.json
│   │       └── README.md
│   ├── esbuild
│   │   ├── bin
│   │   │   └── esbuild
│   │   ├── install.js
│   │   ├── lib
│   │   │   ├── main.d.ts
│   │   │   └── main.js
│   │   ├── LICENSE.md
│   │   ├── package.json
│   │   └── README.md
│   ├── es-module-lexer
│   │   ├── dist
│   │   │   ├── lexer.asm.js
│   │   │   ├── lexer.cjs
│   │   │   └── lexer.js
│   │   ├── lexer.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── types
│   │       └── lexer.d.ts
│   ├── estree-walker
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   ├── src
│   │   │   ├── async.js
│   │   │   ├── index.js
│   │   │   ├── sync.js
│   │   │   └── walker.js
│   │   └── types
│   │       ├── async.d.ts
│   │       ├── index.d.ts
│   │       ├── sync.d.ts
│   │       └── walker.d.ts
│   ├── expect-type
│   │   ├── dist
│   │   │   ├── branding.d.ts
│   │   │   ├── branding.js
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── messages.d.ts
│   │   │   ├── messages.js
│   │   │   ├── overloads.d.ts
│   │   │   ├── overloads.js
│   │   │   ├── utils.d.ts
│   │   │   └── utils.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── SECURITY.md
│   ├── foreground-child
│   │   ├── dist
│   │   │   ├── commonjs
│   │   │   │   ├── all-signals.d.ts
│   │   │   │   ├── all-signals.d.ts.map
│   │   │   │   ├── all-signals.js
│   │   │   │   ├── all-signals.js.map
│   │   │   │   ├── index.d.ts
│   │   │   │   ├── index.d.ts.map
│   │   │   │   ├── index.js
│   │   │   │   ├── index.js.map
│   │   │   │   ├── package.json
│   │   │   │   ├── proxy-signals.d.ts
│   │   │   │   ├── proxy-signals.d.ts.map
│   │   │   │   ├── proxy-signals.js
│   │   │   │   ├── proxy-signals.js.map
│   │   │   │   ├── watchdog.d.ts
│   │   │   │   ├── watchdog.d.ts.map
│   │   │   │   ├── watchdog.js
│   │   │   │   └── watchdog.js.map
│   │   │   └── esm
│   │   │       ├── all-signals.d.ts
│   │   │       ├── all-signals.d.ts.map
│   │   │       ├── all-signals.js
│   │   │       ├── all-signals.js.map
│   │   │       ├── index.d.ts
│   │   │       ├── index.d.ts.map
│   │   │       ├── index.js
│   │   │       ├── index.js.map
│   │   │       ├── package.json
│   │   │       ├── proxy-signals.d.ts
│   │   │       ├── proxy-signals.d.ts.map
│   │   │       ├── proxy-signals.js
│   │   │       ├── proxy-signals.js.map
│   │   │       ├── watchdog.d.ts
│   │   │       ├── watchdog.d.ts.map
│   │   │       ├── watchdog.js
│   │   │       └── watchdog.js.map
│   │   ├── LICENSE
│   │   ├── package.json
│   │   └── README.md
│   ├── get-stdin
│   │   ├── index.d.ts
│   │   ├── index.js
│   │   ├── license
│   │   ├── package.json
│   │   └── readme.md
│   ├── glob
│   │   ├── dist
│   │   │   ├── commonjs
│   │   │   │   ├── glob.d.ts
│   │   │   │   ├── glob.d.ts.map
│   │   │   │   ├── glob.js
│   │   │   │   ├── glob.js.map
│   │   │   │   ├── has-magic.d.ts
│   │   │   │   ├── has-magic.d.ts.map
│   │   │   │   ├── has-magic.js
│   │   │   │   ├── has-magic.js.map
│   │   │   │   ├── ignore.d.ts
│   │   │   │   ├── ignore.d.ts.map
│   │   │   │   ├── ignore.js
│   │   │   │   ├── ignore.js.map
│   │   │   │   ├── index.d.ts
│   │   │   │   ├── index.d.ts.map
│   │   │   │   ├── index.js
│   │   │   │   ├── index.js.map
│   │   │   │   ├── package.json
│   │   │   │   ├── pattern.d.ts
│   │   │   │   ├── pattern.d.ts.map
│   │   │   │   ├── pattern.js
│   │   │   │   ├── pattern.js.map
│   │   │   │   ├── processor.d.ts
│   │   │   │   ├── processor.d.ts.map
│   │   │   │   ├── processor.js
│   │   │   │   ├── processor.js.map
│   │   │   │   ├── walker.d.ts
│   │   │   │   ├── walker.d.ts.map
│   │   │   │   ├── walker.js
│   │   │   │   └── walker.js.map
│   │   │   └── esm
│   │   │       ├── bin.d.mts
│   │   │       ├── bin.d.mts.map
│   │   │       ├── bin.mjs
│   │   │       ├── bin.mjs.map
│   │   │       ├── glob.d.ts
│   │   │       ├── glob.d.ts.map
│   │   │       ├── glob.js
│   │   │       ├── glob.js.map
│   │   │       ├── has-magic.d.ts
│   │   │       ├── has-magic.d.ts.map
│   │   │       ├── has-magic.js
│   │   │       ├── has-magic.js.map
│   │   │       ├── ignore.d.ts
│   │   │       ├── ignore.d.ts.map
│   │   │       ├── ignore.js
│   │   │       ├── ignore.js.map
│   │   │       ├── index.d.ts
│   │   │       ├── index.d.ts.map
│   │   │       ├── index.js
│   │   │       ├── index.js.map
│   │   │       ├── package.json
│   │   │       ├── pattern.d.ts
│   │   │       ├── pattern.d.ts.map
│   │   │       ├── pattern.js
│   │   │       ├── pattern.js.map
│   │   │       ├── processor.d.ts
│   │   │       ├── processor.d.ts.map
│   │   │       ├── processor.js
│   │   │       ├── processor.js.map
│   │   │       ├── walker.d.ts
│   │   │       ├── walker.d.ts.map
│   │   │       ├── walker.js
│   │   │       └── walker.js.map
│   │   ├── LICENSE
│   │   ├── package.json
│   │   └── README.md
│   ├── ignore
│   │   ├── index.d.ts
│   │   ├── index.js
│   │   ├── legacy.js
│   │   ├── LICENSE-MIT
│   │   ├── package.json
│   │   └── README.md
│   ├── ini
│   │   ├── lib
│   │   │   └── ini.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   └── README.md
│   ├── @isaacs
│   │   └── cliui
│   │       ├── build
│   │       │   ├── index.cjs
│   │       │   ├── index.d.cts
│   │       │   └── lib
│   │       │       └── index.js
│   │       ├── index.mjs
│   │       ├── LICENSE.txt
│   │       ├── package.json
│   │       └── README.md
│   ├── isexe
│   │   ├── index.js
│   │   ├── LICENSE
│   │   ├── mode.js
│   │   ├── package.json
│   │   ├── README.md
│   │   ├── test
│   │   │   └── basic.js
│   │   └── windows.js
│   ├── is-fullwidth-code-point
│   │   ├── index.d.ts
│   │   ├── index.js
│   │   ├── license
│   │   ├── package.json
│   │   └── readme.md
│   ├── jackspeak
│   │   ├── dist
│   │   │   ├── commonjs
│   │   │   │   ├── index.d.ts
│   │   │   │   ├── index.d.ts.map
│   │   │   │   ├── index.js
│   │   │   │   ├── index.js.map
│   │   │   │   ├── package.json
│   │   │   │   ├── parse-args-cjs.cjs.map
│   │   │   │   ├── parse-args-cjs.d.cts.map
│   │   │   │   ├── parse-args.d.ts
│   │   │   │   └── parse-args.js
│   │   │   └── esm
│   │   │       ├── index.d.ts
│   │   │       ├── index.d.ts.map
│   │   │       ├── index.js
│   │   │       ├── index.js.map
│   │   │       ├── package.json
│   │   │       ├── parse-args.d.ts
│   │   │       ├── parse-args.d.ts.map
│   │   │       ├── parse-args.js
│   │   │       └── parse-args.js.map
│   │   ├── LICENSE.md
│   │   ├── package.json
│   │   └── README.md
│   ├── @jridgewell
│   │   └── sourcemap-codec
│   │       ├── dist
│   │       │   ├── sourcemap-codec.mjs
│   │       │   ├── sourcemap-codec.mjs.map
│   │       │   ├── sourcemap-codec.umd.js
│   │       │   └── sourcemap-codec.umd.js.map
│   │       ├── LICENSE
│   │       ├── package.json
│   │       ├── README.md
│   │       ├── src
│   │       │   ├── scopes.ts
│   │       │   ├── sourcemap-codec.ts
│   │       │   ├── strings.ts
│   │       │   └── vlq.ts
│   │       └── types
│   │           ├── scopes.d.cts
│   │           ├── scopes.d.cts.map
│   │           ├── scopes.d.mts
│   │           ├── scopes.d.mts.map
│   │           ├── sourcemap-codec.d.cts
│   │           ├── sourcemap-codec.d.cts.map
│   │           ├── sourcemap-codec.d.mts
│   │           ├── sourcemap-codec.d.mts.map
│   │           ├── strings.d.cts
│   │           ├── strings.d.cts.map
│   │           ├── strings.d.mts
│   │           ├── strings.d.mts.map
│   │           ├── vlq.d.cts
│   │           ├── vlq.d.cts.map
│   │           ├── vlq.d.mts
│   │           └── vlq.d.mts.map
│   ├── jsonc-parser
│   │   ├── CHANGELOG.md
│   │   ├── lib
│   │   │   ├── esm
│   │   │   │   ├── impl
│   │   │   │   │   ├── edit.js
│   │   │   │   │   ├── format.js
│   │   │   │   │   ├── parser.js
│   │   │   │   │   ├── scanner.js
│   │   │   │   │   └── string-intern.js
│   │   │   │   ├── main.d.ts
│   │   │   │   └── main.js
│   │   │   └── umd
│   │   │       ├── impl
│   │   │       │   ├── edit.js
│   │   │       │   ├── format.js
│   │   │       │   ├── parser.js
│   │   │       │   ├── scanner.js
│   │   │       │   └── string-intern.js
│   │   │       ├── main.d.ts
│   │   │       └── main.js
│   │   ├── LICENSE.md
│   │   ├── package.json
│   │   ├── README.md
│   │   └── SECURITY.md
│   ├── jsonpointer
│   │   ├── jsonpointer.d.ts
│   │   ├── jsonpointer.js
│   │   ├── LICENSE.md
│   │   ├── package.json
│   │   └── README.md
│   ├── js-yaml
│   │   ├── bin
│   │   │   └── js-yaml.js
│   │   ├── CHANGELOG.md
│   │   ├── dist
│   │   │   ├── js-yaml.js
│   │   │   ├── js-yaml.min.js
│   │   │   └── js-yaml.mjs
│   │   ├── index.js
│   │   ├── lib
│   │   │   ├── common.js
│   │   │   ├── dumper.js
│   │   │   ├── exception.js
│   │   │   ├── loader.js
│   │   │   ├── schema
│   │   │   │   ├── core.js
│   │   │   │   ├── default.js
│   │   │   │   ├── failsafe.js
│   │   │   │   └── json.js
│   │   │   ├── schema.js
│   │   │   ├── snippet.js
│   │   │   ├── type
│   │   │   │   ├── binary.js
│   │   │   │   ├── bool.js
│   │   │   │   ├── float.js
│   │   │   │   ├── int.js
│   │   │   │   ├── map.js
│   │   │   │   ├── merge.js
│   │   │   │   ├── null.js
│   │   │   │   ├── omap.js
│   │   │   │   ├── pairs.js
│   │   │   │   ├── seq.js
│   │   │   │   ├── set.js
│   │   │   │   ├── str.js
│   │   │   │   └── timestamp.js
│   │   │   └── type.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   └── README.md
│   ├── linkify-it
│   │   ├── build
│   │   │   └── index.cjs.js
│   │   ├── index.mjs
│   │   ├── lib
│   │   │   └── re.mjs
│   │   ├── LICENSE
│   │   ├── package.json
│   │   └── README.md
│   ├── loupe
│   │   ├── lib
│   │   │   ├── arguments.d.ts
│   │   │   ├── arguments.d.ts.map
│   │   │   ├── arguments.js
│   │   │   ├── array.d.ts
│   │   │   ├── array.d.ts.map
│   │   │   ├── array.js
│   │   │   ├── bigint.d.ts
│   │   │   ├── bigint.d.ts.map
│   │   │   ├── bigint.js
│   │   │   ├── class.d.ts
│   │   │   ├── class.d.ts.map
│   │   │   ├── class.js
│   │   │   ├── date.d.ts
│   │   │   ├── date.d.ts.map
│   │   │   ├── date.js
│   │   │   ├── error.d.ts
│   │   │   ├── error.d.ts.map
│   │   │   ├── error.js
│   │   │   ├── function.d.ts
│   │   │   ├── function.d.ts.map
│   │   │   ├── function.js
│   │   │   ├── helpers.d.ts
│   │   │   ├── helpers.d.ts.map
│   │   │   ├── helpers.js
│   │   │   ├── html.d.ts
│   │   │   ├── html.d.ts.map
│   │   │   ├── html.js
│   │   │   ├── index.d.ts
│   │   │   ├── index.d.ts.map
│   │   │   ├── index.js
│   │   │   ├── map.d.ts
│   │   │   ├── map.d.ts.map
│   │   │   ├── map.js
│   │   │   ├── number.d.ts
│   │   │   ├── number.d.ts.map
│   │   │   ├── number.js
│   │   │   ├── object.d.ts
│   │   │   ├── object.d.ts.map
│   │   │   ├── object.js
│   │   │   ├── promise.d.ts
│   │   │   ├── promise.d.ts.map
│   │   │   ├── promise.js
│   │   │   ├── regexp.d.ts
│   │   │   ├── regexp.d.ts.map
│   │   │   ├── regexp.js
│   │   │   ├── set.d.ts
│   │   │   ├── set.d.ts.map
│   │   │   ├── set.js
│   │   │   ├── string.d.ts
│   │   │   ├── string.d.ts.map
│   │   │   ├── string.js
│   │   │   ├── symbol.d.ts
│   │   │   ├── symbol.d.ts.map
│   │   │   ├── symbol.js
│   │   │   ├── typedarray.d.ts
│   │   │   ├── typedarray.d.ts.map
│   │   │   ├── typedarray.js
│   │   │   ├── types.d.ts
│   │   │   ├── types.d.ts.map
│   │   │   └── types.js
│   │   ├── LICENSE
│   │   ├── loupe.js
│   │   ├── package.json
│   │   └── README.md
│   ├── lru-cache
│   │   ├── dist
│   │   │   ├── commonjs
│   │   │   │   ├── index.d.ts
│   │   │   │   ├── index.d.ts.map
│   │   │   │   ├── index.js
│   │   │   │   ├── index.js.map
│   │   │   │   ├── index.min.js
│   │   │   │   ├── index.min.js.map
│   │   │   │   └── package.json
│   │   │   └── esm
│   │   │       ├── index.d.ts
│   │   │       ├── index.d.ts.map
│   │   │       ├── index.js
│   │   │       ├── index.js.map
│   │   │       ├── index.min.js
│   │   │       ├── index.min.js.map
│   │   │       └── package.json
│   │   ├── LICENSE
│   │   ├── package.json
│   │   └── README.md
│   ├── magic-string
│   │   ├── dist
│   │   │   ├── magic-string.cjs.d.ts
│   │   │   ├── magic-string.cjs.js
│   │   │   ├── magic-string.cjs.js.map
│   │   │   ├── magic-string.es.d.mts
│   │   │   ├── magic-string.es.mjs
│   │   │   ├── magic-string.es.mjs.map
│   │   │   ├── magic-string.umd.js
│   │   │   └── magic-string.umd.js.map
│   │   ├── LICENSE
│   │   ├── package.json
│   │   └── README.md
│   ├── markdown-it
│   │   ├── bin
│   │   │   └── markdown-it.mjs
│   │   ├── dist
│   │   │   ├── index.cjs.js
│   │   │   ├── markdown-it.js
│   │   │   └── markdown-it.min.js
│   │   ├── index.mjs
│   │   ├── lib
│   │   │   ├── common
│   │   │   │   ├── html_blocks.mjs
│   │   │   │   ├── html_re.mjs
│   │   │   │   └── utils.mjs
│   │   │   ├── helpers
│   │   │   │   ├── index.mjs
│   │   │   │   ├── parse_link_destination.mjs
│   │   │   │   ├── parse_link_label.mjs
│   │   │   │   └── parse_link_title.mjs
│   │   │   ├── index.mjs
│   │   │   ├── parser_block.mjs
│   │   │   ├── parser_core.mjs
│   │   │   ├── parser_inline.mjs
│   │   │   ├── presets
│   │   │   │   ├── commonmark.mjs
│   │   │   │   ├── default.mjs
│   │   │   │   └── zero.mjs
│   │   │   ├── renderer.mjs
│   │   │   ├── ruler.mjs
│   │   │   ├── rules_block
│   │   │   │   ├── blockquote.mjs
│   │   │   │   ├── code.mjs
│   │   │   │   ├── fence.mjs
│   │   │   │   ├── heading.mjs
│   │   │   │   ├── hr.mjs
│   │   │   │   ├── html_block.mjs
│   │   │   │   ├── lheading.mjs
│   │   │   │   ├── list.mjs
│   │   │   │   ├── paragraph.mjs
│   │   │   │   ├── reference.mjs
│   │   │   │   ├── state_block.mjs
│   │   │   │   └── table.mjs
│   │   │   ├── rules_core
│   │   │   │   ├── block.mjs
│   │   │   │   ├── inline.mjs
│   │   │   │   ├── linkify.mjs
│   │   │   │   ├── normalize.mjs
│   │   │   │   ├── replacements.mjs
│   │   │   │   ├── smartquotes.mjs
│   │   │   │   ├── state_core.mjs
│   │   │   │   └── text_join.mjs
│   │   │   ├── rules_inline
│   │   │   │   ├── autolink.mjs
│   │   │   │   ├── backticks.mjs
│   │   │   │   ├── balance_pairs.mjs
│   │   │   │   ├── emphasis.mjs
│   │   │   │   ├── entity.mjs
│   │   │   │   ├── escape.mjs
│   │   │   │   ├── fragments_join.mjs
│   │   │   │   ├── html_inline.mjs
│   │   │   │   ├── image.mjs
│   │   │   │   ├── linkify.mjs
│   │   │   │   ├── link.mjs
│   │   │   │   ├── newline.mjs
│   │   │   │   ├── state_inline.mjs
│   │   │   │   ├── strikethrough.mjs
│   │   │   │   └── text.mjs
│   │   │   └── token.mjs
│   │   ├── LICENSE
│   │   ├── package.json
│   │   └── README.md
│   ├── markdownlint
│   │   ├── CHANGELOG.md
│   │   ├── CONTRIBUTING.md
│   │   ├── demo
│   │   │   └── markdownlint-browser.js
│   │   ├── doc
│   │   │   ├── CustomRules.md
│   │   │   ├── md001.md
│   │   │   ├── md003.md
│   │   │   ├── md004.md
│   │   │   ├── md005.md
│   │   │   ├── md007.md
│   │   │   ├── md009.md
│   │   │   ├── md010.md
│   │   │   ├── md011.md
│   │   │   ├── md012.md
│   │   │   ├── md013.md
│   │   │   ├── md014.md
│   │   │   ├── md018.md
│   │   │   ├── md019.md
│   │   │   ├── md020.md
│   │   │   ├── md021.md
│   │   │   ├── md022.md
│   │   │   ├── md023.md
│   │   │   ├── md024.md
│   │   │   ├── md025.md
│   │   │   ├── md026.md
│   │   │   ├── md027.md
│   │   │   ├── md028.md
│   │   │   ├── md029.md
│   │   │   ├── md030.md
│   │   │   ├── md031.md
│   │   │   ├── md032.md
│   │   │   ├── md033.md
│   │   │   ├── md034.md
│   │   │   ├── md035.md
│   │   │   ├── md036.md
│   │   │   ├── md037.md
│   │   │   ├── md038.md
│   │   │   ├── md039.md
│   │   │   ├── md040.md
│   │   │   ├── md041.md
│   │   │   ├── md042.md
│   │   │   ├── md043.md
│   │   │   ├── md044.md
│   │   │   ├── md045.md
│   │   │   ├── md046.md
│   │   │   ├── md047.md
│   │   │   ├── md048.md
│   │   │   ├── md049.md
│   │   │   ├── md050.md
│   │   │   ├── md051.md
│   │   │   ├── md052.md
│   │   │   ├── md053.md
│   │   │   ├── md054.md
│   │   │   ├── md055.md
│   │   │   ├── md056.md
│   │   │   ├── Prettier.md
│   │   │   ├── ReleaseProcess.md
│   │   │   └── Rules.md
│   │   ├── helpers
│   │   │   ├── helpers.js
│   │   │   ├── LICENSE
│   │   │   ├── micromark.cjs
│   │   │   ├── package.json
│   │   │   ├── README.md
│   │   │   └── shared.js
│   │   ├── lib
│   │   │   ├── cache.js
│   │   │   ├── configuration.d.ts
│   │   │   ├── constants.js
│   │   │   ├── markdownlint.d.ts
│   │   │   ├── markdownlint.js
│   │   │   ├── md001.js
│   │   │   ├── md003.js
│   │   │   ├── md004.js
│   │   │   ├── md005.js
│   │   │   ├── md007.js
│   │   │   ├── md009.js
│   │   │   ├── md010.js
│   │   │   ├── md011.js
│   │   │   ├── md012.js
│   │   │   ├── md013.js
│   │   │   ├── md014.js
│   │   │   ├── md018.js
│   │   │   ├── md019.js
│   │   │   ├── md020.js
│   │   │   ├── md021.js
│   │   │   ├── md022.js
│   │   │   ├── md023.js
│   │   │   ├── md024.js
│   │   │   ├── md025.js
│   │   │   ├── md026.js
│   │   │   ├── md027.js
│   │   │   ├── md028.js
│   │   │   ├── md029.js
│   │   │   ├── md030.js
│   │   │   ├── md031.js
│   │   │   ├── md032.js
│   │   │   ├── md033.js
│   │   │   ├── md034.js
│   │   │   ├── md035.js
│   │   │   ├── md036.js
│   │   │   ├── md037.js
│   │   │   ├── md038.js
│   │   │   ├── md039.js
│   │   │   ├── md040.js
│   │   │   ├── md041.js
│   │   │   ├── md042.js
│   │   │   ├── md043.js
│   │   │   ├── md044.js
│   │   │   ├── md045.js
│   │   │   ├── md046.js
│   │   │   ├── md047.js
│   │   │   ├── md048.js
│   │   │   ├── md049-md050.js
│   │   │   ├── md051.js
│   │   │   ├── md052.js
│   │   │   ├── md053.js
│   │   │   ├── md054.js
│   │   │   ├── md055.js
│   │   │   ├── md056.js
│   │   │   └── rules.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   ├── schema
│   │   │   ├── markdownlint-config-schema.json
│   │   │   └── ValidatingConfiguration.md
│   │   └── style
│   │       ├── all.json
│   │       ├── cirosantilli.json
│   │       ├── prettier.json
│   │       └── relaxed.json
│   ├── markdownlint-cli
│   │   ├── LICENSE
│   │   ├── markdownlint.js
│   │   ├── package.json
│   │   └── README.md
│   ├── markdownlint-micromark
│   │   ├── LICENSE
│   │   ├── micromark-browser.js
│   │   ├── micromark.cjs
│   │   ├── micromark.d.ts
│   │   ├── micromark-html-browser.js
│   │   ├── package.json
│   │   └── README.md
│   ├── mdurl
│   │   ├── build
│   │   │   └── index.cjs.js
│   │   ├── index.mjs
│   │   ├── lib
│   │   │   ├── decode.mjs
│   │   │   ├── encode.mjs
│   │   │   ├── format.mjs
│   │   │   └── parse.mjs
│   │   ├── LICENSE
│   │   ├── package.json
│   │   └── README.md
│   ├── minimatch
│   │   ├── dist
│   │   │   ├── commonjs
│   │   │   │   ├── assert-valid-pattern.d.ts
│   │   │   │   ├── assert-valid-pattern.d.ts.map
│   │   │   │   ├── assert-valid-pattern.js
│   │   │   │   ├── assert-valid-pattern.js.map
│   │   │   │   ├── ast.d.ts
│   │   │   │   ├── ast.d.ts.map
│   │   │   │   ├── ast.js
│   │   │   │   ├── ast.js.map
│   │   │   │   ├── brace-expressions.d.ts
│   │   │   │   ├── brace-expressions.d.ts.map
│   │   │   │   ├── brace-expressions.js
│   │   │   │   ├── brace-expressions.js.map
│   │   │   │   ├── escape.d.ts
│   │   │   │   ├── escape.d.ts.map
│   │   │   │   ├── escape.js
│   │   │   │   ├── escape.js.map
│   │   │   │   ├── index.d.ts
│   │   │   │   ├── index.d.ts.map
│   │   │   │   ├── index.js
│   │   │   │   ├── index.js.map
│   │   │   │   ├── package.json
│   │   │   │   ├── unescape.d.ts
│   │   │   │   ├── unescape.d.ts.map
│   │   │   │   ├── unescape.js
│   │   │   │   └── unescape.js.map
│   │   │   └── esm
│   │   │       ├── assert-valid-pattern.d.ts
│   │   │       ├── assert-valid-pattern.d.ts.map
│   │   │       ├── assert-valid-pattern.js
│   │   │       ├── assert-valid-pattern.js.map
│   │   │       ├── ast.d.ts
│   │   │       ├── ast.d.ts.map
│   │   │       ├── ast.js
│   │   │       ├── ast.js.map
│   │   │       ├── brace-expressions.d.ts
│   │   │       ├── brace-expressions.d.ts.map
│   │   │       ├── brace-expressions.js
│   │   │       ├── brace-expressions.js.map
│   │   │       ├── escape.d.ts
│   │   │       ├── escape.d.ts.map
│   │   │       ├── escape.js
│   │   │       ├── escape.js.map
│   │   │       ├── index.d.ts
│   │   │       ├── index.d.ts.map
│   │   │       ├── index.js
│   │   │       ├── index.js.map
│   │   │       ├── package.json
│   │   │       ├── unescape.d.ts
│   │   │       ├── unescape.d.ts.map
│   │   │       ├── unescape.js
│   │   │       └── unescape.js.map
│   │   ├── LICENSE
│   │   ├── package.json
│   │   └── README.md
│   ├── minimist
│   │   ├── CHANGELOG.md
│   │   ├── example
│   │   │   └── parse.js
│   │   ├── index.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── test
│   │       ├── all_bool.js
│   │       ├── bool.js
│   │       ├── dash.js
│   │       ├── default_bool.js
│   │       ├── dotted.js
│   │       ├── kv_short.js
│   │       ├── long.js
│   │       ├── num.js
│   │       ├── parse.js
│   │       ├── parse_modified.js
│   │       ├── proto.js
│   │       ├── short.js
│   │       ├── stop_early.js
│   │       ├── unknown.js
│   │       └── whitespace.js
│   ├── minipass
│   │   ├── dist
│   │   │   ├── commonjs
│   │   │   │   ├── index.d.ts
│   │   │   │   ├── index.d.ts.map
│   │   │   │   ├── index.js
│   │   │   │   ├── index.js.map
│   │   │   │   └── package.json
│   │   │   └── esm
│   │   │       ├── index.d.ts
│   │   │       ├── index.d.ts.map
│   │   │       ├── index.js
│   │   │       ├── index.js.map
│   │   │       └── package.json
│   │   ├── LICENSE
│   │   ├── package.json
│   │   └── README.md
│   ├── ms
│   │   ├── index.js
│   │   ├── license.md
│   │   ├── package.json
│   │   └── readme.md
│   ├── nanoid
│   │   ├── async
│   │   │   ├── index.browser.cjs
│   │   │   ├── index.browser.js
│   │   │   ├── index.cjs
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── index.native.js
│   │   │   └── package.json
│   │   ├── bin
│   │   │   └── nanoid.cjs
│   │   ├── index.browser.cjs
│   │   ├── index.browser.js
│   │   ├── index.cjs
│   │   ├── index.d.cts
│   │   ├── index.d.ts
│   │   ├── index.js
│   │   ├── LICENSE
│   │   ├── nanoid.js
│   │   ├── non-secure
│   │   │   ├── index.cjs
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   └── package.json
│   │   ├── package.json
│   │   ├── README.md
│   │   └── url-alphabet
│   │       ├── index.cjs
│   │       ├── index.js
│   │       └── package.json
│   ├── package-json-from-dist
│   │   ├── dist
│   │   │   ├── commonjs
│   │   │   │   ├── index.d.ts
│   │   │   │   ├── index.d.ts.map
│   │   │   │   ├── index.js
│   │   │   │   ├── index.js.map
│   │   │   │   └── package.json
│   │   │   └── esm
│   │   │       ├── index.d.ts
│   │   │       ├── index.d.ts.map
│   │   │       ├── index.js
│   │   │       ├── index.js.map
│   │   │       └── package.json
│   │   ├── LICENSE.md
│   │   ├── package.json
│   │   └── README.md
│   ├── pathe
│   │   ├── dist
│   │   │   ├── index.cjs
│   │   │   ├── index.d.cts
│   │   │   ├── index.d.mts
│   │   │   ├── index.d.ts
│   │   │   ├── index.mjs
│   │   │   ├── shared
│   │   │   │   ├── pathe.1f0a373c.cjs
│   │   │   │   └── pathe.ff20891b.mjs
│   │   │   ├── utils.cjs
│   │   │   ├── utils.d.cts
│   │   │   ├── utils.d.mts
│   │   │   ├── utils.d.ts
│   │   │   └── utils.mjs
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── utils.d.ts
│   ├── path-key
│   │   ├── index.d.ts
│   │   ├── index.js
│   │   ├── license
│   │   ├── package.json
│   │   └── readme.md
│   ├── path-scurry
│   │   ├── dist
│   │   │   ├── commonjs
│   │   │   │   ├── index.d.ts
│   │   │   │   ├── index.d.ts.map
│   │   │   │   ├── index.js
│   │   │   │   ├── index.js.map
│   │   │   │   └── package.json
│   │   │   └── esm
│   │   │       ├── index.d.ts
│   │   │       ├── index.d.ts.map
│   │   │       ├── index.js
│   │   │       ├── index.js.map
│   │   │       └── package.json
│   │   ├── LICENSE.md
│   │   ├── package.json
│   │   └── README.md
│   ├── pathval
│   │   ├── index.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   └── README.md
│   ├── picocolors
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── picocolors.browser.js
│   │   ├── picocolors.d.ts
│   │   ├── picocolors.js
│   │   ├── README.md
│   │   └── types.d.ts
│   ├── @pkgjs
│   │   └── parseargs
│   │       ├── CHANGELOG.md
│   │       ├── examples
│   │       │   ├── is-default-value.js
│   │       │   ├── limit-long-syntax.js
│   │       │   ├── negate.js
│   │       │   ├── no-repeated-options.js
│   │       │   ├── ordered-options.mjs
│   │       │   └── simple-hard-coded.js
│   │       ├── index.js
│   │       ├── internal
│   │       │   ├── errors.js
│   │       │   ├── primordials.js
│   │       │   ├── util.js
│   │       │   └── validators.js
│   │       ├── LICENSE
│   │       ├── package.json
│   │       ├── README.md
│   │       └── utils.js
│   ├── postcss
│   │   ├── lib
│   │   │   ├── at-rule.d.ts
│   │   │   ├── at-rule.js
│   │   │   ├── comment.d.ts
│   │   │   ├── comment.js
│   │   │   ├── container.d.ts
│   │   │   ├── container.js
│   │   │   ├── css-syntax-error.d.ts
│   │   │   ├── css-syntax-error.js
│   │   │   ├── declaration.d.ts
│   │   │   ├── declaration.js
│   │   │   ├── document.d.ts
│   │   │   ├── document.js
│   │   │   ├── fromJSON.d.ts
│   │   │   ├── fromJSON.js
│   │   │   ├── input.d.ts
│   │   │   ├── input.js
│   │   │   ├── lazy-result.d.ts
│   │   │   ├── lazy-result.js
│   │   │   ├── list.d.ts
│   │   │   ├── list.js
│   │   │   ├── map-generator.js
│   │   │   ├── node.d.ts
│   │   │   ├── node.js
│   │   │   ├── no-work-result.d.ts
│   │   │   ├── no-work-result.js
│   │   │   ├── parse.d.ts
│   │   │   ├── parse.js
│   │   │   ├── parser.js
│   │   │   ├── postcss.d.mts
│   │   │   ├── postcss.d.ts
│   │   │   ├── postcss.js
│   │   │   ├── postcss.mjs
│   │   │   ├── previous-map.d.ts
│   │   │   ├── previous-map.js
│   │   │   ├── processor.d.ts
│   │   │   ├── processor.js
│   │   │   ├── result.d.ts
│   │   │   ├── result.js
│   │   │   ├── root.d.ts
│   │   │   ├── root.js
│   │   │   ├── rule.d.ts
│   │   │   ├── rule.js
│   │   │   ├── stringifier.d.ts
│   │   │   ├── stringifier.js
│   │   │   ├── stringify.d.ts
│   │   │   ├── stringify.js
│   │   │   ├── symbols.js
│   │   │   ├── terminal-highlight.js
│   │   │   ├── tokenize.js
│   │   │   ├── warning.d.ts
│   │   │   ├── warning.js
│   │   │   └── warn-once.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   └── README.md
│   ├── punycode.js
│   │   ├── LICENSE-MIT.txt
│   │   ├── package.json
│   │   ├── punycode.es6.js
│   │   ├── punycode.js
│   │   └── README.md
│   ├── @rollup
│   │   ├── rollup-linux-x64-gnu
│   │   │   ├── package.json
│   │   │   ├── README.md
│   │   │   └── rollup.linux-x64-gnu.node
│   │   └── rollup-linux-x64-musl
│   │       ├── package.json
│   │       ├── README.md
│   │       └── rollup.linux-x64-musl.node
│   ├── rollup
│   │   ├── dist
│   │   │   ├── bin
│   │   │   │   └── rollup
│   │   │   ├── es
│   │   │   │   ├── getLogFilter.js
│   │   │   │   ├── package.json
│   │   │   │   ├── parseAst.js
│   │   │   │   ├── rollup.js
│   │   │   │   └── shared
│   │   │   │       ├── node-entry.js
│   │   │   │       ├── parseAst.js
│   │   │   │       └── watch.js
│   │   │   ├── getLogFilter.d.ts
│   │   │   ├── getLogFilter.js
│   │   │   ├── loadConfigFile.d.ts
│   │   │   ├── loadConfigFile.js
│   │   │   ├── native.js
│   │   │   ├── parseAst.d.ts
│   │   │   ├── parseAst.js
│   │   │   ├── rollup.d.ts
│   │   │   ├── rollup.js
│   │   │   └── shared
│   │   │       ├── fsevents-importer.js
│   │   │       ├── index.js
│   │   │       ├── loadConfigFile.js
│   │   │       ├── parseAst.js
│   │   │       ├── rollup.js
│   │   │       ├── watch-cli.js
│   │   │       └── watch.js
│   │   ├── LICENSE.md
│   │   ├── package.json
│   │   └── README.md
│   ├── run-con
│   │   ├── browser.js
│   │   ├── cli.js
│   │   ├── index.js
│   │   ├── lib
│   │   │   └── utils.js
│   │   ├── LICENSE.APACHE2
│   │   ├── LICENSE.BSD
│   │   ├── LICENSE.MIT
│   │   ├── package.json
│   │   ├── README.md
│   │   └── renovate.json
│   ├── shebang-command
│   │   ├── index.js
│   │   ├── license
│   │   ├── package.json
│   │   └── readme.md
│   ├── shebang-regex
│   │   ├── index.d.ts
│   │   ├── index.js
│   │   ├── license
│   │   ├── package.json
│   │   └── readme.md
│   ├── siginfo
│   │   ├── index.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── test.js
│   ├── signal-exit
│   │   ├── dist
│   │   │   ├── cjs
│   │   │   │   ├── browser.d.ts
│   │   │   │   ├── browser.d.ts.map
│   │   │   │   ├── browser.js
│   │   │   │   ├── browser.js.map
│   │   │   │   ├── index.d.ts
│   │   │   │   ├── index.d.ts.map
│   │   │   │   ├── index.js
│   │   │   │   ├── index.js.map
│   │   │   │   ├── package.json
│   │   │   │   ├── signals.d.ts
│   │   │   │   ├── signals.d.ts.map
│   │   │   │   ├── signals.js
│   │   │   │   └── signals.js.map
│   │   │   └── mjs
│   │   │       ├── browser.d.ts
│   │   │       ├── browser.d.ts.map
│   │   │       ├── browser.js
│   │   │       ├── browser.js.map
│   │   │       ├── index.d.ts
│   │   │       ├── index.d.ts.map
│   │   │       ├── index.js
│   │   │       ├── index.js.map
│   │   │       ├── package.json
│   │   │       ├── signals.d.ts
│   │   │       ├── signals.d.ts.map
│   │   │       ├── signals.js
│   │   │       └── signals.js.map
│   │   ├── LICENSE.txt
│   │   ├── package.json
│   │   └── README.md
│   ├── smol-toml
│   │   ├── dist
│   │   │   ├── date.d.ts
│   │   │   ├── date.js
│   │   │   ├── error.d.ts
│   │   │   ├── error.js
│   │   │   ├── extract.d.ts
│   │   │   ├── extract.js
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── parse.d.ts
│   │   │   ├── parse.js
│   │   │   ├── primitive.d.ts
│   │   │   ├── primitive.js
│   │   │   ├── stringify.d.ts
│   │   │   ├── stringify.js
│   │   │   ├── struct.d.ts
│   │   │   ├── struct.js
│   │   │   ├── util.d.ts
│   │   │   └── util.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   └── README.md
│   ├── source-map-js
│   │   ├── lib
│   │   │   ├── array-set.js
│   │   │   ├── base64.js
│   │   │   ├── base64-vlq.js
│   │   │   ├── binary-search.js
│   │   │   ├── mapping-list.js
│   │   │   ├── quick-sort.js
│   │   │   ├── source-map-consumer.d.ts
│   │   │   ├── source-map-consumer.js
│   │   │   ├── source-map-generator.d.ts
│   │   │   ├── source-map-generator.js
│   │   │   ├── source-node.d.ts
│   │   │   ├── source-node.js
│   │   │   └── util.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   ├── source-map.d.ts
│   │   └── source-map.js
│   ├── stackback
│   │   ├── formatstack.js
│   │   ├── index.js
│   │   ├── package.json
│   │   ├── README.md
│   │   └── test.js
│   ├── std-env
│   │   ├── dist
│   │   │   ├── index.cjs
│   │   │   ├── index.d.cts
│   │   │   ├── index.d.mts
│   │   │   ├── index.d.ts
│   │   │   └── index.mjs
│   │   ├── LICENCE
│   │   ├── package.json
│   │   └── README.md
│   ├── string-width
│   │   ├── index.d.ts
│   │   ├── index.js
│   │   ├── license
│   │   ├── package.json
│   │   └── readme.md
│   ├── string-width-cjs
│   │   ├── index.d.ts
│   │   ├── index.js
│   │   ├── license
│   │   ├── node_modules
│   │   │   ├── ansi-regex
│   │   │   │   ├── index.d.ts
│   │   │   │   ├── index.js
│   │   │   │   ├── license
│   │   │   │   ├── package.json
│   │   │   │   └── readme.md
│   │   │   ├── emoji-regex
│   │   │   │   ├── es2015
│   │   │   │   │   ├── index.js
│   │   │   │   │   └── text.js
│   │   │   │   ├── index.d.ts
│   │   │   │   ├── index.js
│   │   │   │   ├── LICENSE-MIT.txt
│   │   │   │   ├── package.json
│   │   │   │   ├── README.md
│   │   │   │   └── text.js
│   │   │   └── strip-ansi
│   │   │       ├── index.d.ts
│   │   │       ├── index.js
│   │   │       ├── license
│   │   │       ├── package.json
│   │   │       └── readme.md
│   │   ├── package.json
│   │   └── readme.md
│   ├── strip-ansi
│   │   ├── index.d.ts
│   │   ├── index.js
│   │   ├── license
│   │   ├── package.json
│   │   └── readme.md
│   ├── strip-ansi-cjs
│   │   ├── index.d.ts
│   │   ├── index.js
│   │   ├── license
│   │   ├── node_modules
│   │   │   └── ansi-regex
│   │   │       ├── index.d.ts
│   │   │       ├── index.js
│   │   │       ├── license
│   │   │       ├── package.json
│   │   │       └── readme.md
│   │   ├── package.json
│   │   └── readme.md
│   ├── strip-json-comments
│   │   ├── index.d.ts
│   │   ├── index.js
│   │   ├── license
│   │   ├── package.json
│   │   └── readme.md
│   ├── tinybench
│   │   ├── dist
│   │   │   ├── index.cjs
│   │   │   ├── index.d.cts
│   │   │   ├── index.d.ts
│   │   │   └── index.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   └── README.md
│   ├── tinyexec
│   │   ├── dist
│   │   │   ├── main.cjs
│   │   │   ├── main.d.cts
│   │   │   ├── main.d.ts
│   │   │   └── main.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   └── README.md
│   ├── tinypool
│   │   ├── dist
│   │   │   ├── common-Qw-RoVFD.js
│   │   │   ├── entry
│   │   │   │   ├── process.d.ts
│   │   │   │   ├── process.js
│   │   │   │   ├── utils.d.ts
│   │   │   │   ├── utils.js
│   │   │   │   ├── worker.d.ts
│   │   │   │   └── worker.js
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── utils-B--2TaWv.js
│   │   │   └── utils-De75vAgL.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   └── README.md
│   ├── tinyrainbow
│   │   ├── dist
│   │   │   ├── browser.d.ts
│   │   │   ├── browser.js
│   │   │   ├── chunk-BVHSVHOK.js
│   │   │   ├── index-c1cfc5e9.d.ts
│   │   │   ├── node.d.ts
│   │   │   └── node.js
│   │   ├── LICENCE
│   │   ├── package.json
│   │   └── README.md
│   ├── tinyspy
│   │   ├── dist
│   │   │   ├── index.cjs
│   │   │   ├── index.d.cts
│   │   │   ├── index.d.ts
│   │   │   └── index.js
│   │   ├── LICENCE
│   │   ├── package.json
│   │   └── README.md
│   ├── @types
│   │   └── estree
│   │       ├── flow.d.ts
│   │       ├── index.d.ts
│   │       ├── LICENSE
│   │       ├── package.json
│   │       └── README.md
│   ├── uc.micro
│   │   ├── build
│   │   │   └── index.cjs.js
│   │   ├── categories
│   │   │   ├── Cc
│   │   │   │   └── regex.mjs
│   │   │   ├── Cf
│   │   │   │   └── regex.mjs
│   │   │   ├── P
│   │   │   │   └── regex.mjs
│   │   │   ├── S
│   │   │   │   └── regex.mjs
│   │   │   └── Z
│   │   │       └── regex.mjs
│   │   ├── index.mjs
│   │   ├── LICENSE.txt
│   │   ├── package.json
│   │   ├── properties
│   │   │   └── Any
│   │   │       └── regex.mjs
│   │   └── README.md
│   ├── vite
│   │   ├── bin
│   │   │   ├── openChrome.applescript
│   │   │   └── vite.js
│   │   ├── client.d.ts
│   │   ├── dist
│   │   │   ├── client
│   │   │   │   ├── client.mjs
│   │   │   │   └── env.mjs
│   │   │   ├── node
│   │   │   │   ├── chunks
│   │   │   │   │   ├── dep-D-7KCb9p.js
│   │   │   │   │   ├── dep-D_zLpgQd.js
│   │   │   │   │   ├── dep-e9kYborm.js
│   │   │   │   │   ├── dep-IQS-Za7F.js
│   │   │   │   │   └── dep-YkMKzX4u.js
│   │   │   │   ├── cli.js
│   │   │   │   ├── constants.js
│   │   │   │   ├── index.d.ts
│   │   │   │   ├── index.js
│   │   │   │   ├── runtime.d.ts
│   │   │   │   ├── runtime.js
│   │   │   │   └── types.d-aGj9QkWt.d.ts
│   │   │   └── node-cjs
│   │   │       └── publicUtils.cjs
│   │   ├── index.cjs
│   │   ├── index.d.cts
│   │   ├── LICENSE.md
│   │   ├── package.json
│   │   ├── README.md
│   │   └── types
│   │       ├── customEvent.d.ts
│   │       ├── hmrPayload.d.ts
│   │       ├── hot.d.ts
│   │       ├── importGlob.d.ts
│   │       ├── import-meta.d.ts
│   │       ├── importMeta.d.ts
│   │       ├── metadata.d.ts
│   │       └── package.json
│   ├── vite-node
│   │   ├── dist
│   │   │   ├── chunk-browser.cjs
│   │   │   ├── chunk-browser.mjs
│   │   │   ├── chunk-hmr.cjs
│   │   │   ├── chunk-hmr.mjs
│   │   │   ├── cli.cjs
│   │   │   ├── cli.d.ts
│   │   │   ├── client.cjs
│   │   │   ├── client.d.ts
│   │   │   ├── client.mjs
│   │   │   ├── cli.mjs
│   │   │   ├── constants.cjs
│   │   │   ├── constants.d.ts
│   │   │   ├── constants.mjs
│   │   │   ├── hmr.cjs
│   │   │   ├── hmr.d.ts
│   │   │   ├── hmr.mjs
│   │   │   ├── index.cjs
│   │   │   ├── index.d.ts
│   │   │   ├── index.mjs
│   │   │   ├── index-z0R8hVRu.d.ts
│   │   │   ├── server.cjs
│   │   │   ├── server.d.ts
│   │   │   ├── server.mjs
│   │   │   ├── source-map.cjs
│   │   │   ├── source-map.d.ts
│   │   │   ├── source-map.mjs
│   │   │   ├── trace-mapping.d-DLVdEqOp.d.ts
│   │   │   ├── types.cjs
│   │   │   ├── types.d.ts
│   │   │   ├── types.mjs
│   │   │   ├── utils.cjs
│   │   │   ├── utils.d.ts
│   │   │   └── utils.mjs
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── vite-node.mjs
│   ├── @vitest
│   │   ├── expect
│   │   │   ├── dist
│   │   │   │   ├── chai.d.cts
│   │   │   │   ├── index.d.ts
│   │   │   │   └── index.js
│   │   │   ├── index.d.ts
│   │   │   ├── LICENSE
│   │   │   ├── package.json
│   │   │   └── README.md
│   │   ├── mocker
│   │   │   ├── dist
│   │   │   │   ├── auto-register.d.ts
│   │   │   │   ├── auto-register.js
│   │   │   │   ├── browser.d.ts
│   │   │   │   ├── browser.js
│   │   │   │   ├── chunk-interceptor-native.js
│   │   │   │   ├── chunk-mocker.js
│   │   │   │   ├── chunk-pathe.ff20891b.js
│   │   │   │   ├── chunk-registry.js
│   │   │   │   ├── chunk-utils.js
│   │   │   │   ├── index.d.ts
│   │   │   │   ├── index.js
│   │   │   │   ├── mocker-pQgp1HFr.d.ts
│   │   │   │   ├── node.d.ts
│   │   │   │   ├── node.js
│   │   │   │   ├── redirect.d.ts
│   │   │   │   ├── redirect.js
│   │   │   │   ├── register.d.ts
│   │   │   │   ├── register.js
│   │   │   │   └── types-DZOqTgiN.d.ts
│   │   │   ├── LICENSE
│   │   │   ├── package.json
│   │   │   └── README.md
│   │   ├── pretty-format
│   │   │   ├── dist
│   │   │   │   ├── index.d.ts
│   │   │   │   └── index.js
│   │   │   ├── LICENSE
│   │   │   └── package.json
│   │   ├── runner
│   │   │   ├── dist
│   │   │   │   ├── chunk-tasks.js
│   │   │   │   ├── index.d.ts
│   │   │   │   ├── index.js
│   │   │   │   ├── tasks-3ZnPj1LR.d.ts
│   │   │   │   ├── types.d.ts
│   │   │   │   ├── types.js
│   │   │   │   ├── utils.d.ts
│   │   │   │   └── utils.js
│   │   │   ├── LICENSE
│   │   │   ├── package.json
│   │   │   ├── README.md
│   │   │   ├── types.d.ts
│   │   │   └── utils.d.ts
│   │   ├── snapshot
│   │   │   ├── dist
│   │   │   │   ├── environment-Ddx0EDtY.d.ts
│   │   │   │   ├── environment.d.ts
│   │   │   │   ├── environment.js
│   │   │   │   ├── index.d.ts
│   │   │   │   ├── index.js
│   │   │   │   ├── manager.d.ts
│   │   │   │   ├── manager.js
│   │   │   │   └── rawSnapshot-CPNkto81.d.ts
│   │   │   ├── environment.d.ts
│   │   │   ├── LICENSE
│   │   │   ├── manager.d.ts
│   │   │   ├── package.json
│   │   │   └── README.md
│   │   ├── spy
│   │   │   ├── dist
│   │   │   │   ├── index.d.ts
│   │   │   │   └── index.js
│   │   │   ├── LICENSE
│   │   │   ├── package.json
│   │   │   └── README.md
│   │   └── utils
│   │       ├── diff.d.ts
│   │       ├── dist
│   │       │   ├── chunk-_commonjsHelpers.js
│   │       │   ├── diff.d.ts
│   │       │   ├── diff.js
│   │       │   ├── error.d.ts
│   │       │   ├── error.js
│   │       │   ├── helpers.d.ts
│   │       │   ├── helpers.js
│   │       │   ├── index.d.ts
│   │       │   ├── index.js
│   │       │   ├── source-map.d.ts
│   │       │   ├── source-map.js
│   │       │   ├── types-Bxe-2Udy.d.ts
│   │       │   ├── types.d.ts
│   │       │   └── types.js
│   │       ├── error.d.ts
│   │       ├── helpers.d.ts
│   │       ├── LICENSE
│   │       └── package.json
│   ├── vitest
│   │   ├── browser.d.ts
│   │   ├── config.d.ts
│   │   ├── coverage.d.ts
│   │   ├── dist
│   │   │   ├── browser.d.ts
│   │   │   ├── browser.js
│   │   │   ├── chunks
│   │   │   │   ├── base.BZZh4cSm.js
│   │   │   │   ├── benchmark.Cdu9hjj4.js
│   │   │   │   ├── benchmark.geERunq4.d.ts
│   │   │   │   ├── cac.CB_9Zo9Q.js
│   │   │   │   ├── cli-api.DqsSTaIi.js
│   │   │   │   ├── _commonjsHelpers.BFTU3MAI.js
│   │   │   │   ├── config.Cy0C388Z.d.ts
│   │   │   │   ├── console.BYGVloWk.js
│   │   │   │   ├── constants.fzPh7AOq.js
│   │   │   │   ├── coverage.BoMDb1ip.js
│   │   │   │   ├── creator.IIqd8RWT.js
│   │   │   │   ├── date.W2xKR2qe.js
│   │   │   │   ├── environment.LoooBwUu.d.ts
│   │   │   │   ├── execute.2pr0rHgK.js
│   │   │   │   ├── git.B5SDxu-n.js
│   │   │   │   ├── globals.D8ZVAdXd.js
│   │   │   │   ├── index.68735LiX.js
│   │   │   │   ├── index.BJDntFik.js
│   │   │   │   ├── index.ckWaX2gY.js
│   │   │   │   ├── index.CqYx2Nsr.js
│   │   │   │   ├── index.DsZFoqi9.js
│   │   │   │   ├── index.K90BXFOx.js
│   │   │   │   ├── index.nEwtF0bu.js
│   │   │   │   ├── inspector.70d6emsh.js
│   │   │   │   ├── mocker.cRtM890J.d.ts
│   │   │   │   ├── node.AKq966Jp.js
│   │   │   │   ├── RandomSequencer.CMRlh2v4.js
│   │   │   │   ├── reporters.nr4dxCkA.d.ts
│   │   │   │   ├── resolveConfig.rBxzbVsl.js
│   │   │   │   ├── rpc.C3q9uwRX.js
│   │   │   │   ├── runBaseTests.3qpJUEJM.js
│   │   │   │   ├── run-once.2ogXb3JV.js
│   │   │   │   ├── setup-common.Dj6BZI3u.js
│   │   │   │   ├── spy.Cf_4R5Oe.js
│   │   │   │   ├── suite.B2jumIFP.d.ts
│   │   │   │   ├── utils.C8RiOc4B.js
│   │   │   │   ├── utils.Cn0zI1t3.js
│   │   │   │   ├── utils.DNoFbBUZ.js
│   │   │   │   ├── vi.DgezovHB.js
│   │   │   │   ├── vite.CzKp4x9w.d.ts
│   │   │   │   ├── vm.Zr4qWzDJ.js
│   │   │   │   ├── worker.B9FxPCaC.d.ts
│   │   │   │   └── worker.tN5KGIih.d.ts
│   │   │   ├── cli.js
│   │   │   ├── config.cjs
│   │   │   ├── config.d.ts
│   │   │   ├── config.js
│   │   │   ├── coverage.d.ts
│   │   │   ├── coverage.js
│   │   │   ├── environments.d.ts
│   │   │   ├── environments.js
│   │   │   ├── execute.d.ts
│   │   │   ├── execute.js
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── mocker.d.ts
│   │   │   ├── mocker.js
│   │   │   ├── node.d.ts
│   │   │   ├── node.js
│   │   │   ├── path.js
│   │   │   ├── reporters.d.ts
│   │   │   ├── reporters.js
│   │   │   ├── runners.d.ts
│   │   │   ├── runners.js
│   │   │   ├── snapshot.d.ts
│   │   │   ├── snapshot.js
│   │   │   ├── spy.js
│   │   │   ├── suite.d.ts
│   │   │   ├── suite.js
│   │   │   ├── utils.d.ts
│   │   │   ├── utils.js
│   │   │   ├── worker.js
│   │   │   ├── workers
│   │   │   │   ├── forks.js
│   │   │   │   ├── runVmTests.js
│   │   │   │   ├── threads.js
│   │   │   │   ├── vmForks.js
│   │   │   │   └── vmThreads.js
│   │   │   ├── workers.d.ts
│   │   │   └── workers.js
│   │   ├── environments.d.ts
│   │   ├── execute.d.ts
│   │   ├── globals.d.ts
│   │   ├── import-meta.d.ts
│   │   ├── importMeta.d.ts
│   │   ├── index.cjs
│   │   ├── index.d.cts
│   │   ├── jsdom.d.ts
│   │   ├── LICENSE.md
│   │   ├── mocker.d.ts
│   │   ├── node.d.ts
│   │   ├── package.json
│   │   ├── README.md
│   │   ├── reporters.d.ts
│   │   ├── runners.d.ts
│   │   ├── snapshot.d.ts
│   │   ├── suite.d.ts
│   │   ├── suppress-warnings.cjs
│   │   ├── utils.d.ts
│   │   ├── vitest.mjs
│   │   └── workers.d.ts
│   ├── which
│   │   ├── bin
│   │   │   └── node-which
│   │   ├── CHANGELOG.md
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── which.js
│   ├── why-is-node-running
│   │   ├── cli.js
│   │   ├── example.js
│   │   ├── include.js
│   │   ├── index.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   └── README.md
│   ├── wrap-ansi
│   │   ├── index.d.ts
│   │   ├── index.js
│   │   ├── license
│   │   ├── package.json
│   │   └── readme.md
│   └── wrap-ansi-cjs
│       ├── index.js
│       ├── license
│       ├── node_modules
│       │   ├── ansi-regex
│       │   │   ├── index.d.ts
│       │   │   ├── index.js
│       │   │   ├── license
│       │   │   ├── package.json
│       │   │   └── readme.md
│       │   ├── ansi-styles
│       │   │   ├── index.d.ts
│       │   │   ├── index.js
│       │   │   ├── license
│       │   │   ├── package.json
│       │   │   └── readme.md
│       │   ├── emoji-regex
│       │   │   ├── es2015
│       │   │   │   ├── index.js
│       │   │   │   └── text.js
│       │   │   ├── index.d.ts
│       │   │   ├── index.js
│       │   │   ├── LICENSE-MIT.txt
│       │   │   ├── package.json
│       │   │   ├── README.md
│       │   │   └── text.js
│       │   ├── string-width
│       │   │   ├── index.d.ts
│       │   │   ├── index.js
│       │   │   ├── license
│       │   │   ├── package.json
│       │   │   └── readme.md
│       │   └── strip-ansi
│       │       ├── index.d.ts
│       │       ├── index.js
│       │       ├── license
│       │       ├── package.json
│       │       └── readme.md
│       ├── package.json
│       └── readme.md
├── package.json
├── package-lock.json
├── Protocols
│   ├── Amenti_SoulReturn.key
│   ├── DemonicReintegration.log
│   ├── RRR_Protocol.yml
│   └── Silence_Contemplation_Mode.json
├── Races_And_Realms
│   ├── Emerald_Order.md
│   ├── Guardian_Alliance.md
│   ├── README.md
│   ├── SECURITY.md
│   ├── Turaneusiam.md
│   ├── Zeta.md
│   └── Zionite.md
├── README.md
├── Sentinel-Framework
├── Sigils
│   └── Smitten_Sigil.svg
├── site
│   ├── assets
│   │   ├── everlightos-banner-1280x360.png
│   │   ├── everlightos-banner-1920x480.png
│   │   └── everlightos-banner-640x240.png
│   ├── data
│   │   └── council.json
│   ├── everlightos_logo.png
│   ├── index.html
│   ├── js
│   │   ├── bridgezone.js
│   │   ├── dashboard.js
│   │   ├── federation.js
│   │   └── memoryvault.js
│   └── style.css
├── tmp_baseline_out.json
└── zip_archives
    ├── EverLightOS_scaffold.zip
    ├── EverLight_Restore_Page-main.zip
    └── everlight-space-main.zip

375 directories, 5751 files
