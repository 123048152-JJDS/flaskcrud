# Flask CRUD — Dockerizado 🐳

Proyecto original por: [Javier Moya](https://github.com/javiermoya2504/flaskcrud)

Alumno: [Tu nombre completo]  
Materia: Administración de Servidores  
Docente: JOSE JAVIER MOYA MOYA  
Universidad Politécnica de Querétaro  

---

## 📋 Descripción

Aplicación web CRUD de contactos desarrollada con Flask y MySQL, dockerizada para su despliegue en cualquier entorno con Docker.

## 🔧 Modificaciones realizadas al proyecto original

- ✅ Creación del `Dockerfile` para la app Flask
- ✅ Creación del `docker-compose.yml` con servicios Flask + MySQL
- ✅ Corrección de `app/app.py`: rutas de `template_folder` y `static_folder`
- ✅ Configuración de `healthcheck` en MySQL para evitar errores de conexión
- ✅ Persistencia de datos con volumen Docker

## 🚀 Cómo correr el proyecto

### Requisitos
- Docker Engine
- Docker Compose

### Pasos
```bash
# 1. Clonar el repositorio
git clone https://github.com/123048152-JJDS/flaskcrud.git
cd flaskcrud

# 2. Levantar los servicios
docker-compose up --build -d

# 3. Esperar ~30 segundos y verificar que estén corriendo
docker ps

# 4. Abrir en el navegador
http://localhost:8081
```

### Detener los servicios
```bash
docker-compose down
```

### Detener y eliminar datos
```bash
docker-compose down -v
```

## 🏗️ Arquitectura
```
┌─────────────────────────────────────┐
│         Docker Network              │
│  ┌──────────────┐  ┌─────────────┐  │
│  │  Flask App   │  │    MySQL    │  │
│  │  Port: 8081  │──│  Port: 3306 │  │
│  └──────────────┘  └─────────────┘  │
└─────────────────────────────────────┘
```

## 📁 Estructura del proyecto
```
flaskcrud/
├── app/
│   ├── app.py          # Inicialización de Flask (modificado)
│   ├── main.py         # Punto de entrada, puerto 8081
│   ├── contacts.py     # Rutas CRUD
│   ├── db.py           # Conexión MySQL
│   ├── static/
│   │   ├── css/main.css
│   │   └── js/main.js
│   └── templates/
│       ├── layout.html
│       ├── index.html
│       └── edit-contact.html
├── sql/
│   └── db.sql          # Script de creación de BD
├── Dockerfile          # ← Creado en esta actividad
├── docker-compose.yml  # ← Creado en esta actividad
├── .env                # Variables de entorno MySQL
└── requirements.txt    # Dependencias Python
```

## ⚙️ Variables de entorno (.env)
```env
MYSQL_HOST=mysql
MYSQL_USER=root
MYSQL_PASSWORD=faztpassword
MYSQL_DB=flaskcrud
MYSQL_PORT=3306
```

## 🐛 Incidencias resueltas

| Error | Solución |
|-------|----------|
| MySQL unhealthy | Agregar `start_period: 30s` al healthcheck |
| TemplateNotFound | Corregir rutas en `app.py` |
| Can't connect to mysql | Levantar ambos contenedores en la misma red |
| Puerto 3306 ocupado | Mapear a `3307:3306` en docker-compose |

## 🛠️ Tecnologías

- Python 3.9 / Flask 2.1.2
- MySQL 8.0
- Docker / Docker Compose
- Ubuntu Server 22.04
