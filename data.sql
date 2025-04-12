-- Limpiar tablas 
DELETE FROM reservas;
DELETE FROM asientos;
DELETE FROM usuarios;
DELETE FROM eventos;

-- Insertar un evento
INSERT INTO eventos (id_evento, nombre, fecha, hora, lugar, descripcion)
VALUES (
    1,
    'Festival Tech 2025',
    '2025-07-20',
    '18:00:00',
    'Auditorio Central',
    'Un evento para amantes de la tecnología y la música en vivo.'
);

-- Insertar 30 asientos para el evento
INSERT INTO asientos (id_asiento, id_evento, fila, numero, tipo, precio)
VALUES 
-- Fila A (VIP)
(1, 1, 'A', 1, 'VIP', 150.00),
(2, 1, 'A', 2, 'VIP', 150.00),
(3, 1, 'A', 3, 'VIP', 150.00),
(4, 1, 'A', 4, 'VIP', 150.00),
(5, 1, 'A', 5, 'VIP', 150.00),
(6, 1, 'A', 6, 'VIP', 150.00),
(7, 1, 'A', 7, 'VIP', 150.00),
(8, 1, 'A', 8, 'VIP', 150.00),
(9, 1, 'A', 9, 'VIP', 150.00),
(10, 1, 'A', 10, 'VIP', 150.00),

-- Fila B (General)
(11, 1, 'B', 1, 'General', 100.00),
(12, 1, 'B', 2, 'General', 100.00),
(13, 1, 'B', 3, 'General', 100.00),
(14, 1, 'B', 4, 'General', 100.00),
(15, 1, 'B', 5, 'General', 100.00),
(16, 1, 'B', 6, 'General', 100.00),
(17, 1, 'B', 7, 'General', 100.00),
(18, 1, 'B', 8, 'General', 100.00),
(19, 1, 'B', 9, 'General', 100.00),
(20, 1, 'B', 10, 'General', 100.00),

-- Fila C (Económica)
(21, 1, 'C', 1, 'Económica', 70.00),
(22, 1, 'C', 2, 'Económica', 70.00),
(23, 1, 'C', 3, 'Económica', 70.00),
(24, 1, 'C', 4, 'Económica', 70.00),
(25, 1, 'C', 5, 'Económica', 70.00),
(26, 1, 'C', 6, 'Económica', 70.00),
(27, 1, 'C', 7, 'Económica', 70.00),
(28, 1, 'C', 8, 'Económica', 70.00),
(29, 1, 'C', 9, 'Económica', 70.00),
(30, 1, 'C', 10, 'Económica', 70.00);

-- Insertar usuarios de prueba
INSERT INTO usuarios (id_usuario, nombre, email, telefono)
VALUES 
(1, 'Laura Torres', 'laura.torres@email.com', '321456789'),
(2, 'Juan Herrera', 'juan.herrera@email.com', '322111223'),
(3, 'Sofía Martínez', 'sofia.martinez@email.com', '320987654'),
(4, 'Pedro Reyes', 'pedro.reyes@email.com', '310998877'),
(5, 'Carla Gómez', 'carla.gomez@email.com', '300123456');

-- Insertar algunas reservas iniciales (para simular uso real)
INSERT INTO reservas (id_reserva, id_usuario, id_asiento, fecha_reserva, estado)
VALUES 
(1, 1, 5, now(), 'Pagada'),
(2, 2, 12, now(), 'Pagada'),
(3, 3, 18, now(), 'Activa');
