# implement in jupyter notebook

import numpy as np 
from PIL import Image 
from tensorflow.keras.preprocessing import image 
# Unet code 
import tensorflow as tf 

def unet_model(input_shape = (256, 256, 3), num_classes = 1): 
	inputs = tf.keras.layers.Input(input_shape) 
	
	# Contracting Path 
	s1 = encoder_block(inputs, 64) 
	s2 = encoder_block(s1, 128) 
	s3 = encoder_block(s2, 256) 
	s4 = encoder_block(s3, 512) 
	
	# Bottleneck 
	b1 = tf.keras.layers.Conv2D(1024, 3, padding = 'valid')(s4) 
	b1 = tf.keras.layers.Activation('relu')(b1) 
	b1 = tf.keras.layers.Conv2D(1024, 3, padding = 'valid')(b1) 
	b1 = tf.keras.layers.Activation('relu')(b1) 
	
	# Expansive Path 
	s5 = decoder_block(b1, s4, 512) 
	s6 = decoder_block(s5, s3, 256) 
	s7 = decoder_block(s6, s2, 128) 
	s8 = decoder_block(s7, s1, 64) 
	
	# Output 
	outputs = tf.keras.layers.Conv2D(num_classes, 
									1, 
									padding = 'valid', 
									activation = 'sigmoid')(s8) 
	
	model = tf.keras.models.Model(inputs = inputs, 
								outputs = outputs, 
								name = 'U-Net') 
	return model 

if __name__ == '__main__': 
	model = unet_model(input_shape=(572, 572, 3), num_classes=2) 
	model.summary()

  
# Load the image 
img = Image.open('  ') 
# Preprocess the image 
img = img.resize((572, 572)) 
img_array = image.img_to_array(img) 
img_array = np.expand_dims(img_array[:,:,:3], axis=0) 
img_array = img_array / 255.
  
# Load the model 
model = unet_model(input_shape=(572, 572, 3), num_classes=2) 
  
# Make predictions 
predictions = model.predict(img_array) 
  
# Convert predictions to a numpy array and resize to original image size 
predictions = np.squeeze(predictions, axis=0) 
predictions = np.argmax(predictions, axis=-1) 
predictions = Image.fromarray(np.uint8(predictions*255)) 
predictions = predictions.resize((img.width, img.height)) 
  
# Save the predicted image 
predictions.save('predicted_image.jpg') 
predictions
