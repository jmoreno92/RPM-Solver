from PIL import Image, ImageFilter
import os

print("Hello World")
print()

### Display image on screen
image1 = Image.open('Pinno.png')
# image1.show()
# Square = Image.open('Square.png')
# Square.show()

### Save in different format
# image1.save('Pinno_diff_format.jpg')      # doesn't work
image1.save('Pinno_diff_format.gif')

### Loop on files in current directory and convert to different format
for f in os.listdir('.'):   # Dot represents current directory
    # print(f)    # Lists everything we have in current directory
    if f.endswith('.png'):
        print(f)    # Lists .png's we have in current directory
        i = Image.open(f)   # Open file
        fn, fext = os.path.splitext(f)  # Save file name and file extension
        print(fn)   # Prints file name (without extension)
        i.save('gifs/{}.gif'.format(fn))    # Save

### Resize figures keeping same aspect ratio (useful for websites and thumbnails)
size_300 = (300,300)   # Define maximum size as tuple
size_700 = (700,700)   # Define maximum size as tuple

for f in os.listdir('.'):   # Dot represents current directory
    if f.endswith('.png'):
        i = Image.open(f)   # Open file
        fn, fext = os.path.splitext(f)  # Save file name and file extension

        i.thumbnail(size_700)
        i.save('700/{}_700{}'.format(fn,fext))    # Save in 700 folder

        i.thumbnail(size_300)
        i.save('300/{}_300{}'.format(fn,fext))    # Save in 300 folder

### Rotate image 90 degrees and save
image1 = Image.open('Pinno.png')
image1.rotate(90).save('Pinno_rotated.png')

### Modify to black and white image and save
image1 = Image.open('Pinno.png')
image1.convert(mode='L').save('Pinno_blackwhite.png')

### Blur image using ImageFilter
image1 = Image.open('Pinno.png')
# image1.filter(ImageFilter.GaussianBlur()).save('Pinno_blur.png')  # A little blurred with default values
image1.filter(ImageFilter.GaussianBlur(15 )).save('Pinno_blur.png')