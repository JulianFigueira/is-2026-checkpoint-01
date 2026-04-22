-- Crea la tabla members con los campos exactos pedidos
CREATE TABLE IF NOT EXISTS members (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    legajo VARCHAR(20),
    feature VARCHAR(100),
    servicio VARCHAR(100),
    estado VARCHAR(50)
);

-- Inserta una fila por cada integrante del grupo
INSERT INTO members (nombre, apellido, legajo, feature, servicio, estado) 
VALUES 
('Julian', 'Figueira', '33369', 'Feature 01', 'coordinador', 'activo'),
('Bernardita', 'La Gioiosa', '33289', 'Feature 02', 'frontend', 'activo'),
('Yamil', 'Tundis', '33648', 'Feature 03', 'backend', 'activo'),
('Ulises', 'Bucchino', '33326', 'Feature 04', 'database', 'activo'),
('Lautaro', 'Amado', '33146', 'Feature 05', 'portainer', 'activo');