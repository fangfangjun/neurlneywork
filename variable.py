# -*- coding:utf-8 -*-

"""
@author: Fan
@file:variable.py
@time:2017/6/19 10:55
"""

import tensorflow as tf
state = tf.Variable(0,name='counter')
number = tf.constant(1)

new_value = tf.add(state,number)
update = tf.assign(state,new_value)

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for i in range(3):
        sess.run(update)
        print(sess.run(state))