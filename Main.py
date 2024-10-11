from ClaseAlumno import Alumno
# Ejemplo de uso:

#crear la instancia del objeto
'''
una instancia es la creacion de un objeto a partir de una clase
'''
alumno = Alumno()

# y lo vamos llenando
alumno.set_nombre("Juan")
alumno.set_apellido_paterno("Pérez")
alumno.set_apellido_materno("López")
alumno.set_no_control("12345678")
alumno.set_semestre(5)

''' 
mostramos lo ingresado
'''
print("Nombre:", alumno.get_nombre())
print("Apellido Paterno:", alumno.get_apellido_paterno())
print("Apellido Materno:", alumno.get_apellido_materno())
print("No. Control:", alumno.get_no_control())
print("Semestre:", alumno.get_semestre())
print("Nombre completo: ",alumno.get_nombre_completo())
print("___________________________________________")
#________________________________________________________________________________________--
registro_alumnos = {}

for i in range(3):
    print("\n")
    # Asignamos valores a cada alumno
    alumno.set_nombre(input("Ingresa el nombre del alumno: "))
    alumno.set_apellido_paterno(input("Ingresa el apellido paterno: "))
    alumno.set_apellido_materno(input("Ingresa el apellido materno: "))
    alumno.set_no_control(input("Ingresa el número de control: "))
    alumno.set_semestre(int(input("Ingresa el semestre: ")))

    # iteramos los alumnos en el diccionario (los guardamos)
    registro_alumnos[i] = alumno



print("________________________________________________________")
for i in range(3):
    # imprimimos los valores
    print(f"nombre: {registro_alumnos[i].get_nombre()}")
    print(f"apellido paterno: {registro_alumnos[i].get_apellido_paterno()}")
    print(f"apellido materno: {registro_alumnos[i].get_apellido_materno()}")
    print(f"No de control: {registro_alumnos[i].get_no_control()}")
    print(f"semestre: {registro_alumnos[i].get_semestre()}")
    print("\n")

