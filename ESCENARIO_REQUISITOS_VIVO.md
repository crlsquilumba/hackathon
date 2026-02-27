# ESCENARIO EN VIVO: FASE DE REQUISITOS

---

## 🎬 ESCENARIO: Product Owner vs Requirements Agent

### Contexto
El Product Owner (PO) tiene una necesidad de negocio y se la comunica al Requirements Agent (IA).

---

## Paso 1: PO Expresa la Necesidad

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  👤 PRODUCT OWNER (Humano)                                                    │
└─────────────────────────────────────────────────────────────────────────────────┘

"Hola, necesito crear una plataforma de gestión de certificaciones 
de empleados para nuestra empresa. 

Contexto:
- Tenemos aproximadamente 200 empleados
- Cada empleado necesita mantener al día varias certificaciones 
  (cursos técnicos, normas ISO, capacitaciones de seguridad)
- Actualmente usamos un sistema llamado D2L pero nos van a dar de baja
- Necesitamos que los empleados puedan:
  1. Ver qué certificaciones tienen pendientes
  2. Registrarse en nuevos cursos
  3. Los managers puedan ver el progreso de su equipo
  4. El área de Talento Humano pueda generar reportes

También necesitamos alertas cuando una certificación está por vencer 
y que el sistema genere automáticamente constancias cuando un 
empleado complete un curso."

Necesidad negocio: Gestión integral de certificaciones y cursos
```

---

## Paso 2: Requirements Agent Procesa y Genera Documentos

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  🤖 REQUIREMENTS AGENT (IA)                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘

Procesando requirements...

[1] Extrayendo entidades...
    ✓ Empleado
    ✓ Certification
    ✓ Curso
    ✓ Manager
    ✓ Constancia
    ✓ Alerta

[2] Generando historias de usuario...

═══════════════════════════════════════════════════════════════════════════════════
                         HISTORIAS DE USUARIO
═══════════════════════════════════════════════════════════════════════════════════

┌─────────────────────────────────────────────────────────────────────────────┐
│ HU-001: Registro de Empleados                                               │
│─────────────────────────────────────────────────────────────────────────────│
│ COMO administrador de Talento Humano                │
│ QUIERO registrar nuevos empleados en el sistema    │
│ PARA que puedan acceder a la plataforma y gestionar sus certificaciones    │
│                                                                             │
│ Criterios de aceptación:                                                   │
│ □ El empleado debe tener: nombre, correo, departamento, puesto            │
│ □ El correo debe ser único en el sistema                                  │
│ □ Se debe asignar un manager al empleado                                  │
│ □ El sistema debe enviar correo de bienvenida                             │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ HU-002: Matricularse en Cursos                                             │
│─────────────────────────────────────────────────────────────────────────────│
│ COMO empleado                                                               │
│ QUIERO ver los cursos disponibles y matricularme                          │
│ PARA completar las certificaciones requeridas                               │
│                                                                             │
│ Criterios de aceptación:                                                   │
│ □ Ver lista de cursos con descripción, duración, certificación asociada   │
│ □ Filtrar por categoría, fecha, disponibilidad                            │
│ □ Confirmación de matrícula                                                │
│ □ Notificar al manager de la matrícula                                    │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ HU-003: Seguimiento de Certificaciones                                    │
│─────────────────────────────────────────────────────────────────────────────│
│ COMO manager de equipo                                                     │
│ QUIERO ver el progreso de certificaciones de mi equipo                    │
│ PARA identificar quién necesita completar requisitos                        │
│                                                                             │
│ Criterios de aceptación:                                                   │
│ □ Dashboard con resumen de estado (completado, pendiente, vencido)        │
│ □ Detalle por empleado                                                   │
│ □ Filtros por tipo de certificación                                      │
│ □ Alertas visuales para certificaciones próximas a vencer                 │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ HU-004: Generación Automática de Constancias                              │
│─────────────────────────────────────────────────────────────────────────────│
│ COMO empleado que completó un curso                                        │
│ QUIERO recibir automáticamente una constancia digital                      │
│ PARA demostrar que completé la certificación                               │
│                                                                             │
│ Criterios de aceptación:                                                   │
│ □ PDF con: nombre empleado, curso, fecha, institución, código único        │
│ □ Descarga disponible desde el perfil                                    │
│ □ Envío automático por email                                             │
│ □ QR para verificación de autenticidad                                    │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ HU-005: Alertas de Vencimiento                                            │
│─────────────────────────────────────────────────────────────────────────────│
│ COMO sistema                                                               │
│ QUIERO enviar alertas automáticas                                          │
│ PARA que empleados y managers estén informados                            │
│                                                                             │
│ Criterios de aceptación:                                                   │
│ □ Alerta 30 días antes del vencimiento                                   │
│ □ Alerta 7 días antes del vencimiento                                    │
│ □ Alerta el día del vencimiento                                          │
│ □ Notificaciones por email y dentro de la plataforma                      │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Paso 3: Agent Genera Diagrama de Casos de Uso

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  🤖 REQUIREMENTS AGENT - DIAGRAMA DE CASOS DE USO                            │
└─────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│                        PLATAFORMA DE GESTIÓN                                │
│                      DE CERTIFICACIONES                                     │
│                                                                              │
│  ┌──────────────┐                                                          │
│  │   EMPLEADO  │                                                          │
│  └──────┬───────┘                                                          │
│         │                                                                    │
│         │ 1. Registrarse en curso                                          │
│         │ 2. Ver mis certificaciones                                        │
│         │ 3. Descargar constancia                                           │
│         │ 4. Ver alertas                                                   │
│         │ 5. Actualizar perfil                                             │
│         │                                                                   │
│  ┌──────┴───────┐         ┌──────────────────┐                            │
│  │              │         │                  │                            │
│  │  ┌────────┐ │         │  SISTEMA         │                            │
│  │  │        │ │         │                  │                            │
│  └─▶│  GESTION│◀────────│  DE               │                            │
│     │  DE     │         │  CERTIFICACIONES  │                            │
│     │  CURSOS │         │                  │                            │
│     └────────┘         └────────┬─────────┘                            │
│                                 │                                          │
│     ┌────────┐                  │              ┌─────────────┐           │
│     │        │                  │              │             │           │
│     │ ALERTAS│◀─────────────────┴──────────────│  MANAGER   │           │
│     │        │                                │             │           │
│     └────────┘                                └──────┬──────┘           │
│                                                      │                    │
│     ┌────────┐                                       │                    │
│     │        │                                       │ 1. Ver equipo     │
│     │CONSTAN-│◀──────────────────────────────────────┤ 2. Reportes       │
│     │ CIAS   │                                       │ 3. Asignar curso  │
│     └────────┘                                       │                   │
│                                                      └────────────────────┘
│                                                                              
│                         ┌──────────────────┐                                 
│                         │    TALENTO       │                                 
│                         │    HUMANO        │                                 
│                         └────────┬─────────┘                                 
│                                  │                                           
│         ┌───────────────────────┼───────────────────────┐                  
│         │                       │                       │                  
│         ▼                       ▼                       ▼                  
│  ┌─────────────┐       ┌─────────────┐       ┌─────────────┐            
│  │  Reportes   │       │   Admin      │       │   Auditoría │            
│  │  globales   │       │   total     │       │   acceso    │            
│  └─────────────┘       └─────────────┘       └─────────────┘            
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Paso 4: Agent Genera Modelo de Datos

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  🤖 REQUIREMENTS AGENT - MODELO DE DATOS (ERD)                                │
└─────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────┐         ┌──────────────────────┐
│      EMPLEADO        │         │       DEPARTAMENTO    │
├──────────────────────┤         ├──────────────────────┤
│ id (PK)              │         │ id (PK)              │
│ nombre               │    ┌───▶│ nombre               │
│ email (unique)       │    │    │ descripcion         │
│ fecha_contratacion   │    │    └──────────────────────┘
│ puesto               │    │
│ manager_id (FK)      │────┘
│ departamento_id (FK) │
│ fecha_creacion       │
│ activo               │
└──────────────────────┘
         │
         │ 1:N
         ▼
┌──────────────────────┐         ┌──────────────────────┐
│  CERTIFICACION       │         │        CURSO         │
├──────────────────────┤         ├──────────────────────┤
│ id (PK)              │    N:M │ id (PK)              │
│ empleado_id (FK)     │◀──────▶│ nombre               │
│ curso_id (FK)        │         │ descripcion         │
│ fecha_inicio         │         │ duracion_horas      │
│ fecha_vencimiento    │         │ categoria           │
│ estado               │         │ proveedor            │
│ constancia_url       │         │ prerequisites       │
│ alertas_enviadas     │         │ activo              │
└──────────────────────┘         └──────────────────────┘
         │
         │ 1:N
         ▼
┌──────────────────────┐
│      CONSTANCIA      │
├──────────────────────┤
│ id (PK)              │
│ certificacion_id (FK)│
│ codigo_verificacion  │
│ url_pdf              │
│ fecha_emision        │
│ qr_code              │
│ firmante             │
└──────────────────────┘
```

---

## Paso 5: Agent Genera Backlog de Features

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  🤖 REQUIREMENTS AGENT - BACKLOG PRIORIZADO                                  │
└─────────────────────────────────────────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════════════════════════════

  PRIORIDAD 1 - MUST HAVE (Sprint 1)
  ═══════════════════════════════════
  
  [ ] Autenticación de usuarios (login con email/password)
  [ ] Registro de empleados (admin Talento Humano)
  [ ] Perfil de empleado
  [ ] Catálogo de cursos
  [ ] Matrícula en cursos
  [ ] Seguimiento de certificaciones por empleado
  [ ] Dashboard básico de progreso
  
═══════════════════════════════════════════════════════════════════════════════════

  PRIORIDAD 2 - SHOULD HAVE (Sprint 2)
  ═══════════════════════════════════
  
  [ ] Vista de equipo para managers
  [ ] Reportes de cumplimiento por departamento
  [ ] Alertas automáticas de vencimiento
  [ ] Generación de constancias PDF
  [ ] Notificaciones dentro de la app
  
═══════════════════════════════════════════════════════════════════════════════════

  PRIORIDAD 3 - COULD HAVE (Sprint 3)
  ═══════════════════════════════════
  
  [ ] Integración con calendario
  [ ] Gamificación (badges, puntos)
  [ ] Encuestas de satisfacción post-curso
  [ ] Exportación a Excel/PDF
  [ ] Dashboard ejecutivo
  
═══════════════════════════════════════════════════════════════════════════════════

  PRIORIDAD 4 - WON'T HAVE (Backlog)
  ═══════════════════════════════════
  
  [ ] App móvil nativa
  [ ] Integración con LinkedIn Learning
  [ ] Certificaciones blockchain
  [ ] Integración con Zoom/Teams para clases en vivo
```

---

## Paso 6: Revisión Humana del PO

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  👤 PRODUCT OWNER (Revisión)                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘

Excelente trabajo. Algunos ajustes:

✓ Las historias de usuario cubren lo que necesitamos
✓ El modelo de datos parece correcto
⚠️ FALTA: Necesitamos también:
  - Un rol de "Instructor" que pueda cargar cursos
  - Un campo de "costo" en los cursos para presupuesto
  - La constancia debe tener firma digital del gerente de Talento Humano

Con esos ajustes, proceedemos a la siguiente fase.

APROBADO CON COMENTARIOS ✓
```

---

## Resumen del Flujo

```
     👤 PO                              🤖 IA
      │                                    │
      │ "Necesito una plataforma de       │
      │  gestión de certificaciones..."   │
      │───────────────────────────────────▶
      │                                    │
      │                                    │ [1] Extrae entidades
      │                                    │ [2] Genera historias de usuario
      │                                    │ [3] Crea diagrama de casos de uso
      │                                    │ [4] Diseña modelo de datos
      │                                    │ [5] Prioriza backlog
      │                                    │
      │ ◀──────────────────────────────────│
      │                                    │
      │ Documentos generados:              │
      │ - 5 Historias de usuario          │
      │ - Diagrama de casos de uso        │
      │ - Modelo de datos (ERD)          │
      │ - Backlog priorizado              │
      │                                    │
      │ ✓ APROBADO                        │
      │ (con 3 ajustes menores)           │
```

---

## Siguiente Fase

Una vez aprobado el Requirements Agent, el flujo continúa:

```
REQUIREMENTS AGENT ──▶ PLANNING AGENT ──▶ ARCHITECTURE AGENT ──▶ CODE AGENT
```
