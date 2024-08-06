import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Path to the image
image_path = '/Users/saprativasarkar/Desktop/gitContri/SignboardTextTranslator/1_text_detection_easyocr/data/test3.png'

# Read the image using OpenCV
img = cv2.imread(image_path)

# Check if the image is loaded properly
if img is None:
    print("Error: Unable to load image. Check the file path.")
else:
    # Instance text detector
    reader = easyocr.Reader(['en'], gpu=False)

    # Detect text on image
    text_ = reader.readtext(img)

    # Create a list to store text data
    text_data = []

    threshold = 0.25
    # Draw bounding boxes and text
    for t_ in text_:
        bbox, text, score = t_

        if score > threshold:
            # Convert bbox coordinates to integer tuples
            bbox = np.array(bbox, dtype=int)
            pt1 = tuple(bbox[0])  # Top-left corner
            pt2 = tuple(bbox[2])  # Bottom-right corner

            # Draw bounding box
            cv2.rectangle(img, pt1, pt2, (0, 255, 0), 4)

            # Append text data to the list
            text_data.append({
                'text': text
                  # Convert numpy array to list for DataFrame
            })

    # Create a DataFrame from the text data
    df = pd.DataFrame(text_data)

    # Save DataFrame to CSV
    df.to_csv('detected_text_data.csv', index=False)

    # Display the image with bounding boxes and text
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

    # Print DataFrame to console
    print(df)
