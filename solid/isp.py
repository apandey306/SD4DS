from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def connect_to_wifi(self):
        pass

    @abstractmethod
    def play_sound(self):
        pass

class SmartTV(Device):
    def turn_on(self):
        print("TV turning on")

    def turn_off(self):
        print("TV turning off")

    def connect_to_wifi(self):
        print("TV connecting to Wi-Fi")

    def play_sound(self):
        print("TV playing sound")

class SimpleLamp(Device):
    def turn_on(self):
        print("Lamp turning on")

    def turn_off(self):
        print("Lamp turning off")

    def connect_to_wifi(self):
        # Lamps don't connect to Wi-Fi, so this is unnecessary
        pass

    def play_sound(self):
        # Lamps don't play sound, so this is unnecessary
        pass

def operate_device(device: Device):
    device.turn_on()
    device.connect_to_wifi()
    device.play_sound()
    device.turn_off()

# Usage
tv = SmartTV()
operate_device(tv)
# Output:
# TV turning on
# TV connecting to Wi-Fi
# TV playing sound
# TV turning off

lamp = SimpleLamp()
operate_device(lamp)
# Output:
# Lamp turning on
# (no output for connect_to_wifi and play_sound)
# Lamp turning off