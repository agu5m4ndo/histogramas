import time
import math

print()
time.sleep(1)
print('  -Introducí uno a uno los números de tus mediciones (Usa puntos para incluir los decimales)')
time.sleep(1.7)
print('  -Al finalizar, escribí "fin" para procesar tus datos')

listaMedidas=[]
listaColumnas=[]
asteriscoColumna=[]

introducir=1

class miclase:
	def metiendoNumeros():
		global listaMedidas
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

			listaMedidas.sort()

	metiendoNumeros()

#________________________________________________________________________________
#----------------------------CREACION Y CALCULO DE COLUMNAS----------------------
#________________________________________________________________________________

	def evaluarDatos():
		global listaMedidas

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

			global listaColumnas

			nroMaximo=max([float(item) for item in listaMedidas])
			nroMinimo=min([float(item1) for item1 in listaMedidas])

			r=(float(nroMaximo)-float(nroMinimo))
			n=len(listaMedidas)
			k=1+(3.322*math.log10(n))
			Δx=round(r/k,3)
			columnas=round(k,0)





			print()
			time.sleep(1.5)
			print('  -el valor de r es: '+str("{:.3f}".format(r)))
			print('  -el valor de k es: '+str("{:.2f}".format(k)))
			print('  -el valor de Δx es: '+str("{:.6f}".format(Δx)))
			
			if columnas==1:
				print('  -Habrá 1 columna')
			else:
				print('  -Habrán '+str("{:.0f}".format(columnas))+' columnas')


			
			listaColumnas.append(str(nroMinimo))

			for element in range(int(columnas)):

				anchodecolumna=(float(listaColumnas[-1])+float(Δx))
				ancho=round(anchodecolumna,2)
				listaColumnas.append(str(ancho))

			
			maxIntervalo=max([float(item2) for item2 in listaColumnas])

			if nroMaximo>=maxIntervalo:

				ColumnaUnNroMas=(float(listaColumnas[-1])+float(Δx))
				ultimoNroColumna=round(ColumnaUnNroMas,2)
				listaColumnas.append(str(ultimoNroColumna))

			print()
			#print('los números que encabezan cada columna son: ', listaColumnas)

#________________________________________________________________________________
#----------------------------EVALUACION DE NUMEROS EN COLUMNAS-------------------
#________________________________________________________________________________


			ind=0
			ind1=0
			amount=0

			def comparador(ind, ind1, amount):

				global asteriscoColumna

				for i in listaColumnas:
					for j in listaMedidas:
				
						

						while (float(listaColumnas[ind]))<=(float(listaMedidas[ind1])) and (float(listaMedidas[ind1]))<(float(listaColumnas[ind+1])):
							amount=amount+1
							#print(amount, ' esto deberia ser la cantidad de una columna cuando listaColumnas=',listaColumnas[ind],' y listaMedidas=',listaMedidas[ind1])
							
							if ind1==(len(listaMedidas)-1):
								ind1=0
								break
							else:
								ind1=ind1+1
						break



					asteriscoColumna.append(amount)
					amount=0

					ind=ind+1

					if ind==len(listaColumnas)-1:
						break

			comparador(ind, ind1, amount)



		else:
			print('  -no hay suficientes datos, introducí más mediciones')  
			metiendoNumeros(ind, ind1, amount)

	evaluarDatos()




	

#________________________________________________________________________________
#----------------------------CREACION DEL HISTOGRAMA-----------------------------
#________________________________________________________________________________



	def creandoHist():
		print()
		print('  -Creando tu histograma...')
		time.sleep(1.5)
		print()
		print('    [Histograma creado]')
		time.sleep(1.5)
		print()


		indice=0
			
		x=('⬛')
		vel=0

#		print(listaColumnas)
		print(f"{'':<14} {'▏－－－－－－－－－－－－－－－－－－'}")

		for elemento in asteriscoColumna:

			intervalo1=listaColumnas[vel]
			intervalo2=listaColumnas[vel+1]
			
			print(f"{'('+str(intervalo1)+';'+str(intervalo2)+')':<14} {'▏ '+x*asteriscoColumna[indice]}")
			indice=indice+1
			
			
			if vel==len(listaColumnas)-1:
				break
			else:
				vel=vel+1
		print(f"{'':<14} {'▏－－－－－－－－－－－－－－－－－－'}")
		#print('(Cantidad de')
		#print('   medidas)')
	creandoHist()

