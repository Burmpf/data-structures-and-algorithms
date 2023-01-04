from data_structures.queue import Queue


class AnimalShelter:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, animal):
        new_animal = animal
        if self.front is None:
            self.front = new_animal

        if self.rear:
            self.rear.next = new_animal
        self.rear = new_animal

    def dequeue(self, pref):

        # If they don't want a cat or dog, return none
        if pref is not 'cat' and pref is not 'dog':
            return None

        # If they have no preference, return the first in the queue
        if pref is None:
            temp = self.front
            self.front = temp.next
            temp.next = None
            adopted_animal = temp
            return adopted_animal

        # While the animal is not the preferred animal, remove to the holding pen
        holding_pen = []
        adopted_animal = None
        while self.front.species != pref:
            temp = self.front
            self.front = temp.next
            temp.next = None
            holding_pen.append(temp)

        # Hold adopted animal to return to user
        temp = self.front
        self.front = temp.next
        temp.next = None
        adopted_animal = temp

        # Move holding pen animals back to shelter
        num_held = len(holding_pen)
        while holding_pen:
            return_animal = holding_pen[num_held - 1]
            return_animal.next = self.front
            self.front = return_animal
            holding_pen.pop()

        # Return the adopted animal to the user
        return adopted_animal

class Dog:
    def __init__(self, species="dog", next=None):
        self.species = species
        self.next = next

    def __str__(self):
        return self.species

class Cat:
    def __init__(self, species="cat", next=None):
        self.species = species
        self.next = next

    def __str__(self):
        return self.species

if __name__ == '__main__':
    shelter = AnimalShelter()
    cat = Cat()
    print(f"cat instance: {cat}")
    print(type(cat))
    print(cat.__repr__())
    print(f"dir: {dir(cat)}")
    shelter.enqueue(cat)
    print(f"front: {shelter.front}")
    print(f"species: {shelter.front.species}")
    shelter.dequeue('cat')