
Credit : We would like to give credit to AIZoo for their excellent mask detection model. For information about their work, see https://github.com/AIZOOTech/FaceMaskDetection for their repo.

# Introduction 

**MaskIt** is a Raspberry Pi system that captures live images and sends them via POST request to a server. As a proof of concept, we have created our own server (see `simple_server.py`). The server then uses the pre-trained TensorFlow model to identify human faces and classify them as 0) wearing a mas or 1) not wearing a mask and sends the response back to the Raspberry Pi. In our current implementation, as a proof of concept, the Raspberry Pi controls a servor motor to activate a welcome flag if and only if all people identified are wearing a mask. Else, the Raspberry Pi does nothing.

This proof of concept lays the foundation for more sophisticated systems that businesses can reopen, e.g. open doors only if all people are wearing a mask, speaker telling customers to put on a mask, etc. This system furthermore faciliates easier social distancing (no need to man the entrances to ensure compliance with mask orders) and hopefully will allow us to return to normalcy even quicker.

Main contributors: 
- citronella3alain
- hansgundlach


# Usage
Requirements for ML model usage are found on AIZoo's page, i.e. https://github.com/AIZOOTech/FaceMaskDetection

### Setting up the desktop server:
```
python simple_server.py
```

### Raspberry Pi Client:
```
python3 upload_img_post.py
```
In its current setting, the Raspberry Pi takes just 2 images for classification. However, this can be changed in line 22 to even an infinite while loop. One tentative idea at the moment is to use Ultrasonic distance sensors to identify incoming people.
