"""
AI Factory - Framework de Desarrollo con IA
"""
from .orchestrator import create_orchestrator, AIAgentOrchestrator
from .agents import *

__version__ = "1.0.0"
__author__ = "Tu Equipo"

__all__ = [
    'create_orchestrator',
    'AIAgentOrchestrator'
]
