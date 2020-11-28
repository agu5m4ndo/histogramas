import time
import math

print()
time.sleep(1)
print('  -Introducí uno a uno los números de tus mediciones (Usa puntos para incluir los decimales)')
time.sleep(1.7)
print('  -Al finalizar, escribí "fin" para procesar tus datos')

listaMedidas=list()
introducir=1


def metiendoNumeros():
	while introducir==1:

		mediciones=input()
		progreso=1

		try:
			valor=float(mediciones)
			listaMedidas.append(mediciones)
			print('  -Siguiente número')
			progreso=progreso+1

		except:
			if mediciones=='fin':
				introducir==0
				break
			else:
				print('  -solo podés introducir números')



def evaluarDatos():
	if len(listaMedidas)==0:
		print('  -No introdujiste ningun valor')
		metiendoNumeros()
	else:
		print()
		time.sleep(1.2)
		print('  -Tus mediciones son '+str(listaMedidas))

	nroMaximo=max([float(item) for item in listaMedidas])
	nroMinimo=min([float(item1) for item1 in listaMedidas])

	if len(listaMedidas)>1:
		r=(float(nroMaximo)-float(nroMinimo))
		n=len(listaMedidas)
		k=math.sqrt(n)
		Δx=r/k
		columnas=k
	else:
		print('  -no hay suficientes datos, introducí mas mediciones')  
		metiendoNumeros()

	print()
	time.sleep(1.5)
	print('  -el valor de r es: '+str("{:.3f}".format(r)))
	print('  -el valor de k es: '+str("{:.2f}".format(k)))
	print('  -el valor de Δx es: '+str("{:.6f}".format(Δx)))
	print('  -las columnas se separarán cada '+str("{:.2f}".format(columnas)))


def distribucion():

	listaColumnas=list()

#	largoDeColumna=



def creandoHist():
	print()
	print('  -Creando tu histograma...')
	time.sleep(1.5)
	print()
	print('    [Histograma creado]')
	time.sleep(1.5)
	print()

#	listaMedidas=list(listaMedidas)

		
	indice=0
		
	x=('*')


	print('   |--------------------------')
	for elemento in listaColumnas:

			
		print('   |'+x*listaColumnas[indice])
		indice=indice+1
	print('   |--------------------------')
		

metiendoNumeros()
evaluarDatos()
#creandoHist()