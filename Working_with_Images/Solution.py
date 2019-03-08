from PIL import Image

try:
    #1.  Opening image from specific path
    filename = "image.png"
    with Image.open(filename) as image:
        #2. retrieving information about image
        width, height = image.size

        # Rotating image with given angle
        img = image.rotate(180)

        # Saved in the same relative location
        img.save("rotated_picture.jpg")
except IOError:
    pass

print("Width: " + str(width))
print("Height: " + str(height))

#3.