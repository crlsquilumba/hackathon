"""
AI Factory - Deployment Agent
Despliega aplicaciones a producción
"""
from crewai import Agent
from crewai_tools import BashTool


def create_deployment_agent():
    """Crea el agente de despliegues"""
    return Agent(
        role="DevOps Engineer",
        goal="Desplegar aplicaciones de forma automatizada, segura y confiable",
        backstory="""
        Eres un DevOps engineer con más de 10 años de experiencia.
        Has configurado CI/CD pipelines en AWS, Azure y GCP.
        Conoces Docker, Kubernetes, Terraform, Ansible.
        Sabes implementaciones Blue-Green, Canary y Rollback.
        """,
        verbose=True,
        allow_delegation=False,
        tools=[
            BashTool()
        ]
    )


DEPLOYMENT_PROMPT = """
## Proyecto a Desplegar

### Nombre: {project_name}
### Entorno: {environment}
### Cloud: {cloud_provider}

## Tu Tarea
Crea pipeline de deployment:

### 1. CI/CD Pipeline
- Stages: Build, Test, Deploy
- Scripts por cada stage
- Notifications

### 2. Dockerfile
- Multi-stage build
- Optimizado para producción

### 3. Infraestructura como Código
- Terraform o Bicep
- Recursos necesarios

### 4. Scripts de Deploy
- Pre-deploy
- Deploy
- Post-deploy
- Rollback

### 5. Health Checks
- Endpoints de salud
- Verificaciones post-deploy

##cloud Provider Commands
{provide_commands}

## Formato de Salida
Archivos de configuración listos.
"""
