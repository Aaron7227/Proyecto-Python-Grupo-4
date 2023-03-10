# Pedir información al usuario
correoElectronico = input("Introduzca su correo electrónico: ")
nombreComercio = input("Introduzca el nombre de su comercio: ")
telefonoComercio = input("Introduzca el teléfono de su comercio: ")
nombreDueno = input("Introduzca su nombre completo: ")
ubicacionLocal = input("Introduzca la ubicación de su local: ")

# Imprimir información registrada
print("¡Registro exitoso!")
print("Correo electrónico: ",correoElectronico)
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
