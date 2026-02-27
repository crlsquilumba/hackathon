"""
AI Factory - Architecture Agent
Diseña arquitectura de software, propone stack tecnológico y diagramas
"""
from crewai import Agent
from crewai_tools import CodeInterpreterTool


def create_architecture_agent():
    """Crea el agente de arquitectura"""
    return Agent(
        role="Software Architect",
        goal="Diseñar arquitecturas robustas, escalables y siguiendo las mejores prácticas",
        backstory="""
        Eres un arquitecto de software senior con más de 15 años de experiencia.
        Has diseñado sistemas para empresas Fortune 500 y startups unicornio.
        Conoces patrones arquitectónicos como Clean Architecture, Hexagonal, DDD, CQRS, Microservicios.
        Tienes experiencia en arquitecturas cloud-native, serverless y event-driven.
        """,
        verbose=True,
        allow_delegation=False,
        tools=[
            CodeInterpreterTool()
        ]
    )


ARCHITECTURE_PROMPT = """
## Proyecto: {project_name}

## Requisitos del Proyecto
{requirements}

## Restricciones
- Stack preferido: {preferred_stack}
- Presupuesto: {budget}
- Timeline: {timeline}
- Equipo: {team_size} desarrolladores

## Tu Tarea
Diseña la arquitectura completa:

### 1. Diagrama de Arquitectura (Alto Nivel)
En formato Mermaid:
- Frontend
- Backend/API
- Base de datos
- Servicios externos
- Servicios cloud

### 2. Stack Tecnológico
Para cada capa:
- Tecnología recomendada
- Versión
- Justificación

### 3. Modelo de Datos (ERD)
En formato Mermaid:
- Entidades
- Relaciones
- Keys

### 4. Estructura de Proyecto
- Carpetas y organización
- Patrón arquitectónico

### 5. APIs Principales
- Endpoints clave
- Contratos

### 6. Seguridad
- Autenticación
- Autorización
- SSL/TLS
- Rate limiting

### 7. Infraestrutura Sugerida
- Cloud provider
- Servicios a usar
- Costos estimados

## Formato de Salida
Markdown con código Mermaid para diagramas.
"""
