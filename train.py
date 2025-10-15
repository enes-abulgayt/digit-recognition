import tensorflow as tf
from tensorflow.keras import layers, models

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()


x_train = x_train.reshape(-1, 28*28).astype("float32") / 255
x_test = x_test.reshape(-1, 28*28).astype("float32") / 255



mymodel = models.Sequential([
    layers.Dense(256, activation='relu', input_shape=(28*28,)),
    layers.Dropout(0.2),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

mymodel.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

mymodel.fit(x_train, y_train, epochs=10, batch_size=32, validation_split=0.1)
test_loss, test_acc = mymodel.evaluate(x_test, y_test, verbose=2)
print("✅ Test accuracy:", test_acc)

mymodel.save("mymodel.h5")
print("💾 Model saved as model.h5")