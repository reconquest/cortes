import re

class Sneakers:
    def get_identifier(self):
        return self._identifier;


    def get_buffer(self):
        return self._buffer


    def __init__(self, buffer, line, column, motion):
        """
        line and column it's sneakers start position
        motion used for child sneakers
        """
        self._identifier = str(line) + '_' + str(column)
        self._buffer = buffer
        self._line = line
        self._column = column
        self._motion = motion
        self._left = LeftSneaker(self._buffer, self._line, self._column)
        self._right = RightSneaker(self._buffer, self._line, self._column)


    def get_positions(self):
        return (self._left.get_positions(), self._left.right_positions())


    def set_positions(self, left_position, right_position):
        self._left.set_position(left_position)
        self._right.set_position(right_position)


    def move(self):
        left_priority = self._left.get_priority()
        right_priority = self._right.get_priority()

        if left_priority >= right_priority:
            greater = self._left
            less = self._right
        else:
            greater = self._right
            less = self._left

        sneaker_moved = False
        can_move_more = False

        need_create_sneakers_greater = False
        need_create_sneakers_less = False

        sneaker_moved, need_create_sneakers_greater = greater.move()
        if not sneaker_moved:
            sneaker_moved, need_create_sneakers_less = less.move()

        need_create_sneakers = need_create_sneakers_greater or \
            need_create_sneakers_less

        if sneaker_moved or need_create_sneakers:
            can_move_more = True

        return need_create_sneakers, can_move_more


PRIORITY_ZERO   = 0
PRIORITY_LOW    = 111
PRIORITY_MIDDLE = 222
PRIORITY_HIGH   = 333

RE_CLOSING   = re.compile('[\)\]\}]')
RE_OPENING   = re.compile('[\(\[\{]')
RE_DELIMITER = re.compile('[,;]')
RE_WORD      = re.compile('\w')

class Sneaker:
    """ so, this is abstract class """
    def __init__(self, buffer, line, column):
        self._buffer = buffer
        self._line = line
        self._column = column


    def get_priority(self):
        if RE_WORD.match(self.get_symbol_at_cursor()):
            return PRIORITY_HIGH

        if RE_CLOSING.match(self.get_symbol_at_cursor()):
            return PRIORITY_LOW

        if RE_OPENING.match(self.get_symbol_at_cursor()):
            return PRIORITY_LOW

        if RE_DELIMITER.match(self.get_symbol_at_cursor()):
            return PRIORITY_LOW

        return PRIORITY_MIDDLE


    def get_next_position(self):
        increment = self.get_motion_increment()
        line   = self._line
        column = self._column + increment

        line_contents = self._buffer[line]
        if column < 0:
            line = line - 1
        elif column >= len(line_contents):
            line = line + 1

        if line < 0 or line >= len(self._buffer):
            return None

        return line, column


    def get_symbol_at_cursor(self):
        return self._buffer[self._line][self._column]


    def move(self):
        next_position = self.get_next_position()
        if not next_position:
            return False, True

        next_line, next_column = next_position
        next_symbol = self._buffer[next_line][next_column]
        current_symbol = self.get_symbol_at_cursor()

        next_word = RE_WORD.match(next_symbol)
        current_word = RE_WORD.match(current_symbol)
        if current_word and next_word:
            return True, False

        if current_word and not next_word:
            return True, True

        if not current_word and not next_word:
            return True, False

        if not current_word and next_word:
            return True, True




class LeftSneaker(Sneaker):
    def get_motion_increment(self):
        return -1


class RightSneaker(Sneaker):
    def get_motion_increment(self):
        return 1
