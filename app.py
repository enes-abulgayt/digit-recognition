import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np
import cv2
from tensorflow.keras.models import load_model
import os
if not os.path.exists("mymodel.keras"):
    st.error("Model file not found. Please upload 'mymodel.keras' to the app directory.")
    st.stop()

model = load_model("mymodel.keras")

st.title("Handwritten Digit Recognition")
st.write("draw a number from 0 to 9 the model will guss it")

CANVAS_SIZE = 280

# Canvas
canvas_result = st_canvas(
    fill_color="rgba(255,255,255,1)",
    stroke_width=15,
    stroke_color="black",
    background_color="white",
    width=CANVAS_SIZE,
    height=CANVAS_SIZE,
    drawing_mode="freedraw",
    key="canvas",
)

if canvas_result.image_data is not None:
    img = canvas_result.image_data.astype("uint8")

   
    gray = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)

    
    gray = cv2.bitwise_not(gray)

    
    coords = cv2.findNonZero(gray)
    if coords is not None:
        x, y, w, h = cv2.boundingRect(coords)
        roi = gray[y:y+h, x:x+w] 

        digit = cv2.resize(roi, (20, 20), interpolation=cv2.INTER_AREA)
        final_img = np.zeros((28, 28), dtype=np.uint8)
        final_img[4:24, 4:24] = digit  

       
        input_img = final_img.reshape(1, 28*28).astype("float32") / 255.0

        if st.button(" Predict"):
            prediction = model.predict(input_img)
            digit_pred = np.argmax(prediction)

            st.image(final_img, caption="Processed Input (28x28)", width=150)
            st.write(f"### the model pridect : **{digit_pred}**")
            st.bar_chart(prediction[0])
