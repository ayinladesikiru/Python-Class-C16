class Tv:
    def __init__(self, channel):
        self.__is_on = False
        self.__volume = 0
        self.channel = channel

    def power_on(self):
        self.__is_on = True
        return self.__is_on

    def increase_volume(self):
        self.power_on()
        if self.__is_on:
            self.__volume += 1

    def decrease_volume(self):
        self.power_on()
        if self.__is_on:
            if 0 <= self.__volume < 100:
                self.__volume -= 1

    @property
    def channel(self):
        return self.__channel

    @channel.setter
    def channel(self, number):
        if number < 0:
            raise ValueError("Invalid channel number")
        self.__channel = number

    def increase_channel(self):
        self.power_on()
        if self.__is_on:
            self.channel += 1

    def decrease_channel(self):
        self.power_on()
        if self.__is_on:
            self.channel -= 1

    def __str__(self):
        return f"channel is {self.channel} and the volume is {self.__volume}"

# we use classes to bundle data and method into one unit or together


tv1 = Tv(25)
tv1.increase_volume()
tv1.increase_volume()
tv1.increase_volume()
tv1.decrease_volume()
tv1.increase_channel()
print(tv1)

