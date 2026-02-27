# GUÍA RÁPIDA: CÓMO USAR AI FACTORY

---

## OPCIÓN 1: USAR CON GITHUB COPILOT (Más fácil)

### Paso 1: Abre VS Code
```bash
code ai-factory/
```

### Paso 2: Activa Copilot
- Click en icono de Copilot en VS Code
- O usa `Ctrl + Shift + P` → "Copilot: Toggle"

### Paso 3: Usa los prompts

Copia y pega en Copilot Chat:

```
Eres el Requirements Agent de AI Factory. 
Mi necesidad: "Necesito una plataforma de gestión de empleados"

Genera:
1. 5 historias de usuario
2. Diagrama de casos de uso (Mermaid)
3. Modelo de entidades
4. Backlog priorizado (MoSCoW)
```

---

## OPCIÓN 2: USAR PYTHON DIRECTO

### Paso 1: Instalar
```bash
cd ai-factory/
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

### Paso 2: Configurar .env
```bash
cp .env.example .env
# Edita con tus API keys
nano .env
```

### Paso 3: Usar

```python
# main.py
from ai_factory import create_orchestrator

# Crear orquestador
orchestrator = create_orchestrator("Mi Proyecto")

# Ejecutar pipeline completo
result = orchestrator.run_full_pipeline(
    user_need="Una app de gestión de empleados",
    project_context="Empresa de 200 personas",
    preferred_stack="React + .NET + PostgreSQL"
)

print(result)
```

---

## EJEMPLO PRÁCTICO: MÓDULO 1 - AUTH

### Paso 1: Define la necesidad

**Prompt para Requirements Agent:**
```
"Necesito crear un sistema de autenticación con:
- Registro de usuarios con email/contraseña
- Login con JWT
- Reset de contraseña
- Roles (admin, usuario)
- Protección de rutas

Genera historias de usuario y modelo de datos."
```

### Paso 2: El agente genera

**Resultado esperado:**

```markdown
## Historias de Usuario

### HU-001: Registro de Usuarios
COMO usuario nuevo
QUIERO registrarme con email y contraseña
PARA acceder al sistema

Criterios:
- [ ] Email válido
- [ ] Contraseña min 8 caracteres
- [ ] Confirmar email
```

### Paso 3: Code Agent genera código

**Prompt:**
```
Basado en el modelo de datos, genera código para:
- Backend: FastAPI con JWT
- Frontend: React con Zustand

Incluye:
- Models de usuario
- Endpoints /register, /login, /me
- Hook de autenticación
- ProtectedRoute
```

---

## FLUJO COMPLETO EN CODPILOT

### 1. REQUISITOS (10 min)
```
@workspace Eres Requirements Agent. 
Negocio: "Plataforma de certificaciones para 200 empleados"

Genera:
- Historias de usuario
- Casos de uso
- Modelo de datos
```

### 2. ARQUITECTURA (10 min)
```
@workspace Eres Architecture Agent.
Stack: React + .NET 9 + PostgreSQL + Azure

Genera:
- Diagrama de arquitectura
- Estructura de carpetas
- Stack tecnológico
```

### 3. CÓDIGO (20 min)
```
@workspace Eres Code Agent.
Módulo: Autenticación

Genera:
- Backend: FastAPI endpoints
- Frontend: React components
```

### 4. TESTS (10 min)
```
@workspace Eres Test Agent.
Código: (pegar código anterior)

Genera:
- Tests unitarios
- Coverage target 80%
```

---

## COMANDOS RÁPIDOS

### En Copilot Chat:

| Comando | Descripción |
|---------|-------------|
| `@workspace generame las historias de usuario` | Requirements |
| `@workspace diseña la arquitectura` | Architecture |
| `@workspace genera código para auth` | Code |
| `@workspace crea los tests` | Test |
| `@workspace analiza seguridad` | Security |
| `@workspace despliega a azure` | Deployment |

---

## PARA EL HACKATHON (7 horas)

| Hora | Actividad | Con Copilot |
|------|-----------|--------------|
| 9:00-10:00 | Requirements | Copilot genera historias |
| 10:00-10:30 | Arquitectura | Copilot propone stack |
| 10:30-12:30 | Código | Copilot genera + Devs ajustan |
| 12:30-13:30 | Lunch | - |
| 13:30-15:00 | Tests | Copilot genera tests |
| 15:00-15:30 | Deploy | Script automático |
| 15:30-16:00 | Demo | - |

---

## RESUMEN: LO QUE NECESITAS

### Para usar AI Factory necesitas:

1. ✅ **VS Code** instalado
2. ✅ **Copilot** activo (o cuenta gratuita)
3. ✅ **Git** configurado
4. ✅ **Python 3.12+** (para método directo)

### No necesitas:
- ❌ Instalar CrewAI (si usas Copilot)
- ❌ API Keys de OpenAI (Copilot ya tiene)
- ❌ Servidor propio

### Lo único que haces tú:
- Dar la necesidad en palabras simples
- Revisar lo que Copilot genera
- Aprobar o ajustar
- Copiar el código

---

## PRÓXIMO PASSO

¿Quieres que pruebe un ejemplo real contigo?
