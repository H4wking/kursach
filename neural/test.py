import tensorflow as tf
from tensorflow import keras
from tensorflow.python.feature_column.feature_column_v2 import DenseFeatures

new_model = keras.models.load_model('my_model.h5')
new_model.summary

