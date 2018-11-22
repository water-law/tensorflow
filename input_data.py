# -*- coding:utf-8 -*-

"""
解压 MNIST_data 下的数据集
"""
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
