Credit : We would like to give credit to AIZoo for making an excellent mask detection model in tensorflow.

MaskIt is a Raspberry-pi camera to capture live images then sends the captured image to a custom HTTP Linux server. On the server, we use a TensorFlow model to examine the image from the Raspberry-pi. If the image contains a person with a mask the objection detection model will return true and send a request for the Raspberry pi to move a servo (“ie open the door”).

The inference model from AIzoo is tensorflow_infer.py while test_recieve_image.py, test_camera_steam.py, and upload_img.py manage the HTTP server component. 
