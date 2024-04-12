# Importamos todas las funciones desde el módulo funciones

from main import borrar_paciente, informe_afiliacion_eps, ingresar_paciente, validar_numero

def mostrar_menu_principal():
    print("¡Bienvenido al sistema de administración médica de pacientes!")
    print("Por favor, selecciona una opción del menú:")
    print("1. Ingresar nuevo paciente")
    print("2. Informe de afiliación a EPS")
    print("3. Borrar paciente")
    print("4. Salir")

# Mostramos un menú principal y ejecutamos las funciones correspondientes según la opción seleccionada por el usuario.
while True:
    mostrar_menu_principal()
    opcion = validar_numero("Ingresa el número de la opción que deseas: ")

    if opcion == 1:
        ingresar_paciente()
    elif opcion == 2:
        informe_afiliacion_eps()
    elif opcion == 3:
        borrar_paciente()
    elif opcion == 4:
        print("Gracias por utilizar nuestro sistema. ¡Hasta luego!")
        break
    else:
        print("Por favor, selecciona una opción válida del menú.")
