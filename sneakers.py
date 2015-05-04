class Sneakers:
    def get_identifier():
        return self._identifier;


    def __init__(self, line, column):
        self._identifier = str(line) + '_' + str(column)
        self._line = line
        self._column = column

        self._left = LeftSneaker(self._line, self._column)
        self._right = RightSneaker(self._line, self._column)


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
        need_create_sneakers = False
        can_move_more = False

        sneaker_moved, need_create_sneakers_greater = greater.move()
        if not sneaker_moved:
            sneaker_moved, need_create_sneakers_less = less.move()

        need_create_sneakers = need_create_sneakers_greater or
            need_create_sneakers_less

        if sneaker_moved or need_create_sneakers:
            can_move_more = True

        return need_create_sneakers, can_move_more


class Sneaker:
    def __init__(self, line, column):
        self.line = line
        self.column = column


class LeftSneaker(Sneaker):
    pass


class RightSneaker(Sneaker):
    pass
