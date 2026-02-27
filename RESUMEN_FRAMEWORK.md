# RESUMEN: FRAMEWORK FÁBRICA IA DEVELOPMENT

---

## 1. ESTRUCTURA DEL EQUIPO (20 personas)

| Grupo | Personas | Enfoque |
|-------|----------|----------|
| Steering Committee | 3 | CIO + PO + Tech Lead |
| Equipo Frontend | 7 | React + Tailwind + Zustand |
| Equipo Backend | 7 | .NET 9 + Clean Architecture |
| Equipo IA | 3 | Python + CrewAI + FastAPI |

---

## 2. STACK TECNOLÓGICO

| Capa | Tecnología |
|-------|------------|
| Frontend | React 19 + TypeScript + Tailwind 4 + Zustand |
| Backend | .NET 9 + C# 13 + EF Core 9 + PostgreSQL 17 |
| IA | Python 3.12 + FastAPI + CrewAI + LangChain |
| BD | PostgreSQL 17 (Flexible) con pgvector |
| Cloud | Azure (App Service, PostgreSQL Flexible, OpenAI) |

---

## 3. AGENTES IA (CrewAI)

| Agente | Función |
|--------|---------|
| Requirements Agent | Transforma necesidades en requisitos |
| Planning Agent | Crea plan de desarrollo |
| Architecture Agent | Propone arquitectura |
| Code Agent | Genera código |
| Test Agent | Crea pruebas |
| Security Agent | Analiza vulnerabilidades |
| Deployment Agent | Despliega a Azure |

---

## 4. FLUJO DE TRABAJO

```
PO dice necesidad
        ↓
Requirements Agent → GitHub Issue (Módulo)
        ↓
Equipo toma Issue → Código → PR → Review → Merge → Deploy
        ↓
Siguiente Issue
```

---

## 5. MÓDULOS (8 Issues en GitHub)

| # | Módulo | Entregable |
|---|--------|------------|
| 1 | Auth + DB | Login, JWT, PostgreSQL |
| 2 | Empleados | CRUD completo |
| 3 | Cursos | Catálogo |
| 4 | Matrículas/Certifs | Núcleo del sistema |
| 5 | Dashboards | Reportes |
| 6 | IA Agents | Automatización |
| 7 | Constancias | PDFs + Notif. |
| 8 | Deploy | Producción |

---

## 6. GITHUB

- **1 Repo principal**: `ai-factory-hackathon`
- **4 Carpetas**: frontend, backend, ia-service, infrastructure
- **8 Issues**: Uno por módulo
- **3 Milestones**: Sprint 1, Sprint 2, Sprint Final

---

## 7. CRONOGRAMA (1 día)

| Hora | Actividad |
|------|-----------|
| 9:00-10:30 | Sprint 1: Setup + Módulos 1-3 |
| 10:30-12:30 | Módulos 4-5 |
| 12:30-13:30 | Lunch |
| 13:30-15:30 | Módulos 6-7 |
| 15:30-16:00 | Deploy + Demo |

---

## 8. ARQUITECTURA

```
┌─────────────────────────────────────┐
│         FRONTEND (React 19)        │
│         Zustand + Tailwind         │
└──────────────┬──────────────────────┘
               │ REST API
┌──────────────▼──────────────────────┐
│         BACKEND (.NET 9)           │
│    Clean Architecture + CQRS       │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│      DATABASE (PostgreSQL 17)      │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│       IA SERVICE (Python 3.12)     │
│         CrewAI + FastAPI           │
│        Azure OpenAI                │
└─────────────────────────────────────┘
```

---

## 9. COSTOS

| Recurso | Costo Hackathon | Costo Mensual |
|---------|-----------------|---------------|
| Azure (todo) | ~$5-10 | ~$260-350 |
| GitHub | $0 | $0 |
| Claude/Copilot | $0 ( trial) | ~$20 |

---

## 10. HERRAMIENTAS POR ROL

| Rol | Herramienta |
|-----|-------------|
| Desarrollador | VS Code + Copilot + Claude Code |
| Backend | .NET 9 SDK + EF Core |
| Frontend | Node.js + Vite + npm |
| IA | Python 3.12 + CrewAI |
| Infra | Azure CLI + Terraform |
| Revisión | GitHub PRs |

---

## RESUMEN VISUAL

```
GITHUB (8 Issues) → EQUIPOS (4 grupos) → CÓDIGO → AZURE

    PO → Requirements Agent → Issue → Build → Deploy
                                   ↑
                              Claude/Copilot
```

---

**En 3 palabras**: Equipos + Agentes + Azure
