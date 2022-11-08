# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import sys

# Open open.txt for reading
with open ('name.txt', 'rt') as myfile:

    # For each line, read to a string,
    for myline in myfile:  

        # Open an Image
        img = Image.open('certificate.jpeg')

        # Custom font style and font size
        Font = ImageFont.truetype("arial.ttf",50)

        # Call draw Method to add 2D graphics in an image
        I1 = ImageDraw.Draw(img)

        # Add Text to an image
        I1.text((100, 330), myline, fill=(0, 0, 0),font=Font)

        # name for image with extension
        jpg='.jpg'
        name = myline.strip() + jpg.strip()

        # Save the edited image
        img.save('certi/'+name)