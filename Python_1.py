import os
import cv2
import matplotlib.pyplot as plt
import pandas as pd

# Folder path
folder_path = r"C:\Users\HP\Documents\Images_IOT"


# List to store image info
image_info = []

# Read all files in the folder
for file in os.listdir(folder_path):
    if file.lower().endswith(('.jpg', '.png')):

        # Read image
        img_path = os.path.join(folder_path, file)
        img = cv2.imread(img_path)

        if img is None:
            continue

        # Convert BGR to RGB for displaying
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Get width and height
        height, width = img.shape[:2]

        # Display image
        plt.imshow(img_rgb)
        plt.title(f"{file} ({width}×{height})")
        plt.axis('off')
        plt.show()

        # Store in list of dictionaries
        image_info.append({
            "filename": file,
            "width": width,
            "height": height
        })

# Convert to DataFrame
df = pd.DataFrame(image_info)

# Calculate area
df["area"] = df["width"] * df["height"]

# Find largest and smallest images
largest = df.loc[df["area"].idxmax()]
smallest = df.loc[df["area"].idxmin()]

print("Largest Image:")
print(largest, "\n")

print("Smallest Image:")
print(smallest, "\n")

# Save to CSV
df.to_csv("image_sizes.csv", index=False)
print("CSV file saved as image_sizes.csv")