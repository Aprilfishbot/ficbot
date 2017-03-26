from things import Thing


class Inanimate(Thing):
    listof = []
    def __init__(self, name, names):
        Thing.__init__(self, name, names)
        Inanimate.listof.append(self)

class Garment(Inanimate):
    listof = []
    def __init__(self, name, names, elements):
        Inanimate.__init__(self, name, names)
        Garment.listof.append(self)
        self.elements = list(elements)

