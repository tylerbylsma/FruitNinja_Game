"""CS 108 Final Project testing

This module runs tests on the fruit class

@author: Ben Kosters (bak32)
@author: Tyler Bylsma (tjb65)
@date: December, 2022
"""

from orange import Fruit

fruit = Fruit(10,10,height = 40, pos_direction = True, fruit_type = 'Watermelon')



assert fruit.slices(20,20)
print("pass")