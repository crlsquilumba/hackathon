# FRAMEWORK: ROLES, HERRAMIENTAS Y GITHUB

---

## 1. MAPA GENERAL

```
                    ┌─────────────────┐
                    │   GITHUB       │
                    │  (Repositorio) │
                    └────────┬────────┘
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
          ▼                  ▼                  ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│  ORCHESTRATOR   │ │  AGENTES IA     │ │  HUMANOS       │
│  (CrewAI)       │ │  (Automatizados)│ │  (Supervisan)  │
└────────┬────────┘ └────────┬────────┘ └────────┬────────┘
         │                   │                   │
         └───────────────────┼───────────────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   AZURE        │
                    │  (Infra + Deploy)
                    └─────────────────┘
```

---

## 2. ROLES HUMANOS + HERRAMIENTAS

| ROL | RESPONSABILIDAD | HERRAMIENTAS |
|-----|-----------------|--------------|
| **Product Owner** | Definir qué necesita el negocio | Slack, Navegador, GitHub (ver docs) |
| **Tech Lead** | Supervisar arquitectura, aprobar decisiones técnicas | VS Code, GitHub, Azure Portal |
| **Developer/QA** | Revisar calidad, ejecutar pruebas manuales | VS Code, Postman, GitHub Actions |

---

## 3. ROLES IA + HERRAMIENTAS

| AGENTE | RESPONSABILIDAD | USA HERRAMIENTAS |
|--------|-----------------|------------------|
| **Orchestrator** | Coordinar agentes | CrewAI, Azure OpenAI, Memory |
| **Requirements Agent** | Crear documentos | GPT-4, Mermaid, GitHub API |
| **Planning Agent** | Crear plan de desarrollo | GPT-4, GitHub Issues API |
| **Architecture Agent** | Proponer stack tecnológico | GPT-4, Terraform, Docker |
| **Code Agent** | Generar código fuente | GPT-4, VS Code, GitHub API |
| **Test Agent** | Generar y ejecutar pruebas | Pytest, Playwright, GitHub Actions |
| **Security Agent** | Analizar seguridad | Semgrep, Bandit |
| **Deployment Agent** | Desplegar a Azure | Azure CLI, Terraform, GitHub Actions |

---

## 4. INTEGRACIÓN CON GITHUB

### Estructura del Repo

```
📁 github.com/org/hackathon-certificaciones/
├── 📁 .github/workflows/
│   └── ci-cd.yml          ← Pipeline CI/CD
├── 📁 docs/               ← Documentación
├── 📁 src/
│   ├── backend/
│   └── frontend/
├── 📁 infrastructure/    ← Terraform
├── 📁 tests/
├── README.md
└── CONTRIBUTING.md
```

### Flujo con GitHub

```
1. CODE AGENT → Crea branch (feature/crear-empleado)
                    │
2. CODE AGENT → Push código
                    │
3. GITHUB ACTIONS → CI: Lint → Test → Build
                    │
4. TECH LEAD → Aprueba Merge
                    │
5. MERGE MAIN → CD: Deploy a Azure
```

---

## 5. WORKFLOWS DE GITHUB ACTIONS

### CI: Validación (en cada Push/PR)

```yaml
name: CI - Validate & Test
on: [push, pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run linters
        run: pip install ruff black && ruff check src/

  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run tests
        run: pytest --cov=src tests/
```

### CD: Despliegue (solo en Merge a Main)

```yaml
name: CD - Deploy to Azure
on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Login to Azure
        uses: azure/login@v1
        with:
          creds: ${{ secrets.AZURE_CREDENTIALS }}
      - name: Deploy to Azure
        uses: azure/webapps-deploy@v3
        with:
          app-name: hackathon-api
```

---

## 6. PERMISOS EN GITHUB

| ACCIÓN | ORCHESTRATOR | AGENTES | TECH LEAD | DEV/QA | PO |
|--------|-------------|---------|-----------|--------|-----|
| Crear branch | ✓ | ✓ | ✓ | ✓ | ✗ |
| Push código | ✓ | ✓ | ✓ | ✓ | ✗ |
| Crear PR | ✓ | ✓ | ✓ | ✓ | ✗ |
| Aprobar PR | ✗ | ✗ | ✓ | ✗ | ✗ |
| Merge PR | ✗ | ✗ | ✓ | ✗ | ✗ |
| Ver código | ✓ | ✓ | ✓ | ✓ | ✓ |
| Ver workflows | ✓ | ✓ | ✓ | ✓ | ✓ |
| Gestionar Settings | ✗ | ✗ | ✓ | ✗ | ✗ |

---

## 7. FLUJO DE COMUNICACIÓN

```
     ┌──────────────┐
     │   USER/PO    │ ← "Necesito X"
     └──────┬───────┘
            │
            ▼
     ┌──────────────┐
     │ORCHESTRATOR  │ ← Coordina todo
     │  (CrewAI)    │
     └──────┬───────┘
            │
     ┌──────┼───────┬──────────┬──────────┐
     ▼      ▼       ▼          ▼          ▼
  ┌────┐ ┌────┐ ┌──────┐ ┌──────┐ ┌─────────┐
  │Req │ │Plan │ │Arch  │ │Code  │ │ Test   │
  │Agt │ │Agt │ │Agt   │ │Agent │ │ Agent  │
  └──┬─┘ └──┬─┘ └──┬───┘ └──┬────┘ └────┬────┘
     │      │      │        │            │
     └──────┼──────┼────────┼────────────┘
            │      │        │
            ▼      ▼        ▼
     ┌──────────────┐
     │  HUMANO      │ ← Revisa, Aprueba
     │ (Tech Lead)  │
     └──────────────┘
```

---

## 8. RESUMEN

| ROL | HERRAMIENTA CLAVE | GITHUB |
|-----|-------------------|--------|
| Orchestrator | CrewAI + Azure OpenAI | Coordina todo |
| Requirements Agent | GPT-4 + Mermaid | Crea docs |
| Planning Agent | GPT-4 | Crea issues |
| Architecture Agent | GPT-4 + Terraform | Crea configs |
| Code Agent | GPT-4 + VS Code | Push code |
| Test Agent | Pytest + GitHub Actions | Ejecuta CI |
| Security Agent | Semgrep | Scan code |
| Deployment Agent | Azure CLI + Terraform | Ejecuta CD |
| Tech Lead (Humano) | VS Code + Azure Portal | Aprueba PRs |
| Developer (Humano) | VS Code + Postman | Revisa código |
| PO (Humano) | Navegador + Slack | Ver docs |

¿Te sirve este framework?