from actions import Action
from facts import Fact, Opinion
from inanimate import Inanimate
from people import Person
from settings import Place, TimeOfDay
from states import State
from things import Thing

cosette = Person('Cosette', ['Fantine\'s daughter', 'the blue eyed girl'], 'F')

valjean = Person('Valjean', '', 'M')

morning = TimeOfDay('morning', '')

tuileries = Place('the Tuileries', '')

protagonist = cosette.name

confidant = valjean.name

timeofday = morning.name

placetowalk = tuileries.name

story = ("Cosette and {confidant} were walking in {placetowalk}. It was {timeofday}, "
          "but Cosette was sad. She said, \"I want a new hat\".".format(**vars()))
print(story)

print [Thing.name for Thing in Thing.listof]
print [Person.name for Person in Person.listof]

print ', '.join(cosette.names)