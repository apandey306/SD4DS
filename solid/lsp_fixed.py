from abc import ABC, abstractmethod

# Base class for all birds - no fly method here
class Bird:
    # Common bird properties/methods
    def eat(self):
        print("Bird is eating.")
    
    def lay_eggs(self):
        print("Bird is laying eggs.")


# Interface for flying behavior
class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass


# Concrete class for a bird that can fly
class Sparrow(Bird, Flyable):
    def fly(self):
        print("Sparrow is flying high!")


# Concrete class for a bird that cannot fly
class Penguin(Bird):  # No Flyable interface implemented
    # Penguin-specific methods, e.g.,
    def swim(self):
        print("Penguin is swimming gracefully.")


# A class that expects a Flyable object, not just any Bird
class Aviary:
    def make_bird_fly(self, flying_bird: Flyable):
        print("In the aviary: ", end="")
        flying_bird.fly()


if __name__ == "__main__":
    my_sparrow = Sparrow()
    my_penguin = Penguin()
    
    aviary = Aviary()
    
    # This works correctly because Sparrow implements Flyable
    aviary.make_bird_fly(my_sparrow)
    
    # This will raise a TypeError at runtime if we try to pass a Penguin
    # aviary.make_bird_fly(my_penguin)  # Error: Penguin doesn't implement Flyable
    
    # If we have a Bird object, we must check its capabilities
    generic_bird = Sparrow()
    if isinstance(generic_bird, Flyable):
        generic_bird.fly()  # Safe to call fly
    else:
        print("This bird cannot fly.")
    
    another_generic_bird = Penguin()
    if isinstance(another_generic_bird, Flyable):
        another_generic_bird.fly()
    else:
        print("This bird cannot fly.")  # Correctly identifies Penguin