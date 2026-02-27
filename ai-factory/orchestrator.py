"""
AI Factory - Orchestrator
Coordina todos los agentes del workflow
"""
from crewai import Agent, Task, Crew
from .agents.requirements_agent import create_requirements_agent
from .agents.planning_agent import create_planning_agent
from .agents.architecture_agent import create_architecture_agent
from .agents.code_agent import create_code_agent
from .agents.test_agent import create_test_agent
from .agents.security_agent import create_security_agent
from .agents.deployment_agent import create_deployment_agent


class AIAgentOrchestrator:
    """
    Orquestador principal de la AI Factory.
    Coordina todos los agentes para el desarrollo incremental.
    """
    
    def __init__(self, project_name: str, openai_api_key: str = None):
        self.project_name = project_name
        self.openai_api_key = openai_api_key
        self.agents = {}
        self.tasks = []
        self.crew = None
        
    def setup_agents(self):
        """Inicializa todos los agentes"""
        self.agents = {
            'requirements': create_requirements_agent(),
            'planning': create_planning_agent(),
            'architecture': create_architecture_agent(),
            'code': create_code_agent(),
            'test': create_test_agent(),
            'security': create_security_agent(),
            'deployment': create_deployment_agent()
        }
        
    def create_task(self, name: str, description: str, agent_key: str, expected_output: str):
        """Crea una tarea para un agente específico"""
        task = Task(
            description=description,
            agent=self.agents[agent_key],
            expected_output=expected_output,
            name=name
        )
        self.tasks.append(task)
        return task
    
    def build_crew(self, agents: list = None, tasks: list = None, verbose: bool = True):
        """Construye el crew con agentes y tareas"""
        agents_to_use = agents or list(self.agents.values())
        tasks_to_use = tasks or self.tasks
        
        self.crew = Crew(
            agents=agents_to_use,
            tasks=tasks_to_use,
            verbose=verbose,
            memory=True,  # Mantiene contexto entre tareas
            planning=True  # Planifica antes de ejecutar
        )
        
        return self.crew
    
    def run_requirements_phase(self, user_need: str, project_context: str = ""):
        """Ejecuta la fase de requisitos"""
        requirements_agent = self.agents['requirements']
        
        task = Task(
            description=f"""
            Analiza la siguiente necesidad de negocio y transforma en requisitos técnicos:
            
            Necesidad: {user_need}
            Contexto: {project_context}
            """,
            agent=requirements_agent,
            expected_output="Documento de requisitos completo en Markdown"
        )
        
        crew = Crew(
            agents=[requirements_agent],
            tasks=[task],
            verbose=True
        )
        
        return crew.kickoff()
    
    def run_planning_phase(self, user_stories: str, total_hours: int = 40):
        """Ejecuta la fase de planificación"""
        planning_agent = self.agents['planning']
        
        task = Task(
            description=f"""
            Crea un plan de desarrollo basado en estas historias de usuario:
            
            {user_stories}
            
            Horas totales disponibles: {total_hours}
            """,
            agent=planning_agent,
            expected_output="Plan de desarrollo con tareas y estimaciones"
        )
        
        crew = Crew(
            agents=[planning_agent],
            tasks=[task],
            verbose=True
        )
        
        return crew.kickoff()
    
    def run_architecture_phase(self, requirements: str, preferred_stack: str):
        """Ejecuta la fase de arquitectura"""
        architecture_agent = self.agents['architecture']
        
        task = Task(
            description=f"""
            Diseña la arquitectura para estos requisitos:
            
            {requirements}
            
            Stack preferido: {preferred_stack}
            """,
            agent=architecture_agent,
            expected_output="Documento de arquitectura con diagramas Mermaid"
        )
        
        crew = Crew(
            agents=[architecture_agent],
            tasks=[task],
            verbose=True
        )
        
        return crew.kickoff()
    
    def run_code_generation_phase(self, module: str, description: str, tech_stack: str):
        """Ejecuta la fase de generación de código"""
        code_agent = self.agents['code']
        
        task = Task(
            description=f"""
            Genera código para el módulo: {module}
            
            Descripción: {description}
            Stack: {tech_stack}
            """,
            agent=code_agent,
            expected_output="Código fuente completo"
        )
        
        crew = Crew(
            agents=[code_agent],
            tasks=[task],
            verbose=True
        )
        
        return crew.kickoff()
    
    def run_full_pipeline(self, user_need: str, project_context: str = "", preferred_stack: str = ""):
        """Ejecuta el pipeline completo de desarrollo"""
        # Fase 1: Requisitos
        print("=" * 50)
        print("FASE 1: REQUISITOS")
        print("=" * 50)
        requirements_result = self.run_requirements_phase(user_need, project_context)
        
        # Fase 2: Planificación
        print("\n" + "=" * 50)
        print("FASE 2: PLANIFICACIÓN")
        print("=" * 50)
        planning_result = self.run_planning_phase(str(requirements_result))
        
        # Fase 3: Arquitectura
        print("\n" + "=" * 50)
        print("FASE 3: ARQUITECTURA")
        print("=" * 50)
        architecture_result = self.run_architecture_phase(str(requirements_result), preferred_stack)
        
        return {
            'requirements': requirements_result,
            'planning': planning_result,
            'architecture': architecture_result
        }


def create_orchestrator(project_name: str = "AI Factory Project") -> AIAgentOrchestrator:
    """Factory function para crear el orquestador"""
    orchestrator = AIAgentOrchestrator(project_name=project_name)
    orchestrator.setup_agents()
    return orchestrator
