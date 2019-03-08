from PIL import Image

try:
    #1.  Opening image from specific path
    filename = "image.png"
    with Image.open(filename) as image:
        #2. retrieving information about image
        width, height = image.size

        print("---------------- Image infor ---------------")
        print("Width: " + str(width))
        print("Height: " + str(height))

        print("---------------- Rotating image ---------------")
        #3. Rotating image with given angle
        img = image.rotate(180)

        #4. Saved in the same relative location
        img.save("rotated_picture.png")

        print("---------------- Cropping image ---------------")
        #5. Cropping the image
        area = (0, 0, width / 2, height / 2)
        img = image.crop(area)

        # Saved in the same relative location
        img.save("cropped_picture.png")

        #6. Resizing image
        img = img.resize((width / 2, height / 2))

        # Saved in the same relative location
        img.save("resized_picture.png")


except IOError:
    pass


