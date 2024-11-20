import cv2
import numpy as np
from matplotlib import pyplot as plt
import streamlit as st

# Functions for image enhancement
def adjust_brightness_contrast(image, alpha=1.5, beta=50): 
    return cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

def smooth_image(image, ksize=7):
     return cv2.GaussianBlur(image, (ksize, ksize), 0)

def sharpen_image(image):
     kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    return cv2.filter2D(image, -1, kernel)

def apply_mask(image, center, axes, angle=0):
     height, width = image.shape[:2]
    mask = np.zeros((height, width), dtype=np.uint8)
    cv2.ellipse(mask, center, axes, angle, 0, 360, 255, -1)
    return cv2.bitwise_and(image, image, mask=mask)

def enhance_image(image_path):
     original_image = cv2.imread(image_path)
    
     brightness_contrast_image = adjust_brightness_contrast(original_image)
    smoothed_image = smooth_image(original_image)
    sharpened_image = sharpen_image(original_image)

     height, width = original_image.shape[:2]
    center = (width // 2, height // 2)  # Center of the oval
    axes = (width // 4, height // 6)  # Major and minor axes
    masked_image = apply_mask(original_image, center, axes)

     final_image = apply_mask(
        sharpen_image(
            smooth_image(
                adjust_brightness_contrast(original_image)
            )
        ), center, axes
    )

     titles = [
        "Original Image",
        "Brightness & Contrast Adjusted",
        "Smoothed Image",
        "Sharpened Image",
        "Masked Image",
        "Final Enhanced Image"
    ]
    images = [
        original_image,
        brightness_contrast_image,
        smoothed_image,
        sharpened_image,
        masked_image,
        final_image
    ]
    
    return images, titles

 st.title("Image Enhancement Web App")
st.write("Upload an image to apply enhancements!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
     image_path = "uploaded_image.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

     images, titles = enhance_image(image_path)
    
     for i in range(len(images)):
        st.subheader(titles[i])
        st.image(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB), caption=titles[i], use_column_width=True)
