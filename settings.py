from things import Thing

class Place(Thing):
    listof = []
    def __init__(self, name, names):
        Thing.__init__(self, name, names)
        Place.listof.append(self)


class TimeOfDay(Thing):
    listof = []
    def __init__(self, name, names):
        Thing.__init__(self, name, names)
        TimeOfDay.listof.append(self)

