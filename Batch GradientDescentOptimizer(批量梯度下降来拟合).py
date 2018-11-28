# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 17:57:28 2018

@author: DELL
"""

#批量梯度下降算法
import tensorflow as tf
import numpy as np
#输出结果可视化模块
import matplotlib.pyplot as plt
#定义一个添加神经层的函数
def add_layer(inputs,in_size,out_size,activation_function=None):
    Weights=tf.Variable(tf.random_normal([in_size,out_size]))
    biases=tf.Variable(tf.zeros([1,out_size])+0.1)#因为biases（偏差）推荐值不能为0，所以加上一个0.1
    Wx_plus_b=tf.matmul(inputs,Weights)+biases#inputs+Weights+biases
    if activation_function is None:
        outputs=Wx_plus_b
    else:
        outputs=activation_function(Wx_plus_b)
    return outputs

x_data=np.linspace(-1,1,300)[:,np.newaxis]#（-1,1）区间的生成300个数等差数列，np.newaxis定义格式为300个行
#define a noise，定义一个噪声，来让它不是正规的二次函数。
noise=np.random.normal(0,0.05,x_data.shape)#定义跟x_data数据一样的格式
#真实值
y_data=np.square(x_data)-0.5+noise#这个是拟合函数y=x^2+nosie
#placeholder用来参数
xs=tf.placeholder(tf.float32,[None,1])
ys=tf.placeholder(tf.float32,[None,1])
#隐藏层随便有多少个神经元，越少，越差，先定义一个
l1=add_layer(xs,1,10,activation_function=tf.nn.relu)
#预测值
prediction=add_layer(l1,10,1,activation_function=None)
#误差
loss=tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),
                   reduction_indices=[1]))
train_step=tf.train.GradientDescentOptimizer(0.1).minimize(loss)#GradientDescentOptimizer给定一个learning rate,通常是小于1
#must step,初始化变量
init=tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)
    #显示图形
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    ax.scatter(x_data,y_data)
    plt.ion()#就是让图片show了后不用暂停
    plt.show()
    
    for i in range(1000):#执行1000次
        sess.run(train_step,feed_dict={xs:x_data,ys:y_data})#只用通过placeholder的，都要用feed_dict传参数
        if i%50:                  
            #to see the step improvement控制台看，每一步的误差减少
            #print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))            
            try:  
                #预测值
                prediction_value=sess.run(prediction,feed_dict={xs:x_data})
                lines=ax.plot(x_data,prediction_value,'r-',lw=5)             
                #每次抹除线，先暂停0.1秒
                plt.pause(0.1)
                ax.lines.remove(lines[0])  #在图片中，去除掉第一个线段
            except Exception:
                pass
           
           



