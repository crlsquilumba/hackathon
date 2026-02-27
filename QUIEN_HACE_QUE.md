# QUIÉN HACE QUÉ: ROLES Y RESPONSABILIDADES

---

## EL FLUJO COMPLETO

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                         QUIÉN HACE QUÉ                                                │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

    ┌─────────────────────────────────────────────────────────────────────────────┐
    │                         1. REQUISITOS                                      │
    │                                                                         │
    │   👤 PRODUCT OWNER                                                      │
    │   - Dice la necesidad en palabras simples:                               │
    │     "Necesito una plataforma para gestionar certificaciones"            │
    │                                                                         │
    │   → Se la da al REQUIREMENTS AGENT (IA)                                │
    │                                                                         │
    │   🤖 REQUIREMENTS AGENT (IA)                                           │
    │   - Transforma la necesidad en documentos técnicos:                    │
    │     • Historias de usuario                                             │
    │     • Casos de uso                                                    │
    │     • Modelo de datos                                                 │
    │     • Crea el ISSUE en GitHub                                         │
    │                                                                         │
    │   ✅ El ISSUE queda listo para que el equipo trabaje                   │
    └─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
    ┌─────────────────────────────────────────────────────────────────────────────┐
    │                         2. DISEÑO / ARQUITECTURA                        │
    │                                                                         │
    │   🤖 ARCHITECTURE AGENT (IA)                                          │
    │   - Analiza los requisitos                                             │
    │   - Propone la arquitectura:                                           │
    │     • Stack tecnológico                                                │
    │     • Estructura de carpetas                                           │
    │     • Modelo de datos (ERD)                                           │
    │     • Diagramas                                                       │
    │                                                                         │
    │   👤 TECH LEAD (Humano)                                               │
    │   - Revisa la arquitectura propuesta                                   │
    │   - Aprueba o solicita cambios                                         │
    │   - Ajusta si hay consideraciones específicas                         │
    │                                                                         │
    │   ✅ Arquitectura definida y aprobada                                   │
    └─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
    ┌─────────────────────────────────────────────────────────────────────────────┐
    │                         3. DESARROLLO                                    │
    │                                                                         │
    │   🤖 CODE AGENT (IA)                                                  │
    │   - Genera el código base                                             │
    │   - Sigue la arquitectura aprobada                                     │
    │                                                                         │
    │   👤 DESARROLLADORES (Equipo)                                         │
    │   - Revisan el código generado                                         │
    │   - Ajustan si es necesario                                           │
    │   - Completan lo que falta                                             │
    │   - Hacen code review                                                  │
    │                                                                         │
    │   ✅ Código completo y revisado                                        │
    └─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
    ┌─────────────────────────────────────────────────────────────────────────────┐
    │                         4. TESTING + QA                                 │
    │                                                                         │
    │   🤖 TEST AGENT (IA)                                                  │
    │   - Genera tests unitarios                                            │
    │   - Genera tests de integración                                       │
    │                                                                         │
    │   👤 QA (Equipo)                                                      │
    │   - Ejecuta pruebas                                                   │
    │   - Prueba manualmente                                               │
    │   - Encuentra bugs                                                    │
    │                                                                         │
    │   ✅ Código probado y funcionando                                      │
    └─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
    ┌─────────────────────────────────────────────────────────────────────────────┐
    │                         5. DEPLOY                                        │
    │                                                                         │
    │   🤖 DEPLOYMENT AGENT (IA)                                           │
    │   - Despliega a Azure                                                │
    │   - Configura servicios                                              │
    │   - Verifica que funcione                                            │
    │                                                                         │
    │   👤 DEVOPS (Equipo)                                                 │
    │   - Supervisa el deploy                                              │
    │   - Aprueba si todo está bien                                         │
    │                                                                         │
    │   ✅ Aplicación en producción                                         │
    └─────────────────────────────────────────────────────────────────────────────┘
```

---

## RESUMEN: QUIÉN HACE QUÉ

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                         TABLA DE RESPONSABILIDADES                                       │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

╔═══════════════════════════╦═══════════════════╦═══════════════════╦═══════════════════╗
║         FASE             ║       IA (AGENTE) ║   HUMANO (ROLES) ║      OUTPUT       ║
╠═══════════════════════════╬═══════════════════╬═══════════════════╬═══════════════════╣
║                         ║                   ║                   ║                   ║
║  1. REQUISITOS        ║ Requirements Agent ║    Product Owner   ║  GitHub Issues   ║
║                         ║ → Crea documentos ║ → Da la necesidad ║  + Historias     ║
║                         ║                   ║ → Aprueba docs    ║                   ║
╠═══════════════════════════╬═══════════════════╬═══════════════════╬═══════════════════╣
║                         ║                   ║                   ║                   ║
║  2. ARQUITECTURA       ║ Architecture Agent║    Tech Lead      ║  Arquitectura    ║
║                         ║ → Propone stack   ║ → Aprueba diseño ║  + Diagramas      ║
║                         ║ → Crea diagramas  ║ → Ajusta si es   ║  + Estructura    ║
║                         ║ → Diseña modelo   ║   necesario       ║                   ║
║                         ║                   ║                   ║                   ║
╠═══════════════════════════╬═══════════════════╬═══════════════════╬═══════════════════╣
║                         ║                   ║                   ║                   ║
║  3. DESARROLLO         ║ Code Agent        ║ Desarrolladores   ║  Código fuente   ║
║                         ║ → Genera código  ║ → Revisan código  ║                   ║
║                         ║                   ║ → Completan code  ║                   ║
║                         ║                   ║ → Code review     ║                   ║
║                         ║                   ║                   ║                   ║
╠═══════════════════════════╬═══════════════════╬═══════════════════╬═══════════════════╣
║                         ║                   ║                   ║                   ║
║  4. TESTING            ║ Test Agent        ║ QA Engineers      ║  Tests           ║
║                         ║ → Genera tests   ║ → Ejecutan tests  ║  + Resultados    ║
║                         ║                   ║ → Pruebas manual ║                   ║
║                         ║                   ║                   ║                   ║
╠═══════════════════════════╬═══════════════════╬═══════════════════╬═══════════════════╣
║                         ║                   ║                   ║                   ║
║  5. SEGURIDAD          ║ Security Agent    ║ Security Analyst  ║  Reporte         ║
║                         ║ → Scan código    ║ → Revisa reporte  ║  + Recomendac.   ║
║                         ║ → Recomienda     ║ → Aprueba         ║                   ║
║                         ║                   ║                   ║                   ║
╠═══════════════════════════╬═══════════════════╬═══════════════════╬═══════════════════╣
║                         ║                   ║                   ║                   ║
║  6. DEPLOY             ║ Deployment Agent ║ DevOps            ║  App en Azure    ║
║                         ║ → Despliega      ║ → Supervisa        ║  + URL pública   ║
║                         ║ → Configura      ║ → Aprueba         ║                   ║
║                         ║                   ║                   ║                   ║
╚═══════════════════════════╩═══════════════════╩═══════════════════╩═══════════════════╝
```

---

## QUIÉN INICIA EL PROCESO

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                         EL ORDEN DE EJECUCIÓN                                           │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

    1. 👤 PRODUCT OWNER
         │
         │ "Necesito X"
         ▼
    2. 🤖 REQUIREMENTS AGENT
         │
         │ Crea ISSUE en GitHub
         ▼
    3. 👤 TECH LEAD
         │
         │ Aprueba y asigna
         ▼
    4. 🤖 ARCHITECTURE AGENT
         │
         │ Propone arquitectura
         ▼
    5. 👤 DESARROLLADORES
         │
         │ Desarrollan + Revisan
         ▼
    6. 🤖 CODE AGENT + TEST AGENT
         │
         │ Generan código + tests
         ▼
    7. 👤 QA + SECURITY
         │
         │ Prueban y validan
         ▼
    8. 🤖 DEPLOYMENT AGENT
         │
         │ Despliega
         ▼
    9. 👤 TODOS
         │
         │ Demo al CIO
```

---

## EN EL HACKATHON: 7 HORAS

```
HORA 9:00 - 9:30  │ 👤 PO da la necesidad
                    │ 🤖 Requirements Agent crea ISSUE

HORA 9:30 - 10:00  │ 🤖 Architecture Agent propone arquitectura
                    │ 👤 Tech Lead aprueba

HORA 10:00 - 12:30 │ 🤖 Code Agent genera código
                    │ 👤 Desarrolladores revisan y ajustan

HORA 12:30 - 13:30 │ LUNCH

HORA 13:30 - 15:00 │ 🤖 Test Agent genera tests
                    │ 👤 QA ejecuta y reporta

HORA 15:00 - 15:30 │ 🤖 Deployment Agent despliega
                    │ 👤 DevOps supervisa

HORA 15:30 - 16:00 │ 👤 Demo al CIO
```

---

## CLARO Y SIMPLE

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                         RESUMEN                                                          │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

🤖 IA HACE:
   - El trabajo "pesado" de generar código, documentos, tests
   - Propuestas iniciales
   - Tareas repetitivas

👤 HUMANO HACE:
   - Definir QUÉ necesita (PO)
   - Aprueba/diseña QUÉ está bien (Tech Lead)
   - Revisa y completa el código (Desarrolladores)
   - Valida que funcione (QA)
   - Supervisa el deploy (DevOps)

✅ LA IA NO SUSTITUYE AL HUMANO - LO ASISTE
   El humano siempre tiene la ÚLTIMA PALABRA
```

---

¿Te queda claro ahora?