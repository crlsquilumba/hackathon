# 🔄 CICLO DE VIDA DE DESARROLLO CON IA: MARCOS REALES Y VALIDADOS

## FUENTES REALES

> **Arthur.ai ADLC** - https://www.arthur.ai/blog/introducing-adlc  
> **AWS AI-DLC** - https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/  
> **InfoQ** - https://www.infoq.com/articles/prompts-to-production-playbook-for-agentic-development/

---

# PARTE 1: SDLC TRADICIONAL (Modelo Clásico)

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                           SDLC TRADICIONAL                                                  │
│   Requirements → Design → Implementation → Testing → Deployment → Maintenance             │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
    │   1.     │    │   2.     │    │   3.     │    │   4.     │    │   5.     │    │   6.     │
    │REQUISITES│───▶│  DESIGN  │───▶│IMPLEMENT │───▶│  TESTING │───▶│ DEPLOY   │───▶│MAINTENANCE│
    └──────────┘    └──────────┘    └──────────┘    └──────────┘    └──────────┘    └──────────┘
         │              │              │              │              │              │
         ▼              ▼              ▼              ▼              ▼              ▼
    - Business     - Arquitectura   - Código      - Unit tests   - CI/CD       - Bug fixes
      analysis     - UML           - Backend     - Integration  - Prod       - Updates
    - User stories - DB design     - Frontend    - E2E          - Monitoring  - Support
    - BRD         - APIs            - DevOps      - QA Manual    - Rollback

    ⏱️ Duración típica: 3-6 meses
    👥 Equipo: PO, PM, Lead, Arq, Devs, QA, DevOps
```

---

# PARTE 2: AGENT DEVELOPMENT LIFECYCLE (ADLC) - Arthur.ai

**Fuente:** https://www.arthur.ai/blog/introducing-adlc

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                    AGENT DEVELOPMENT LIFECYCLE (ADLC)                                       │
│                 Planning → Flywheel (Tuning) → Governance                                  │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

                         ┌─────────────────────────────────────────────────────────────────┐
                         │                    PHASE 1: PLANNING                           │
                         │              🤝 Planning & Initial Implementation               │
                         └─────────────────────────────────────────────────────────────────┘
                                                  │
                    ┌─────────────────────────────┼─────────────────────────────┐
                    ▼                             ▼                             ▼
            ┌──────────────┐              ┌──────────────┐              ┌──────────────┐
            │Align on      │              │Connect agent │              │Set up        │
            │outcomes &    │              │to real       │              │observability │
            │KPIs         │              │systems/data  │              │& tracing     │
            └──────────────┘              └──────────────┘              └──────────────┘
                    │                             │                             │
                    └─────────────────────────────┼─────────────────────────────┘
                                                  ▼
                         ┌─────────────────────────────────────────────────────────────────┐
                         │              PHASE 2: THE AGENT DEVELOPMENT FLYWHEEL          │
                         │                        ❤️ CORAZÓN DEL ADLC                      │
                         └─────────────────────────────────────────────────────────────────┘
                                                  │
        ┌────────────────────────────────────────┼────────────────────────────────────────┐
        │                                        │                                        │
        ▼                                        ▼                                        ▼
┌───────────────────┐                ┌───────────────────┐                ┌───────────────────┐
│ 1. LIVE &         │                │ 2. IDENTIFY      │                │ 3. ENHANCE       │
│    SIMULATED      │──────▶         │    FAILURE       │──────▶         │    BEHAVIORAL    │
│    USAGE          │                │    MODES         │                │    SUITES        │
│                   │                │                  │                │    & EVALS       │
│ - Internal tests  │                │ - Brittle prompts│                │                  │
│ - Pilots          │                │ - Unpredictable  │                │ - Add edge cases │
│ - Production      │                │   retrievals     │                │ - Regression     │
│ - Stress testing  │                │ - Fragile        │                │   testing       │
│                   │                │   orchestration  │                │                  │
└───────────────────┘                └───────────────────┘                └───────────────────┘
        │                                        │                                        │
        └────────────────────────────────────────┼────────────────────────────────────────┘
                                                  ▼
                                        ┌───────────────────┐
                                        │ 4. EXPERIMENT    │
                                        │    & IMPROVE     │
                                        │                   │
                                        │ - Prompt tuning  │
                                        │ - Context opt    │
                                        │ - New tools      │
                                        │ - A/B testing    │
                                        └───────────────────┘
                                                  │
                                                  └──────────┬─────────────┬──────────────┘
                                                             │             │
                                                             ▼             ▼
                                                 ┌───────────────────┐  ┌───────────────────┐
                                                 │Did reasoning      │  │Did business KPIs  │
                                                 │quality improve?   │  │move?              │
                                                 └───────────────────┘  └───────────────────┘
                                                  │
                                                  ▼
                         ┌─────────────────────────────────────────────────────────────────┐
                         │                    PHASE 3: AGENTIC GOVERNANCE                   │
                         │                         🛡️ GOBIERNO                                │
                         └─────────────────────────────────────────────────────────────────┘
                                                  │
                    ┌─────────────────────────────┼─────────────────────────────┐
                    ▼                             ▼                             ▼
            ┌──────────────┐              ┌──────────────┐              ┌──────────────┐
            │Ensure        │              │Communicate   │              │Automatically │
            │adherence     │              │KPIs to       │              │detect &      │
            │to policy    │              │stakeholders  │              │escalate      │
            │(expected    │              │               │              │performance   │
            │behaviors)   │              │               │              │concerns      │
            └──────────────┘              └──────────────┘              └──────────────┘
```

---

# PARTE 3: AI-DRIVEN DEVELOPMENT LIFECYCLE (AI-DLC) - AWS

**Fuente:** https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                    AI-DRIVEN DEVELOPMENT LIFECYCLE (AI-DLC) - AWS                           │
│                    Inception → Construction → Operations                                   │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

    ┌───────────────────────────────────────────────────────────────────────────────────────┐
    │                           MODELO MENTAL: AI CREA-PREGUNTA-VALIDA                     │
    │                                                                                       │
    │        AI CREA PLAN            IA PREGUNTA           HUMANO VALIDA                   │
    │            │                        │                      │                          │
    │            ▼                        ▼                      ▼                          │
    │     ┌──────────┐            ┌──────────┐           ┌──────────┐                   │
    │     │  AI      │──────▶     │  AI      │──────▶    │  HUMAN   │──────▶              │
    │     │ creates  │            │ seeks    │           │ makes    │                   │
    │     │  plan    │            │clarifica-│           │ critical │                   │
    │     │          │            │  tion    │           │ decisions│                   │
    │     └──────────┘            └──────────┘           └──────────┘                   │
    │                                                                                       │
    │    Este patrón se REPITE en CADA ACTIVIDAD del SDLC                                  │
    └───────────────────────────────────────────────────────────────────────────────────────┘

    ┌───────────────────────────────────────────────────────────────────────────────────────┐
    │  FASE 1: INCEPTION (Inicio)                                                          │
    │  "Mob Elaboration" - Todo el equipo valida preguntas y propuestas de IA              │
    └───────────────────────────────────────────────────────────────────────────────────────┘
    
         ┌────────────────────────────────────────────────────────────────────────────┐
         │ AI TRANSFORMA: Business Intent → Requisitos detallados → Historias        │
         └────────────────────────────────────────────────────────────────────────────┘
                                          │
         ┌────────────────────────────────┴───────────────────────────────────────────┐
         │                         ACTIVIDADES                                       │
         │  ┌────────────────┐    ┌────────────────┐    ┌────────────────┐          │
         │  │ Requirement    │    │ User Stories   │    │ Acceptance    │          │
         │  │ Analysis       │    │ Generation     │    │ Criteria      │          │
         │  │ (AI-driven)   │    │ (AI-assisted)  │    │ Definition    │          │
         │  └────────────────┘    └────────────────┘    └────────────────┘          │
         │         │                    │                     │                      │
         │         └────────────────────┼─────────────────────┘                      │
         │                              ▼                                              │
         │                    🤝 MOB ELABORATION                                       │
         │              (Equipo valida preguntas y propuestas de IA)                  │
         └────────────────────────────────────────────────────────────────────────────┘
                                          │
                                          ▼
    ┌───────────────────────────────────────────────────────────────────────────────────────┐
    │  FASE 2: CONSTRUCTION (Construcción)                                              │
    │  "Mob Construction" - Equipo proporciona clarificaciones en tiempo real          │
    └───────────────────────────────────────────────────────────────────────────────────────┘

         ┌────────────────────────────────────────────────────────────────────────────┐
         │ AI PROPONE: Arquitectura → Modelos de dominio → Código → Tests          │
         └────────────────────────────────────────────────────────────────────────────┘
                                          │
         ┌────────────────────────────────┴───────────────────────────────────────────┐
         │                         ACTIVIDADES                                       │
         │  ┌────────────────┐    ┌────────────────┐    ┌────────────────┐          │
         │  │ Architecture   │    │ Code           │    │ Test          │          │
         │  │ Proposal       │    │ Generation     │    │ Generation    │          │
         │  │ (AI-driven)    │    │ (AI-driven)    │    │ (AI-assisted) │          │
         │  └────────────────┘    └────────────────┘    └────────────────┘          │
         │         │                    │                     │                      │
         │         └────────────────────┼─────────────────────┘                      │
         │                              ▼                                              │
         │                    🤝 MOB CONSTRUCTION                                     │
         │         (Equipo da clarificaciones sobre decisiones técnicas)             │
         └────────────────────────────────────────────────────────────────────────────┘
                                          │
                                          ▼
    ┌───────────────────────────────────────────────────────────────────────────────────────┐
    │  FASE 3: OPERATIONS (Operaciones)                                                   │
    │  AI gestiona infraestructura como código y despliegues                             │
    └───────────────────────────────────────────────────────────────────────────────────────┘

         ┌────────────────────────────────────────────────────────────────────────────┐
         │ AI APLICA: Contexto acumulado → IaC → Despliegues                       │
         └────────────────────────────────────────────────────────────────────────────┘
                                          │
         ┌────────────────────────────────┴───────────────────────────────────────────┐
         │                         ACTIVIDADES                                       │
         │  ┌────────────────┐    ┌────────────────┐    ┌────────────────┐          │
         │  │ Infrastructure │    │ CI/CD          │    │ Monitoring     │          │
         │  │ as Code       │    │ Pipeline       │    │ & Alerts       │          │
         │  │ (AI-assisted) │    │ (AI-assisted)  │    │ (AI-assisted)  │          │
         │  └────────────────┘    └────────────────┘    └────────────────┘          │
         └────────────────────────────────────────────────────────────────────────────┘

    ┌───────────────────────────────────────────────────────────────────────────────────────┐
    │                           CONCEPTOS CLAVE AI-DLC                                    │
    │                                                                                       │
    │  ⚡ BOLTS (vs Sprints) - Ciclos más cortos, intensidad alta, medidos en horas      │
    │  📦 UNITS OF WORK (vs Epics) - Unidades de trabajo más granulares                  │
    │  💾 PERSISTENT CONTEXT - AI guarda y mantiene contexto entre fases                │
    │  🤝 HUMAN-IN-TLOOP - Humano valida en puntos críticos                              │
    └───────────────────────────────────────────────────────────────────────────────────────┘
```

---

# PARTE 4: COMPARATIVA REAL

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                    COMPARATIVA: SDLC vs ADLC vs AI-DLC                                    │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────┬─────────────────┬─────────────────┬─────────────────┐
│              CARACTERÍSTICA                  │  SDLC TRADICIONAL│  ADLC (Arthur)  │  AI-DLC (AWS)  │
├──────────────────────────────────────────────┼─────────────────┼─────────────────┼─────────────────┤
│ ENFOQUE PRINCIPAL                           │ Determinístico  │ Probabilístico  │ Colaborativo    │
│                                              │                 │                 │                 │
│ PLANIFICACIÓN                               │ 2-4 semanas     │ 1-2 días        │ 1-2 horas       │
│                                             │                 │                 │                 │
│ DISEÑO                                      │ Documentos      │ Baseline        │ Mob Elaboration │
│                                             │ extensivos      │ behaviors       │ (equipo completo)│
│                                             │                 │                 │                 │
│ DESARROLLO                                  │ Developers      │ Code Agent      │ AI + Human      │
│                                             │ escriben 100%    │ genera 80%      │ Collaboration   │
│                                             │                 │                 │                 │
│ TESTING                                     │ QA manual +     │ Evals           │ AI genera       │
│                                             │ automatizado     │ automatizados   │ tests           │
│                                             │                 │                 │                 │
│ GOBIERNO                                    │ Reviews         │ Automated       │ Policy          │
│                                             │ humanos         │ governance      │ enforcement     │
│                                             │                 │                 │                 │
│ ITERACIÓN                                   │ Semanas         │ Flywheel        │ Bolts           │
│                                             │                 │ (horas/días)    │ (horas)         │
│                                             │                 │                 │                 │
│ CONTEXTO                                    │ Se pierde       │ Acumulado      │ Persistente     │
│                                             │ entre sprints   │ y refinado     │ entre fases     │
│                                             │                 │                 │                 │
│ DECISIONES                                  │ Humanos         │ Humanos         │ Humanos         │
│                                             │ solos           │ (con IA info)  │ (AI pregunta)   │
│                                             │                 │                 │                 │
│ DURACIÓN PROYECTO (Medio)                   │ 3-6 meses       │ 2-4 semanas     │ 1-2 semanas     │
│                                             │                 │                 │                 │
│ ROL DEL HUMANO                              │ Creador         │ Supervisor      │ Colaborador     │
│                                             │                 │ + Validator     │ + Validador     │
└──────────────────────────────────────────────┴─────────────────┴─────────────────┴─────────────────┘
```

---

# PARTE 5: MAPEO DEL HACKATHON A LOS FRAMEWORKS REALES

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│              CÓMO TU HACKATHON SE MAPEA A LOS FRAMEWORKS REALES                           │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────────────────────────────────────────────┐
│                           TU HACKATHON (6 horas)                                         │
└───────────────────────────────────────────────────────────────────────────────────────────┘

    HORA    FASE HACKATHON          ║  ADLC (Arthur.ai)      ║  AI-DLC (AWS)              │
    ────    ─────────────           ║  ──────────────────    ║  ──────────────────────    │
                                                                                            
    9:00    SETUP                   ║  Planning:             ║  Inception:               │
    │       - Configurar CrewAI     ║  - Setup observability ║  - Connect to systems     │
    │       - API Keys Azure        ║  - Set up baseline     ║  - Define KPIs            │
    │       - GitHub repo           ║    behavioral suite    ║  - Align outcomes         │
    │                              ║                         ║                            │
    9:30    REQUISITOS             ║                         ║                            │
    │       - PO define besoin     ║  Planning:             ║  Inception:               │
    │       - Requirements Agent   ║  - Requirements Agent  ║  - AI transforms intent   │
    │         extrae historias     ║    creates stories     ║    to detailed reqs      │
    │       - Backlog creado       ║                         ║                            │
    │                              ║                         ║  🤝 Mob Elaboration:      │
    │                              ║                         ║  Team validates AI        │
    │                              ║                         ║    questions              │
    │                              ║                         ║                            │
    10:00   PLANIFICACIÓN          ║                         ║                            │
    │       - Planning Agent       ║  Planning:             ║  Inception:               │
    │         crea roadmap         ║  - Planning Agent      ║  - AI creates plan        │
    │       - Estimación tareas   ║    defines tasks       ║  - AI seeks clarification │
    │                              ║                         ║                            │
    10:30   ARQUITECTURA           ║  ═══════════════════   ║  ═══════════════════════  │
    │       - Architecture Agent   ║      TRANSICIÓN        ║      TRANSICIÓN           │
    │         propone stack        ║      AL FLYWHEEL       ║      A CONSTRUCTION       │
    │       - Tech Lead approve   ║                         ║                            │
    │                              ║  Flywheel:             ║  Construction:            │
    │                              ║  1. Live/Simulated    ║  - AI proposes           │
    │                              ║     Usage              ║    architecture          │
    │                              ║                         ║                            │
    11:00   DESARROLLO             ║                         ║                            │
    │       - Code Generator      ║  Flywheel:             ║  Construction:           │
    │         Agent               ║  2. Identify Failure   ║  - AI generates code     │
    │       - Frontend/Backend   ║     Modes              ║  - Human clarifies       │
    │       - Iterar prompts      ║  3. Enhance Evals     ║    decisions             │
    │                              ║  4. Experiment        ║                            │
    │       🤝 HUMAN REVIEW        ║     & Improve         ║  🤝 Mob Construction:    │
    │         en cada paso        ║                         ║  Team guides AI          │
    │                              ║                         ║                            │
    12:30   LUNCH                  ║        (pausa)        ║       (pausa)             │
    │                              ║                         ║                            │
    13:30   TESTING                ║                         ║                            │
    │       - Test Agent          ║  Flywheel:             ║  Construction:           │
    │         genera tests        ║  - Testing Agent      ║  - AI generates tests    │
    │       - Security scan       ║    finds bugs         ║  - AI runs security      │
    │       - Fix Agent corrige   ║  - Fix Agent fixes    ║    scans                 │
    │                              ║                         ║                            │
    14:30   DESPLIEGUE            ║  ═══════════════════   ║  ═══════════════════════  │
    │       - Deployment Agent    ║      TRANSICIÓN        ║      TRANSICIÓN           │
    │       - Azure/App Service   ║      A GOVERNANCE      ║      A OPERATIONS         │
    │                              ║                         ║                            │
    │                              ║  Governance:           ║  Operations:             │
    │                              ║  - Policy adherence   ║  - AI manages IaC        │
    │                              ║  - KPIs reporting     ║  - AI handles deploy     │
    │                              ║  - Auto-escalation    ║  - Monitoring setup      │
    │                              ║                         ║                            │
    15:30   REVISIÓN               ║  Governance:           ║  Operations:             │
    │       - Review Agent        ║  - Final eval          ║  - Final validation      │
    │       - Métricas            ║  - KPIs measured       ║  - Demo to stakeholders  │
    │       - Lecciones           ║  - Lessons learned     ║  - Review metrics        │
    │                              ║                         ║                            │
    16:00   DEMO                   ║  Governance:           ║  Operations:             │
    │       - Presentación        ║  - Stakeholder         ║  - Show to committee     │
    │         al comité             │    communication       │  - Gather feedback       │
    └──────────────────────────────┴─────────────────────────┴──────────────────────────┘

    ═══════════════════════════════════════════════════════════════════════════════════════
                                    RESUMEN DEL MAPEO
    ═══════════════════════════════════════════════════════════════════════════════════════

    TU FASE HACKATHON              ║  CORRESPONDE A (Arthur)      ║  CORRESPONDE A (AWS)
    ─────────────────────          ║  ─────────────────────        ║  ─────────────────
    SETUP (30 min)                 ║  Planning                    ║  Inception
    REQUISITOS (1 hr)              ║  Planning                    ║  Inception + Mob Elaboration
    PLANIFICACIÓN (30 min)         ║  Planning                    ║  Inception
    ARQUITECTURA (30 min)          ║  Flywheel Step 1             ║  Construction + Mob Construction
    DESARROLLO (2 hr)              ║  Flywheel Steps 2-4         ║  Construction + Mob Construction
    TESTING (1 hr)                 ║  Flywheel Step 2             ║  Construction
    DESPLIEGUE (30 min)            ║  Governance                  ║  Operations
    REVISIÓN (30 min)              ║  Governance                  ║  Operations
```

---

# PARTE 6: DIAGRAMA INTEGRADO FINAL

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                    MARCO INTEGRADO: TU HACKATHON BASADO EN ESTÁNDARES REALES               │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

                        ┌──────────────────────────────────────────────────────┐
                        │                    🤖 AI                            │
                        │   (CrewAI + Azure OpenAI + Agents)                │
                        └──────────────────────────┬───────────────────────────┘
                                                   │
         ┌────────────────────────────────────────┼────────────────────────────────────────┐
         │                                        │                                        │
         ▼                                        ▼                                        ▼
┌─────────────────────┐                ┌─────────────────────┐                ┌─────────────────────┐
│   PLANIFICACIÓN     │                │   CONSTRUCCIÓN      │                │    OPERACIONES      │
│    (Arthur:         │                │    (Arthur:         │                │    (Arthur:         │
│    Planning)        │                │    Flywheel)        │                │    Governance)      │
│    AWS: Inception)  │                │    AWS: Construction)               │    AWS: Operations) │
└─────────────────────┘                └─────────────────────┘                └─────────────────────┘
         │                                        │                                        │
    ┌────┴────┐                             ┌────┴────┐                             ┌────┴────┐
    │         │                             │         │                             │         │
    ▼         ▼                             ▼         ▼                             ▼         ▼
┌───────┐ ┌───────┐                    ┌───────┐ ┌───────┐                    ┌───────┐ ┌───────┐
│Reqs   │ │Plan   │                    │Code   │ │Test   │                    │Deploy │ │Review │
│Agent  │ │Agent  │                    │Agent  │ │Agent  │                    │Agent  │ │Agent  │
└───┬───┘ └───┬───┘                    └───┬───┘ └───┬───┘                    └───┬───┘ └───┬───┘
    │         │                             │         │                             │         │
    └────┬────┘                             └────┬────┘                             └────┬────┘
         │                                        │                                        │
         ▼                                        ▼                                        ▼
    ┌──────────────────────────────────────────────────────────────────────────────────────┐
    │                           🤝 HUMANO (SUPERVISIÓN)                                    │
    │                                                                                       │
    │   PO: Valida requisitos    │   Tech Lead: Aprueba arquitectura  │  QA: Valida tests  │
    │   PM: Supervisa timeline   │   Dev: Revisa código               │  Lead: Aprueba     │
    │                            │   QA: Feedback inmediato            │    deploy           │
    └──────────────────────────────────────────────────────────────────────────────────────┘
         │                                        │                                        │
         └────────────────────────────────────────┼────────────────────────────────────────┘
                                                  ▼
                                        ┌─────────────────────┐
                                        │       OUTPUT        │
                                        │   MVP FUNCIONAL     │
                                        │   EN PRODUCCIÓN     │
                                        └─────────────────────┘

    ═══════════════════════════════════════════════════════════════════════════════════
                              FLUJO SEGÚN AWS AI-DLC
    ═══════════════════════════════════════════════════════════════════════════════════

    [AI crea plan] ──▶ [AI pregunta] ──▶ [Humano valida] ──▶ [AI implementa] ──▶ [Repite]

    Este patrón se aplica en CADA FASE del hackathon
```

---

## 📚 FUENTES

| Framework | Fuente | URL |
|-----------|--------|-----|
| **ADLC** | Arthur.ai | https://www.arthur.ai/blog/introducing-adlc |
| **AI-DLC** | AWS | https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/ |
| **Agentic Development** | InfoQ | https://www.infoq.com/articles/prompts-to-production-playbook-for-agentic-development/ |

---

## 🎯 CONCLUSIÓN

Tu hackathon sigue la estructura de **AWS AI-DLC** (Inception → Construction → Operations) con el **Flywheel de ADLC** (Arthur.ai) como método de mejora continua.

**La diferencia clave vs SDLC tradicional:**
- **Antes:** Humano crea → Humano revisa → Humano aprueba
- **Ahora:** IA crea → IA pregunta → Humano valida → IA implementa → IA itera

**Para el comité:** Esto no es inventado - AWS y Arthur.ai (entre otros) ya tienen metodologías formales documentadas y utilizadas en producción por empresas reales.
