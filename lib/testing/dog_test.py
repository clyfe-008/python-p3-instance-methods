from dog import Dog
from lib.person import Person

# Dog tests
def test_dog_bark():
    fido = Dog("Fido")
    fido.bark()
    # Your assertions here...

def test_dog_sit():
    fido = Dog("Fido")
    fido.sit()
    # Your assertions here...

# Person tests
def test_person_talk():
    person = Person("Alice")
    person.talk()
    # Your assertions here...

def test_person_walk():
    person = Person("Alice")
    person.walk()
    # Your assertions here...
