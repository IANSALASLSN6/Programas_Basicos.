celsius = float( input( 'Temperatura en ªC: ' ) )

print("1. Fahrenheit\n2. Kelvin")

opcion = int( input( 'Elige opcion: ' ) )

match opcion :
    case 1 :
        resultado = celsius * 9 / 5 + 32
        unidad = "ªF"
    case 2 :
        resultado = celsius + 273.15
        unidad = "K"
    case _ :
        resultado = None
        print( "Opcion invalida" )

if resultado is not None :
    print( "Convertido: " , resultado , unidad )