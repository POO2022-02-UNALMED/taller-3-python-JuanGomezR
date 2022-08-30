class marca:
    def __init__(self, nombre):
        self.nombre = nombre
    def getNombre(self):
        return self.nombre

class TV:
    numTV = 0
    def __init__(self, marca, estado, control):
        self.marca = marca
        self.canal = 1
        self.precio = 500
        self.estado = estado
        self.volumen = 1
        self.control = control
    def getNumTV(self):
        return self.numTV
    def getMarca(self):
        return self.marca
    def getControl(self):
        return self.control
    def getPrecio(self):
        return self.precio
    def getVolumen(self):
        return self.volumen
    def getCanal(self):
        return self.canal
    def getEstado(self):
        return self.estado
    def setMarca(self, marca):
        self.marca = marca
    def setControl(self, control):
        self.control = control
    def setPrecio(self, precio):
        self.precio = precio
    def setVolumen(self, volumen):
        if self.estado == True and volumen >= 0 and volumen <= 7:
            self.volumen = volumen
    def setCanal(self, canal):
        if self.estado == True and canal >= 1 and canal <= 120:
            self.canal = canal
    def turnOn(self):
        self.estado = True
    def turnOff(self):
        self.estado = False
    def canalUp(self):
        if self.estado == True and self.canal+1 <= 120:
            self.canal += 1
    def canalDown(self):
        if self.estado == True and self.canal-1 >= 1:
            self.canal -= 1
    def volumenUp(self):
        if self.estado == True and self.volumen+1 <= 7:
            self.volumen += 1
    def volumenDown(self):
        if self.estado == True and self.canal-1 >= 0:
            self.volumen -=1

class Control:
    def __init__(self, tv):
        self.tv = tv
    def enlazar(self, tv):
        self.tv = tv
        self.tv.control = self
    def turnOn(self):
        self.tv.turnOn()
    def turnOff(self):
        self.tv.turnOff()
    def canalUp(self):
        self.tv.canalUp()
    def canalDown(self):
        self.tv.canalDown()
    def volumenUp(self):
        self.tv.volumenUp()
    def volumenDown(self):
        self.tv.volumenDown()
    def setCanal(self, canal):
        self.tv.setCanal(canal)
    def getTv(self):
        return self.tv
    def setTv(self, tv):
        self.tv = tv