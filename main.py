import PIL.Imagedef main():
    path = input("Enter the path to the image fiel : \n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "Unable to find image ")  # resize image
    image = resize(image)  # convert image to greyscale image
    # convert greyscale image to ascii characters
    greyscale_image = to_greyscale(image)
    ascii_str = pixel_to_ascii(greyscale_image)
    img_width = greyscale_image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ""  # Split the string based on width  of the image
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + \
            "\n"  # save the string to a file
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_img)
main()
