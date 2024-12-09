CREATE TABLE Estudiantes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    edad INT,
    ciudad VARCHAR(50)
);

INSERT INTO Estudiantes (nombre, edad, ciudad)
VALUES ('Ana', 22, 'Bogotá'), 
       ('Luis', 19, 'Medellín'), 
       ('Sofía', 24, 'Cali');

SELECT * FROM Estudiantes;
SELECT * FROM Estudiantes WHERE ciudad = 'Cali';
SELECT * FROM Estudiantes WHERE edad > 20;
