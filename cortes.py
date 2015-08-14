# coding=utf8

from sneakers import *

import re
import context
import time

def extract(buffer, cursor):
    line, column = cursor

    sneakers_stack = []
    sneakers_stack.append(Sneakers(buffer, line, column, NEUTRAL_MOTION))

    parent_sneakers = None
    while True:
        print "cortes.py:16 sneakers_stack: %s" % sneakers_stack
        sneakers = sneakers_stack[-1]

        print "cortes.py:19 sneakers: %s" % sneakers


        print "cortes.py:22 parent_sneakers: %s" % parent_sneakers

        if parent_sneakers:
            if sneakers.get_identifier() != parent_sneakers.get_identifier():
                print "cortes.py:26 get_ident != parent"
                update_sneakers_positions(sneakers, parent_sneakers)
                parent_sneakers = sneakers
        else:
            parent_sneakers = sneakers

        move_sneakers(sneakers, sneakers_stack)
        time.sleep(1)


def update_sneakers_positions(sneakers, parent_sneakers):
    left_position, right_position = parent_sneakers.get_positions()
    sneakers.set_positions(left_position, right_position)


def move_sneakers(sneakers, sneakers_stack):
    need_create_sneakers, can_move_more = sneakers.move()
    print "cortes.py:44 need_create_sneakers: %s" % need_create_sneakers
    print "cortes.py:44 can_move_more: %s" % can_move_more

    if need_create_sneakers:
        create_new_sneakers(sneakers, sneakers_stack)

    if not can_move_more:
        create_context(sneakers)
        sneakers_stack.pop()


def create_new_sneakers(sneakers, sneakers_stack):
    buffer = sneakers.get_buffer()
    position, motion = sneakers.get_cursor_for_new_sneakers()
    if not position:
        print "cortes.py:59 NOT POSITION PANIC"
        return False

    new_sneakers = Sneakers(buffer, line, column, motion)
    sneakers_stack.append(new_sneakers)
    return True
