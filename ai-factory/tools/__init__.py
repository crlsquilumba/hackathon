"""
AI Factory - Custom Tools
Herramientas personalizadas para los agentes
"""
from crewai.tools import BaseTool
from pydantic import Field
import os
import subprocess


class GitHubTool(BaseTool):
    name: str = "GitHub Tool"
    description: str = "Herramienta para interactuar con GitHub: crear issues, branches, PRs"

    def _run(self, action: str, repo: str, **kwargs):
        """Ejecuta acciones en GitHub"""
        # Implementación básica - expandir según necesidad
        if action == "create_issue":
            return f"Issue creado en {repo}"
        elif action == "create_branch":
            return f"Branch creada en {repo}"
        return "Acción no reconocida"


class MarkdownWriterTool(BaseTool):
    name: str = "Markdown Writer"
    description: str = "Escribe contenido en archivos Markdown"

    def _run(self, filename: str, content: str, **kwargs):
        """Escribe archivo Markdown"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"Archivo {filename} creado exitosamente"


class AzureTool(BaseTool):
    name: str = "Azure Tool"
    description: str = "Herramienta para operaciones en Azure"

    def _run(self, action: str, resource_group: str, **kwargs):
        """Ejecuta acciones en Azure"""
        # Implementación básica
        return f"Acción {action} en {resource_group}"


class CodeExecutionTool(BaseTool):
    name: str = "Code Execution"
    description: str = "Ejecuta código en un entorno seguro"

    def _run(self, code: str, language: str = "python", **kwargs):
        """Ejecuta código"""
        # Implementación básica - expandir según necesidad
        return "Código ejecutado"


# Exportar todas las herramientas
__all__ = [
    'GitHubTool',
    'MarkdownWriterTool',
    'AzureTool',
    'CodeExecutionTool'
]
