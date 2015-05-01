# coding=utf8

import re

identifier_re = re.compile(r'\w')

class Context:
    def __init__(self, text, start, end):
        self.text = text
        self.start = start
        self.end = end

    def __str__(self):
        result = ""
        line, column = 0, 0

        for text_line in self.text:
            for char in text_line:
                if (line, column) == self.start:
                    result += "["

                result += char

                if (line, column) == self.end:
                    result += "]"

                column += 1
            line += 1

            return result

def extract(text, cursor):
    left, right = cursor, cursor
    done = False
    while not done:
        done = True

        new_left, changed = _decrement_cursor(text, left)
        if changed and identifier_re.match(_get_char_at(text, new_left)):
            left = new_left
            done = False

        new_right, changed = _increment_cursor(text, right)
        if changed and identifier_re.match(_get_char_at(text, new_right)):
            right = new_right
            done = False


    return Context(text, left, right)

def _get_char_at(text, cursor):
    return text[cursor[0]][cursor[1]]

def _decrement_cursor(text, cursor):
    (line, column) = cursor
    column -= 1

    if column < 0:
        line -= 1
        column = len(text[line]) - 1

    return _return_valid_cursor(text, (line, column), cursor)

def _increment_cursor(text, cursor):
    (line, column) = cursor
    column += 1

    if column >= len(text[line]):
        line += 1
        column = 0

    return _return_valid_cursor(text, (line, column), cursor)

def _is_cursor_valid(text, cursor):
    (line, column) = cursor
    if line < 0:
        return False
    if line >= len(text):
        return False
    if column < 0:
        return False
    if column >= len(text[line]):
        return False
    return True

#def _is_cursor_at_eof(text, cursor):
#    if cursor == (0, 0):
#        return True
#    if len(text[cursor[0]]) - 1 == cursor[1]:
#        return True
#    return False

def _return_valid_cursor(text, new_cursor, old_cursor):
    if _is_cursor_valid(text, new_cursor):
        return new_cursor, True
    else:
        return old_cursor, False
