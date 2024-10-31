import sqlite3

def init_db():
    conn = sqlite3.connect('videostream.db')
    c = conn.cursor()

    # Crear tabla de usuarios
    c.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            dni TEXT NOT NULL,
            email TEXT NOT NULL,
            telefono TEXT NOT NULL,
            direccion TEXT NOT NULL
        )
    ''')

    # Crear tabla de contenido
    c.execute('''
        CREATE TABLE IF NOT EXISTS contenido (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            genero TEXT NOT NULL,
            ano INTEGER NOT NULL,
            director TEXT NOT NULL,
            protagonista TEXT NOT NULL,
            tipo_contenido TEXT NOT NULL
        )
    ''')

    # Crear tabla de alquileres
    c.execute('''
        CREATE TABLE IF NOT EXISTS alquileres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER NOT NULL,
            contenido_id INTEGER NOT NULL,
            fecha_alquiler TEXT NOT NULL,
            fecha_devolucion TEXT NOT NULL,
            importe REAL NOT NULL,
            alquilado BOOLEAN NOT NULL,
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
            FOREIGN KEY (contenido_id) REFERENCES contenido(id)
        )
    ''')

    # Cargar datos de usuarios
    usuarios = [
    (1, "Juan Pérez", "12345678", "juan.perez@algunmail.com", "1234567890", "Calle Falsa 123"),
    (2, "María Gómez", "23456789", "maria.gomez@algunmail.com", "2345678901", "Avenida Siempre Viva 456"),
    (3, "Luis Martínez", "34567890", "luis.martinez@algunmail.com", "3456789012", "Calle 7 789"),
    (4, "Ana Lopez", "45678901", "ana.lopez@algunmail.com", "4567890123", "Calle del Sol 101"),
    (5, "Carlos Sánchez", "56789012", "carlos.sanchez@algunmail.com", "5678901234", "Calle del Mar 202"),
    (6, "Laura Ramírez", "67890123", "laura.ramirez@algunmail.com", "6789012345", "Avenida de la Luna 303"),
    (7, "Diego Torres", "78901234", "diego.torres@algunmail.com", "7890123456", "Calle del Río 404"),
    (8, "Lucía Hernández", "89012345", "lucia.hernandez@algunmail.com", "8901234567", "Calle Verde 505"),
    (9, "Javier García", "90123456", "javier.garcia@algunmail.com", "9012345678", "Calle de los Pinos 606"),
    (10, "Sofía Díaz", "01234567", "sofia.diaz@algunmail.com", "0123456789", "Avenida del Sol 707"),
    (11, "Pablo Cruz", "12345679", "pablo.cruz@algunmail.com", "1234567891", "Calle de la Paz 808"),
    (12, "Claudia Vega", "23456780", "claudia.vega@algunmail.com", "2345678902", "Calle del Viento 909"),
    (13, "Ricardo Morales", "34567891", "ricardo.morales@algunmail.com", "3456789013", "Calle de la Esperanza 1010"),
    (14, "Teresa Ríos", "45678902", "teresa.rios@algunmail.com", "4567890124", "Calle de la Libertad 1111"),
    (15, "Andrés Castillo", "56789013", "andres.castillo@algunmail.com", "5678901235", "Calle de la Amistad 1212"),
    (16, "Carmen Jiménez", "67890124", "carmen.jimenez@algunmail.com", "6789012346", "Calle del Jardín 1313"),
    (17, "Fernando Salas", "78901235", "fernando.salas@algunmail.com", "7890123457", "Calle de la Esperanza 1414"),
    (18, "Isabel Moreno", "89012346", "isabel.moreno@algunmail.com", "8901234568", "Calle del Álamo 1515"),
    (19, "Antonio Mendoza", "90123457", "antonio.mendoza@algunmail.com", "9012345679", "Avenida de la Victoria 1616"),
    (20, "Paola Córdova", "01234568", "paola.cordova@algunmail.com", "0123456790", "Calle de la Alegría 1717"),
    (21, "Martín Paniagua", "12345680", "martin.paniagua@algunmail.com", "1234567892", "Calle de la Sabiduría 1818"),
    (22, "Nadia Almeida", "23456781", "nadia.almeida@algunmail.com", "2345678903", "Calle de la Unión 1919"),
    (23, "Jorge González", "34567892", "jorge.gonzalez@algunmail.com", "3456789014", "Calle del Progreso 2020"),
    (24, "Verónica Alonso", "45678903", "veronica.alonso@algunmail.com", "4567890125", "Calle de la Libertad 2121"),
    (25, "Diego Castro", "56789014", "diego.castro@algunmail.com", "5678901236", "Calle de la Tranquilidad 2222"),
    (26, "Gloria Valdez", "67890125", "gloria.valdez@algunmail.com", "6789012347", "Calle de la Fortaleza 2323"),
    (27, "Felipe Rojas", "78901236", "felipe.rojas@algunmail.com", "7890123459", "Calle de la Amistad 2424"),
    (28, "Rosa Sierra", "89012347", "rosa.sierra@algunmail.com", "8901234569", "Avenida de la Esperanza 2525"),
    (29, "Emilio Bermúdez", "90123458", "emilio.bermudez@algunmail.com", "9012345680", "Calle de la Concordia 2626"),
    (30, "Laura Santiago", "01234569", "laura.santiago@algunmail.com", "0123456791", "Calle del Mar 2727"),
    (31, "Cristian Núñez", "12345681", "cristian.nunez@algunmail.com", "1234567893", "Calle de la Alegría 2828"),
    (32, "Fabiola Pérez", "23456782", "fabiola.perez@algunmail.com", "2345678904", "Calle de la Ternura 2929"),
    (33, "Alberto Guerrero", "34567893", "alberto.guerrero@algunmail.com", "3456789015", "Calle del Camino 3030"),
    (34, "Patricia Cáceres", "45678904", "patricia.caceres@algunmail.com", "4567890126", "Calle de la Amistad 3131"),
    (35, "Eduardo Mora", "56789015", "eduardo.mora@algunmail.com", "5678901237", "Calle de la Tranquilidad 3232"),
    (36, "Santiago Paz", "67890126", "santiago.paz@algunmail.com", "6789012348", "Calle del Refugio 3333"),
    (37, "Gabriela Maldonado", "78901237", "gabriela.maldonado@algunmail.com", "7890123459", "Calle de la Esperanza 3434"),
    (38, "Samuel Salcedo", "89012348", "samuel.salcedo@algunmail.com", "8901234570", "Avenida de la Libertad 3535"),
    (39, "Nicolás Ramírez", "90123459", "nicolas.ramirez@algunmail.com", "9012345681", "Calle del Sol 3636"),
    (40, "Daniela Bravo", "01234560", "daniela.bravo@algunmail.com", "0123456792", "Calle de la Libertad 3737"),
    (41, "Leonardo Paredes", "12345682", "leonardo.paredes@algunmail.com", "1234567894", "Calle del Paraíso 3838"),
    (42, "Silvia Ocampo", "23456783", "silvia.ocampo@algunmail.com", "2345678905", "Calle de la Amistad 3939"),
    (43, "Héctor Jiménez", "34567894", "hector.jimenez@algunmail.com", "3456789016", "Calle del Sueño 4040"),
    (44, "Alma Escobar", "45678905", "alma.escobar@algunmail.com", "4567890127", "Calle de la Esperanza 4141"),
    (45, "Esteban Ramos", "56789016", "esteban.ramos@algunmail.com", "5678901238", "Calle de la Serenidad 4242"),
    (46, "Cristina Oliva", "67890127", "cristina.oliva@algunmail.com", "6789012349", "Calle del Jardín 4343"),
    (47, "Patricio Delgado", "78901238", "patricio.delgado@algunmail.com", "7890123460", "Calle de la Armonía 4444"),
    (48, "Cecilia Lira", "89012349", "cecilia.lira@algunmail.com", "8901234571", "Avenida de la Paz 4545"),
    (49, "Mauro Castillo", "90123460", "mauro.castillo@algunmail.com", "9012345682", "Calle de la Dignidad 4646"),
    (50, "Valentina Cordero", "01234571", "valentina.cordero@algunmail.com", "0123456793", "Calle de la Esperanza 4747"),
    ]

    c.executemany('INSERT INTO usuarios VALUES (?, ?, ?, ?, ?, ?)', usuarios)

    # Cargar datos de contenido
    contenido = [
    (1, "Inception", "Ciencia Ficción", 2010, "Christopher Nolan", "Leonardo DiCaprio", "Película"),
    (2, "Breaking Bad", "Drama", 2008, "Vince Gilligan", "Bryan Cranston", "Serie"),
    (3, "The Crown", "Drama", 2016, "Peter Morgan", "Claire Foy", "Serie"),
    (4, "Interstellar", "Ciencia Ficción", 2014, "Christopher Nolan", "Matthew McConaughey", "Película"),
    (5, "Stranger Things", "Fantasía", 2016, "The Duffer Brothers", "Winona Ryder", "Serie"),
    (6, "The Godfather", "Drama", 1972, "Francis Ford Coppola", "Marlon Brando", "Película"),
    (7, "The Office", "Comedia", 2005, "Greg Daniels", "Steve Carell", "Serie"),
    (8, "Parasite", "Thriller", 2019, "Bong Joon-ho", "Song Kang-ho", "Película"),
    (9, "Game of Thrones", "Fantasía", 2011, "David Benioff", "Emilia Clarke", "Serie"),
    (10, "Pulp Fiction", "Crimen", 1994, "Quentin Tarantino", "John Travolta", "Película"),
    (11, "The Witcher", "Fantasía", 2019, "Lauren Schmidt Hissrich", "Henry Cavill", "Serie"),
    (12, "Titanic", "Romance", 1997, "James Cameron", "Leonardo DiCaprio", "Película"),
    (13, "The Mandalorian", "Ciencia Ficción", 2019, "Jon Favreau", "Pedro Pascal", "Serie"),
    (14, "Fight Club", "Drama", 1999, "David Fincher", "Brad Pitt", "Película"),
    (15, "Friends", "Comedia", 1994, "David Crane", "Jennifer Aniston", "Serie"),
    (16, "The Dark Knight", "Acción", 2008, "Christopher Nolan", "Christian Bale", "Película"),
    (17, "Sherlock", "Misterio", 2010, "Mark Gatiss", "Benedict Cumberbatch", "Serie"),
    (18, "Forrest Gump", "Drama", 1994, "Robert Zemeckis", "Tom Hanks", "Película"),
    (19, "Black Mirror", "Ciencia Ficción", 2011, "Charlie Brooker", "Daniel Kaluuya", "Serie"),
    (20, "Gladiator", "Acción", 2000, "Ridley Scott", "Russell Crowe", "Película"),
    (21, "The Big Bang Theory", "Comedia", 2007, "Chuck Lorre", "Johnny Galecki", "Serie"),
    (22, "The Social Network", "Drama", 2010, "David Fincher", "Jesse Eisenberg", "Película"),
    (23, "Westworld", "Ciencia Ficción", 2016, "Jonathan Nolan", "Evan Rachel Wood", "Serie"),
    (24, "The Shawshank Redemption", "Drama", 1994, "Frank Darabont", "Tim Robbins", "Película"),
    (25, "Better Call Saul", "Drama", 2015, "Vince Gilligan", "Bob Odenkirk", "Serie"),
    (26, "Jurassic Park", "Aventura", 1993, "Steven Spielberg", "Sam Neill", "Película"),
    (27, "Stranger Things", "Fantasía", 2016, "The Duffer Brothers", "Winona Ryder", "Serie"),
    (28, "The Matrix", "Ciencia Ficción", 1999, "The Wachowskis", "Keanu Reeves", "Película"),
    (29, "The Simpsons", "Comedia", 1989, "Matt Groening", "Dan Castellaneta", "Serie"),
    (30, "Deadpool", "Acción", 2016, "Tim Miller", "Ryan Reynolds", "Película"),
    (31, "How I Met Your Mother", "Comedia", 2005, "Carter Bays", "Josh Radnor", "Serie"),
    (32, "The Silence of the Lambs", "Thriller", 1991, "Jonathan Demme", "Jodie Foster", "Película"),
    (33, "The Sopranos", "Drama", 1999, "David Chase", "James Gandolfini", "Serie"),
    (34, "Avatar", "Ciencia Ficción", 2009, "James Cameron", "Sam Worthington", "Película"),
    (35, "The Handmaid's Tale", "Drama", 2017, "Bruce Miller", "Elisabeth Moss", "Serie"),
    (36, "Saving Private Ryan", "Guerra", 1998, "Steven Spielberg", "Tom Hanks", "Película"),
    (37, "The Crown", "Drama", 2016, "Peter Morgan", "Claire Foy", "Serie"),
    (38, "Zodiac", "Thriller", 2007, "David Fincher", "Jake Gyllenhaal", "Película"),
    (39, "The Good Place", "Comedia", 2016, "Michael Schur", "Kristen Bell", "Serie"),
    (40, "The Revenant", "Aventura", 2015, "Alejandro González Iñárritu", "Leonardo DiCaprio", "Película"),
    (41, "Mindhunter", "Drama", 2017, "Joe Penhall", "Jonathan Groff", "Serie"),
    (42, "The Intouchables", "Comedia", 2011, "Olivier Nakache", "François Cluzet", "Película"),
    (43, "Narcos", "Drama", 2015, "Eric Newman", "Pedro Pascal", "Serie"),
    (44, "Coco", "Animación", 2017, "Lee Unkrich", "Anthony Gonzalez", "Película"),
    (45, "Ozark", "Drama", 2017, "Bill Dubuque", "Jason Bateman", "Serie"),
    (46, "The Usual Suspects", "Crimen", 1995, "Bryan Singer", "Kevin Spacey", "Película"),
    (47, "Parks and Recreation", "Comedia", 2009, "Greg Daniels", "Amy Poehler", "Serie"),
    (48, "Memento", "Thriller", 2000, "Christopher Nolan", "Guy Pearce", "Película"),
    (49, "Fargo", "Crimen", 1996, "Joel Coen", "Frances McDormand", "Película"),
    (50, "The West Wing", "Drama", 1999, "Aaron Sorkin", "Martin Sheen", "Serie")
    ]

    c.executemany('INSERT INTO contenido VALUES (?, ?, ?, ?, ?, ?, ?)', contenido)

    # Cargar datos de alquileres
    alquileres = [
    (1, 1, 1, "2024-01-01", "2024-01-08", 5.99, True),
    (2, 2, 2, "2024-01-02", "2024-01-09", 3.99, True),
    (3, 3, 3, "2024-01-03", "2024-01-10", 4.99, False),
    (4, 4, 4, "2024-01-04", "2024-01-11", 6.99, True),
    (5, 5, 5, "2024-01-05", "2024-01-12", 4.49, False),
    (6, 6, 6, "2024-01-06", "2024-01-13", 5.49, True),
    (7, 7, 7, "2024-01-07", "2024-01-14", 2.99, False),
    (8, 8, 8, "2024-01-08", "2024-01-15", 7.99, True),
    (9, 9, 9, "2024-01-09", "2024-01-16", 4.99, False),
    (10, 10, 10, "2024-01-10", "2024-01-17", 3.49, True),
    (11, 11, 11, "2024-01-11", "2024-01-18", 8.99, False),
    (12, 12, 12, "2024-01-12", "2024-01-19", 6.49, True),
    (13, 13, 13, "2024-01-13", "2024-01-20", 2.49, False),
    (14, 14, 14, "2024-01-14", "2024-01-21", 5.99, True),
    (15, 15, 15, "2024-01-15", "2024-01-22", 3.99, False),
    (16, 16, 16, "2024-01-16", "2024-01-23", 4.99, True),
    (17, 17, 17, "2024-01-17", "2024-01-24", 6.99, False),
    (18, 18, 18, "2024-01-18", "2024-01-25", 5.49, True),
    (19, 19, 19, "2024-01-19", "2024-01-26", 7.49, False),
    (20, 20, 20, "2024-01-20", "2024-01-27", 2.99, True),
    (21, 21, 21, "2024-01-21", "2024-01-28", 4.49, False),
    (22, 22, 22, "2024-01-22", "2024-01-29", 3.49, True),
    (23, 23, 23, "2024-01-23", "2024-01-30", 8.49, False),
    (24, 24, 24, "2024-01-24", "2024-01-31", 5.99, True),
    (25, 25, 25, "2024-01-25", "2024-02-01", 6.49, False),
    (26, 26, 26, "2024-01-26", "2024-02-02", 7.99, True),
    (27, 27, 27, "2024-01-27", "2024-02-03", 2.99, False),
    (28, 28, 28, "2024-01-28", "2024-02-04", 4.99, True),
    (29, 29, 29, "2024-01-29", "2024-02-05", 3.49, False),
    (30, 30, 30, "2024-01-30", "2024-02-06", 8.99, True),
    (31, 31, 31, "2024-01-31", "2024-02-07", 5.49, False),
    (32, 32, 32, "2024-02-01", "2024-02-08", 6.99, True),
    (33, 33, 33, "2024-02-02", "2024-02-09", 4.49, False),
    (34, 34, 34, "2024-02-03", "2024-02-10", 3.99, True),
    (35, 35, 35, "2024-02-04", "2024-02-11", 5.99, False),
    (36, 36, 36, "2024-02-05", "2024-02-12", 6.49, True),
    (37, 37, 37, "2024-02-06", "2024-02-13", 2.99, False),
    (38, 38, 38, "2024-02-07", "2024-02-14", 4.99, True),
    (39, 39, 39, "2024-02-08", "2024-02-15", 3.49, False),
    (40, 40, 40, "2024-02-09", "2024-02-16", 7.99, True),
    (41, 41, 41, "2024-02-10", "2024-02-17", 5.99, False),
    (42, 42, 42, "2024-02-11", "2024-02-18", 6.49, True),
    (43, 43, 43, "2024-02-12", "2024-02-19", 4.99, False),
    (44, 44, 44, "2024-02-13", "2024-02-20", 8.49, True),
    (45, 45, 45, "2024-02-14", "2024-02-21", 3.99, False),
    (46, 46, 46, "2024-02-15", "2024-02-22", 5.49, True),
    (47, 47, 47, "2024-02-16", "2024-02-23", 2.99, False),
    (48, 48, 48, "2024-02-17", "2024-02-24", 4.49, True),
    (49, 49, 49, "2024-02-18", "2024-02-25", 6.99, False),
    (50, 50, 50, "2024-02-19", "2024-02-26", 5.49, True)
    ]


    c.executemany('INSERT INTO alquileres VALUES (?, ?, ?, ?, ?, ?, ?)', alquileres)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()