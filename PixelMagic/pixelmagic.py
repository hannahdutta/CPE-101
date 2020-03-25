# Name:         Parth Ray
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Pixel Magic
# Term:         Fall 2019
import sys


def main():
    if valid_args():
        return
    pixelswh = get_pixelswh()
    pixels = pixelswh[2:]
    width, height = pixelswh[0][0], pixelswh[0][1] 
    if "fade" == sys.argv[1]:
        pixels = fade_image(pixels, width, int(sys.argv[3]), 
                int(sys.argv[4]), int(sys.argv[5]))
        fp = open("fade.ppm", "w")
        write_pixels(pixels, width, height, fp)   
    else:
        try:
            reach = int(sys.argv[3])
        except IndexError:
            reach = 4
        pixels = blur_image(pixels, width, reach)
        fp = open("blur.ppm", "w")            
        write_pixels(pixels, width, height, fp)


def get_pixelswh():
    fp = open(sys.argv[2], "r")
    pixelswh = fp.readlines()
    pixelswh.remove("P3\n") 
    for i in range(len(pixelswh)):
        strpix = pixelswh[i][:-1].split(" ")
        pixelswh[i] = [int(j) for j in strpix]
    fp.close()
    return pixelswh


def write_pixels(pixels, width, height, fp):
    fp.write("P3\n")
    fp.write(f"{width} {height}\n")
    fp.write("255\n")
    for i in range(len(pixels)):
        string = ""
        for j in range(len(pixels[i])):
            if j == 0:
                string += str(pixels[i][j])
            else:
                string = string + " " + str(pixels[i][j])
        fp.write(string + "\n")


def valid_args():
    if len(sys.argv) < 3:
        print("Usage: python pixelmagic.py <mode> <image>")
        return True
    if sys.argv[1] != "fade" and sys.argv[1] != "blur":
        print("Error: Invalid Mode")
        return True
    if sys.argv[1] == "fade" and len(sys.argv) != 6:
        print("Usage: python pixelmagic.py fade <image> <row> <col> <radius>")
        return True
    if ".ppm" in sys.argv[2]: 
        try:
            f = open(sys.argv[2], "r")
            f.close()
        except FileNotFoundError:
            print("Error: Unable to Open " + sys.argv[2])
            return True
        


def fade_image(pixels, width, row, col, radius):
    for i in range(len(pixels)):
        dist = ((((i // width) - row) ** 2) + (((i % width) - col) ** 2)) ** .5
        scale = (radius - dist) / radius
        if scale < .2:
            scale = .2
        for j in range(len(pixels[i])):
            pixels[i][j] = int(pixels[i][j] * scale)
    return pixels


def blur_image(pixels, width, reach):
    blurredlist = []
    for i in range(len(pixels)):
        row, col = i // width, i % width
        blurpixel = [0, 0, 0]
        red, green, blue = 0, 0, 0
        pixcount = 0
        for y in range(row - reach, row + reach + 1):
            if y >= 0 and (y < len(pixels) // width):
                for x in range(col - reach, col + reach + 1):
                    if x >= 0 and x < width:
                        pixcount += 1
                        red += pixels[width * y + x][0]
                        green += pixels[width * y + x][1]
                        blue += pixels[width * y + x][2]
        blurpixel[0] = red // pixcount
        blurpixel[1] = green // pixcount
        blurpixel[2] = blue // pixcount
        blurredlist.append(blurpixel)
    return blurredlist


if __name__ == "__main__":
    main()
