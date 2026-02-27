# ☁️ ARQUITECTURA AZURE PARA EL HACKATHON

---

## 🔧 SERVICIOS AZURE A UTILIZAR

### Nivel de Servicios Recomendados

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                    ARQUITECTURA AZURE PARA HACKATHON IA                                    │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                               USUARIO FINAL                                                 │
│                    (Accede a la aplicación web)                                            │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
                                        │
                                        ▼
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                         🔒 AZURE FRONT DOOR / APP GATEWAY                                  │
│                    (SSL Termination, WAF, CDN)                                              │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
                                        │
                    ┌───────────────────┼───────────────────┐
                    ▼                                       ▼
        ┌───────────────────┐                   ┌───────────────────┐
        │  Azure App Service │                   │  Azure App Service │
        │  (Backend API)     │                   │  (Frontend React) │
        │  ───────────────  │                   │  ───────────────  │
        │  B1 Plan          │                   │  B1 Plan          │
        │  $54.76/mes       │                   │  $54.76/mes       │
        └───────────────────┘                   └───────────────────┘
                    │                                       │
                    └───────────────────┬───────────────────┘
                                        ▼
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                            📦 AZURE SQL DATABASE                                           │
│                    (PostgreSQL - Flexible Server)                                          │
│                    ──────────────────────────────────────                                   │
│                    Tier: Burstable (B1)                                                    │
│                    Costo: ~$15/mes                                                         │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
                                        │
                                        ▼
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                            🔑 AZURE KEY VAULT                                             │
│                    (Secrets, API Keys, Certificados)                                       │
│                    ──────────────────────────────────────                                   │
│                    Tier: Standard                                                          │
│                    Costo: ~$0.03/10k ops                                                   │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
                                        │
                                        ▼
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                            🤖 AZURE OPENAI SERVICE                                         │
│                    (Modelos GPT-4, GPT-4 Turbo, embedding)                                 │
│                    ──────────────────────────────────────                                   │
│                    Deployment: gpt-4                                                       │
│                    Costo: $30-60/1M tokens (input/output)                                 │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
                                        │
                                        ▼
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                            📊 AZURE MONITOR                                               │
│                    (Application Insights + Log Analytics)                                  │
│                    ──────────────────────────────────────                                   │
│                    Costo: ~$2.30/GB                                                       │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
                                        │
                                        ▼
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                            🐳 AZURE CONTAINER REGISTRY (ACR)                              │
│                    (Imágenes Docker)                                                       │
│                    ──────────────────────────────────────                                   │
│                    Tier: Basic                                                             │
│                    Costo: ~$5/mes                                                          │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 💰 COSTO ESTIMADO DEL HACKATHON

### Breakdown de Costos (7 horas de uso)

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                         COSTO DEL HACKATHON (7 HORAS)                                     │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────┬────────────────┬────────────────┬────────────────────┐
│            RECURSO                  │   USO HACKATHON│   COSTO UNIT  │     TOTAL          │
├─────────────────────────────────────┼────────────────┼────────────────┼────────────────────┤
│ Azure App Service (Backend)         │  7 horas       │  $0.075/hora  │  $0.53             │
│                                     │                │  (B1 pro-rated)│                   │
├─────────────────────────────────────┼────────────────┼────────────────┼────────────────────┤
│ Azure App Service (Frontend)       │  7 horas       │  $0.075/hora  │  $0.53             │
│                                     │                │  (B1 pro-rated)│                   │
├─────────────────────────────────────┼────────────────┼────────────────┼────────────────────┤
│ Azure SQL Database                 │  7 horas       │  $0.02/hora   │  $0.14             │
│                                     │                │  (B1 pro-rated)│                   │
├─────────────────────────────────────┼────────────────┼────────────────┼────────────────────┤
│ Azure OpenAI (GPT-4)               │  ~100K tokens  │  $30/1M input │  $3.00             │
│                                     │  input         │                │                    │
├─────────────────────────────────────┼────────────────┼────────────────┼────────────────────┤
│ Azure OpenAI (GPT-4)               │  ~50K tokens   │  $60/1M output│  $3.00             │
│                                     │  output        │                │                    │
├─────────────────────────────────────┼────────────────┼────────────────┼────────────────────┤
│ Azure Key Vault                     │  ~1K ops       │  $0.03/10K    │  $0.003            │
├─────────────────────────────────────┼────────────────┼────────────────┼────────────────────┤
│ Azure Monitor                      │  ~10 MB        │  $2.30/GB     │  $0.023            │
├─────────────────────────────────────┼────────────────┼────────────────┼────────────────────┤
│ Azure Container Registry            │  1 push        │  $0.10/GB     │  $0.10             │
├─────────────────────────────────────┼────────────────┼────────────────┼────────────────────┤
│ Transferencia Salida                │  ~50 MB        │  $0.087/GB   │  $0.004            │
├─────────────────────────────────────┼────────────────┼────────────────┼────────────────────┤
│                                     │                │                │                    │
│                                     │                │   SUBTOTAL    │  ~$7.33           │
│                                     │                │   (+20% var) │  ~$8.80           │
│                                     │                │                │                    │
└─────────────────────────────────────┴────────────────┴────────────────┴────────────────────┘

⚠️ NOTA: Los primeros $200 de Azure son gratuitos con la cuenta de prueba
✅ COSTO REAL ESTIMADO: $0 (usando créditos de prueba Azure)
```

---

## 🔐 SEGURIDAD AZURE

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                         SEGURIDAD EN AZURE                                                │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                        CAPAS DE SEGURIDAD                                                  │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

    ┌──────────────────────────────────────────────────────────────────────────────────┐
    │  NIVEL 1: PERÍMETRO                                                          │
    │  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────────────┐   │
    │  │ Azure Front Door│───▶│ WAF Enabled    │───▶│ DDoS Protection        │   │
    │  │ (SSL Term)     │    │ (OWASP Rules)  │    │ (Standard)             │   │
    │  └─────────────────┘    └─────────────────┘    └─────────────────────────┘   │
    └──────────────────────────────────────────────────────────────────────────────────┘
                                        │
    ┌──────────────────────────────────────────────────────────────────────────────────┐
    │  NIVEL 2: RED                                                              │
    │  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────────────┐   │
    │  │ VNet           │───▶│ Private Endpoints│───│ NSG Rules             │   │
    │  │ Integration    │    │ (App Service)   │    │ (Allow HTTPS only)    │   │
    │  └─────────────────┘    └─────────────────┘    └─────────────────────────┘   │
    └──────────────────────────────────────────────────────────────────────────────────┘
                                        │
    ┌──────────────────────────────────────────────────────────────────────────────────┐
    │  NIVEL 3: APLICACIÓN                                                      │
    │  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────────────┐   │
    │  │ Azure AD        │───▶│ RBAC            │───│ Managed Identity       │   │
    │  │ (Authentication)│    │ (Roles)         │    │ (No credentials)       │   │
    │  └─────────────────┘    └─────────────────┘    └─────────────────────────┘   │
    └──────────────────────────────────────────────────────────────────────────────────┘
                                        │
    ┌──────────────────────────────────────────────────────────────────────────────────┐
    │  NIVEL 4: DATOS                                                           │
    │  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────────────┐   │
    │  │ SQL TDE         │───▶│ Key Vault       │───│ Encryption at Rest    │   │
    │  │ (Transparent)   │    │ (Secrets)       │    │ (AES-256)             │   │
    │  └─────────────────┘    └─────────────────┘    └─────────────────────────┘   │
    └──────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                     CONFIGURACIÓN DE SEGURIDAD PARA HACKATHON                             │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

✅ HABILITAR:
  • Azure AD Authentication (Entra ID)
  • SSL/TLS con certificados gestionados
  • Azure Key Vault para secrets
  • Managed Identities (no credentials en código)
  • HTTPS only
  • CORS configurado
  
⚠️  PARA EL HACKATHON (Demo):
  • Usar Managed Identity
  • No exponer keys en código
  • Usar HTTPS
  • No hacer públicas las credenciales
```

---

## 🏗️ INFRAESTRUCTURA COMO CÓDIGO (Terraform)

### Archivo principal de infraestructura

```hcl
# main.tf - Hackathon Azure Infrastructure

# ─────────────────────────────────────────────────────────────────────────────
# RESOURCE GROUP
# ─────────────────────────────────────────────────────────────────────────────
resource "azurerm_resource_group" "hackathon" {
  name     = "rg-hackathon-ia-${var.environment}"
  location = "eastus"
  
  tags = {
    Environment = var.environment
    Project     = "Hackathon-IA"
  }
}

# ─────────────────────────────────────────────────────────────────────────────
# APP SERVICE PLAN (Backend)
# ─────────────────────────────────────────────────────────────────────────────
resource "azurerm_app_service_plan" "backend" {
  name                = "asp-hackathon-backend-${var.environment}"
  resource_group_name = azurerm_resource_group.hackathon.name
  location            = azurerm_resource_group.hackathon.location
  kind                = "Linux"
  reserved            = true

  sku {
    tier = "Basic"
    size = "B1"
  }
}

# ─────────────────────────────────────────────────────────────────────────────
# APP SERVICE PLAN (Frontend)
# ─────────────────────────────────────────────────────────────────────────────
resource "azurerm_app_service_plan" "frontend" {
  name                = "asp-hackathon-frontend-${var.environment}"
  resource_group_name = azurerm_resource_group.hackathon.name
  location            = azurerm_resource_group.hackathon.location
  kind                = "Linux"
  reserved            = true

  sku {
    tier = "Basic"
    size = "B1"
  }
}

# ─────────────────────────────────────────────────────────────────────────────
# APP SERVICE (Backend API)
# ─────────────────────────────────────────────────────────────────────────────
resource "azurerm_app_service" "backend" {
  name                = "app-hackathon-api-${var.environment}"
  resource_group_name = azurerm_resource_group.hackathon.name
  location            = azurerm_resource_group.hackathon.location
  app_service_plan_id = azurerm_app_service_plan.backend.id
  https_only         = true

  identity {
    type = "SystemAssigned"
  }

  app_settings = {
    "AZURE_OPENAI_ENDPOINT" = azurerm_cognitive_account.openai.endpoint
    "DATABASE_URL"         = azurerm_postgresql_flexible_server.db.connection_string
  }
  
  site_config {
    linux_fx_version = "PYTHON:3.11"
    always_on        = false
  }
}

# ─────────────────────────────────────────────────────────────────────────────
# POSTGRESQL FLEXIBLE SERVER
# ─────────────────────────────────────────────────────────────────────────────
resource "azurerm_postgresql_flexible_server" "db" {
  name                   = "psql-hackathon-${var.environment}"
  resource_group_name    = azurerm_resource_group.hackathon.name
  location              = azurerm_resource_group.hackathon.location
  version               = "15"
  sku_name              = "B_Standard_B1s"
  storage_mb            = 32768
  
  administrator_login    = var.db_admin
  administrator_password = var.db_password
  
  backup_retention_days = 7
  
  tags = {
    Environment = var.environment
  }
}

# ─────────────────────────────────────────────────────────────────────────────
# DATABASE (certificaciones_db)
# ─────────────────────────────────────────────────────────────────────────────
resource "azurerm_postgresql_flexible_server_database" "certificaciones" {
  name                = "certificaciones_db"
  server_id           = azurerm_postgresql_flexible_server.db.id
  charset             = "utf8"
  collation           = "en_US.utf8"
}

# ─────────────────────────────────────────────────────────────────────────────
# COGNITIVE SERVICES (Azure OpenAI)
# ─────────────────────────────────────────────────────────────────────────────
resource "azurerm_cognitive_account" "openai" {
  name                = "openai-hackathon-${var.environment}"
  resource_group_name = azurerm_resource_group.hackathon.name
  location            = "eastus"
  sku_name            = "S0"
  
  identity {
    type = "SystemAssigned"
  }
}

# ─────────────────────────────────────────────────────────────────────────────
# DEPLOYMENTS (GPT-4)
# ─────────────────────────────────────────────────────────────────────────────
resource "azurerm_cognitive_deployment" "gpt4" {
  name                = "gpt-4"
  cognitive_account_id = azurerm_cognitive_account.openai.id
  
  model {
    format  = "OpenAI"
    name    = "gpt-4"
    version = "0125-Preview"
  }
  
  sku {
    name     = "Standard"
    capacity = 10
  }
}

# ─────────────────────────────────────────────────────────────────────────────
# KEY VAULT
# ─────────────────────────────────────────────────────────────────────────────
resource "azurerm_key_vault" "kv" {
  name                = "kv-hackathon-${var.environment}"
  resource_group_name = azurerm_resource_group.hackathon.name
  location            = azurerm_resource_group.hackathon.location
  tenant_id           = data.azurerm_client_config.current.tenant_id
  
  sku_name = "standard"
  
  enable_rbac_authorization = true
  
  tags = {
    Environment = var.environment
  }
}

# ─────────────────────────────────────────────────────────────────────────────
# APPLICATION INSIGHTS
# ─────────────────────────────────────────────────────────────────────────────
resource "azurerm_application_insights" "appinsights" {
  name                = "appi-hackathon-${var.environment}"
  resource_group_name = azurerm_resource_group.hackathon.name
  location            = "eastus"
  application_type    = "web"
  
  retention_in_days = 7
  
  tags = {
    Environment = var.environment
  }
}
```

---

## 📋 CHECKLIST DE AZURE ANTES DEL HACKATHON

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                         CHECKLIST PRE-HACKATHON AZURE                                     │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

⬜ ANTES DEL HACKATHON (Un día antes):
  ┌─────────────────────────────────────────────────────────────────────────────────────┐
  │  CUENTA AZURE                                                                       │
  │  ☐ Verificar suscripción activa                                                   │
  │  ☐ Verificar créditos disponibles (mínimo $50)                                     │
  │  ☐ Verificar permisos de Contributor                                               │
  │                                                                                     │
  │  RECURSOS PRE-CREADOS                                                               │
  │  ☐ Resource Group creado: rg-hackathon-ia                                          │
  │  ☐ App Service Plan (B1)                                                           │
  │  ☐ App Service para Backend                                                        │
  │  ☐ App Service para Frontend                                                      │
  │  ☐ PostgreSQL Flexible Server (B1)                                                │
  │  ☐ Azure OpenAI con deployment de GPT-4                                           │
  │  ☐ Key Vault configurado                                                          │
  │  ☐ Application Insights                                                            │
  │                                                                                     │
  │  CONFIGURACIÓN                                                                      │
  │  ☐ Variables de entorno configuradas                                               │
  │  ☐ Secrets en Key Vault                                                           │
  │  ☐ Managed Identity asignada a App Services                                        │
  │  ☐ Rules de CORS configuradas                                                     │
  └─────────────────────────────────────────────────────────────────────────────────────┘

⬜ DÍA DEL HACKATHON (Mañana):
  ┌─────────────────────────────────────────────────────────────────────────────────────┐
  │  VERIFICACIÓN                                                                        │
  │  ☐ Acceder a Azure Portal                                                          │
  │  ☐ Verificar estado de todos los recursos                                          │
  │  ☐ Probar conectividad a la base de datos                                         │
  │  ☐ Probar endpoint de OpenAI                                                      │
  │  ☐ Verificar logs en Application Insights                                         │
  │                                                                                     │
  │  EQUIPO PREPARADO                                                                    │
  │  ☐ Todos tienen acceso al resource group                                           │
  │  ☐ Credentials de Azure CLI configurados                                            │
  │  ☐ Acceso a repositorio GitHub                                                     │
  └─────────────────────────────────────────────────────────────────────────────────────┘

⬜ DURANTE EL HACKATHON:
  ┌─────────────────────────────────────────────────────────────────────────────────────┐
  │  MONITOREO                                                                           │
  │  ☐ Revisar Application Insights para errores                                       │
  │  ☐ Monitorear uso de tokens OpenAI                                                 │
  │  ☐ Verificar costos en Cost Management                                             │
  │                                                                                     │
  │  SI HAY PROBLEMAS                                                                   │
  │  ☐ Restart App Service si no responde                                              │
  │  ☐ Verificar logs en Azure Monitor                                                 │
  │  ☐ Revisar Azure Advisor para recomendaciones                                     │
  └─────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🚀 COMANDOS DEPLOYMENT RÁPIDO

### scripts/deploy.sh

```bash
#!/bin/bash
# Deploy script para Hackathon

set -e

echo "🚀 Starting deployment to Azure..."

# 1. Login to Azure
echo "📱 Logging into Azure..."
az login

# 2. Set subscription
az account set --subscription "SUBSCRIPTION_ID"

# 3. Create resource group (if not exists)
echo "📦 Creating resource group..."
az group create --name rg-hackathon-ia --location eastus

# 4. Deploy infrastructure
echo "🏗️ Deploying infrastructure..."
terraform init
terraform apply -var-file="prod.tfvars" -auto-approve

# 5. Build and deploy backend
echo "🐍 Building backend..."
cd backend
az webapp up --name hackathon-api --resource-group rg-hackathon-ia --runtime "PYTHON:3.11"

# 6. Build and deploy frontend
echo "⚛️ Building frontend..."
cd ../frontend
az webapp up --name hackathon-web --resource-group rg-hackathon-ia --runtime "NODE:18-lts"

echo "✅ Deployment complete!"
echo "🌐 Frontend: https://hackathon-web.azurewebsites.net"
echo "� API: https://hackathon-api.azurewebsites.net"
```

---

## 📊 MONITOREO DURANTE EL HACKATHON

### Métricas Clave en Azure Monitor

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                         DASHBOARD HACKATHON AZURE                                           │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│ METRICAS A MONITOREAR                                                                    │
├─────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                             │
│  APP SERVICE (Backend)                                                                    │
│  ┌───────────────────────────────────────────────────────────────────────────────────┐   │
│  │ • HTTP Requests (count)        - Esperado: 100-500                              │   │
│  │ • Response Time (ms)           - Esperado: < 500ms                               │   │
│  │ • CPU Percentage               - Esperado: < 70%                                 │   │
│  │ • Memory Percentage            - Esperado: < 80%                                 │   │
│  │ • HTTP 5xx Errors              - Esperado: 0                                      │   │
│  └───────────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                             │
│  AZURE OPENAI                                                                               │
│  ┌───────────────────────────────────────────────────────────────────────────────────┐   │
│  │ • Tokens Used (Total)          - Controlar: no exceder presupuesto             │   │
│  │ • Latency (ms)                 - Esperado: < 5000ms                             │   │
│  │ • Errors                       - Esperado: 0                                     │   │
│  │ • Token quota remaining        - Monitorear para no agotar                       │   │
│  └───────────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                             │
│  DATABASE                                                                                   │
│  ┌───────────────────────────────────────────────────────────────────────────────────┐   │
│  │ • CPU Percentage               - Esperado: < 50%                                 │   │
│  │ • Storage Used (MB)           - Monitorear crecimiento                          │   │
│  │ • Active Connections          - Esperado: < 10                                  │   │
│  │ • Query Performance           - Monitorear queries lentas                       │   │
│  └───────────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                             │
│  COST MANAGEMENT                                                                          │
│  ┌───────────────────────────────────────────────────────────────────────────────────┐   │
│  │ • Daily Cost                   - Mantener < $10/día                             │   │
│  │ • Forecast Month-end           - Estimar costo total                             │   │
│  └───────────────────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🆘 TROUBLESHOOTING RÁPIDO

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                         PROBLEMAS COMUNES Y SOLUCIONES                                     │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────┬───────────────────────────────────────────────────────┐
│ PROBLEMA                            │ SOLUCIÓN                                           │
├─────────────────────────────────────┼───────────────────────────────────────────────────────┤
│ App Service no responde             │ • Restart desde Azure Portal                       │
│                                     │ • Revisar Application Logs                        │
│                                     │ • Verificar configuración de variables            │
├─────────────────────────────────────┼───────────────────────────────────────────────────────┤
│ Error de conexión a DB              │ • Verificar connection string                    │
│                                     │ • Verificar firewall de PostgreSQL                │
│                                     │ • Probar conexión desde Cloud Shell               │
├─────────────────────────────────────┼───────────────────────────────────────────────────────┤
│ OpenAI retorna error 429            │ • Rate limit alcanzado                            │
│                                     │ • Esperar 1 minuto                                │
│                                     │ • Reducir tamaño de prompts                      │
├─────────────────────────────────────┼───────────────────────────────────────────────────────┤
│ Error de autenticación              │ • Verificar Managed Identity                     │
│                                     │ • Revisar Key Vault access                       │
│                                     │ • Verificar tokens en App Settings               │
├─────────────────────────────────────┼───────────────────────────────────────────────────────┤
│ Slow performance                    │ • Verificar tier de App Service                  │
│                                     │ • Revisar queries lentos                         │
│                                     │ • Considerar escalar a S1                        │
├─────────────────────────────────────┼───────────────────────────────────────────────────────┤
│ CORS errors                         │ • Configurar CORS en App Service                 │
│                                     │ • Agregar origen del frontend                    │
└─────────────────────────────────────┴───────────────────────────────────────────────────────┘
```

---

## 📞 CONTACTOS DE SOPORTE AZURE

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                         RECURSOS DE SOPORTE                                                │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

• Azure Portal: https://portal.azure.com
• Azure Status: https://status.azure.com
• Azure Support: https://azure.microsoft.com/support/
• Documentation: https://docs.microsoft.com/azure/
• Stack Overflow: Etiquetar #azure #hackathon
```
