from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.is_open = False

    def open(self):
        if self.is_open:
            raise InvalidOperationError("Invalid operation, cannot open already opened stream")
        self.is_open = True

    @abstractmethod
    def write(self):
        pass


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network...")

    def write(self):
        print("Writing to a network stream")


class MemoryStream(Stream):
    def read(self):
        print("Reading Data from a memory stream")

    def write(self):
        print("writing to a memory stream...")
