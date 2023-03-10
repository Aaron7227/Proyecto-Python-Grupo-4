# Pedir información al usuario
correoElectronicoComercio = input("Introduzca su correo electrónico: ")
nombreComercio = input("Introduzca el nombre de su comercio: ")
telefonoComercio = input("Introduzca el teléfono de su comercio: ")
nombreDueno = input("Introduzca su nombre completo: ")
ubicacionLocal = input("Introduzca la ubicación de su local: ")

# Imprimir información registrada
print("¡Registro exitoso!")
print("Correo electrónico: ",correoElectronicoComercio)
print("Nombre del comercio: ",nombreComercio)
print("Teléfono del comercio: ",telefonoComercio)
print("Nombre del dueño: ",nombreDueno)
print("Ubicación del local: ",ubicacionLocal)

#Factura electrónica

#Preguntar por el tipo de cédula

print("Digite que tipo de documento de identidad posee")
print("(1) Para residente nacional")
print("(2) Para residente extranjero-nacionalizado")
print("(3) Cédula Jurídica \n")

tipoCedula = int(input("Ingrese la opción: "))

if tipoCedula == 1:
    print("Residente nacional")
    cedulaComprador=input("Digíte su número de cédula: \n")

if tipoCedula == 2:
    print("Residente extranjero nacionalizado")
    cedulaComprador=input("Digíte su número de cédula: \n")

if tipoCedula == 3:
    print("Cédula juridica")
    cedulaComprador=input("Digíte su número de cédula: \n")

#Preguntar por el nombre del comprador
nombreComprador = input("Digíte su nombre completo: \n")

#Preguntar por el número de télefono del comprador
telefonoComprador = input("Digíte su número de teléfono: \n")

#Preguntar por el correo electrónico del comprador
correoComprador = input("Digíte su correo electrónico: \n")

#preguntar por el lugar de residencia del comprador
provinciaComprador=input("Ingrese su provincia de residencia: \n")

cantonComprador=input("Ingrese su cantón de residencia: \n")

distritoComprador=input("Ingrese su distrito de residencia: \n")

#Imprimir la factura electrónica
print("Factura electrónica: \n")

print("Nombre completo: ", nombreComprador)

if tipoCedula == 1:
    print("Cédula Nacional: ",cedulaComprador)

if tipoCedula == 2:
    print("Cédula residente extranjero nacionalizado: ",cedulaComprador)

if tipoCedula == 3:
    print("Cédula Jurídica: ",cedulaComprador)

print("Número de teléfono: ",telefonoComprador)
print("Correo electrónico: ", correoComprador)
print("Lugar de residencia: ")
print("Provincia:", provinciaComprador,"Cantón:",cantonComprador,"Distrito:", distritoComprador)



