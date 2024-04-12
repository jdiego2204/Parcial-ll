contador = 0
pacientes = {}

def generar_codigo(menueps, nombre_eps=None):
    global contador
    contador += 1
    if menueps == 1:
        eps = f"EPS SISBEN-{contador}"
    elif menueps == 2:
        if nombre_eps is None:
            nombre_eps = input("Ingrese el nombre de la EPS: ")
        eps = f"EPS {nombre_eps}-{contador}"
    return eps

def validar_numero(mensaje):
    intentos = 3
    while intentos > 0:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Por favor, ingrese un número válido.")
            intentos -= 1
    print("Demasiados intentos fallidos. Regresando al menú principal.")
    return None

def validar_fecha(fecha_str):
    try:
        from datetime import datetime
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
        return fecha
    except ValueError:
        print("Por favor, ingrese una fecha válida (YYYY-MM-DD)")
        return None

def ingresar_paciente():
    global contador
    nombre = input("Ingrese el nombre completo del paciente: ")
    genero = validar_numero("Ingrese el género del paciente \n 1. Hombre \n 2. Mujer \nOpción: ")
    edad = validar_numero("Ingrese la edad del paciente: ")
    if genero == 1:
        genero = "M"
        if edad > 18:
            diagnostico = "Niveles normales de LH"
        elif 0 <= edad <= 18:
            diagnostico = "Niveles bajos de LH"
    elif genero == 2:
        genero = "F"
        if 0 <= edad <= 18:
            diagnostico = "Niveles muy bajos de LH"
        elif edad >= 51:
            diagnostico = "Niveles altos de LH"
        elif edad >= 52:
            diagnostico = "Niveles muy altos de LH"
    else:
        print("Género inválido.")
        return

    nacimiento = input("Ingrese la fecha de nacimiento del paciente (YYYY-MM-DD): ")
    nacimiento_validado = validar_fecha(nacimiento)
    if not nacimiento_validado:
        return

    id_paciente = validar_numero("Ingrese el número de identificación del paciente: ")
    menueps = validar_numero("Seleccione una opción para la EPS:\n1. SISBEN\n2. EPS\nOpción: ")
    eps = generar_codigo(menueps)
    lh = "lh" + str(contador)

    pacientes[id_paciente] = [nombre, eps, nacimiento_validado, edad, (lh, diagnostico)]

    print(f"El paciente {nombre} ha sido registrado correctamente. Su diagnóstico es: {diagnostico}.")

def informe_afiliacion_eps():
    print("Seleccione una opción:")
    print("1) Buscar paciente")
    print("2) Ver cantidad total de pacientes")
    print("3) Ver cantidad de pacientes menores de 10 años")
    print("4) Ver cantidad de pacientes mayores de 60 años")
    sub_menu = input("Opción: ")

    if sub_menu == "1":
        id_paciente = validar_numero("Ingrese el número de identificación del paciente que desea buscar: ")
        paciente = pacientes.get(id_paciente)
        if paciente:
            print(f"Paciente encontrado:\nNombre: {paciente[0]}\nEPS: {paciente[1]}\nFecha de nacimiento: {paciente[2].strftime('%Y-%m-%d')}\nEdad: {paciente[3]}\nDiagnóstico: {paciente[4][1]}")
        else:
            print("El paciente con el número de identificación proporcionado no existe en la base de datos.")
    elif sub_menu == "2":
        print(f"La cantidad total de pacientes es: {len(pacientes)}")
    elif sub_menu == "3":
        menores_10 = len(list(filter(lambda x: pacientes[x][3] < 10, pacientes)))
        print(f"La cantidad de pacientes menores de 10 años es: {menores_10}")
    elif sub_menu == "4":
        mayores_60 = len(list(filter(lambda x: pacientes[x][3] > 60, pacientes)))
        print(f"La cantidad de pacientes mayores de 60 años es: {mayores_60}")

def borrar_paciente():
    id_paciente = validar_numero("Ingrese el número de identificación del paciente que desea borrar: ")
    if id_paciente in pacientes:
        pacientes.pop(id_paciente)
        print("El paciente ha sido eliminado correctamente.")
    else:
        print("El paciente no está registrado en la base de datos.")
