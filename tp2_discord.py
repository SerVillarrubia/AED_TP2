#Validaciones:
#1-Validar que haya un solo tipo de moneda dentro del rango ISO en la orden.
def validar_moneda(linea):
	caracter, anteultimo_char, penultimo_char, ultimo_char = "", "", "", ""
	contador_caracter = 0
	moneda_aceptada = False
	monedas_validas = ('ARS', 'USD', 'EUR', 'GBP', 'JPY')
	codigo_moneda = anteultimo_char + penultimo_char + ultimo_char
	primera_moneda = False
	moneda_registrada = ""

	for caracter in linea:
		if 30 <= contador_caracter <= 39:
			codigo_moneda = anteultimo_char + penultimo_char + ultimo_char  #<<<La única manera coherente de
			if codigo_moneda in monedas_validas:                            #   hacerlo sin LEN ni SUBSTRING
				if primera_moneda is False:                                 # (6HS sin funcionar porque faltaba
					primera_moneda = True                                   # un contador_caracter)
					moneda_aceptada = True
					moneda_registrada = codigo_moneda
				elif primera_moneda is True:
					if moneda_registrada != codigo_moneda:
						moneda_aceptada = False

		anteultimo_char = penultimo_char    #Reemplazos para el siguiente bucle
		penultimo_char = ultimo_char        #(El orden estaba al revés)
		ultimo_char = caracter
		contador_caracter += 1
	return moneda_aceptada

def validar_id(linea):  #Lo de (linea) es mejor dejarlo así para mantener la coherencia en las funciones.
	contador_caracter = contador_de_guiones = 0
	id_valida = True

	for caracter in linea:
		if 20 <= contador_caracter <= 29:
			if caracter == "-" or caracter == "_":
				contador_de_guiones +=1
			if caracter not in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789-_ ":
				id_valida = False
				return id_valida
		if contador_de_guiones == 10:
			id_valida = False
		contador_caracter += 1
	return id_valida
#Fin de las validaciones.

def calculo_de_comision(moneda, monto_nominal):
	monto_base = 0
	monto_fijo = 100
	if moneda == 'ARS':
		comision = monto_nominal / 9 * 100
		monto_base = monto_nominal - comision
		if monto_nominal < 500000:
			comision = 0.
		if monto_nominal >= 500000:
			comision = monto_nominal / 7 * 100
		if comisión > 50000:
			comision = 50000
		if monto_nominal < 500000:
			comision = monto_nominal / 7 * 100

	if moneda == 'ARS':
		if comision > 50000:
			comision = 50000
			monto_base = monto_nominal - comision

	if moneda == 'USD':
		if monto_nominal < 50000:
			comision = 0
		if monto_nominal >= 50000 and monto_nominal < 80000:
			comision = monto_nominal / 5 * 100
		if monto_nominal >= 80000:
			comisión = montonominal / 7.8 * 100
			monto_base = monto_nominal - comision


	if moneda == 'EUR' or 'GBP':
		if monto_nominal > 25000:
			comision = monto_nominal / 6 * 100
			monto_base = monto_nominal - (monto_fijo + comision)

	if moneda == 'JPY':
		if monto_nominal <= 100000:
			comision = 500
		if monto_nominal > 100000:
			comision = 1000
			monto_base = monto_nominal - comision
	return monto_base

def cantidad_de_ordenes(linea):
	moneda = ""
	caracter, anteultimo_char, penultimo_char, ultimo_char = "", "", "", ""
	contador_caracter = 0
	moneda_aceptada = primera_moneda = False
	monedas_validas = ('ARS', 'USD', 'EUR', 'GBP', 'JPY')
	codigo_moneda = anteultimo_char + penultimo_char + ultimo_char
	moneda_registrada = ""

	for caracter in linea:
		if 30 <= contador_caracter <= 39:
			codigo_moneda = anteultimo_char + penultimo_char + ultimo_char  # <<<La única manera coherente de
			if codigo_moneda in monedas_validas:  # hacerlo sin LEN ni SUBSTRING
				if primera_moneda is False:  # (6HS sin funcionar porque faltaba
					primera_moneda = True  # un contador_caracter)
					moneda_aceptada = True
					moneda_registrada = codigo_moneda
				elif primera_moneda is True:
					if moneda_registrada != codigo_moneda:
						moneda_aceptada = False
		anteultimo_char = penultimo_char  # Reemplazos para el siguiente bucle
		penultimo_char = ultimo_char  # (El orden estaba al revés)
		ultimo_char = caracter
		contador_caracter += 1
	moneda = moneda_registrada
	return moneda

def principal():
	archivo = open("ordenes25.txt", 'rt')
	orden = archivo.readline() #lee la primera línea del archivo y la asigna a la variable orden.
	#también avanza el cursor del archivo, la próxima lectura comenzará desde la segunda línea.
	#################
	cant_minvalida = cant_binvalido = cant_oper_validas = suma_mf_validas = 0   #<<
	cant_ARS = cant_USD = cant_EUR = cant_GBP = cant_JPY = 0                    # <
	cod_my = mont_nom_my = mont_fin_my = 0                                      # <<<VARIABLES DE SALIDA
	nom_primer_benef = ""                                                       # <        (no tocar)
	cant_nom_primer_benef = porcentaje = promedio = 0                           #<<

	contador_de_lineas = 0
	operaciones_invalidas = 0

	for orden in archivo:
		#Salidas r1 y r2
		if validar_moneda(orden) is False:  #<<<<<<
			cant_minvalida += 1                     #Validaciones de la página 3 del TP
		if validar_id(orden) is False:      #<<<<<<
			cant_binvalido += 1
			if validar_moneda(orden) is False:
				cant_binvalido -= 1
		#Salida 3
		if validar_moneda(orden) is True and validar_id(orden) is True:
			cant_oper_validas += 1
		#Salidas de r5 a r9
		if validar_moneda(orden) is True:
			if cantidad_de_ordenes(orden) == "ARS":
				cant_ARS += 1
			if cantidad_de_ordenes(orden) == "USD":         #Hay que debuggear las salidas del r5 al r9
				cant_USD += 1
			if cantidad_de_ordenes(orden) == "EUR":
				cant_EUR += 1
			if cantidad_de_ordenes(orden) == "GBP":
				cant_GBP += 1
			if cantidad_de_ordenes(orden) == "JPY":
				cant_JPY += 1

		if validar_moneda(orden) is False or validar_id(orden) is False:
			operaciones_invalidas += 1
		contador_de_lineas += 1
	porcentaje = (operaciones_invalidas * 100) // contador_de_lineas
	archivo.close()     #Cierra archivo

#Por las dudas, se puede abrir el .txt en PyCharm y se guardará solo, se pueden agregar lineas para comprobar
#el funcionamiento de las funciones y las salidas.
	print(' (r1) - Cantidad de ordenes invalidas - moneda no autorizada:', cant_minvalida)
	print(' (r2) - Cantidad de ordenes invalidas - beneficiario mal identificado:', cant_binvalido)
	print(' (r3) - Cantidad de operaciones validas:', cant_oper_validas)
	print(' (r4) - Suma de montos finales de operaciones validas:', suma_mf_validas)
	print(' (r5) - Cantidad de ordenes para moneda ARS:', cant_ARS)
	print(' (r6) - Cantidad de ordenes para moneda USD:', cant_USD)
	print(' (r7) - Cantidad de ordenes para moneda EUR:', cant_EUR)
	print(' (r8) - Cantidad de ordenes para moneda GBP:', cant_GBP)
	print(' (r9) - Cantidad de ordenes para moneda JPN:', cant_JPY)
	print('(r10) - Codigo de la orden de pago con mayor diferencia nominal - final:', cod_my)
	print('(r11) - Monto nominal de esa misma orden:', mont_nom_my)
	print('(r12) - Monto final de esa misma orden:', mont_fin_my)
	print('(r13) - Nombre del primer beneficiario del archivo:', nom_primer_benef)
	print('(r14) - Cantidad de veces que apareció ese mismo nombre:', cant_nom_primer_benef)
	print('(r15) - Porcentaje de operaciones inválidas sobre el total:', porcentaje)
	print('(r16) - Monto final promedio de las ordenes validas en moneda ARS:', promedio)

principal()
