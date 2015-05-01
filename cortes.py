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

class Seeker:
    def __init__(self, line, column):
        self.line = line
        self.column = column

    def get_weight(self):
        symbol = self.get_symbol_at_cursor()


class LeftSeeker(Seeker):
    def get_symbol_at_cursor(self):
        #not implemented




class Right Seeker(Seeker):
    def Move():
        self.column += 1


def extract(buffer, cursor):
    line, column = cursor

    stack = []
    stack.append(create_seekers(line, column))
    while True:
        left, right = stack.pop()


# returns left and right seekers by line and column.
def create_seekers(line, column):
    return (Seeker(line, column), Seeker(line, column))
