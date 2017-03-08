from things import Thing


class Inanimate(Thing):
    listof = []
    def __init__(self, name, names=None):
        Thing.__init__(self, name, names)
        Inanimate.listof.append(self)
