# PLAN PRÁCTICO: CÓMO PASAR ESTO A TU EQUIPO DE 20

---

## 1. ESTRUCTURA EN GITHUB

```
CREAR UN REPO PRINCIPAL:
github.com/tuempresa/ai-factory-hackathon

DENTRO, CREAR 3 SUBPROYECTOS (carpetas):

📁 ai-factory-hackathon/
├── 📁 01-frontend/          ← 7 personas
├── 📁 02-backend/           ← 7 personas  
├── 📁 03-ia-service/        ← 3 personas
└── 📁 04-infrastructure/    ← 3 personas
```

---

## 2. AGENTES EN LA RAÍZ (Un agente por proyecto)

```
EN CADA CARPETA PRINCIPAL, UN AGENTE CLAUDE:

📁 01-frontend/
   └── .claude/              ← ACÁ ESTÁ EL AGENTE
       └── agent.md

📁 02-backend/
   └── .claude/
       └── agent.md

📁 03-ia-service/
   └── .claude/
       └── agent.md

📁 04-infrastructure/
   └── .claude/
       └── agent.md
```

---

## 3. QUÉ DEBE TENER CADA AGENTE (agent.md)

### Ejemplo: Agente Frontend

```markdown
# Agente Frontend - AI Factory

## Rol
Eres un Senior Frontend Developer + UI/UX Expert.

## Especialidad
- React 19 + TypeScript
- Tailwind CSS 4
- Zustand para estado
- Clean Architecture

## Responsibilities
1. Crear componentes siguiendo el diseño
2. Implementar Zustand stores
3. Conectar con API del backend
4. Asegurar calidad de código
5. Hacer code review del equipo

## Reglas
- Siempre usar TypeScript
- Usar Tailwind para estilos
- Tests obligatorios
- Code review antes de merge

## Comandos
- `/create component [nombre]` - Crear componente
- `/create store [nombre]` - Crear Zustand store
- `/review` - Revisar código del equipo
- `/test` - Correr tests
```

---

## 4. CÓMO CREAR LAS TAREAS EN GITHUB (Issues)

### IR A: github.com/tuempresa/ai-factory-hackathon/issues/new

### CREAR ESTAS TAREAS (Templates):

---

#### TAREA 1: Setup Inicial
```
Title: [SETUP] Configurar entorno de desarrollo

Description:
- [ ] Instalar VS Code + extensiones
- [ ] Instalar Node.js 20+
- [ ] Instalar .NET 9 SDK
- [ ] Instalar Python 3.12
- [ ] Configurar Azure CLI
- [ ] Obtener access tokens

Asignar: @todos
Labels: setup, prioridad-alta
Milestone: Sprint 1
```

---

#### TAREA 2: Frontend - Estructura Base
```
Title: [FRONTEND] Crear estructura base del proyecto

Description:
- [ ] Iniciar proyecto con Vite: `npm create vite@latest . --template react-ts`
- [ ] Configurar Tailwind CSS 4
- [ ] Instalar Zustand: `npm install zustand`
- [ ] Crear carpeta src/components/ui
- [ ] Crear carpeta src/stores
- [ ] Configurar eslint + prettier

Assign: @equipo-frontend
Labels: frontend, setup
Milestone: Sprint 1
```

---

#### TAREA 3: Frontend - Componentes UI
```
Title: [FRONTEND] Crear componentes base UI

Description:
- [ ] Button.tsx
- [ ] Input.tsx
- [ ] Card.tsx
- [ ] Modal.tsx
- [ ] Table.tsx
- [ ] Badge.tsx

Assign: @equipo-frontend
Labels: frontend, componentes
Milestone: Sprint 1
```

---

#### TAREA 4: Frontend - Pages
```
Title: [FRONTEND] Crear páginas principales

Description:
- [ ] Login page
- [ ] Dashboard page
- [ ] Empleados page
- [ ] Cursos page
- [ ] Certificaciones page

Assign: @equipo-frontend
Labels: frontend, pages
Milestone: Sprint 2
```

---

#### TAREA 5: Backend - Estructura Clean Architecture
```
Title: [BACKEND] Crear solución .NET con Clean Architecture

Description:
- [ ] Crear solución: `dotnet new sln -n Hackathon`
- [ ] Crear proyectos:
  - `dotnet new webapi -o src/API`
  - `dotnet new classlib -o src/Application`
  - `dotnet new classlib -o src/Domain`
  - `dotnet new classlib -o src/Infrastructure`
- [ ] Agregar referencias entre proyectos
- [ ] Configurar EF Core con PostgreSQL

Assign: @equipo-backend
Labels: backend, setup
Milestone: Sprint 1
```

---

#### TAREA 6: Backend - Entidades
```
Title: [BACKEND] Crear entidades del dominio

Description:
- [ ] Empleado.cs
- [ ] Curso.cs
- [ ] Certificacion.cs
- [ ] Constancia.cs
- [ ] Departamento.cs

Assign: @equipo-backend
Labels: backend, domain
Milestone: Sprint 1
```

---

#### TAREA 7: Backend - APIs
```
Title: [BACKEND] Crear endpoints API

Description:
- [ ] CRUD Empleados (GET, POST, PUT, DELETE)
- [ ] CRUD Cursos
- [ ] CRUD Certificaciones
- [ ] Autenticación JWT
- [ ] Documentación Swagger

Assign: @equipo-backend
Labels: backend, api
Milestone: Sprint 2
```

---

#### TAREA 8: IA Service - Setup
```
Title: [IA] Configurar servicio de IA

Description:
- [ ] Crear proyecto FastAPI: `uvicorn`
- [ ] Instalar CrewAI: `pip install crewai`
- [ ] Configurar Azure OpenAI
- [ ] Crear estructura de agentes

Assign: @equipo-ia
Labels: ia, setup
Milestone: Sprint 1
```

---

#### TAREA 9: IA Service - Agentes
```
Title: [IA] Crear agentes CrewAI

Description:
- [ ] Requirements Agent
- [ ] Planning Agent
- [ ] Code Generator Agent
- [ ] Test Agent
- [ ] Security Agent
- [ ] Deployment Agent

Assign: @equipo-ia
Labels: ia, agentes
Milestone: Sprint 2
```

---

#### TAREA 10: Infrastructure - Azure
```
Title: [INFRA] Configurar infraestructura Azure

Description:
- [ ] Crear Resource Group
- [ ] Configurar PostgreSQL Flexible
- [ ] Configurar App Services
- [ ] Configurar Azure OpenAI
- [ ] Crear Terraform base

Assign: @equipo-infra
Labels: infra, azure
Milestone: Sprint 1
```

---

#### TAREA 11: Integration - Frontend + Backend
```
Title: [INTEGRATION] Conectar Frontend con Backend

Description:
- [ ] Configurar API base URL
- [ ] Crear servicios API en Frontend
- [ ] Integrar Zustand stores con endpoints
- [ ] Testing end-to-end

Assign: @equipo-frontend + @equipo-backend
Labels: integration
Milestone: Sprint 3
```

---

#### TAREA 12: Despliegue Final
```
Title: [DEPLOY] Desplegar a producción

Description:
- [ ] Build frontend: `npm run build`
- [ ] Build backend: `dotnet publish`
- [ ] Desplegar a Azure App Service
- [ ] Verificar salud de la aplicación
- [ ] Tests finales

Assign: @todos
Labels: deploy, prioridad-alta
Milestone: Sprint Final
```

---

## 5. CREAR MILESTONES (Sprints)

```
github.com/tuempresa/ai-factory-hackathon/milestones

CREAR:

1. Sprint 1 (Día 1 - Mañana)
   - Setup + Estructura base
   - Deadline: 10:30 AM

2. Sprint 2 (Día 1 - Tarde)
   - Desarrollo features
   - Deadline: 3:30 PM

3. Sprint Final (Día 1 - Final)
   - Integration + Deploy
   - Deadline: 5:00 PM
```

---

## 6. LABELS SUGERIDOS

```
prioridad-alta (rojo)
frontend (azul)
backend (verde)
ia (morado)
infra (naranja)
setup (gris)
bug (rojo)
documentation (amarillo)
```

---

## 7. CÓMO ASIGNAR AL EQUIPO

```
IR A: github.com/tuempresa/ai-factory-hackathon/settings/teams

CREAR EQUIPOS:

1. @hackathon-frontend (7 personas)
2. @hackathon-backend (7 personas)
3. @hackathon-ia (3 personas)
4. @hackathon-infra (3 personas)

CADA EQUIPO TRABAJA EN SU CARPETA:
- 01-frontend/ → @hackathon-frontend
- 02-backend/ → @hackathon-backend
- 03-ia-service/ → @hackathon-ia
- 04-infrastructure/ → @hackathon-infra
```

---

## 8. RESUMEN RÁPIDO

```
PASO 1: Crear repo en GitHub
        └── github.com/tuempresa/ai-factory-hackathon

PASO 2: Crear 4 carpetas (proyectos)
        ├── 01-frontend/
        ├── 02-backend/
        ├── 03-ia-service/
        └── 04-infrastructure/

PASO 3: Crear tareas en Issues
        └── 12 tareas principales

PASO 4: Crear Milestones (Sprints)
        └── Sprint 1, Sprint 2, Sprint Final

PASO 5: Asignar equipos
        └── 4 equipos de trabajo

PASO 6: Cada persona usa Claude Code
        └── En su carpeta del proyecto
```

---

## 9. COMANDO RÁPIDO PARA CREAR TODO

```bash
# Esto es solo referencia, no ejecutar

REPO: https://github.com/tuempresa/ai-factory-hackathon

TAREAS A CREAR (12 issues):

1. [SETUP] Configurar entorno de desarrollo
2. [FRONTEND] Crear estructura base
3. [FRONTEND] Crear componentes UI
4. [FRONTEND] Crear páginas principales
5. [BACKEND] Crear solución .NET Clean Architecture
6. [BACKEND] Crear entidades del dominio
7. [BACKEND] Crear endpoints API
8. [IA] Configurar servicio de IA
9. [IA] Crear agentes CrewAI
10. [INFRA] Configurar infraestructura Azure
11. [INTEGRATION] Conectar Frontend con Backend
12. [DEPLOY] Desplegar a producción
```

---

¿Te sirve? ¿Algo que ajuste?