# Pedir información al usuario
correoElectronicoComercio = input("Introduzca el correo electrónico de su comercio: ")
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
print("Ubicación del local: ",ubicacionLocal,"\n")

#Factura electrónica
print("Factura electrónica \n")
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
print("Provincia:", provinciaComprador,"Cantón:",cantonComprador,"Distrito:", distritoComprador, "\n")


#Nombre destinario
#Numero de telefono
#Numero de cedula
print("A continuación ingrese los siguientes datos para continuar con la compra")

nombreDestinatario=input("Ingrese nombre destinatario:")

numeroCedulaDestinatario=input("ingrese el numero de cedula:")

telefonoDestinatario = input("Ingrese su número de teléfono: ")

confirmacionTelefono = input("Confirme su número de teléfono: ")

while telefonoDestinatario != confirmacionTelefono:
    print("Error, vuelva a intentarlo.")
    numeroTelefono = input("Ingrese su número de teléfono: ")
    confirmacionTelefono = input("Confirme su número de teléfono: ")

print("¡Continúe con su compra!")
pesoPaquete = 0
pesoPaquete = int(input("Ingrese el peso de su paquete en kg: "))

if pesoPaquete <= 1:
    print("El envío de su paquete es gratis.")
else:

    if pesoPaquete <= 5:
        print("El costo de envío de su paquete es de 2500 colones.")
    else:
            
        if pesoPaquete <= 10:
            print("El costo de envío de su paquete es de 5000 colones.")
        else: 
        
            if pesoPaquete <= 20:
                print("El costo de envío de su paquete es de 10000 colones.")
            else:
                
                if pesoPaquete <= 50:
                    print("El costo de envío de su paquete es de 20000 colones.")
                else:
                    
                    if pesoPaquete > 50:
                        print("El peso ingresado es mayor al peso máximo permitido, por favor divida su paquete en paquetes más pequeños.")

confirmacion = 0
print("Desea continuar con la compra?:")
print("Digite (1) para continuar con la compra")
print("Digite (2) para salir")

if confirmacion == 1:
    print("Continuará con la compra")

    else:
        print("Canceló la compra")



