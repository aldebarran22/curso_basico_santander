class Grupo:
    def __init__(self, identificador="", *personas):
        self.identificador = identificador
        self.grupo = []
        self.grupo.extend(personas)
        self.indice = 0

    def addPersona(self, *personas):
        self.grupo.extend(personas)

    def __len__(self):
        return len(self.grupo)

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice == len(self.grupo):
            self.indice = 0
            raise StopIteration
        else:
            p = self.grupo[self.indice]
            self.indice += 1
            return p
