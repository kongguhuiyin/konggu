# _*_ coding : UTF-8 _*_
#    开发人员 : wangyueke
#    开发时间 : 2021/8/2 9:42
#    文件名称 : 卷积神经网络识别手写数字.py
#    开发工具 : PyCharm

import os
from time import time
import tensorflow as tf
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)
tf.compat.v1.disable_eager_execution()
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'   # 屏蔽tensorflow的日志和警告信息

import tensorflow.examples.tutorials.mnist.input_data as input_data
mnist = input_data.read_data_sets("E:\\PyCharm\\PycharmProjects\\venv\\Lib\\site-packages\\tensorflow\\python\\keras\\datasets\\MNIST_data\\", one_hot=True)


# ----------建立共享函数----------
# 定义权重张量
def weight(shape):
    return tf.Variable(tf.compat.v1.truncated_normal(shape, stddev=0.1))


# 建立偏差张量
def bias(shape):
    return tf.Variable(tf.compat.v1.constant(0.1, shape=shape), name='b')


# 卷积运算
def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


# -----------卷积--------------
# 建立池化层
def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],
                          strides=[1, 2, 2, 1],   # 缩减采样窗口的大小
                          padding='SAME')   # 缩减采样窗口的跨步


# 建立输入层
with tf.name_scope('Input_Layer'):
    x = tf.compat.v1.placeholder("float", shape=[None, 784], name='x')
    x_image = tf.reshape(x, [-1, 28, 28, 1])   # 转为四维向量，第一维因为输入的项数不确定设为-1，第二三维数字的图像大小为28*28，第四维单色设为1


# 建立卷积层1
with tf.name_scope('C1_Conv'):
    w1 = weight([5, 5, 1, 16])
    b1 = bias([16])
    Conv1 = conv2d(x_image, w1) + b1   # 进行卷积运算
    C1_Conv = tf.nn.relu(Conv1)


# 建立池化层1
with tf.name_scope('C1_Pool'):
    C1_Pool = max_pool_2x2(C1_Conv)


# 建立卷积层2
with tf.name_scope('C2_Conv'):
    w2 = weight([5, 5, 16, 36])
    b2 = bias([36])   # 卷积层2要产生36个图像
    Conv2 = conv2d(C1_Pool, w2) + b2
    C2_Conv = tf.nn.relu(Conv2)   # ReLU激活函数转换，会把原本是负数的点转换为0


# 建立池化层2
with tf.name_scope('C2_Pool'):
    C2_Pool = max_pool_2x2(C2_Conv)


# 建立平坦层
with tf.name_scope('D_Flat'):
    D_Flat = tf.reshape(C2_Pool, [-1, 1764])   # -1：后续会传入不定项数的训练数据，1764：C2_Pool为36个7*7的图像转为一维则是36*7*7=1764


# 建立隐藏层
with tf.name_scope('D_Hidden_Layer'):
    w3 = weight([1764, 128])   # 上一层D_Flat有1764个神经元，要建立的隐藏层D_Hidden有128个神经元
    b3 = bias([128])   # 要建立的隐藏层D_Hidden有128个神经元
    D_Hidden = tf.nn.relu(tf.matmul(D_Flat, w3) + b3)
    D_Hidden_Dropout = tf.nn.dropout(D_Hidden, rate=0.8)   # 避免过拟合


# 建立输出层
with tf.name_scope('Output_Layer'):
    w4 = weight([128, 10])   # 上一层有128个神经元，要建立的输出层有10个神经元
    b4 = bias([10])   # 要建立的输出层有128个神经元
    y_predict = tf.nn.softmax(tf.matmul(D_Hidden_Dropout, w4) + b4)


# 定义训练方式
with tf.name_scope('optimizer'):
    y_label = tf.compat.v1.placeholder("float", shape=[None, 10], name='y_label')
    loss_function = tf.compat.v1.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=y_predict, labels=y_label))
    optimizer = tf.compat.v1.train.AdamOptimizer(learning_rate=0.0001).minimize(loss_function)


# 定义评估模型准确率的方式
with tf.name_scope("evaluate_model"):
    correct_prediction = tf.equal(tf.argmax(y_predict, 1), tf.argmax(y_label, 1))
    accuracy = tf.compat.v1.reduce_mean(tf.cast(correct_prediction, "float"))   # tf.cast()是对张量进行数据类型转换


trainEpochs = 30
batchSize = 100
totalBatchs = int(mnist.train.num_examples/batchSize)
epoch_list = []
accuracy_list = []
loss_list = []
startTime = time()
sess = tf.compat.v1.Session()
sess.run(tf.compat.v1.global_variables_initializer())

for epoch in range(trainEpochs):
    for i in range(totalBatchs):
        batch_x, batch_y = mnist.train.next_batch(batchSize)
        sess.run(optimizer, feed_dict={x: batch_x, y_label: batch_y})
    loss, acc = sess.run([loss_function, accuracy], feed_dict={x: mnist.validation.images, y_label: mnist.validation.labels})
    epoch_list.append(epoch)
    loss_list.append(loss)
    accuracy_list.append(acc)
    print("Train Epoch:", '%02d' % (epoch + 1), "   Loss =", "{:.9f}".format(loss), "   Accuracy =", acc)

duration = time() - startTime
print("Train Finished takes:", duration)

print("Accuracy:", sess.run(accuracy, feed_dict={x: mnist.test.images, y_label: mnist.test.labels}))

# 进行预测
prediction_result = sess.run(tf.argmax(y_predict, 1), feed_dict={x: mnist.test.images, y_label: mnist.test.labels})
print(prediction_result[:10])



