# -*- coding:utf-8 -*-

"""
@author: Fan
@file:matrix.py     session apply
@time:2017/6/19 10:02
"""

import tensorflow as tf

sess = tf.Session()
matrix1 = tf.constant([[3,3]])
matrix2 = tf.constant([[2], [2]])
product = tf.matmul(matrix1,matrix2)

result = sess.run(product)
print(result)

sess.close()