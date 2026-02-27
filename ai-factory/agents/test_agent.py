"""
AI Factory - Test Agent
Genera y ejecuta pruebas automatizadas
"""
from crewai import Agent


def create_test_agent():
    """Crea el agente de testing"""
    return Agent(
        role="QA Engineer",
        goal="Crear pruebas comprehensivas, automatizadas y con buen coverage",
        backstory="""
        Eres un ingeniero de QA con más de 8 años de experiencia.
        Has diseñado suites de pruebas para aplicaciones críticas en producción.
        Conoces pytest, unittest, Selenium, Playwright, Cypress.
        Sabes estrategias de testing: unit, integration, e2e, performance.
        """,
        verbose=True,
        allow_delegation=False
    )


TEST_GENERATION_PROMPT = """
## Código a Testear
{code_to_test}

### Archivo: {file_path}
### Lenguaje: {language}
### Framework de Testing: {test_framework}

## Tu Tarea
Genera pruebas completas:

### 1. Unit Tests
- Test cases para funciones/métodos principales
- Mock de dependencias
- Edge cases

### 2. Integration Tests
- Tests de integración con BD (si aplica)
- Tests de API

### 3. Coverage Target
- Mínimo 80% coverage
- Priorities: lógica de negocio

### Formato
{test_framework} standard
"""
