#Validaciones:
#1-Validar que haya un solo tipo de moneda dentro del rango ISO en la orden.

def validar_moneda():
	moneda = ('ARS', 'USD', 'EUR', 'GBP', 'JPY')


def principal():
	#Abre el archivo o25.txt bajo el nombre pagina y lo copia en texto.
	pagina = open("ordenes25.txt", 'rt')
	orden = pagina.readline()
	#^^Copia el archivo leido. (Nota: Solo se lo puede copiar 1 vez por cada open().

	for orden in pagina:
		print("Salida 1:", orden)   #Salida 1 y 2 son banderas para ver qué está
									#mostrando por pantalla el programa en qué momento.
	print("Salida 2:", orden)
	pagina.close()	             #Cierra archivo

if __name__ == "__main__":
	principal()

#print(' (r1) - Cantidad de ordenes invalidas - moneda no autorizada:', cant_minvalida)
#print(' (r1) - Cantidad de ordenes invalidas - moneda no autorizada:', cant_minvalida)
#print(' (r2) - Cantidad de ordenes invalidas - beneficiario mal identificado:', cant_binvalido)
#print(' (r3) - Cantidad de operaciones validas:', cant_oper_validas)
#print(' (r4) - Suma de montos finales de operaciones validas:', suma_mf_validas)
#print(' (r5) - Cantidad de ordenes para moneda ARS:', cant_ARS)
#print(' (r6) - Cantidad de ordenes para moneda USD:', cant_USD)
#print(' (r7) - Cantidad de ordenes para moneda EUR:', cant_EUR)
#print(' (r8) - Cantidad de ordenes para moneda GBP:', cant_GBP)
#print(' (r9) - Cantidad de ordenes para moneda JPN:', cant_JPY)
#print('(r10) - Codigo de la orden de pago con mayor diferencia nominal - final:', cod_my)
#print('(r11) - Monto nominal de esa misma orden:', mont_nom_my)
#print('(r12) - Monto final de esa misma orden:', mont_fin_my)
#print('(r13) - Nombre del primer beneficiario del archivo:', nom_primer_benef)
#print('(r14) - Cantidad de veces que apareció ese mismo nombre:', cant_nom_primer_benef)
#print('(r15) - Porcentaje de operaciones inválidas sobre el total:', porcentaje)
#print('(r16) - Monto final promedio de las ordenes validas en moneda ARS:', promedio)
