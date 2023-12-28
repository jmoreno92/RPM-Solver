from PIL import Image, ImageFilter

def main():

    ### 01 INTRODUCTION AND NEW()
    # Create 'size' variable with tuple
    size = width, height = 320, 240;

    # First argument represents 'mode'. Refer to: https://pillow.readthedocs.io/en/stable/handbook/concepts.html
    # Second argument for size (as tuple)
    image = Image.new("RGB", size)  # Default black color
    image.show()

    # image_white = Image.new("RGB", size, 'white')
    image_white = Image.new("RGB", size, '#ffffff')
    image_white.show()

    # Other options:
    image_test = Image.new("RGB", size, '#adef32')
    image_test = Image.new("RGB", size, 'rgb(205,100, 200)')
    image_test = Image.new("RGB", size, 'rgb(0%,100%, 0%)')
    image_test.show()

    del image;


    ### 02 IMAGE OPEN
    ### 03 BLEND
    # 'Blend' has to have figures with the same size and mode
    filename_one = 'Square.png'
    filename_two = 'Triangle.png'

    image_one = Image.open(filename_one)
    image_two = Image.open(filename_two)

    Image.blend(image_one, image_two, 0.5).show()   # Images 'blended' 50%


    ### 04 COMPOSITE
    # 'Composite' has to have figures with the same size and mode
    Image.composite(image_one, image_two, image_one).show()
    Image.composite(image_one, image_two, image_two).show()

    del image_one, image_two

    ### 05 CONVERT()
    filename = 'py.png'
    image = Image.open(filename)

    # Different options and arguments. See documentation
    image.convert("L").show()
    # image.convert("1").show()

    del image


    ## 06 CROP
    filename = 'py.png'
    image = Image.open(filename)
    # Crop takes box 4-tuple defining left upper right and lower pixel coordinates
    image.crop( (10, 10, 1000, 1000) ).show()
    del image


    ## 07 FILTER
    filename = 'py.png'
    image = Image.open(filename)
    # image.filter( ImageFilter.BLUR).show()
    image.filter(ImageFilter.CONTOUR).show()
    # image.filter(ImageFilter.DETAIL).show()
    # image.filter(ImageFilter.DETAIL).show()
    # image.filter(ImageFilter.EDGE_ENHANCE).show()
    # image.filter(ImageFilter.EDGE_ENHANCE_MORE).show()
    # image.filter(ImageFilter.EMBOSS).show()
    # image.filter(ImageFilter.FIND_EDGES).show()
    # image.filter(ImageFilter.SMOOTH).show()
    # image.filter(ImageFilter.SMOOTH_MORE).show()
    # image.filter(ImageFilter.SHARPEN).show()

    del image


    ## 08 IMAGE SIZE
    filename = 'py.png'
    image = Image.open(filename)
    print(image.size)
    size = width, height = image.size
    del image




    ## XXX
    filename = 'py.png'
    image = Image.open(filename)
    del image




if (__name__ == "__main__"):

    main();