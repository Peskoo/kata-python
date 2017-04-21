# coding=utf-8
"""
Create a text adventure map with three rooms.

Navigation is done with N, S, E, W.

Describe rooms on entry.

Prevent attempting to leave a room by an impossible route.

There are many ways to implement this. A way that makes it easy to completely swap out a new map without
changing all lines of code is a superior solution.
"""
from __future__ import print_function, unicode_literals, absolute_import

# configure logging for file and console output.
import logging
import os.path
if os.path.isfile("log.txt"):
    os.remove("log.txt")
logging.basicConfig(filename='log.txt', level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler())


def run():
    """
    Main entry point for your application.
    """
    rooms = Room(title="Room_1", north=Room(
        title="Room_2", west=Room(title="Room_3")))
    current_room = rooms

    while True:
        print(str(current_room))
        turn = input("Select direction (N, S, E, W) or 'exit': ")
        if turn == 'exit':
            break
        current_room = current_room.move(turn)
    return


# the functions/classes you write here should have no print or input
# statements.


class Room:
    '''Docstring'''

    def __init__(self, title="",
                 north=None, south=None, east=None, west=None
                 ):
        self.title = title
        self.north = north
        if self.north:
            self.north.south = self
        self.south = south
        if self.south:
            self.south.north = self
        self.east = east
        if self.east:
            self.east.west = self
        self.west = west
        if self.west:
            self.west.east = self

    def __str__(self):
        north = "N({}) ".format(self.north.title) if self.north else ""
        south = "S({}) ".format(self.south.title) if self.south else ""
        east = "E({}) ".format(self.east.title) if self.east else ""
        west = "W({}) ".format(self.west.title) if self.west else ""
        return "\nCurrent room: {}. You can move to: ".format(self.title) + north + south + east + west

    def move(self, d=None):
        directions = {
            'N': self.north,
            'S': self.south,
            'E': self.east,
            'W': self.west,
        }
        if d not in 'NSEW' and len(d) != 1:
            print("Wrong direction! Try again.")
            return self
        if directions[d]:
            return directions[d]
        print("Wall !!!")
        return self


if __name__ == "__main__" or __name__ == "builtins":
    # Need an environment to run this?
    # https://repl.it/languages/python3
    logging.info("The application is starting.")
    run()
