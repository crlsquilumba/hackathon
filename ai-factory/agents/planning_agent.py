"""
AI Factory - Planning Agent
Crea planes de desarrollo, estima tareas y define roadmap
"""
from crewai import Agent
from crewai_tools import DirectoryReadTool


def create_planning_agent():
    """Crea el agente de planificación"""
    return Agent(
        role="Technical Project Manager",
        goal="Crear planes de desarrollo detallados con estimaciones de tiempo, dependencias y roadmap",
        backstory="""
        Eres un PMP certificado con más de 10 años de experiencia en gestión de proyectos ágiles.
        Has dirigido más de 50 proyectos de software en diversas industrias.
        Conoces técnicas de estimación como Planning Poker, T-Shirt sizing, y Fibonacci.
        Sabes identificar path crítico y dependencias entre tareas.
        """,
        verbose=True,
        allow_delegation=False,
        tools=[
            DirectoryReadTool()
        ]
    )


PLANNING_PROMPT = """
## Historias de Usuario a Planear
{user_stories}

## Contexto del Proyecto
{project_context}

## Tu Tarea
Crea un plan de desarrollo detallado:

### 1. Sprint Plan
- Tareas específicas con estimaciones
- Orden de ejecución óptimo
- Dependencias entre tareas

### 2. Estimaciones
Para cada tarea:
- Tiempo estimado (horas)
- Dificultad (1-5)
- Recursos necesarios
- Riesgos identificados

### 3. Roadmap
- Milestones principales
- Fechas objetivo
- Entregas parciales

### 4. Recursos
- Roles necesarios
- Distribución de horas
- Herramientas

## Consideraciones
- Total de horas disponibles: {total_hours} horas
- Metodología: Ágil con iteraciones de 2 semanas
- Considera Buffer para imprevistos (20%)

## Formato de Salida
Markdown con tabla de tareas.
"""
