class Campo:
    def __init__(self, indice, posX, posY, campoMina, campoRevelado, campoBandeira):
        self.indice = indice
        self.posX = posX
        self.posY = posY
        self.campoMina = campoMina
        self.campoRevelado = campoRevelado
        self.campoBandeira = campoBandeira

    def revelado(self):
        self.campoRevelado = True

    def bandeira(self):
        estado = False if (True) else True # Operador ternario
        self.campoBandeira = estado