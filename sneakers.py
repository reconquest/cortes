import re

LEFT_MOTION = -1
RIGHT_MOTION = 1
NEUTRAL_MOTION = 0

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


    def get_cursor_for_new_sneakers(self):
        left_next_position = self._left.get_next_position()
        if self._motion == LEFT_MOTION:
            return left_next_position, LEFT_MOTION

        right_next_position = self._right.get_next_position()
        if self._motion == RIGHT_MOTION:
            return right_next_position, RIGHT_MOTION

        left_line_changed = True
        if left_next_position:
            print "sneakers.py:45 left get"
            _, _, left_line_changed = left_next_position

        right_line_changed = True
        if right_next_position:
            print "sneakers.py:50 right get"
            _, _, right_line_changed = right_next_position

        print "sneakers.py:51 left_line_changed: %s" % left_line_changed
        print "sneakers.py:51 right_line_changed: %s" % right_line_changed



        if left_line_changed and not right_line_changed:
            if right_position:
                return right_next_position, RIGHT_MOTION
            else:
                return left_next_position, LEFT_MOTION

        if left_next_position:
            return left_next_position, LEFT_MOTION
        else:
            return right_next_position, RIGHT_MOTION


    def set_positions(self, left_position, right_position):
        self._left.set_position(left_position)
        self._right.set_position(right_position)


    def move(self):
        left_priority = self._left.get_priority()
        right_priority = self._right.get_priority()

        print "sneakers.py:39 left_priority: %s" % left_priority
        print "sneakers.py:39 right_priority: %s" % right_priority

        if right_priority >= left_priority:
            greater = self._right
            less = self._left
        else:
            greater = self._left
            less = self._right

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
            next_line = line - 1
        elif column >= len(line_contents):
            next_line = line + 1
        else:
            next_line = line

        if next_line < 0 or next_line >= len(self._buffer):
            return None

        line_changed = False
        next_line_contents = self._buffer[next_line]
        if column < 0:
            next_column = len(next_line_contents) - 1
            line_changed = True
        elif column >= len(line_contents):
            next_column = 0
            line_changed = True
        else:
            next_column = column

        return (next_line, next_column, line_changed)


    def get_symbol_at_cursor(self):
        return self._buffer[self._line][self._column]


    def move(self):
        """ sneaker_moved, need_create_sneakers_greater """
        next_position = self.get_next_position()

        if not next_position:
            return False, True

        print "sneakers.py:125 next_position[0]: %s" % next_position[0]
        print "sneakers.py:126 next_position[1]: %s" % next_position[1]

        next_line, next_column, motion = next_position
        next_symbol = self._buffer[next_line][next_column]

        print "sneakers.py:134 next_symbol: %s" % next_symbol


        current_symbol = self.get_symbol_at_cursor()

        next_word = RE_WORD.match(next_symbol)
        current_word = RE_WORD.match(current_symbol)
        print "sneakers.py:141 next_word: %s" % next_word
        print "sneakers.py:142 current_word: %s" % current_word

        self._line = next_line
        self._column = next_column

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
