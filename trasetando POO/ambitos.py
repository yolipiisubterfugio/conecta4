variable = 0

def funcion_cambia_variable():
    global variable
    variable += 1


def funcion_juega_con_variable():
    variable = 39

print(variable)
print(funcion_cambia_variable())
print(funcion_cambia_variable())
print(funcion_cambia_variable())
print(variable)