from things import Thing

class State(Thing):
    listof = []
    def __init__(self, name, names, positivity):
        Thing.__init__(self, name, names)
        self.positivity = positivity
        State.listof.append(self)

class Weather(State):
    listof = []
    def __init__(self, name, names, positivity):
        State.__init__(self, name, names, positivity)
        Weather.listof.append(self)


class Mood(State):
    listof = []
    def __init__(self, name, names, positivity):
        State.__init__(self, name, names, positivity)
        Mood.listof.append(self)