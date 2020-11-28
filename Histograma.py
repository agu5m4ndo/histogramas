import time

listadevalores=list()


print()
print('              [HISTOGRAMA]')
time.sleep(1)
print()
print('  -Introducí el número de columnas totales')



columnas=int(input())

print('  -Ahora introducí el valor de cada columna en orden')

introducir=1

while introducir==1:

	progreso=1
	y=1

	while y==1:
		valores=int(input())
		listadevalores.append(valores)
		
		if progreso==columnas:
			y=0
			break

		print('  -Siguiente número ('+str(progreso)+'/'+str(columnas)+')')
		progreso=progreso+1

		
	
	if len(listadevalores)==columnas:
		introducir=0

		print()
		time.sleep(1)
		print('valores de tu lista = '+ str(listadevalores))
		time.sleep(1.5)
		print()
		print('  -Creando tu histograma...')
		time.sleep(1.5)
		print()
		print('    [Histograma creado]')
		time.sleep(1.5)
		print()
	

		listadevalores=list(listadevalores) 
		
		indice=0
		
		x=('*')


		print('   |--------------------------')
		for elemento in listadevalores:

			
			print('   |'+x*listadevalores[indice])
			indice=indice+1
		print('   |--------------------------')
		
		break