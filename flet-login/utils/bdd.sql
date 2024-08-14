USE HARD
CREATE TABLE usuarios (
    USUARIO_ID INT(3) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    USUARIO_NOMBRE VARCHAR(30) NOT NULL,
    USUARIO_EMAIL VARCHAR(50) NOT NULL,
    USUARIO_PASSWORD VARCHAR(20) NOT NULL,
    USUARIO_FECHA_REGISTRO TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    USUARIO_FECHA_ACTUALIZACION TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    USUARIO_TIPO VARCHAR(15) NOT NULL
);

--_______________________Impedir incersiones duplicadas_________________________--
CREATE TRIGGER before_insert_usuario
BEFORE INSERT ON USUARIOS
FOR EACH ROW
BEGIN
    DECLARE user_count INT;
    DECLARE email_count INT;

    -- Verificar si ya existe un usuario con el mismo nombre de usuario
    SELECT COUNT(*) INTO user_count FROM USUARIOS WHERE USUARIO_NOMBRE = NEW.USUARIO_NOMBRE;

    -- Verificar si ya existe un usuario con el mismo correo electrónico
    SELECT COUNT(*) INTO email_count FROM USUARIOS WHERE USUARIO_EMAIL = NEW.USUARIO_EMAIL;

    -- Si ya existe un usuario con el mismo nombre de usuario o correo electrónico, cancelar la inserción
    IF user_count > 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Ya existe un usuario con el mismo nombre de usuario';
    END IF;

    IF email_count > 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Ya existe un usuario con el mismo correo electrónico';
    END IF;
END;

--______________________Normalizar el nombre del usuario_________________________--

CREATE TRIGGER normalizar_caracteres BEFORE INSERT ON USUARIOS
FOR EACH ROW
BEGIN
    DECLARE nombre_normalizado VARCHAR(255);
    SET nombre_normalizado = LOWER(NEW.USUARIO_NOMBRE);
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'a', 'A');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'b', 'B');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'c', 'C');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'd', 'D');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'e', 'E');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'f', 'F');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'g', 'G');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'h', 'H');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'i', 'I');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'j', 'J');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'k', 'K');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'l', 'L');
    SET nombre_normalizado = REPLACE(nombre_normalizado,'m', 'M');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'n', 'N');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'o', 'O');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'p', 'P');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'q', 'Q');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'r', 'R');
    SET nombre_normalizado = REPLACE(nombre_normalizado,'s', 'S');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 't', 'T');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'u', 'U');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'v', 'V');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'w', 'W');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'x', 'X');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'y', 'Y');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'z', 'Z');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'á', 'A');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'é', 'E');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'í', 'I');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'ó', 'O');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'ú', 'U');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'à', 'A');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'è', 'E');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'ì', 'I');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'ò', 'O');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'ù', 'U');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'ä', 'A');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'ë', 'E');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'ï', 'I');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'ö', 'O');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'ü', 'U');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'ã', 'A');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'õ', 'O');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'ñ', 'N');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'Ñ', 'N');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'ç', 'C');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'Ç', 'C');
    SET nombre_normalizado = REPLACE(nombre_normalizado, 'ß', 'SS');
    SET nombre_normalizado = REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(nombre_normalizado, '.', ''), ',', ''), ';', ''), ':', ''), '?', ''), '!', ''), '''', ''), '"', ''), '`', '');
    SET NEW.USUARIO_NOMBRE = nombre_normalizado;
END;