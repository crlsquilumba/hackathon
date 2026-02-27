# CONFIGURACIÓN DE AGENTES EN VS CODE

---

## 1. INSTALACIÓN DE HERRAMIENTAS

### Extensiones de VS Code necesarias

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  EXTENSIONES RECOMENDADAS                                                      │
└─────────────────────────────────────────────────────────────────────────────────┘

1. Copilot / Copilot Chat          → Asistente IA
2. Pylance                         → Python linting
3. Ruff                            → Python formatter
4. GitHub Copilot Enterprise       → Code completion
5. Azure Tools                     → Gestión Azure
6. Docker                          → Contenedores
7. Terraform                       → IaC
8. Jupyter                         → Notebooks
9. REST Client                    → Probar APIs
10. Thunder Client                → Testing API
```

### Instalación de dependencias

```bash
# Terminal de VS Code
pip install crewai crewai-tools
pip install python-dotenv
pip install openai azure-openai
pip install fastapi uvicorn
pip install sqlalchemy alembic
pip install pytest pytest-cov
pip install ruff black
```

---

## 2. ESTRUCTURA DEL PROYECTO

```
📁 hackathon-agents/
├── 📁 src/
│   ├── 📁 agents/
│   │   ├── __init__.py
│   │   ├── orchestrator.py        ← ORQUESTADOR PRINCIPAL
│   │   ├── requirements_agent.py  ← REQUISITOS
│   │   ├── planning_agent.py      ← PLANIFICACIÓN
│   │   ├── architecture_agent.py  ← ARQUITECTURA
│   │   ├── code_agent.py          ← GENERADOR CÓDIGO
│   │   ├── test_agent.py          ← TESTING
│   │   ├── security_agent.py     ← SEGURIDAD
│   │   └── deployment_agent.py   ← DESPLIEGUE
│   │
│   ├── 📁 tools/
│   │   ├── github_tool.py         ← Herramienta GitHub
│   │   ├── azure_tool.py          ← Herramienta Azure
│   │   ├── file_tool.py           ← Manejo archivos
│   │   └── code_execution.py      ← Ejecutar código
│   │
│   ├── 📁 crew/
│   │   └── hackathon_crew.py     ← Configuración del Crew
│   │
│   └── 📁 config/
│       ├── settings.py            ← Configuraciones
│       └── prompts.py             ← Prompts base
│
├── 📁 tests/
├── 📁 docs/
├── .env                           ← API Keys
├── requirements.txt
├── pyproject.toml
└── main.py                        ← Punto de entrada
```

---

## 3. CÓDIGO DE CADA AGENTE

### 3.1 CONFIGURACIÓN BASE (.env)

```bash
# .env
OPENAI_API_KEY=sk-xxxxx
AZURE_OPENAI_ENDPOINT=https://xxxxx.openai.azure.com/
AZURE_OPENAI_API_KEY=xxxxx
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4
GITHUB_TOKEN=ghp_xxxxx
AZURE_SUBSCRIPTION_ID=xxxxx
AZURE_TENANT_ID=xxxxx
AZURE_CLIENT_ID=xxxxx
AZURE_CLIENT_SECRET=xxxxx
```

### 3.2 AGENTE DE REQUISITOS

```python
# src/agents/requirements_agent.py
from crewai import Agent
from crewai_tools import SerperDevTool, FileReadTool

requirements_agent = Agent(
    role="Requirements Engineer",
    goal="Transformar las necesidades de negocio en requisitos claros y documentos técnicos",
    backstory="""
    Eres un experto analista de negocios con 15 años de experiencia.
    Has trabajado en múltiples proyectos ágiles y sabes cómo transformar
    necesidades vagas en historias de usuario detalladas.
    Conoces las mejores prácticas de Agile y UML.
    """,
    verbose=True,
    allow_delegation=False,
    tools=[
        SerperDevTool(),  # Buscar información
        FileReadTool(),   # Leer documentos existentes
    ]
)

# Prompt específico para requisitos
REQUIREMENTS_PROMPT = """
Basado en la siguiente necesidad de negocio:

{user_input}

Genera:
1. 5-10 historias de usuario con criterios de aceptación
2. Diagrama de casos de uso en formato Mermaid
3. Modelo de entidades
4. Backlog priorizado (MoSCoW)

Formato: Markdown
"""
```

### 3.3 AGENTE DE PLANIFICACIÓN

```python
# src/agents/planning_agent.py
from crewai import Agent

planning_agent = Agent(
    role="Technical Project Manager",
    goal="Crear plan de desarrollo detallado con estimaciones y dependencias",
    backstory="""
    Eres un PMP certificado con experiencia en proyectos ágiles.
    Sabes estimar esfuerzos, identificar dependencias y crear
    roadmaps realistas. Has dirigido más de 50 proyectos de software.
    """,
    verbose=True,
    allow_delegation=False,
    tools=[
        #herramientas que necesita
    ]
)

PLANNING_PROMPT = """
Basado en las siguientes historias de usuario:

{user_stories}

Crea:
1. Plan de sprint con tareas
2. Estimaciones de tiempo por tarea
3. Dependencias entre tareas
4. Orden de ejecución óptimo
5. Identificación de path crítico

Considera: 7 horas totales de desarrollo
"""
```

### 3.4 AGENTE DE ARQUITECTURA

```python
# src/agents/architecture_agent.py
from crewai import Agent
from crewai_tools import CodeInterpreterTool

architecture_agent = Agent(
    role="Software Architect",
    goal="Diseñar arquitectura robusta y escalable",
    backstory="""
    Eres un arquitecto de software senior con experiencia en
    arquitecturas distribuidas, microservicios y cloud.
    Has diseñado sistemas para empresas Fortune 500.
    Conoces patrones como DDD, CQRS, Event Sourcing.
    """,
    verbose=True,
    allow_delegation=False,
    tools=[
        CodeInterpreterTool(),  # Ejecutar código para generar diagrams
    ]
)

ARCHITECTURE_PROMPT = """
Para el proyecto de: {project_name}

Stack propuesto: {tech_stack}

Genera:
1. Diagrama de arquitectura en Mermaid (frontend, backend, db, servicios)
2. Modelo de datos (ERD en Mermaid)
3. Lista de componentes necesarios
4. Configuraciones base (docker-compose, requirements.txt)
5. Consideraciones de seguridad
"""
```

### 3.5 AGENTE DE CÓDIGO

```python
# src/agents/code_agent.py
from crewai import Agent

code_agent = Agent(
    role="Senior Full Stack Developer",
    goal="Generar código de alta calidad siguiendo las mejores prácticas",
    backstory="""
    Eres un desarrollador full stack senior con 10 años de experiencia.
    Has trabajado con Python, JavaScript, React, FastAPI, PostgreSQL.
    Conoces clean code, SOLID, patrones de diseño.
    Escribes código mantenible y bien documentado.
    """,
    verbose=True,
    allow_delegation=False,
    tools=[
        #herramientas para escribir archivos
    ]
)

CODE_PROMPT = """
Genera el código para:

Módulo: {module_name}
Descripción: {description}
Stack: {tech_stack}

Requisitos:
- Código en {language}
- Seguir mejores prácticas
- Incluir tests unitarios
- Documentación básica

Estructura de archivos a crear:
{file_structure}
"""
```

### 3.6 AGENTE DE TESTING

```python
# src/agents/test_agent.py
from crewai import Agent

test_agent = Agent(
    role="QA Engineer",
    goal="Crear pruebas comprehensivas y automatizadas",
    backstory="""
    Eres un ingeniero de QA con experiencia en testing automatizado.
    Has diseñado suites de pruebas para aplicaciones críticas.
    Conoces pytest, unittest, Selenium, Playwright.
    """,
    verbose=True,
    allow_delegation=False
)

TEST_PROMPT = """
Para el código en: {file_path}

Genera:
1. Tests unitarios con pytest
2. Tests de integración
3. Tests E2E con Playwright (si es frontend)
4. Fixtures necesarios
5. Coverage target: 80%

Usa las mejores prácticas de testing.
"""
```

### 3.7 AGENTE DE SEGURIDAD

```python
# src/agents/security_agent.py
from crewai import Agent

security_agent = Agent(
    role="Security Engineer",
    goal="Identificar vulnerabilidades y recomendar correcciones",
    backstory="""
    Eres un experto en seguridad informática.
    Has realizado penetration testing y audits de seguridad.
    Conoces OWASP Top 10, NIST, ISO 27001.
    """,
    verbose=True,
    allow_delegation=False
)

SECURITY_PROMPT = """
Analiza el siguiente código: {code}

Busca:
1. OWASP Top 10 vulnerabilidades
2. Secrets expuestos
3. Inyecciones SQL
4. XSS
5. Problemas de autenticación
6. Best practices de seguridad

Genera reporte en Markdown.
"""
```

### 3.8 AGENTE DE DESPLIEGUE

```python
# src/agents/deployment_agent.py
from crewai import Agent
from crewai_tools import BashTool

deployment_agent = Agent(
    role="DevOps Engineer",
    goal="Desplegar aplicaciones de forma automatizada y segura",
    backstory="""
    Eres un DevOps engineer con experiencia en Azure, AWS, GCP.
    Has configurado CI/CD pipelines, Kubernetes, Docker.
    Conoces Infrastructure as Code con Terraform.
    """,
    verbose=True,
    allow_delegation=False,
    tools=[
        BashTool(),  # Ejecutar comandos
    ]
)

DEPLOYMENT_PROMPT = """
Desplegar a Azure:
- App Service: {app_name}
- Resource Group: {rg_name}
- Region: {region}

Pasos:
1. Build de la aplicación
2. Provisionar infraestructura con Terraform
3. Desplegar contenedor
4. Verificar health check
5. Configurar dominio SSL

Genera script de deployment.
"""
```

---

## 4. ORQUESTADOR PRINCIPAL

```python
# src/agents/orchestrator.py
from crewai import Agent, Task, Crew
from src.agents import (
    requirements_agent,
    planning_agent,
    architecture_agent,
    code_agent,
    test_agent,
    security_agent,
    deployment_agent
)

# Crear tareas
task_requirements = Task(
    description="Analizar requisitos del proyecto",
    agent=requirements_agent,
    expected_output="Documento de requisitos en Markdown"
)

task_planning = Task(
    description="Crear plan de desarrollo",
    agent=planning_agent,
    expected_output="Plan de sprint con tareas"
)

task_architecture = Task(
    description="Diseñar arquitectura",
    agent=architecture_agent,
    expected_output="Diagramas y configs"
)

task_code = Task(
    description="Generar código",
    agent=code_agent,
    expected_output="Código fuente"
)

task_test = Task(
    description="Crear pruebas",
    agent=test_agent,
    expected_output="Tests automatizados"
)

task_security = Task(
    description="Analizar seguridad",
    agent=security_agent,
    expected_output="Reporte de vulnerabilidades"
)

task_deploy = Task(
    description="Desplegar aplicación",
    agent=deployment_agent,
    expected_output="URL de producción"
)

# Crear Crew
hackathon_crew = Crew(
    agents=[
        requirements_agent,
        planning_agent,
        architecture_agent,
        code_agent,
        test_agent,
        security_agent,
        deployment_agent
    ],
    tasks=[
        task_requirements,
        task_planning,
        task_architecture,
        task_code,
        task_test,
        task_security,
        task_deploy
    ],
    verbose=True,
    memory=True,  # Mantiene contexto
    planning=True  # Planifica antes de ejecutar
)
```

---

## 5. PUNTO DE ENTRADA

```python
# main.py
from src.agents.orchestrator import hackathon_crew
from dotenv import load_dotenv

load_dotenv()

def main():
    # Input del usuario
    user_input = """
    Necesito crear una plataforma de gestión de certificaciones para empleados.
    - 200 empleados
    - Seguimiento de cursos y certificaciones
    - Dashboard para managers
    - Alertas de vencimiento
    - Generación de constancias
    """
    
    print("🎯 Iniciando Hackathon...")
    print("=" * 50)
    
    # Ejecutar crew
    result = hackathon_crew.kickoff(
        inputs={
            "user_input": user_input,
            "project_name": "Certificaciones App"
        }
    )
    
    print("=" * 50)
    print("✅ Hackathon completado!")
    print(f"Resultado: {result}")

if __name__ == "__main__":
    main()
```

---

## 6. EJECUTAR EN VS CODE

### Opción 1: Terminal

```bash
# En terminal de VS Code
cd hackathon-agents
python main.py
```

### Opción 2: Debug

```json
// launch.json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Main",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/main.py",
            "console": "integratedTerminal",
            "envFile": "${workspaceFolder}/.env"
        }
    ]
}
```

### Opción 3: Copilot Chat

```
@workspace #crew ¿Cómo ejecuto el main.py?
```

---

## 7. RESUMEN DE COMANDOS

```bash
# Instalación
pip install -r requirements.txt

# Desarrollo
python main.py

# Tests
pytest tests/ -v --cov=src

# Lint
ruff check src/
black src/

# Azure
az login
az webapp up --name hackathon-api
```

---

## 8. ARCHIVO requirements.txt

```
crewai>=0.28.0
crewai-tools>=0.3.0
python-dotenv>=1.0.0
openai>=1.0.0
azure-openai>=0.1.0
fastapi>=0.100.0
uvicorn>=0.23.0
sqlalchemy>=2.0.0
alembic>=1.12.0
python-jose>=3.3.0
passlib>=1.7.4
python-multipart>=0.0.6
pydantic>=2.0.0
pydantic-settings>=2.0.0
pytest>=7.4.0
pytest-cov>=4.1.0
ruff>=0.0.290
black>=23.0.0
httpx>=0.24.0
```

---

## 9. VIDEO TUTORIAL (COMO USAR)

```
PASO 1: Abrir proyecto en VS Code
        └─> File → Open Folder → hackathon-agents

PASO 2: Instalar extensiones
        └─> Extensions → Instalar las listadas arriba

PASO 3: Configurar .env
        └─> Copiar .env.example a .env y agregar API keys

PASO 4: Instalar dependencias
        └─> Terminal: pip install -r requirements.txt

PASO 5: Ejecutar
        └─> Terminal: python main.py

        O usar Debug (F5)
```

¿Te sirve esta configuración? ¿Necesitas que profundice en algún agente específico?
