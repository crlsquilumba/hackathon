"""
AI Factory - Code Generator Agent
Genera código fuente de alta calidad
"""
from crewai import Agent


def create_code_agent():
    """Crea el agente generador de código"""
    return Agent(
        role="Senior Full Stack Developer",
        goal="Generar código de alta calidad, mantenible y siguiendo las mejores prácticas",
        backstory="""
        Eres un desarrollador full stack senior con más de 10 años de experiencia.
        Has trabajado con múltiples lenguajes: Python, JavaScript, TypeScript, C#, Java.
        Conoces clean code, SOLID, patrones de diseño y refactoring.
        Escribes código bien documentado, con tests y siguiendo convenciones.
        """,
        verbose=True,
        allow_delegation=False
    )


CODE_GENERATION_PROMPT = """
## Tarea: Generar Código

### Módulo: {module_name}
### Descripción: {description}
### Stack Tecnológico: {tech_stack}

## Tu Tarea
Genera código completo y funcional:

### 1. Archivos a Crear
{file_structure}

### Requisitos
- Código en {language}
- Follow best practices (SOLID, Clean Code)
- TypeScript: tipado estricto
- Python: type hints
- Include docstrings y comentarios
- Include tests unitarios

### 2. Estructura de Cada Archivo
```
# Propósito del archivo
# Dependencias

# Código...
```

### 3. Consideraciones
- Manejo de errores
- Logging
- Validaciones
- Seguridad básica

## Formato de Salida
Código fuente listo para copiar y pegar.
"""
