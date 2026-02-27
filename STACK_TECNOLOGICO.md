# 🎯 STACK TECNOLÓGICO - FÁBRICA IA DEVELOPMENT

---

## RESUMEN EJECUTIVO

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                         STACK TECNOLÓGICO DEFINITIVO                                   │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

╔═══════════════════╦═══════════════════════════╦═════════════════════════════════════╗
║     CAPA          ║      TECNOLOGÍA          ║              VERSIÓN                ║
╠═══════════════════╬═══════════════════════════╬═════════════════════════════════════╣
║  FRONTEND         ║  React + TypeScript       ║  React 19.x                        ║
║                   ║  Tailwind CSS            ║  Tailwind 4.x                      ║
║                   ║  Zustand                 ║  Zustand 5.x (estado)              ║
╠═══════════════════╬═══════════════════════════╬═════════════════════════════════════╣
║  BACKEND          ║  .NET                    ║  .NET 9.0 LTS                      ║
║                   ║  ASP.NET Core            ║  ASP.NET Core 9.0                  ║
║                   ║  C#                      ║  C# 13                             ║
╠═══════════════════╬═══════════════════════════╬═════════════════════════════════════╣
║  IA / ML          ║  Python                  ║  Python 3.12                       ║
║                   ║  FastAPI                 ║  FastAPI 0.115.x                   ║
║                   ║  CrewAI                  ║  CrewAI 0.80.x                     ║
║                   ║  LangChain               ║  LangChain 0.3.x                   ║
╠═══════════════════╬═══════════════════════════╬═════════════════════════════════════╣
║  BASE DE DATOS    ║  PostgreSQL              ║  PostgreSQL 17.x (Flexible)        ║
║                   ║  Entity Framework Core   ║  EF Core 9.x                       ║
╠═══════════════════╬═══════════════════════════╬═════════════════════════════════════╣
║  INFRAESTRUCTURA  ║  Azure                  ║  Cloud Native                      ║
║                   ║  Docker                 ║  Docker 27.x                       ║
║                   ║  Terraform              ║  Terraform 1.9.x                   ║
║                   ║  Kubernetes             ║  AKS (Azure Kubernetes)            ║
╚═══════════════════╩═══════════════════════════╩═════════════════════════════════════╝
```

---

## 1. FRONTEND

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                         FRONTEND STACK                                                   │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

╔═══════════════════════════════════════════════════════════════════════════════════════════╗
║  REACT 19 + TAILWIND + ZUSTAND                                                         ║
╚═══════════════════════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────┬────────────────────────────────────────────┐
│  TECNOLOGÍA                                │  JUSTIFICACIÓN                            │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│  React 19.x                                │  Última versión estable                   │
│                                             │  - Server Components                     │
│                                             │  - Actions (async/await en formularios) │
│                                             │  - Mejor rendimiento                     │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│  TypeScript 5.x                            │  Tipado estático obligatorio              │
│                                             │  - Mejor DX (Developer Experience)       │
│                                             │  - Menos bugs en producción             │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│  Tailwind CSS 4.x                          │  Utilidad-first CSS                      │
│                                             │  - Desarrollo rápido                     │
│                                             │  - Bundle pequeño                        │
│                                             │  - Easy customization                   │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│  Zustand 5.x                               │  Estado global ligero                    │
│                                             │  - Solo 1KB (vs 7KB de Redux)          │
│                                             │  - Sin boilerplate                      │
│                                             │  - TypeScript friendly                  │
│                                             │  - Performance excelente                │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│  Vite 6.x                                  │  Build tool moderno                      │
│                                             │  - HMR ultra rápido                     │
│                                             │  - Optimizaciones automáticas           │
└─────────────────────────────────────────────┴────────────────────────────────────────────┘
```

### ¿Por qué Zustand? (vs Redux/Jotai)

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│  COMPARATIVA STATE MANAGEMENT                                                            │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

    ╔═══════════════╦══════════╦══════════╦══════════╦════════════╗
    ║  CRITERIO     ║  Zustand ║   Jotai  ║   Redux   ║   Context  ║
    ╠═══════════════╬══════════╬══════════╬══════════╬════════════╣
    ║  Tamaño       ║   1KB    ║   3KB    ║   7KB    ║    0KB     ║
    ║  Boilerplate  ║    Low   ║    Low   ║   High   ║    Low     ║
    ║  Curva Apr.  ║   Easy   ║  Medium  ║   Hard   ║   Easy     ║
    ║  Performance ║  Excellent║ Excellent║   Good   ║   Poor     ║
    ║  TypeScript  ║ Native   ║ Native   ║   Good   ║   Good     ║
    ╚═══════════════╩══════════╩══════════╩══════════╩════════════╝

    ✅ ZUSTAND = Simple + Performant + TypeScript
```

### Estructura Frontend

```
📁 frontend/
├── 📁 src/
│   ├── 📁 components/          # Componentes reutilizables
│   │   ├── 📁 ui/             # UI base (buttons, inputs)
│   │   └── 📁 features/       # Componentes de features
│   ├── 📁 pages/              # Páginas/routes
│   ├── 📁 stores/            # Zustand stores
│   │   ├── authStore.ts
│   │   ├── userStore.ts
│   │   └── notificationStore.ts
│   ├── 📁 services/          # API calls
│   ├── 📁 hooks/             # Custom hooks
│   ├── 📁 types/             # TypeScript types
│   ├── 📁 utils/             # Utilidades
│   ├── 📁 App.tsx
│   └── 📁 main.tsx
├── 📁 public/
├── tailwind.config.js
├── vite.config.ts
├── tsconfig.json
└── package.json
```

---

## 2. BACKEND

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                         BACKEND STACK                                                    │
└─────────────────────────────────────────────────────────────────┘

╔════════════════════════════════════════════════════════════════────────────────────────────═══════════════════════════╗
║  .NET 9.0 (LTS) - C# 13                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────┬────────────────────────────────────────────┐
│  TECNOLOGÍA                                │  JUSTIFICACIÓN                            │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│  .NET 9.0 LTS                             │  Última versión LTS (24 meses soporte)    │
│  (Nov 2024 - Nov 2026)                    │  - Mejor rendimiento (1000+ mejoras)      │
│                                             │  - Native AOT disponible                  │
│                                             │  - GC adaptativo                         │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│  ASP.NET Core 9.0                          │  Framework web moderno                    │
│                                             │  - Minimal APIs                           │
│                                             │  - SignalR para real-time               │
│                                             │  - Blazor WASM/Hybrid                    │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│  C# 13                                     │  Última versión del lenguaje              │
│                                             │  - Primary constructors                  │
│                                             │  - Pattern matching improvements         │
│                                             │  - Collection expressions                │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│  Entity Framework Core 9.x                  │  ORM oficial de Microsoft                │
│                                             │  - Code First migrations                 │
│                                             │  - LINQ queries                          │
│                                             │  - Multi-provider (PostgreSQL, SQL Srv) │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│  Dapper (micro-ORM)                        │  Para queries complejos                   │
│                                             │  - Alto rendimiento                      │
│                                             │  - SQL plano cuando se necesita         │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│  Minimal APIs                              │  Endpoints con menos boilerplate          │
│                                             │  - Perfecto para microservices          │
│                                             │  - Route handlers simples                │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│  MediatR                                  │  CQRS/Mediator pattern                   │
│                                             │  - Separación Commands/Queries          │
│                                             │  - Pipeline behaviors                    │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│  FluentValidation                         │  Validación declarativa                   │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│  Swashbuckle/OpenAPI                       │  Documentación API automática            │
└─────────────────────────────────────────────┴────────────────────────────────────────────┘
```

### ¿Por qué .NET 9?

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│  .NET 9 vs VERSIONES ANTERIORES                                                         │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

    ╔═══════════════════╦══════════╦══════════╦══════════╦══════════╗
    ║  CARACTERÍSTICA   ║   .NET 9 ║   .NET 8 ║   .NET 7 ║   .NET 6 ║
    ╠═══════════════════╬══════════╬══════════╬══════════╬══════════╣
    ║  LTS              ║    ✅    ║    ✅    ║    ❌    ║    ✅    ║
    ║  Soporte          ║  24 meses║  18 meses║  18 meses║  12 meses║
    ║  Rendimiento      ║  +20%    ║   Base   ║   +10%   ║   Base   ║
    ║  Native AOT       ║   ✅     ║    ✅    ║    ✅    ║    ❌    ║
    ║  GC Adaptativo    ║   ✅     ║    ❌    ║    ❌    ║    ❌    ║
    ╚═══════════════════╩══════════╩══════════╩══════════╩══════════╝

    ✅ .NET 9 = LTS + Mejor Rendimiento + Native AOT
```

### Estructura Backend (Clean Architecture)

```
📁 backend/
├── 📁 src/
│   ├── 📁 API/                     # Capa de Presentación
│   │   ├── 📁 Controllers/
│   │   ├── 📁 Endpoints/           # Minimal APIs
│   │   ├── 📁 Filters/
│   │   ├── 📁 Middlewares/
│   │   └── Program.cs
│   │
│   ├── 📁 Application/             # Capa de Aplicación
│   │   ├── 📁 Commands/            # CQRS Commands
│   │   ├── 📁 Queries/            # CQRS Queries
│   │   ├── 📁 Handlers/
│   │   ├── 📁 DTOs/
│   │   ├── 📁 Interfaces/
│   │   └── 📁 Behaviors/          # Pipeline behaviors
│   │
│   ├── 📁 Domain/                  # Capa de Dominio
│   │   ├── 📁 Entities/
│   │   ├── 📁 ValueObjects/
│   │   ├── 📁 Aggregates/
│   │   ├── 📁 Repositories/        # Interfaces
│   │   └── 📁 Services/            # Interfaces
│   │
│   ├── 📁 Infrastructure/          # Capa de Infraestructura
│   │   ├── 📁 Persistence/        # EF Core + PostgreSQL
│   │   ├── 📁 Repositories/       # Implementaciones
│   │   ├── 📁 Services/          # Implementaciones
│   │   └── 📁 Authentication/
│   │
│   └── 📁 Shared/                  # Código compartido
│       ├── 📁 Common/
│       ├── 📁 Errors/
│       └── 📁 Constants/
│
├── 📁 tests/
│   ├── 📁 Unit/
│   └── 📁 Integration/
│
├── backend.sln
├── Dockerfile
└── README.md
```

---

## 3. IA / ML

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                         IA STACK                                                         │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

╔═══════════════════════════════════════════════════════════════════════════════════════════╗
║  Python 3.12 + CrewAI + FastAPI                                                         ║
╚═══════════════════════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────┬────────────────────────────────────────────┐
│  TECNOLOGÍA                                │  JUSTIFICACIÓN                            │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│  Python 3.12                              │  Última versión estable (Oct 2023)         │
│                                             │  - 25% más rápido que 3.11                │
│                                             │  - type parameter generics                │
│                                             │  - Mejor soporte typing                   │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│  FastAPI 0.115.x                          │  Framework web moderno para IA             │
│                                             │  - Async/await nativo │
│                                             │  - Document                    ación automática (Swagger)    │
│                                             │  - Validación con Pydantic               │
│                                             │  - Alto rendimiento (asyncio)            │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│  CrewAI 0.80.x                            │  Orquestación de agentes                 │
│                                             │  - Agentes con roles específicos         │
│                                             │  - Herramientas personalizables         │
│                                             │  - Memoria y contexto                   │
│                                             │  - Integración con LangChain            │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│  LangChain 0.3.x                           │  Framework para LLMs                     │
│                                             │  - Chains y Agents                       │
│                                             │  - RAG (Retrieval Augmented Generation) │
│                                             │  - Memory y Callbacks                   │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│  LangGraph                                 │  Orquestación avanzada de agentes         │
│                                             │  - Grafos directed                       │
│                                             │  - Control de flujo complejo             │
│                                             │  - Persistencia de estado                │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│  Azure OpenAI                             │  Modelos LLM                              │
│                                             │  - GPT-4 Turbo                          │
│                                             │  - Embeddings                           │
│                                             │  - Speech (opcional)                    │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│  ChromaDB / pgvector                      │  Vector store para RAG                    │
│                                             │  - Búsqueda semántica                    │
│                                             │  - Embeddings storage                    │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│  Pydantic 2.x                             │  Validación de datos                     │
│                                             │  - Modelos tipados                       │
│                                             │  - Serialización                         │
└─────────────────────────────────────────────┴────────────────────────────────────────────┘
```

### Estructura IA Service

```
📁 ai-service/
├── 📁 src/
│   ├── 📁 agents/                 # Definición de agentes
│   │   ├── requirements_agent.py
│   │   ├── planning_agent.py
│   │   ├── code_agent.py
│   │   ├── test_agent.py
│   │   └── deployment_agent.py
│   │
│   ├── 📁 tools/                 # Herramientas personalizadas
│   │   ├── github_tool.py
│   │   ├── azure_tool.py
│   │   ├── file_tool.py
│   │   └── code_execution.py
│   │
│   ├── 📁 crew/                  # Configuración de crews
│   │   └── hackathon_crew.py
│   │
│   ├── 📁 services/              # Lógica de negocio
│   │   ├── llm_service.py
│   │   ├── rag_service.py
│   │   └── embedding_service.py
│   │
│   ├── 📁 api/                   # Endpoints FastAPI
│   │   ├── routes/
│   │   └── main.py
│   │
│   └── 📁 models/               # Modelos Pydantic
│
├── 📁 prompts/                   # Prompts base
├── requirements.txt
├── Dockerfile
└── uv.lock
```

---

## 4. BASE DE DATOS

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                         BASE DE DATOS: PostgreSQL 17                                      │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

╔═══════════════════════════════════════════════════════════════════════════════════════════╗
║  POSTGRESQL 17 (Flexible Server) - Azure Database                                      ║
╚═══════════════════════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────┬────────────────────────────────────────────┐
│  DECISIÓN                                   │  JUSTIFICACIÓN                            │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│  PostgreSQL 17.x                             │  Última versión estable                    │
│  (Septiembre 2024)                          │  - Vacuum 20x más eficiente               │
│                                             │  - JSON improvements                      │
│                                             │  - In-place upgrades                      │
│                                             │  - Mejor rendimiento                     │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│  Azure Database for PostgreSQL               │  Managed service en Azure                 │
│  Flexible Server                            │  - Alta disponibilidad                    │
│                                             │  - Backups automáticos                    │
│                                             │  - Scaling dinámico                       │
│                                             │  - Geo-redundancia                        │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│  Entity Framework Core 9.x                  │  ORM para .NET                            │
│  + Npgsql                                   │  - Driver nativo PostgreSQL               │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│  pgvector                                   │  Vectores para IA/RAG                     │
│  (extensión)                                │  - Embeddings en la misma DB             │
│                                             │  - Búsqueda semántica                    │
└─────────────────────────────────────────────┴────────────────────────────────────────────┘
```

### ¿PostgreSQL vs SQL Server?

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│  POSTGRESQL vs SQL SERVER                                                              │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

    ╔═══════════════════╦═══════════════════╦════════════════════════════╗
    ║  CRITERIO         ║  PostgreSQL 17   ║  SQL Server 2022          ║
    ╠═══════════════════╬═══════════════════╬════════════════════════════╣
    ║  Costo            ║  ⭐ Gratis/Open   ║  💰 $$$$ (Licencia)        ║
    ║                   ║  Azure: $50+/mes ║  Azure: $200+/mes         ║
    ╠═══════════════════╬═══════════════════╬════════════════════════════╣
    ║  Escalabilidad    ║  ⭐ Excelente    ║    ✅ Buena               ║
    ║  Cloud Native     ║  ⭐ Native      ║    ⚠️  Azure-only         ║
    ╠═══════════════════╬═══════════════════╬════════════════════════════╣
    ║  IA/ML            ║  ⭐ pgvector    ║    ❌  No tiene           ║
    ║  Vector Search    ║  Native        ║    Requiere Azure AI     ║
    ╠═══════════════════╬═══════════════════╬════════════════════════════╣
    ║  JSON/JSONB       ║  ⭐ Excelente    ║    ✅ Bueno               ║
    ║  NoSQL            ║  Native         ║    -                       ║
    ╠═══════════════════╬═══════════════════╬════════════════════════════╣
    ║  Rendimiento      ║  ⭐ Excelente    ║    ✅ Bueno               ║
    ║  OLTP             ║  Optimizado     ║    Optimizado             ║
    ╠═══════════════════╬═══════════════════╬════════════════════════════╣
    ║  Ecosistema       ║  ⭐ Grande      ║    ✅ Grande              ║
    ║  Open Source      ║  ✅             ║    ❌                      ║
    ╚═══════════════════╩═══════════════════╩════════════════════════════╝

    ✅ POSTGRESQL = Mejor para IA + Menor Costo + Open Source
```

### Modelo de Datos (Arquitectura Hexagonal)

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                         ARQUITECTURA HEXAGONAL                                           │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

    ┌─────────────────────────────────────────────────────────────────────────────┐
    │                           FRONTEND (React)                                  │
    │                     ┌─────────────────────────────┐                         │
    │                     │     Zustand (Estado)        │                         │
    │                     └─────────────────────────────┘                         │
    └─────────────────────────────────────────────────────────────────────────────┘
                                        │ HTTP/REST
    ┌─────────────────────────────────────────────────────────────────────────────┐
    │                         BACKEND (.NET 9)                                   │
    │  ┌──────────────────────────────────────────────────────────────────────┐   │
    │  │                      API LAYER                                      │   │
    │  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐     │   │
    │  │  │ Controllers │  │ Minimal APIs│  │  DTOs / Mappers        │     │   │
    │  │  └─────────────┘  └─────────────┘  └─────────────────────────┘     │   │
    │  └──────────────────────────────────────────────────────────────────────┘   │
    │                                    │                                        │
    │  ┌──────────────────────────────────────────────────────────────────────┐   │
    │  │                   APPLICATION LAYER                                  │   │
    │  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐     │   │
    │  │  │  Commands   │  │  Queries   │  │  MediatR Handlers     │     │   │
    │  │  │  (CQRS)    │  │  (CQRS)    │  │  (Mediator Pattern)   │     │   │
    │  │  └─────────────┘  └─────────────┘  └─────────────────────────┘     │   │
    │  │                                                                  │   │
    │  │  ┌─────────────────────────────────────────────────────────────┐   │   │
    │  │  │              PORTS (Interfaces)                            │   │   │
    │  │  │  IUserRepository │ ICourseRepository │ INotificationService│   │   │
    │  │  └─────────────────────────────────────────────────────────────┘   │   │
    │  └──────────────────────────────────────────────────────────────────────┘   │
    │                                    │                                        │
    │  ┌──────────────────────────────────────────────────────────────────────┐   │
    │  │                     DOMAIN LAYER                                    │   │
    │  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐     │   │
    │  │  │  Entities   │  │   Value     │  │     Domain             │     │   │
    │  │  │             │  │   Objects   │  │     Services           │     │   │
    │  │  └─────────────┘  └─────────────┘  └─────────────────────────┘     │   │
    │  └──────────────────────────────────────────────────────────────────────┘   │
    │                                    │                                        │
    │  ┌──────────────────────────────────────────────────────────────────────┐   │
    │  │                  INFRASTRUCTURE LAYER                               │   │
    │  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐     │   │
    │  │  │ EF Core     │  │  Repository │  │    External            │     │   │
    │  │  │ (PostgreSQL)│  │  Impl.     │  │    Services            │     │   │
    │  │  └─────────────┘  └─────────────┘  └─────────────────────────┘     │   │
    │  └──────────────────────────────────────────────────────────────────────┘   │
    └─────────────────────────────────────────────────────────────────────────────┘
                                        │
    ┌─────────────────────────────────────────────────────────────────────────────┐
    │                    AI SERVICE (Python 3.12)                               │
    │  ┌──────────────────────────────────────────────────────────────────────┐   │
    │  │  CrewAI Agents → FastAPI → PostgreSQL (pgvector)                   │   │
    │  └──────────────────────────────────────────────────────────────────────┘   │
    └─────────────────────────────────────────────────────────────────────────────┘
```

---

## 5. INFRAESTRUCTURA (AZURE)

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                         INFRAESTRUCTURA AZURE                                            │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

╔═══════════════════════════════════════════════════════════════════════════════════════════╗
║  SERVICIOS AZURE SUGERIDOS                                                             ║
╚═══════════════════════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────┬────────────────────────────────────────────┐
│  SERVICIO                                  │  USO                                      │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│  Azure App Service (Linux)                  │  Hosting Backend .NET                      │
│  - Tier: Premium v3 P1v3                    │  - Contenedores                           │
│  - Price: ~$150/mes                         │  - Auto-scaling                           │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│  Azure App Service (Linux)                  │  Hosting Frontend React                    │
│  - Tier: Standard S1                         │  - Static Web Apps opción                 │
│  - Price: ~$30/mes                          │                                           │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│  Azure Database for PostgreSQL               │  Base de datos principal                  │
│  - Flexible Server (B1)                       │  - $50/mes                                │
│  - 2 vCores, 512GB                          │  - Con pgvector                           │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│  Azure OpenAI                               │  Modelos LLM                              │
│  - GPT-4 Turbo deployment                    │  - Por tokens                             │
│  - Embeddings deployment                     │  - ~$30-60/1M tokens                      │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│  Azure Container Registry (ACR)              │  Imágenes Docker                          │
│  - Tier: Standard                           │  - $5/mes                                 │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│  Azure Key Vault                             │  Secrets y Certificados                   │
│  - Tier: Standard                           │  - $0.03/10k ops                          │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│  Azure Application Insights                  │  Monitoreo                                │
│  - Tier: Per GB                             │  - ~$2.30/GB                              │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│  Azure Front Door / App Gateway              │  SSL, WAF, CDN                           │
│  - Tier: Standard                           │  - ~$25/mes                              │
├─────────────────────────────────────────────┼────────────────────────────────────────────┤
│  Azure Virtual Network                       │  Red virtual                              │
│  - VNet: /24                                │  - Aislamiento                            │
└─────────────────────────────────────────────┴────────────────────────────────────────────┘

COSTO ESTIMADO MENSUAL: ~$260-350/mes (Producción)
COSTO ESTIMADO HACKATHON: ~$5-10 (usando créditos Azure)
```

---

## 6. RESUMEN FINAL

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                         STACK COMPLETO                                                    │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

    ╔═══════════════════════════════════════════════════════════════════════════════════╗
    ║  FRONTEND                    ║  BACKEND         ║  IA SERVICE    ║  DATABASE       ║
    ╠══════════════════════════════╬══════════════════╬═════════════════╬═════════════════╣
    ║  React 19                    ║  .NET 9.0 LTS   ║  Python 3.12   ║  PostgreSQL 17  ║
    ║  TypeScript 5                ║  ASP.NET Core 9 ║  FastAPI       ║  EF Core 9      ║
    ║  Tailwind 4                  ║  C# 13          ║  CrewAI        ║  pgvector       ║
    ║  Zustand 5                  ║  Minimal APIs   ║  LangChain     ║                 ║
    ║  Vite 6                      ║  CQRS/MediatR   ║  Azure OpenAI  ║                 ║
    ╚══════════════════════════════╩══════════════════╩═════════════════╩═════════════════╝

    ╔═══════════════════════════════════════════════════════════════════════════════════╗
    ║  ARQUITECTURA: Clean Architecture + Hexagonal                                     ║
    ║  INFRA: Azure Cloud Native                                                        ║
    ║  CONTENEDORES: Docker + Kubernetes (AKS)                                         ║
    ║  IaC: Terraform                                                                  ║
    ║  CI/CD: GitHub Actions                                                            ║
    ╚═══════════════════════════════════════════════════════════════════════════════════╝
```

---

## 7. VERSIONES EXACTAS INSTALAR

```json
{
  "frontend": {
    "react": "^19.0.0",
    "typescript": "^5.7.0",
    "tailwindcss": "^4.0.0",
    "zustand": "^5.0.0",
    "vite": "^6.0.0"
  },
  "backend": {
    "dotnet": "9.0",
    "aspnetcore": "9.0",
    "csharp": "13.0",
    "efcore": "9.0.0",
    "mediatr": "12.4.0"
  },
  "ia": {
    "python": "3.12",
    "fastapi": "0.115.0",
    "crewai": "0.80.0",
    "langchain": "0.3.0",
    "langgraph": "0.2.0"
  },
  "database": {
    "postgresql": "17",
    "efcore": "9.0.0",
    "npgsql": "9.0.0"
  },
  "infra": {
    "docker": "27.0.0",
    "terraform": "1.9.0",
    "kubectl": "1.31.0"
  }
}
```

---

## 8. PRÓXIMOS PASOS

```
□ 1. Crear repositorio base con estructura definida
□ 2. Configurar Docker Compose para desarrollo local
□ 3. Configurar GitHub Actions para CI/CD
□ 4. Crear template de .NET con Clean Architecture
□ 5. Crear template de React con Vite + Tailwind + Zustand
□ 6. Configurar Azure OpenAI
□ 7. Probar agentes IA con CrewAI
□ 8. Documentar en README
```

¿Te parece este stack? ¿Ajustamos algo?