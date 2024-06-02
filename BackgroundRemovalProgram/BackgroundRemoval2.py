from rembg import remove 
from PIL import Image 
  
# Store path of the image in the variable input_path 
input_path = '283210.jpg'
  
# Store path of the output image in the variable output_path 
output_path = 'new2.png'
  
# Processing the image 
input = Image.open(input_path) 
  
# Removing the background from the given Image 
output = remove(input) 
  
#Saving the image in the given path 
output.save(output_path) 