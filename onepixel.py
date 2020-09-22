#!/usr/bin/env python

import unicornhat as unicorn
from random import randint
from time import sleep

print('''Scroller

Displays each pixel in turn.
Current version picks a random color,
end state should cycle colors after
each complete board cycle
''')

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.6)
width,height=unicorn.get_shape()


while True:
        for y in range(height):
                for x in range(width):
                        unicorn.clear()
                        unicorn.show()
                        r=randint(0, 255)
                        g=randint(0, 255)
                        b=randint(0, 255)
                        unicorn.set_pixel(x,y,r,g,b)
                        unicorn.show()
                        sleep(0.1)