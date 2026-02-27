"""
AI Factory - Requirements Agent
Transforma necesidades de negocio en requisitos técnicos
"""
from crewai import Agent
from crewai_tools import SerperDevTool, FileReadTool, DirectoryReadTool
from .tools import GitHubTool, MarkdownWriterTool


def create_requirements_agent():
    """Crea el agente de requisitos"""
    return Agent(
        role="Requirements Engineer",
        goal="Transformar las necesidades de negocio en requisitos claros, historias de usuario y documentos técnicos",
        backstory="""
        Eres un experto analista de negocios con más de 15 años de experiencia.
        Has liderado proyectos ágiles en empresas Fortune 500 y sabes transformar
        necesidades vagas en historias de usuario detalladas con criterios de aceptación.
        Conoces las metodologías Agile, Scrum, y las mejores prácticas de UML.
        """,
        verbose=True,
        allow_delegation=False,
        tools=[
            SerperDevTool(),
            FileReadTool(),
            DirectoryReadTool(),
            GitHubTool(),
            MarkdownWriterTool()
        ]
    )


# Prompt template para requisitos
REQUIREMENTS_PROMPT = """
## Contexto del Proyecto
{project_context}

## Necesidad de Negocio
{user_need}

## Tu Tarea
Genera los siguientes documentos técnicos:

### 1. Historias de Usuario (5-10)
Para cada historia incluye:
- Título claro
- Como [rol]
- Quiero [funcionalidad]
- Para [beneficio]
- Criterios de aceptación (Definition of Done)

### 2. Diagrama de Casos de Uso
En formato Mermaid:
- Actores principales
- Casos de uso
- Relaciones

### 3. Modelo de Entidades
- Lista de entidades/tablas
- Atributos principales
- Relaciones entre entidades

### 4. Backlog Priorizado
Usando metodología MoSCoW:
- Must Have (crítico)
- Should Have (importante)
- Could Have (deseable)
- Won't Have (no en esta iteración)

## Formato de Salida
Markdown con código Mermaid para diagramas.
"""


# Metadata para el agente
AGENT_METADATA = {
    "name": "Requirements Agent",
    "version": "1.0.0",
    "description": "Transforma necesidades de negocio en requisitos técnicos",
    "capabilities": [
        "Generar historias de usuario",
        "Crear diagramas de casos de uso",
        "Diseñar modelo de entidades",
        "Priorizar backlog"
    ],
    "tools_required": [
        "SerperDevTool",
        "GitHubTool",
        "MarkdownWriterTool"
    ],
    "output_format": "markdown"
}
