# 🤖 AI Factory - Framework de Desarrollo con IA

> Sistema de desarrollo de software 100% impulsado por agentes de IA, basado en metodologías reales (ADLC de Arthur.ai y AI-DLC de AWS).

## 📋 Descripción

AI Factory es un framework que automatiza el ciclo de vida completo del desarrollo de software usando agentes de IA. Cada agente es un experto en su dominio que trabaja en conjunto para construir aplicaciones de forma incremental.

## 🏗️ Arquitectura del Sistema

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         AI FACTORY                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│   ┌─────────────┐    ┌─────────────┐    ┌─────────────┐                │
│   │   HUMAN     │───▶│ORCHESTRATOR │───▶│   OUTPUT    │                │
│   │   (USER)   │    │  (CrewAI)   │    │  (MVP)     │                │
│   └─────────────┘    └──────┬──────┘    └─────────────┘                │
│                             │                                            │
│         ┌───────────────────┼───────────────────┐                      │
│         │                   │                   │                      │
│         ▼                   ▼                   ▼                      │
│   ┌───────────┐      ┌───────────┐      ┌───────────┐                   │
│   │  REQUISITS│      │  PLANNING │      │   ARCH   │                   │
│   │   AGENT   │      │   AGENT   │      │   AGENT  │                   │
│   └───────────┘      └───────────┘      └───────────┘                   │
│         │                   │                   │                      │
│         └───────────────────┼───────────────────┘                      │
│                             │                                            │
│                             ▼                                            │
│   ┌───────────┐      ┌───────────┐      ┌───────────┐                   │
│   │   CODE    │      │   TEST    │      │  SECURITY │                   │
│   │   AGENT   │      │   AGENT   │      │   AGENT   │                   │
│   └───────────┘      └───────────┘      └───────────┘                   │
│         │                   │                   │                      │
│         └───────────────────┼───────────────────┘                      │
│                             │                                            │
│                             ▼                                            │
│                      ┌───────────┐                                      │
│                      │ DEPLOY   │                                      │
│                      │  AGENT   │                                      │
│                      └───────────┘                                      │
└─────────────────────────────────────────────────────────────────────────────┘
```

## 📦 Estructura del Proyecto

```
ai-factory/
├── agents/                    # Definición de agentes
│   ├── requirements_agent.py  # Analista de requisitos
│   ├── planning_agent.py      # Gestor de proyectos
│   ├── architecture_agent.py  # Arquitecto de software
│   ├── code_agent.py         # Generador de código
│   ├── test_agent.py        # Ingeniero de QA
│   ├── security_agent.py     # Analista de seguridad
│   └── deployment_agent.py   # DevOps
├── tools/                     # Herramientas personalizadas
├── prompts/                   # Plantillas de prompts
├── config/                    # Configuraciones
├── scripts/                   # Scripts de utilidad
├── orchestrator.py            # Orquestador principal
└── README.md
```

## 🚀 Instalación

### Prerrequisitos

- Python 3.12+
- Git
- Cuenta de GitHub
- API Key de OpenAI o Azure OpenAI

### Paso 1: Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/ai-factory.git
cd ai-factory
```

### Paso 2: Crear entorno virtual

```bash
# Crear entorno virtual
python -m venv venv

# Activar (Linux/Mac)
source venv/bin/activate

# Activar (Windows)
venv\Scripts\activate
```

### Paso 3: Instalar dependencias

```bash
pip install -r requirements.txt
```

### Paso 4: Configurar variables de entorno

```bash
# Copiar el archivo de ejemplo
cp .env.example .env

# Editar con tus credenciales
nano .env
```

Contenido de `.env`:
```env
# OpenAI (opcional - también puedes usar Azure OpenAI)
OPENAI_API_KEY=sk-tu-api-key-aqui

# Azure OpenAI (recomendado para empresas)
AZURE_OPENAI_ENDPOINT=https://tu-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=tu-azure-key
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4

# GitHub (para automatizaciones)
GITHUB_TOKEN=ghp_tu_token_aqui

# Configuración
PROJECT_NAME=mi-proyecto
LOG_LEVEL=INFO
```

### Paso 5: Verificar instalación

```bash
python -c "from ai_factory import create_orchestrator; print('✅ Instalación correcta')"
```

## 💻 Uso

### Método 1: Uso Programático

```python
from ai_factory import create_orchestrator

# Crear orquestador
orchestrator = create_orchestrator("Mi Proyecto")

# Ejecutar pipeline completo
result = orchestrator.run_full_pipeline(
    user_need="Necesito una aplicación de gestión de empleados...",
    project_context="Empresa de 200 empleados...",
    preferred_stack="React + .NET + PostgreSQL"
)

print(result)
```

### Método 2: Uso Incremental (Recomendado)

```python
from ai_factory import create_orchestrator

orchestrator = create_orchestrator("Mi Proyecto")

# Fase 1: Requisitos
requisitos = orchestrator.run_requirements_phase(
    user_need="Una app de tareas con usuarios y proyectos",
    project_context="Startup de 5 personas"
)

# Fase 2: Planificación
plan = orchestrator.run_planning_phase(
    user_stories=str(requisitos),
    total_hours=40
)

# Fase 3: Arquitectura
arquitectura = orchestrator.run_architecture_phase(
    requirements=str(requisitos),
    preferred_stack="FastAPI + React"
)

# Fase 4: Código (módulo por módulo)
codigo = orchestrator.run_code_generation_phase(
    module="autenticacion",
    description="Sistema de login con JWT",
    tech_stack="Python FastAPI"
)
```

### Método 3: Con GitHub Copilot

En VS Code, configura Copilot para que use los prompts de `ai-factory/prompts/`:

1. Instalar extensión Copilot
2. Crear archivo `.github/copilot-instructions.md`
3. Agregar las instrucciones de los agentes

## 🔧 Configuración de Herramientas

### Azure OpenAI (Recomendado)

```python
from langchain_openai import AzureChatOpenAI

llm = AzureChatOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-15-preview"
)
```

### GitHub Integration

```python
from github import Github

# Autenticar
g = Github("tu-github-token")

# Obtener repo
repo = g.get_repo("tu-usuario/tu-repo")
```

## 📖 Desarrollo Incremental

### Iteración 1: Fundación
```python
# Semana 1
1. Auth + DB
2. Estructura base
```

### Iteración 2: Core Business
```python
# Semana 2
1. CRUD Entidades principales
2. API endpoints
```

### Iteración 3: Features
```python
# Semana 3
1. Dashboards
2. Reportes
3. Notificaciones
```

## 🎯 Roles de Agentes

| Agente | Rol | Herramientas |
|--------|-----|--------------|
| Requirements Agent | Analista de Negocios | SerperDev, GitHub, Markdown |
| Planning Agent | PM | Directory Read |
| Architecture Agent | Arquitecto | Code Interpreter |
| Code Agent | Desarrollador | File Writer, GitHub |
| Test Agent | QA Engineer | Test generators |
| Security Agent | Security Engineer | Code analysis |
| Deployment Agent | DevOps | Bash, Azure CLI |

## 📊 Métricas del Proyecto

El framework trackea:

- Tiempo por fase
- Líneas de código generadas
- Tests generados
- Ciclos de iteración
- Costo en tokens

## 🔒 Seguridad

- ✅ No expone API keys en logs
- ✅ Usa variables de entorno
- ✅ Valida inputs
- ✅ Sanitiza outputs

## 🤝 Contribuir

1. Fork del repo
2. Crear branch: `git checkout -b feature/nueva-caracteristica`
3. Commit: `git commit -m 'feat: nueva caracteristica'`
4. Push: `git push origin feature/nueva-caracteristica`
5. Crear Pull Request

## 📝 Licencia

MIT License - ver LICENSE para detalles.

## 🔗 Recursos

- [CrewAI Documentation](https://docs.crewai.com)
- [LangChain Documentation](https://python.langchain.com)
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Arthur.ai ADLC](https://www.arthur.ai/blog/introducing-adlc)
- [AWS AI-DLC](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/)

---

** Construido con ❤️ usando CrewAI + LangChain + Azure OpenAI**
