# PLAN DE EQUIPO: 20 PERSONAS PARA EL HACKATHON

---

## 1. ESTRUCTURA DEL EQUIPO

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                         ORGANIZACIÓN DEL EQUIPO (20 personas)                            │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

                         ┌─────────────────┐
                         │   STEERING     │
                         │   COMMITTEE    │
                         │  (3 personas)  │
                         │  CIO + PO +    │
                         │  Tech Lead     │
                         └────────┬────────┘
                                  │
         ┌────────────────────────┼────────────────────────┐
         │                        │                        │
         ▼                        ▼                        ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   EQUIPO A     │    │   EQUIPO B     │    │   EQUIPO C     │
│   (Frontend)   │    │   (Backend)    │    │   (Infra/DevOps)│
│  (7 personas)  │    │  (7 personas)  │    │  (6 personas)  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                        │                        │
         ▼                        ▼                        ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ PRODUCT OWNER  │    │ TECH LEAD     │    │ DEVOPS LEAD    │
│ (1 persona)    │    │ (1 persona)   │    │ (1 persona)    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

---

## 2. DISTRIBUCIÓN DE ROLES

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                         ROLES DEL EQUIPO                                                 │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════════════════════════════════════
STEERING COMMITTEE (3 personas)
═══════════════════════════════════════════════════════════════════════════════════════════

┌─────────────────────┬──────────────────────────────────────────────────────────────────┐
│ ROL                 │ RESPONSABILIDAD                                                 │
├─────────────────────┼──────────────────────────────────────────────────────────────────┤
│ CIO                 │ Decisiones estratégicas, validación final, presentación       │
│ Product Owner       │ Define requisitos, prioriza features, valida entregables        │
│ Tech Lead           │ Supervisa arquitectura, approves decisiones técnicas           │
└─────────────────────┴──────────────────────────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════════════════════════════════════
EQUIPO A: FRONTEND (7 personas)
═══════════════════════════════════════════════════════════════════════════════════════════

┌─────────────────────┬──────────────────────────────────────────────────────────────────┐
│ ROL                 │ RESPONSABILIDAD                                                 │
├─────────────────────┼──────────────────────────────────────────────────────────────────┤
│ Frontend Lead       │ Coordina equipo frontend, revisa código, integra con backend    │
│ UI Designer         │ Diseño de interfaces, experiencia de usuario                    │
│ React Developer 1   │ Componentes principales                                         │
│ React Developer 2   │ Páginas y routing                                              │
│ React Developer 3   │ Integración API                                                 │
│ QA Frontend         │ Pruebas visuales, responsive, UX                               │
│ UX Researcher       │ Validación con usuarios, feedback                               │
└─────────────────────┴──────────────────────────────────────────────────────────────────┘

EQUIPO TRABAJA CON:
  - Code Agent (Frontend)
  - Test Agent (Frontend)
  - Deployment Agent

═══════════════════════════════════════════════════════════════════════════════════════════
EQUIPO B: BACKEND (7 personas)
═══════════════════════════════════════════════════════════════════════════════════════════

┌─────────────────────┼──────────────────────────────────────────────────────────────────┐
│ ROL                 │ RESPONSABILIDAD                                                 │
├─────────────────────┼──────────────────────────────────────────────────────────────────┤
│ Backend Lead        │ Coordina equipo backend, revisa arquitectura API               │
│ Python Developer 1  │ Modelos de datos, ORM                                         │
│ Python Developer 2  │ Endpoints API, autenticación                                   │
│ Python Developer 3  │ Lógica de negocio, servicios                                   │
│ Database Admin      │ Diseño DB, migraciones, optimización                          │
│ QA Backend          │ Pruebas API, integración, rendimiento                         │
│ Security Analyst    │ Revisión de seguridad código backend                          │
└─────────────────────┴──────────────────────────────────────────────────────────────────┘

EQUIPO TRABAJA CON:
  - Code Agent (Backend)
  - Test Agent (API)
  - Security Agent

═══════════════════════════════════════════════════════════════════════════════════════════
EQUIPO C: INFRA/DEVOPS (6 personas)
═══════════════════════════════════════════════════════════════════════════════════════════

┌─────────────────────┼──────────────────────────────────────────────────────────────────┐
│ ROL                 │ RESPONSABILIDAD                                                 │
├─────────────────────┼──────────────────────────────────────────────────────────────────┤
│ DevOps Lead         │ Coordina infraestructura, pipelines, deployments              │
│ Cloud Architect     │ Diseño arquitectura Azure, costos, scaling                    │
│ Terraform Dev       │ Infrastructure as Code                                          │
│ Docker/K8s Dev      │ Contenedores, orquestación                                     │
│ CI/CD Engineer      │ Pipelines, automatización                                      │
│ Monitoring Engineer │ Logs, métricas, alertas                                        │
└─────────────────────┴──────────────────────────────────────────────────────────────────┘

EQUIPO TRABAJA CON:
  - Architecture Agent
  - Deployment Agent
  - Security Agent
```

---

## 3. WORKSPACES Y SEGREGACIÓN

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                         WORKSPACES SEPARADOS                                            │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────────────┐
│ REPO PRINCIPAL: github.com/empresa/hackathon                                        │
│                                                                                      │
│ Branch principal: main                                                              │
│ Branches por equipo:                                                                │
│   ├── feature/frontend-xxx    (Equipo A)                                           │
│   ├── feature/backend-xxx     (Equipo B)                                            │
│   └── feature/infra-xxx       (Equipo C)                                            │
│                                                                                      │
│ Merges: Solo mediante PR aprobado por Lead del equipo                              │
└─────────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────────────┐
│ WORKSPACE EQUIPO A (Frontend) - 7 personas                                          │
│                                                                                      │
│ Carpeta: src/frontend/                                                             │
│ Canal Slack: #hackathon-frontend                                                   │
│ Standups: Cada 2 horas                                                             │
│ Revisión: PRs entre pares → Frontend Lead → Merge                                  │
└─────────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────────────┐
│ WORKSPACE EQUIPO B (Backend) - 7 personas                                           │
│                                                                                      │
│ Carpeta: src/backend/                                                              │
│ Canal Slack: #hackathon-backend                                                    │
│ Standups: Cada 2 horas                                                             │
│ Revisión: PRs entre pares → Backend Lead → Merge                                   │
└─────────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────────────┐
│ WORKSPACE EQUIPO C (Infra/DevOps) - 6 personas                                     │
│                                                                                      │
│ Carpeta: infrastructure/                                                           │
│ Canal Slack: #hackathon-infra                                                      │
│ Standups: Cada 2 horas                                                             │
│ Revisión: PRs entre pares → DevOps Lead → Merge                                   │
└─────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. COMO USAR LOS AGENTES IA (EN EQUIPO)

### METODOLOGÍA: "IA como Asistente, Humano como Revisor"

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                         FLUJO DE TRABAJO CON IA                                        │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

         ┌──────────────────────────────────────────────────────────────┐
         │  DESARROLLADOR (Humano)                                     │
         │                                                              │
         │  1. Define qué necesita (prompt claro)                       │
         │  2. Envía a la IA                                          │
         │  3. Revisa el resultado                                    │
         │  4. Aprueba o solicita cambios                             │
         │  5. Push a GitHub                                          │
         └──────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
         ┌──────────────────────────────────────────────────────────────┐
         │  IA (Code Agent)                                          │
         │                                                              │
         │  - Recibe el prompt                                        │
         │  - Genera código                                           │
         │  - Devuelve resultado                                      │
         └──────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
         ┌──────────────────────────────────────────────────────────────┐
         │  CODE REVIEW (Humano)                                      │
         │                                                              │
         │  - Revisa calidad                                          │
         │  - Verifica seguridad                                      │
         │  - Aprueba PR                                              │
         └──────────────────────────────────────────────────────────────┘
```

---

## 5. CADA PERSONA USA LA IA ASÍ

### Ejemplo: Desarrollador Frontend

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                 ESCENARIO: Desarrollador necesita un componente                        │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

1. DESARROLLADOR define necesidad:
   ─────────────────────────────────
   "Necesito un componente de tabla que muestre:
    - Lista de empleados
    - Columnas: nombre, email, departamento, estado
    - Ordenar por cualquier columna
    - Filtrar por búsqueda
    - Paginación
    - Estilo: Material Design"

2. ENVÍA A IA (Copilot/ChatGPT):
   ─────────────────────────────────
   Prompt:
   """
   Genera un componente React usando TypeScript:
   - Tabla con columnas: nombre, email, departamento, estado
   - Sorting por columna
   - Filtering con search input
   - Paginación (10 por página)
   - Estilo: Material UI
   - Tipos TypeScript para Employee
   - Use hooks para estado
   """

3. IA GENERA:
   ─────────────────────────────────
   Componente React + TypeScript + Tests

4. DESARROLLADOR REVISA:
   ─────────────────────────────────
   ✓ ¿Funciona?
   ✓ ¿Sigue patrones del proyecto?
   ✓ ¿Tiene tests?
   ✗ Falta - agregar botón de exportar

5. AJUSTA Y PUSH:
   ─────────────────────────────────
   - Ajusta lo necesario
   - Crea branch feature/tabla-empleados
   - Push a GitHub
   - Crea PR para code review

6. CODE REVIEW:
   ─────────────────────────────────
   - Frontend Lead revisa
   - Aprueba o solicita cambios
   - Merge a main
```

---

## 6. MATRIZ: PERSONA → HERRAMIENTA IA

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                         QUÉ IA USA CADA ROL                                            │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

╔═══════════════════════════╦════════════════════════════╦═════════════════════════════════╗
║ PERSONA / ROL            ║ HERRAMIENTA IA PRINCIPAL   ║ USO                            ║
╠═══════════════════════════╬════════════════════════════╬═════════════════════════════════╣
║ Product Owner             ║ ChatGPT / Copilot         ║ Generar requirements           ║
║                           ║                           ║ Analizar historias de usuario  ║
╠═══════════════════════════╬════════════════════════════╬═════════════════════════════════╣
║ Frontend Lead             ║ Copilot + ChatGPT         ║ Revisar código                 ║
║                           ║                           ║ Generar componentes complejos   ║
╠═══════════════════════════╬════════════════════════════╬═════════════════════════════════╣
║ React Developer           ║ Copilot (VS Code)         ║ Code completion               ║
║                           ║                           ║ Generar componentes            ║
╠═══════════════════════════╬════════════════════════════╬═════════════════════════════════╣
║ UI Designer               ║ ChatGPT / DALL-E          ║ Generar ideas UI                ║
║                           ║                           ║ Prototipos rápidos              ║
╠═══════════════════════════╬════════════════════════════╬═════════════════════════════════╣
║ Python Developer          ║ Copilot + ChatGPT         ║ Generar código                 ║
║                           ║                           ║ Debugging                      ║
╠═══════════════════════════╬════════════════════════════╬═════════════════════════════════╣
║ Database Admin            ║ ChatGPT                   ║ Generar queries                 ║
║                           ║                           ║ Optimización                   ║
╠═══════════════════════════╬════════════════════════════╬═════════════════════════════════╣
║ Cloud Architect           ║ ChatGPT                   ║ Diseñar arquitectura          ║
║                           ║                           ║ Comparar servicios             ║
╠═══════════════════════════╬════════════════════════════╬═════════════════════════════════╣
║ Terraform Dev             ║ ChatGPT                   ║ Generar código IaC             ║
║                           ║                           ║ Debug config                   ║
╠═══════════════════════════╬════════════════════════════╬═════════════════════════════════╣
║ CI/CD Engineer            ║ ChatGPT                   ║ Generar pipelines              ║
║                           ║                           ║ Troubleshooting               ║
╠═══════════════════════════╬════════════════════════════╬═════════════════════════════════╣
║ QA (Frontend/Backend)    ║ ChatGPT                   ║ Generar casos de prueba       ║
║                           ║                           ║ Generar test data              ║
╠═══════════════════════════╬════════════════════════════╬═════════════════════════════════╣
║ Security Analyst          ║ ChatGPT + Semgrep         ║ Análisis de seguridad          ║
║                           ║                           ║ Recomendaciones               ║
╠═══════════════════════════╬════════════════════════════╬═════════════════════════════════╣
║ Monitoring Engineer       ║ ChatGPT                   ║ Configurar alertas            ║
║                           ║                           ║ Dashboards                    ║
╚═══════════════════════════╩════════════════════════════╩═════════════════════════════════╝
```

---

## 7. CRONOGRAMA DEL DÍA

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                         DÍA DEL HACKATHON - 7 HORAS                                      │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

8:30 - 9:00  │ LLEGADA Y SETUP
              │ - Todos acceden a sus estaciones
              │ - Verifican acceso a GitHub, Azure, VS Code
              │ - Verifican conexión a Copilot/ChatGPT

9:00 - 9:30  │ KICKOFF (Todos)
              │ - Presentación del proyecto
              │ - Revisión de objetivos
              │ - Asignación de roles

9:30 - 10:30 │ FASE 1: REQUISITOS (Equipo completo)
              │ - Product Owner presenta necesidad
              │ - Requirements Agent genera historias
              │ - Todos revisan y dan feedback

10:30 - 11:30│ FASE 2: PLAN + ARQUITECTURA
              │ - Planning Agent crea roadmap
              │ - Architecture Agent propone stack
              │ - Tech Leads approves

11:30 - 12:30│ FASE 3: DESARROLLO - Sprint 1
              │ ┌─────────────┬─────────────┬─────────────┐
              │ │  EQUIPO A   │  EQUIPO B   │  EQUIPO C   │
              │ │  Frontend   │  Backend    │   Infra     │
              │ │  Header     │  Auth       │  Terraform  │
              │ │  Login      │  Models     │  Docker     │
              │ └─────────────┴─────────────┴─────────────┘

12:30 - 13:30│ LUNCH

13:30 - 14:30│ FASE 4: DESARROLLO - Sprint 2
              │ ┌─────────────┬─────────────┬─────────────┐
              │ │  EQUIPO A   │  EQUIPO B   │  EQUIPO C   │
              │ │  Dashboard  │  CRUD       │  CI/CD      │
              │ │  Tablas     │  API        │  Azure      │
              │ └─────────────┴─────────────┴─────────────┘

14:30 - 15:30│ FASE 5: TESTING + SECURITY
              │ - Test Agent corre pruebas
              │ - Security Agent scan
              │ - QA manual validation
              │ - Fixes de bugs

15:30 - 16:00│ FASE 6: DEPLOY + DEMO
              │ - Deployment Agent despliega
              │ - Demo al Steering Committee
              │ - Celebración

16:00 - 16:30│ RETROSPECTIVA
              │ - Qué funcionó
              │ - Qué mejorar
              │ - Lecciones aprendidas
```

---

## 8. CANALES DE COMUNICACIÓN

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                         COMUNICACIÓN DURANTE EL HACKATHON                                 │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

CANALES PRINCIPALES:
═══════════════════════════════════════════════════════════════════════════════════════════

📢 #hackathon-general
   - Anuncios globales
   - Decisiones del Steering Committee
   - Problemas que afectan a todos

💬 #hackathon-frontend
   - Equipo A coordinación
   - Problemas específicos de frontend

💬 #hackathon-backend
   - Equipo B coordinación
   - Problemas específicos de backend

💬 #hackathon-infra
   - Equipo C coordinación
   - Problemas de infraestructura

🔧 #hackathon-tech
   - Problemas técnicos
   - Debugging conjunto

📊 #hackathon-metrics
   - Métricas del hackathon
   - Progreso por equipo

REUNIONES:
═══════════════════════════════════════════════════════════════════════════════════════════

- Standup: Cada 2 horas (15 min)
- Sync de leads: Cada 3 horas (30 min)
- Demo al CIO: 16:00
```

---

## 9. REGLAS DE COLABORACIÓN

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                         REGLAS DEL HACKATHON                                               │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

✓ HACER:
  - Usar GitHub para todo el código
  - Pull requests para cada feature
  - Code review antes de merge
  - Comunicación en canales de Slack
  - Documentar decisiones importantes
  - Pedir ayuda si te atascas (max 30 min)

✗ NO HACER:
  - No hacer push directo a main
  - No trabajar en aislamiento (hablar con el equipo)
  - No asumir que alguien más lo hará
  - No guardar problemas (报告 temprano)
  - No comparar velocidad con otros equipos

⚠️ IMPORTANTE:
  - La IA es un ASISTENTE, tú eres el JEFE
  - Siempre revisa lo que la IA genera
  - Si no entiendes el código, pregunta
  - Prioriza calidad sobre velocidad
```

---

## 10. ACCESSOS Y CREDENCIALES

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                         ACCESSOS REQUERIDOS                                               │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

CADA DESARROLLADOR NECESITA:
═══════════════════════════════════════════════════════════════════════════════════════════

✓ VS Code instalado + Extensions
✓ Acceso a GitHub (repo del hackathon)
✓ Cuenta de Copilot Enterprise
✓ Acceso a ChatGPT Plus (opcional)
✓ Azure CLI instalado
✓ Acceso a Azure Portal (lector)

LEADS ADICIONALMENTE NECESITAN:
═══════════════════════════════════════════════════════════════════════════════════════════

✓ Acceso a Azure Portal (contributor)
✓ Permiso para crear recursos
✓ Acceso a GitHub (admin del repo)
✓ Acceso a Slack/Teams admin
```

---

## 11. QUÉ HACER SI...

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                         TROUBLESHOOTING                                                   │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

😱 "La IA me da código que no funciona"
   → No accepts blindly - always test
   → Report the issue, try again with different prompt
   → Ask teammate for help

😱 "No tengo acceso a..."
   → Ask your lead immediately
   → Escalate to Steering Committee if needed

😱 "Mi código hace merge pero rompe la build"
   → Don't panic
   → Check GitHub Actions logs
   → Ask DevOps for help
   → Revert if necessary

😱 "El deployment falló"
   → Check Azure logs
   → Verify configurations
   → Call DevOps Lead

😱 "Tengo un blocker hace 30 min"
   → Ask in team channel
   → If still stuck, call a "war room" meeting

😱 "El CIO pregunta algo que no sé"
   → Be honest: "Voy a verificar y te confirmo"
   → Don't guess
```

---

## 12. RESUMEN: EQUIPO DE 20

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                         RESUMEN                                                            │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

👥 20 PERSONAS DISTRIBUIDAS EN:

   STEERING COMMITTEE (3)
   └── CIO + PO + Tech Lead
   
   EQUIPO A: FRONTEND (7)
   └── Lead + Designer + 3 Devs + QA + UX
   
   EQUIPO B: BACKEND (7)  
   └── Lead + 3 Devs + DBA + QA + Security
   
   EQUIPO C: INFRA/DEVOPS (6)
   └── Lead + Cloud Arch + 2 Infra + CI/CD + Monitoring

🎯 CADA PERSONA USA IA COMO ASISTENTE

📢 CANALES DE COMUNICACIÓN: Slack dedicado

⏰ CRONOGRAMA: 7 horas (9:00 - 16:30)

🔄 FLUJO: IA genera → Humano revisa → GitHub → Merge → Deploy
```

¿Te parece esta estructura? ¿Ajustamos algo antes del hackathon?