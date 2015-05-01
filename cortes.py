# coding=utf8

import re

word_re = re.compile(r'\w')

class Context:
    def __init__(self, buffer, start, end):
        self.buffer = buffer
        self.start = start
        self.end = end

    def __str__(self):
        result = ""
        line, column = 0, 0

        for buffer_line in self.buffer:
            for char in buffer_line:
                if (line, column) == self.start:
                    result += "["

                result += char

                if (line, column) == self.end:
                    result += "]"

                column += 1
            line += 1

            return result

class Sneaker:
    def __init__(self, line, column):
        self.line = line
        self.column = column

    def get_weight(self):
        symbol = self.get_symbol_at_cursor()


class LeftSneaker(Sneaker):
    def get_symbol_at_cursor(self):
        #not implemented


class RightSneaker(Sneaker):
    def Move():
        self.column += 1


def extract(buffer, cursor):
    line, column = cursor

    sneakers_stack = []
    sneakers_stack.append(create_sneakers(line, column))
    while True:
        sneakers = sneakers_stack[-1]

        move_sneakers(sneakers, sneakers_stack)


def move_sneakers(sneakers, sneakers_stack):
    sneaker_moved = False

    for sneaker in sneakers:
        if sneaker.move():
            sneaker_moved = True

    if not sneaker_moved:
        create_context(sneakers)
        update_sneakers_stack(sneakers, sneakers_stack)


def update_sneakers_stack(sneakers, sneakers_stack):
    sneakers_stack.pop()
    for sneaker in sneakers:
        if not sneaker.should_create_new_sneakers():
            continue
        line, column = sneaker.get_cursor_for_new_sneakers()
        new_sneakers = create_sneakers(
            line,
            column
        )

        sneakers_stack.append(new_sneakers)


def create_sneakers(line, column):
    return (LeftSneaker(line, column), RightSneaker(line, column))
