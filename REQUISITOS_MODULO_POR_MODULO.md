# SISTEMA DE REQUISITOS: MÓDULO POR MÓDULO

---

## EL FLUJO DE REQUISITOS

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                         CÓMO LLEGAN LOS REQUISITOS AL EQUIPO                          │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

    ┌──────────────┐
    │   PO (Negocio)│
    │ "Necesito X"  │
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │ REQUIREMENTS │  ← Agent IA transforma
    │    AGENT     │    la necesidad en requisitos
    └──────┬───────┘
           │
           ▼
    ┌──────────────────────────────────────────────┐
    │         GITHUB ISSUES                      │
    │    (Tickets de trabajo para equipos)       │
    └──────┬───────┘
           │
           ▼
    ┌──────────────────────────────────────────────┐
    │         EQUIPOS TOMAN TICKETS              │
    │    Frontend | Backend | IA | Infra         │
    └──────────────────────────────────────────────┘
```

---

## ESTRUCTURA DE ISSUES POR MÓDULO

### Issuetype: "Requirements Module"

Cada módulo tiene SU PROPIO ISSUE que se crea ANTES de empezar a trabajar.

---

## MÓDULO 1: AUTH + BASE DE DATOS

```
═══════════════════════════════════════════════════════════════════════════════════════════
ISSUE #1: [MÓDULO 1] Autenticación + Base de Datos
═══════════════════════════════════════════════════════════════════════════════════════════

LABELS: modulo-1, prioridad-alta, backend
MILESTONE: Sprint 1
ASIGNAR A: @hackathon-backend

DESCRIPCIÓN DEL MÓDULO:
───────────────────────────────────────────────────────────────────────────────
Este módulo establece la fundación de la aplicación:
1. Base de datos PostgreSQL configurada
2. Entity Framework Core conectado
3. Sistema de autenticación JWT
4. Registro y login de usuarios

TAREAS ESPECÍFICAS (Backend):
───────────────────────────────────────────────────────────────────────────────
□ 1. Configurar PostgreSQL en Azure
□ 2. Crear DbContext en EF Core
□ 3. Crear entidad User
□ 4. Implementar JWT Authentication
□ 5. Endpoint POST /api/auth/register
□ 6. Endpoint POST /api/auth/login
□ 7. Endpoint GET /api/auth/me
□ 8. Configurar migraciones
□ 9. Tests unitarios de auth
□ 10. Documentar API en Swagger

TAREAS ESPECÍFICAS (Frontend):
───────────────────────────────────────────────────────────────────────────────
□ 1. Crear Zustand store: authStore
□ 2. Crear página Login.tsx
□ 3. Crear página Register.tsx
□ 4. Crear componente ProtectedRoute
□ 5. Integrar con API /auth/login
□ 6. Integrar con API /auth/register
□ 7. Manejar token JWT en localStorage
□ 8. Tests de componentes auth

DEFINICIÓN DE DONE:
───────────────────────────────────────────────────────────────────────────────
- [ ] Usuario puede registrarse
- [ ] Usuario puede hacer login
- [ ] JWT se guarda correctamente
- [ ] Rutas protegidas funcionan
- [ ] Tests pasando (80% coverage)
- [ ] Deploy a staging exitoso

DEPENDENCIAS:
───────────────────────────────────────────────────────────────────────────────
- Ninguna (es el primer módulo)

COMENTARIOS DEL PO:
───────────────────────────────────────────────────────────────────────────────
"El login debe ser con email y contraseña. No necesita OAuth por ahora."

═══════════════════════════════════════════════════════════════════════════════════════════
```

---

## MÓDULO 2: GESTIÓN DE EMPLEADOS

```
═══════════════════════════════════════════════════════════════════════════════════════════
ISSUE #2: [MÓDULO 2] Gestión de Empleados
═══════════════════════════════════════════════════════════════════════════════════════════

LABELS: modulo-2, prioridad-alta, backend, frontend
MILESTONE: Sprint 1
ASIGNAR A: @hackathon-backend, @hackathon-frontend

DESCRIPCIÓN DEL MÓDULO:
───────────────────────────────────────────────────────────────────────────────
Permite gestionar el registro y mantenimiento de empleados:
1. CRUD completo de empleados
2. Asignación de departamentos
3. Relación empleado-manager

TAREAS ESPECÍFICAS (Backend):
───────────────────────────────────────────────────────────────────────────────
□ 1. Crear entidad Empleado
□ 2. Crear entidad Departamento
□ 3. Endpoint GET /api/empleados (listar todos)
□ 4. Endpoint GET /api/empleados/{id} (ver uno)
□ 5. Endpoint POST /api/empleados (crear)
□ 6. Endpoint PUT /api/empleados/{id} (actualizar)
□ 7. Endpoint DELETE /api/empleados/{id} (eliminar)
□ 8. Endpoint GET /api/departamentos
□ 9. Seed de departamentos iniciales
□ 10. Tests CRUD empleados

TAREAS ESPECÍFICAS (Frontend):
───────────────────────────────────────────────────────────────────────────────
□ 1. Crear Zustand store: empleadoStore
□ 2. Crear página ListaEmpleados.tsx
□ 3. Crear página DetalleEmpleado.tsx
□ 4. Crear formulario EmpleadoForm.tsx
□ 5. Crear modal para crear/editar empleado
□ 6. Tabla con filtros y paginación
□ 7. Integrar con APIs de empleados

DEFINICIÓN DE DONE:
───────────────────────────────────────────────────────────────────────────────
- [ ] CRUD de empleados funcional
- [ ] Listado con filtros funciona
- [ ] Formulario de empleado completa
- [ ] Tests pasando
- [ ] Desplegado a staging

DEPENDENCIAS:
───────────────────────────────────────────────────────────────────────────────
- Issue #1: Auth + DB (debe estar completo)

COMENTARIOS DEL PO:
───────────────────────────────────────────────────────────────────────────────
"Cada empleado debe tener un manager asignado. Mostrar la jerarquía."

═══════════════════════════════════════════════════════════════════════════════════════════
```

---

## MÓDULO 3: GESTIÓN DE CURSOS

```
═══════════════════════════════════════════════════════════════════════════════════════════
ISSUE #3: [MÓDULO 3] Gestión de Cursos
═══════════════════════════════════════════════════════════════════════════════════════════

LABELS: modulo-3, prioridad-alta, backend, frontend
MILESTONE: Sprint 1
ASIGNAR A: @hackathon-backend, @hackathon-frontend

DESCRIPCIÓN DEL MÓDULO:
───────────────────────────────────────────────────────────────────────────────
Catálogo de cursos disponibles para los empleados:
1. CRUD de cursos
2. Filtrado por categoría
3. Información de duración y requisitos

TAREAS ESPECÍFICAS (Backend):
───────────────────────────────────────────────────────────────────────────────
□ 1. Crear entidad Curso
□ 2. Crear entidad Categoria
□ 3. Endpoint GET /api/cursos
□ 4. Endpoint GET /api/cursos/{id}
□ 5. Endpoint POST /api/cursos
□ 6. Endpoint PUT /api/cursos/{id}
□ 7. Endpoint DELETE /api/cursos/{id}
□ 8. Endpoint GET /api/categorias
□ 9. Seed de cursos iniciales
□ 10. Tests

TAREAS ESPECÍFICAS (Frontend):
───────────────────────────────────────────────────────────────────────────────
□ 1. Crear Zustand store: cursoStore
□ 2. Crear página CatalogoCursos.tsx
□ 3. Crear página DetalleCurso.tsx
□ 4. Crear formulario CursoForm.tsx
□ 5. Filtros por categoría
□ 6. Búsqueda por nombre

DEPENDENCIAS:
───────────────────────────────────────────────────────────────────────────────
- Issue #1: Auth + DB

COMENTARIOS DEL PO:
───────────────────────────────────────────────────────────────────────────────
"Los cursos deben mostrar: nombre, descripción, duración en horas, categoría, y si otorga certificación."

═══════════════════════════════════════════════════════════════════════════════════════════
```

---

## MÓDULO 4: MATRÍCULA + CERTIFICACIONES

```
═══════════════════════════════════════════════════════════════════════════════════════════
ISSUE #4: [MÓDULO 4] Matrícula y Certificaciones
═══════════════════════════════════════════════════════════════════════════════════════════

LABELS: modulo-4, prioridad-alta, backend, frontend
MILESTONE: Sprint 2
ASIGNAR A: @hackathon-backend, @hackathon-frontend

DESCRIPCIÓN DEL MÓDULO:
───────────────────────────────────────────────────────────────────────────────
Sistema central de gestión de certificaciones:
1. Empleado se matricula en curso
2. Seguimiento de progreso
3. Registro de certificación completada
4. Estado de certificaciones (pendiente, en progreso, completada, vencida)

TAREAS ESPECÍFICAS (Backend):
───────────────────────────────────────────────────────────────────────────────
□ 1. Crear entidad Matricula
□ 2. Crear entidad Certificacion
□ 3. Endpoint POST /api/matriculas (matricularse)
□ 4. Endpoint GET /api/matriculas/empleado/{id}
□ 5. Endpoint PUT /api/matriculas/{id}/completar
□ 6. Endpoint GET /api/certificaciones/empleado/{id}
□ 7. Endpoint GET /api/certificaciones/vencidas
□ 8. Lógica de vencimiento automático
□ 9. Tests

TAREAS ESPECÍFICAS (Frontend):
───────────────────────────────────────────────────────────────────────────────
□ 1. Crear Zustand store: matriculaStore
□ 2. Página MiProgreso.tsx
□ 3. Botón "Matricularse" en cursos
□ 4. Visualización de certificaciones por empleado
□ 5. Indicador visual de estado (verde/amarillo/rojo)
□ 6. Notificaciones de vencimiento

DEPENDENCIAS:
───────────────────────────────────────────────────────────────────────────────
- Issue #2: Gestión Empleados
- Issue #3: Gestión Cursos

COMENTARIOS DEL PO:
───────────────────────────────────────────────────────────────────────────────
"Cuando un empleado completa un curso, automáticamente se crea una certificación."

═══════════════════════════════════════════════════════════════════════════════════════════
```

---

## MÓDULO 5: DASHBOARD + REPORTES

```
═══════════════════════════════════════════════════════════════════════════════════════════
ISSUE #5: [MÓDULO 5] Dashboard y Reportes
═══════════════════════════════════════════════════════════════════════════════════════════

LABELS: modulo-5, prioridad-media, backend, frontend
MILESTONE: Sprint 2
ASIGNAR A: @hackathon-backend, @hackathon-frontend

DESCRIPCIÓN DEL MÓDULO:
───────────────────────────────────────────────────────────────────────────────
Vistas de gestión para diferentes roles:
1. Dashboard para empleados (mi progreso)
2. Dashboard para managers (progreso de equipo)
3. Dashboard para Talento Humano (reportes globales)

TAREAS ESPECÍFICAS (Backend):
───────────────────────────────────────────────────────────────────────────────
□ 1. Endpoint GET /api/dashboard/empleado/{id}
□ 2. Endpoint GET /api/dashboard/manager/{id}
□ 3. Endpoint GET /api/dashboard/talento-humano
□ 4. Endpoint GET /api/reportes/por-departamento
□ 5. Endpoint GET /api/reportes/por-certificacion
□ 6. Endpoint GET /api/reportes/vencimientos-proximos

TAREAS ESPECÍFICAS (Frontend):
───────────────────────────────────────────────────────────────────────────────
□ 1. Dashboard Empleado (gráfico progreso)
□ 2. Dashboard Manager (lista equipo + estado)
□ 3. Dashboard TH ( KPIs + tablas)
□ 4. Gráfico de barras (certificaciones por depto)
□ 5. Gráfico circular (estado de certifs)
□ 6. Exportar a PDF/Excel

DEPENDENCIAS:
───────────────────────────────────────────────────────────────────────────────
- Issue #4: Matrícula y Certificaciones

COMENTARIOS DEL PO:
───────────────────────────────────────────────────────────────────────────────
"TH necesita ver: total empleados, % cumplimiento, certifs próximas a vencer."

═══════════════════════════════════════════════════════════════════════════════════════════
```

---

## MÓDULO 6: INTEGRACIÓN IA (AGENTES)

```
═══════════════════════════════════════════════════════════════════════════════════════════
ISSUE #6: [MÓDULO 6] Integración Agentes IA
═══════════════════════════════════════════════════════════════════════════════════════════

LABELS: modulo-6, prioridad-alta, ia, backend
MILESTONE: Sprint 2
ASIGNAR A: @hackathon-ia, @hackathon-backend

DESCRIPCIÓN DEL MÓDULO:
───────────────────────────────────────────────────────────────────────────────
Integración de agentes IA para automatización:
1. Requirements Agent integrado
2. Planning Agent integrado
3. Code Generator Agent integrado

TAREAS ESPECÍFICAS (IA Service):
───────────────────────────────────────────────────────────────────────────────
□ 1. Configurar FastAPI + CrewAI
□ 2. Crear Requirements Agent
□ 3. Crear Planning Agent
□ 4. Crear Code Generator Agent
□ 5. Conectar con Azure OpenAI
□ 6. Crear endpoint /api/ia/analizar-requisitos
□ 7. Crear endpoint /api/ia/generar-codigo
□ 8. Tests de agentes

TAREAS ESPECÍFICAS (Backend):
───────────────────────────────────────────────────────────────────────────────
□ 1. Crear endpoint para invocar agentes IA
□ 2. Integrar con frontend
□ 3. Manejo de errores
□ 4. Logging

DEPENDENCIAS:
───────────────────────────────────────────────────────────────────────────────
- Issue #1: Auth + DB
- Issue #5: Dashboard

COMENTARIOS DEL PO:
───────────────────────────────────────────────────────────────────────────────
"Los agentes deben poder generar código basado en requisitos en lenguaje natural."

═══════════════════════════════════════════════════════════════════════════════════════════
```

---

## MÓDULO 7: CONSTANCIAS + NOTIFICACIONES

```
═══════════════════════════════════════════════════════════════════════════════════════════
ISSUE #7: [MÓDULO 7] Constancias y Notificaciones
═══════════════════════════════════════════════════════════════════════════════════════════

LABELS: modulo-7, prioridad-media, backend, frontend
MILESTONE: Sprint 3
ASIGNAR A: @hackathon-backend, @hackathon-frontend

DESCRIPCIÓN DEL MÓDULO:
───────────────────────────────────────────────────────────────────────────────
Funcionalidades adicionales:
1. Generación automática de constancias PDF
2. Notificaciones de vencimiento
3. Envío por email

TAREAS ESPECÍFICAS (Backend):
───────────────────────────────────────────────────────────────────────────────
□ 1. Generar PDF de constancia
□ 2. Endpoint GET /api/constancias/{id}/generar-pdf
□ 3. Servicio de email (SendGrid/SMTP)
□ 4. Job programado para alertas (30, 7, 1 día antes)
□ 5. Registro de notificaciones enviadas

TAREAS ESPECÍFICAS (Frontend):
───────────────────────────────────────────────────────────────────────────────
□ 1. Botón "Descargar Constancia" en perfil
□ 2. Sección "Mis Notificaciones"
□ 3. Configuración de preferencias

DEPENDENCIAS:
───────────────────────────────────────────────────────────────────────────────
- Issue #4: Matrícula y Certificaciones

COMENTARIOS DEL PO:
───────────────────────────────────────────────────────────────────────────────
"La constancia debe incluir: nombre empleado, curso, fecha, código único de verificación."

═══════════════════════════════════════════════════════════════════════════════════════════
```

---

## MÓDULO 8: DESPLIEGUE FINAL

```
═══════════════════════════════════════════════════════════════════════════════════════════
ISSUE #8: [MÓDULO 8] Despliegue a Producción
═══════════════════════════════════════════════════════════════════════════════════════════

LABELS: modulo-8, prioridad-crítica, infra, deploy
MILESTONE: Sprint Final
ASIGNAR A: @hackathon-infra, @todos

DESCRIPCIÓN DEL MÓDULO:
───────────────────────────────────────────────────────────────────────────────
Puesta en producción de toda la aplicación:
1. Pipeline CI/CD configurado
2. Despliegue a Azure
3. Tests E2E
4. Documentación

TAREAS ESPECÍFICAS (Infra):
───────────────────────────────────────────────────────────────────────────────
□ 1. Configurar GitHub Actions
□ 2. Build automático en merge a main
□ 3. Despliegue automático a Azure
□ 4. Health checks configurados
□ 5. Dominio configurado (SSL)
□ 6. Backup automático

TAREAS ESPECÍFICAS (QA):
───────────────────────────────────────────────────────────────────────────────
□ 1. Tests E2E con Playwright
□ 2. Tests de smoke
□ 3. Pruebas de rendimiento
□ 4. Reporte de bugs

TAREAS ESPECÍFICAS (Todos):
───────────────────────────────────────────────────────────────────────────────
□ 1. Demo al Steering Committee
□ 2. Documentación final
□ 3. Lecciones aprendidas

DEPENDENCIAS:
───────────────────────────────────────────────────────────────────────────────
- TODOS LOS ANTERIORES

═══════════════════════════════════════════════════════════════════════════════════════════
```

---

## RESUMEN: ORDEN DE LOS ISSUES

```
ORDEN CRÍTICO (NO EMPEZAR HASTA TENER EL ANTERIOR):

Issue #1 → MÓDULO 1: Auth + DB (FUNDACIÓN)
    ↓
Issue #2 → MÓDULO 2: Gestión Empleados
    ↓
Issue #3 → MÓDULO 3: Gestión Cursos
    ↓
Issue #4 → MÓDULO 4: Matrícula + Certificaciones (NÚCLEO)
    ↓
Issue #5 → MÓDULO 5: Dashboard + Reportes
    ↓
Issue #6 → MÓDULO 6: Integración IA
    ↓
Issue #7 → MÓDULO 7: Constancias + Notificaciones
    ↓
Issue #8 → MÓDULO 8: Deploy Producción (FINAL)
```

---

## CÓMO CREAR ESTOS ISSUES EN GITHUB

```
PASO 1: Ir a github.com/tuempresa/ai-factory-hackathon/issues

PASO 2: Click "New Issue"

PASO 3: Copiar template de arriba (Módulo 1)

PASO 4: Asignar al equipo correspondiente

PASO 5: Poner label "modulo-1"

PASO 6: Repetir para cada módulo

IMPORTANTE:
- Crear los 8 issues ANTES de empezar
- Cada equipo toma solo 1 issue a la vez
- No empezar Issue #2 hasta que #1 esté DONE
```

---

## BOARD KANBAN SUGERIDO

```
github.com/tuempresa/ai-factory-hackathon/projects

COLUMNAS:
───────────
📋 To Do     → Issues sin asignar
🚧 In Progress → Issue actual
🔍 Review    → Esperando code review
✅ Done      → Completados

FLUJO:
1. Tomar issue de "To Do"
2. Mover a "In Progress"
3. Cuando está listo → "Review"
4. Cuando se mergea → "Done"
```

---

¿Te sirve así? ¿Algo que ajuste?