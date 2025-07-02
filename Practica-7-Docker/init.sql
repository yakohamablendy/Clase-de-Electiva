-- Script de inicialización para la base de datos
-- Este archivo se ejecuta automáticamente cuando el contenedor MySQL se inicia por primera vez

USE hola_mundo_db;

-- Crear tabla de mensajes para la aplicación Python
CREATE TABLE IF NOT EXISTS mensajes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mensaje VARCHAR(255) NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insertar mensajes de ejemplo para la aplicación Python Flask
INSERT INTO mensajes (mensaje) VALUES 
('¡Hola Mundo desde Python + Flask!'),
('Aplicación creada con Docker Compose'),
('Python + Flask + MySQL funcionando perfectamente'),
('¡Bienvenido a tu aplicación Python containerizada!'),
('Stack: Python 3.11 + Flask + MySQL 8.0'),
('Desarrollo con Visual Studio Code + Docker');

-- Crear tabla de usuarios para demostrar más funcionalidad
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    rol ENUM('admin', 'usuario', 'moderador') DEFAULT 'usuario',
    activo BOOLEAN DEFAULT TRUE,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insertar usuarios de ejemplo
INSERT INTO usuarios (nombre, email, rol) VALUES 
('Administrador', 'admin@holamundo.com', 'admin'),
('Usuario Demo', 'demo@holamundo.com', 'usuario'),
('Moderador', 'mod@holamundo.com', 'moderador'),
('Juan Pérez', 'juan@ejemplo.com', 'usuario'),
('María García', 'maria@ejemplo.com', 'usuario');

-- Crear tabla de logs para la aplicación
CREATE TABLE IF NOT EXISTS logs_aplicacion (
    id INT AUTO_INCREMENT PRIMARY KEY,
    evento VARCHAR(100) NOT NULL,
    descripcion TEXT,
    ip_usuario VARCHAR(45),
    fecha_evento TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insertar logs de ejemplo
INSERT INTO logs_aplicacion (evento, descripcion, ip_usuario) VALUES 
('INICIO_APLICACION', 'Aplicación Python Flask iniciada correctamente', '172.18.0.1'),
('CONEXION_BD', 'Conexión exitosa a base de datos MySQL', '172.18.0.1'),
('CARGA_INICIAL', 'Datos iniciales cargados en la base de datos', '172.18.0.1');

-- Crear vista para estadísticas básicas
CREATE VIEW estadisticas_basicas AS
SELECT 
    (SELECT COUNT(*) FROM mensajes) as total_mensajes,
    (SELECT COUNT(*) FROM usuarios) as total_usuarios,
    (SELECT COUNT(*) FROM usuarios WHERE activo = TRUE) as usuarios_activos,
    (SELECT COUNT(*) FROM logs_aplicacion) as total_logs;

-- Mostrar información de inicialización
SELECT 'Base de datos inicializada correctamente para la aplicación Python Flask' AS mensaje;