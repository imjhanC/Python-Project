import cv2
import numpy as np
from matplotlib import pyplot as plt

def remove_background(input_image_path, output_image_path):
    # Read the input image
    image = cv2.imread(input_image_path)
    original_image = image.copy()
    
    # Create a mask
    mask = np.zeros(image.shape[:2], np.uint8)
    
    # Define the background and foreground models
    bgd_model = np.zeros((1, 65), np.float64)
    fgd_model = np.zeros((1, 65), np.float64)
    
    # Define the rectangle that contains the foreground object
    height, width = image.shape[:2]
    rect = (10, 10, width - 10, height - 10)
    
    # Apply the GrabCut algorithm
    cv2.grabCut(image, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)
    
    # Modify the mask
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    image = image * mask2[:, :, np.newaxis]
    
    # Create an all white background
    background = np.full_like(original_image, 255)
    
    # Combine the foreground with the all white background
    final_image = background * (1 - mask2[:, :, np.newaxis]) + image
    
    # Save the output image
    cv2.imwrite(output_image_path, final_image)
    print(f"Background removed and image saved to {output_image_path}")
    
    # Display the output image
    plt.imshow(cv2.cvtColor(final_image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

# Example usage:
input_image_path = '283210.jpg'
output_image_path = 'new.py'

remove_background(input_image_path, output_image_path)
