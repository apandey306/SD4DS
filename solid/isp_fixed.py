from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class Connectable(ABC):
    @abstractmethod
    def connect_to_wifi(self):
        pass

class Audible(ABC):
    @abstractmethod
    def play_sound(self):
        pass

class SmartTV(Switchable, Connectable, Audible):
    def turn_on(self):
        print("TV turning on")

    def turn_off(self):
        print("TV turning off")

    def connect_to_wifi(self):
        print("TV connecting to Wi-Fi")

    def play_sound(self):
        print("TV playing sound")

class SimpleLamp(Switchable):
    def turn_on(self):
        print("Lamp turning on")

    def turn_off(self):
        print("Lamp turning off")

# Usage
def switch_device(switchable: Switchable):
    switchable.turn_on()
    switchable.turn_off()

def connect_device(connectable: Connectable):
    connectable.connect_to_wifi()

def play_device_sound(audible: Audible):
    audible.play_sound()

tv = SmartTV()
switch_device(tv)       # Output: TV turning on, TV turning off
connect_device(tv)      # Output: TV connecting to Wi-Fi
play_device_sound(tv)   # Output: TV playing sound

lamp = SimpleLamp()
switch_device(lamp)     # Output: Lamp turning on, Lamp turning off
# Can't call connect_device(lamp) or play_device_sound(lamp) since SimpleLamp doesn't implement Connectable or Audible