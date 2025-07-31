# 🐍 Aplicación Hola Mundo Python + Flask + MySQL con Docker

## 📋 Descripción del Proyecto
Aplicación web simple desarrollada en Python con Flask que se conecta a una base de datos MySQL, todo ejecutándose en contenedores Docker usando Docker Compose.

## 🛠️ Tecnologías Utilizadas
- **Python 3.11** - Lenguaje de programación
- **Flask** - Framework web de Python
- **MySQL 8.0** - Base de datos relacional
- **Docker** - Containerización
- **Docker Compose** - Orquestación de contenedores
- **phpMyAdmin** - Administración web de MySQL

## 📁 Estructura del Proyecto
```
hola-mundo-python-docker/
├── src/
│   ├── app.py              # Aplicación principal Flask
│   └── requirements.txt    # Dependencias de Python
├── Dockerfile              # Imagen personalizada de Python
├── docker-compose.yml      # Configuración de servicios
├── init.sql               # Script de inicialización de BD
└── README.md              # Este archivo
```

## 🚀 Instalación y Ejecución

### Requisitos Previos
- Docker Desktop instalado
- Visual Studio Code (recomendado)

### Pasos para ejecutar:

1. **Clonar o descargar el proyecto**
```bash
git clone [URL_DE_TU_REPOSITORIO]
cd hola-mundo-python-docker
```

2. **Construir y ejecutar los contenedores**
```bash
docker-compose up --build -d
```

3. **Verificar que los contenedores están ejecutándose**
```bash
docker ps
```

4. **Acceder a la aplicación**
- Aplicación Python: http://localhost:5000
- phpMyAdmin: http://localhost:8080

## 🌐 Acceso a los Servicios

| Servicio | URL | Puerto | Credenciales |
|----------|-----|--------|--------------|
| Aplicación Flask | http://localhost:5000 | 5000 | - |
| phpMyAdmin | http://localhost:8080 | 8080 | usuario: `usuario`<br>password: `password123` |
| MySQL | localhost | 3306 | usuario: `usuario`<br>password: `password123` |

## 📊 Funcionalidades

✅ Conexión exitosa a base de datos MySQL  
✅ Interfaz web responsive con Python/Flask  
✅ Creación automática de tablas y datos de ejemplo  
✅ Manejo de errores de conexión  
✅ Información del sistema en tiempo real  
✅ Persistencia de datos con volúmenes Docker  
✅ Administración web de base de datos  

## 🔧 Comandos Útiles

### Desarrollo
```bash
# Ver logs de la aplicación
docker-compose logs -f web

# Ver logs de MySQL
docker-compose logs -f mysql

# Reiniciar solo la aplicación Python
docker-compose restart web

# Acceder al contenedor Python
docker exec -it hola_mundo_python bash
```

### Mantenimiento
```bash
# Detener todos los contenedores
docker-compose down

# Detener y eliminar volúmenes (borra datos)
docker-compose down -v

# Reconstruir imágenes
docker-compose up --build
```

## 📋 Base de Datos

### Tablas creadas automáticamente:
- **mensajes** - Mensajes de ejemplo para la aplicación
- **usuarios** - Usuarios del sistema con roles
- **logs_aplicacion** - Registro de eventos
- **estadisticas_basicas** - Vista con estadísticas

### Datos de ejemplo incluidos:
- Mensajes de bienvenida
- Usuarios con diferentes roles (admin, usuario, moderador)
- Logs de inicio de aplicación

## 🐛 Solución de Problemas

### Puerto ocupado
Si el puerto 5000 está en uso:
```yaml
# En docker-compose.yml cambiar:
ports:
  - "5001:5000"  # Usar puerto 5001
```

### MySQL no se conecta
```bash
# Verificar logs de MySQL
docker-compose logs mysql

# Esperar a que MySQL se inicialice (30-60 segundos)
```

### Cambios no se reflejan
```bash
# Reconstruir contenedores
docker-compose down
docker-compose up --build
```

## 👨‍💻 Desarrollo

### Modificar código Python:
1. Editar archivos en la carpeta `src/`
2. Los cambios se reflejan automáticamente (Flask en modo debug)
3. Refrescar el navegador en http://localhost:5000

### Agregar dependencias:
1. Editar `src/requirements.txt`
2. Ejecutar: `docker-compose up --build`

## 📤 Deployment

### Para producción:
1. Cambiar contraseñas por defecto en `docker-compose.yml`
2. Desactivar modo debug en `app.py`: `debug=False`
3. Usar variables de entorno para credenciales

## 📄 Licencia
Este proyecto es para fines educativos.

## 👤 Autor
[Tu Nombre] - [Tu Email]

---
⭐ Si te gustó este proyecto, dale una estrella en GitHub!