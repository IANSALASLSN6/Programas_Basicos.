parcial = float( input( 'Nota parciales (0 a 100): ' ) )
proyecto = float( input( 'Nota proyecto (0 a 100): ' ) )
examen = float( input( 'Nota examen (0 a 100): ' ) )

if ( parcial < 0 or parcial > 100 ) or ( proyecto < 0 or proyecto > 100 ) or ( examen < 0 or examen > 100 ):
    print( "Error: Las notas deben de estar entre 0 y 100" )
else:
    calificacion_final = ( parcial * 0.40 ) + ( proyecto * 0.30 ) + ( examen * 0.30 )

print( "Calificacion final es:" , calificacion_final )