import tensorflow as tf

# Convert the model.
converter = tf.compat.v1.lite.TFLiteConverter.from_frozen_graph(
    graph_def_file='Freeze_save.pb',
                    # both `.pb` and `.pbtxt` files are accepted.
    input_arrays=['Input_image'],
    input_shapes={'Input_image' : [1, 240, 320,3]},
    output_arrays=['Yolo/Final/conv2d/BiasAdd']
)
tflite_model = converter.convert()

# Save the model.
with open('Freeze_save.tflite', 'wb') as f:
  f.write(tflite_model)

