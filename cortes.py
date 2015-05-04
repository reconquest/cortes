# coding=utf8

import re

import sneakers
import context

def extract(buffer, cursor):
    line, column = cursor

    sneakers_stack = []
    sneakers_stack.append(Sneakers(line, column))

    parent_sneakers = None
    while True:
        sneakers = sneakers_stack[-1]

        if parent_sneakers:
            if sneakers.get_identifier() != parent_sneakers.get_identifier())
                update_sneakers_positions(sneakers, parent_sneakers)
                parent_sneakers = sneakers
        else:
            parent_sneakers = sneakers

        move_sneakers(sneakers, sneakers_stack)


def update_sneakers_positions(sneakers, parent_sneakers):
    left_position, right_position = parent_sneakers.get_positions()
    sneakers.set_positions(left_position, right_position)


def move_sneakers(sneakers, sneakers_stack):
    need_create_sneakers, can_move_more = sneakers.move()

    if need_create_sneakers:
        create_new_sneakers(sneakers, sneakers_stack)

    if not can_move_more:
        create_context(sneakers)
        sneakers_stack.pop()

def create_new_sneakers(sneakers, sneakers_stack):
    pass
    #sneakers_stack.pop()

    #for sneaker in sneakers:
        #if not sneaker.should_create_sneakers():
            #continue
        #line, column = sneaker.get_cursor_for_new_sneakers()
        #new_sneakers = create_sneakers(
            #line,
            #column
        #)

        #sneakers_stack.append(new_sneakers)
