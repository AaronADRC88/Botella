__author__ = 'aferreiradominguez'


class Corcho:
    def __init__(self, bodega):
        self.bodega_name = bodega


class Botella(object):
    def __init__(self, corcho=None):
        self.corcho = corcho


class Sacacorchos(object):

    corcho=None
    def destapar(self, botella):
        if (self.corcho!=None):
            raise TypeError("hai un corcho")
        elif (botella.corcho != None):
            self.corcho=botella.corcho
            botella.corcho=None
            print(self.corcho.bodega_name + " extraido")
        else:
            raise TypeError("no hai corcho")

    def limpiar(self):
        if (self.corcho != None):
            self.corcho=None
        else:
            raise TypeError("no hay corcho")


tapon = Corcho("puta bodega")
botella = Botella(tapon)
saca = Sacacorchos()
#saca.destapar(botella)
saca.limpiar()