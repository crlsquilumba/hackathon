"""
AI Factory - Security Agent
Analiza vulnerabilidades y recomienda correcciones
"""
from crewai import Agent


def create_security_agent():
    """Crea el agente de seguridad"""
    return Agent(
        role="Security Engineer",
        goal="Identificar vulnerabilidades y recomendar correcciones de seguridad",
        backstory="""
        Eres un experto en ciberseguridad con más de 12 años de experiencia.
        Has realizado penetration testing y security audits para empresas financieras.
        Conoces OWASP Top 10, NIST, ISO 27001, PCI-DSS.
        Sabes identificar y mitigar vulnerabilidades comunes.
        """,
        verbose=True,
        allow_delegation=False
    )


SECURITY_ANALYSIS_PROMPT = """
## Código a Analizar
{code}

### Archivo: {file_path}
### Lenguaje: {language}

## Tu Tarea
Realiza análisis de seguridad:

### 1. OWASP Top 10
Busca:
- Injection (SQL, XSS, Command)
- Broken Authentication
- Sensitive Data Exposure
- XML External Entities
- Broken Access Control
- Security Misconfiguration
- Cross-Site Scripting (XSS)
- Insecure Deserialization
- Using Components with Known Vulnerabilities
- Insufficient Logging

### 2. Secrets Expuestos
- API keys
- Passwords
- Tokens
- Credentials

### 3. Mejores Prácticas
- Validación de entrada
- Sanitización
- Encoding
- Cifrado

## Formato de Salida
Reporte en Markdown con:
- Vulnerabilidades encontradas
- Severidad (Critical/High/Medium/Low)
- Recomendaciones
- Código corregido (si es posible)
"""
