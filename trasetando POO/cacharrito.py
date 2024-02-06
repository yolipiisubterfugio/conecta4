class Cacharrito_de_Taida:

    def __init__(self):
        self.contador = 0


    def click(self):
        '''
        Incrementara el contador
        '''
        self.contador =+ 1


    def reset(self):
        '''
        pone el contador a cero
        '''
        self.contador = 0


contador_adultos = Cacharrito_de_Taida()
contador_chiquillos  = Cacharrito_de_Taida()

contador_adultos.click()

print(contador_adultos.contador)
print(contador_chiquillos.contador)