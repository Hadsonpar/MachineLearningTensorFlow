#TITULO DEL TUTORIAL ARTICULO: Trabajando con Visual Studio Code, Anaconda Python y TensorFlow
#LINK DEL TUTORIAL ARTICULO: http://blog.hadsonpar.com/2021/06/trabajando-con-visual-studio-code.html
import tensorflow as tf
tf.executing_eagerly()
with tf.compat.v1.Session() as sess:
    #Create a constant
    hello = tf.constant("Hola mundo Tensorflow")
    #Run the tf.constant
    output = sess.run(hello)
    print(output)