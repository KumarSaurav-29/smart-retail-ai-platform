import numpy as np
from PIL import Image

import app.startup as startup


def predict_image(file):
    """
    Predict image class using the trained MobileNetV2 model.
    """

    image = Image.open(file).convert("RGB")
    image = image.resize((224, 224))

    image = np.array(image)
    image = image.astype("float32") / 255.0
    image = np.expand_dims(image, axis=0)

    prediction = startup.image_model.predict(image, verbose=0)

    predicted_index = np.argmax(prediction)
    confidence = float(np.max(prediction))

    return {
        "predicted_class": startup.class_names[predicted_index],
        "confidence": round(confidence * 100, 2)
    }