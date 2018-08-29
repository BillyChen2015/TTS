import tensorflow as tf
a = tf.constant(2)
b = tf.constant(3)
x = tf.add(2,3)
sess = tf.InteractiveSession()
print(sess.run(x))
