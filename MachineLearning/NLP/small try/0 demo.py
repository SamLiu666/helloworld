import tensorflow as tf


x = tf.constant(range(12))  # 创建一个行向量
X = tf.reshape(x, (3,-1))
print(X)