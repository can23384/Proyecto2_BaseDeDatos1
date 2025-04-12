-- Eliminar tablas si existen (orden inverso por dependencias)
DROP TABLE IF EXISTS reservas;
DROP TABLE IF EXISTS asientos;
DROP TABLE IF EXISTS usuarios;
DROP TABLE IF EXISTS eventos;

-- Tabla de eventos
CREATE TABLE eventos (
    id_evento SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    lugar VARCHAR(100) NOT NULL,
    descripcion TEXT
);

-- Tabla de usuarios
CREATE TABLE usuarios (
    id_usuario SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefono VARCHAR(20)
);

-- Tabla de asientos
CREATE TABLE asientos (
    id_asiento SERIAL PRIMARY KEY,
    id_evento INT NOT NULL REFERENCES eventos(id_evento) ON DELETE CASCADE,
    fila VARCHAR(5) NOT NULL,
    numero INT NOT NULL,
    tipo VARCHAR(20),
    precio DECIMAL(10, 2) NOT NULL CHECK (precio >= 0),
    UNIQUE (id_evento, fila, numero)
);

-- Tabla de reservas
CREATE TABLE reservas (
    id_reserva SERIAL PRIMARY KEY,
    id_usuario INT NOT NULL REFERENCES usuarios(id_usuario) ON DELETE CASCADE,
    id_asiento INT NOT NULL UNIQUE REFERENCES asientos(id_asiento) ON DELETE CASCADE,
    fecha_reserva TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    estado VARCHAR(20) NOT NULL CHECK (estado IN ('Activa', 'Cancelada', 'Pagada'))
);