consulta = input( 'Ingrese nombre de artista, pelicula o serie: ' ).lower()

match consulta :
    case "inception" :
        info = "Pelicula de ciencia ficcion dirigida por Cristhoper Nolan"
    case "beatles" :
        info = "Banda britanica de rock formada en 1960"
    case "rick and morty" :
        info = "Serie animada de comedia y ciencia ficcion"
    case "stranger things" :
        info = "Serie de terror y ciencia ficcion de Netflix"
    case "avengers" :
        info = "Pelicula de superheroes del MCU"
    case "interestellar" :
        info = "Pelicula de ciencia ficcion sobre viajes espaciales y tiempo"
    case "queen" :
        info = "Banda britanica famosa por 'Bohemian Rhapsody'"
    case "friends" :
        info = "Serie de comedia estadounidense muy popular en los 90"
    case "harry potter" :
        info = "Saga de peliculas basada en los libros de J.K Rowling"
    case _ :
        info = "No se encontro info"

print( f"{consulta}: {info}" )