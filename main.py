import cv2 as cv
import numpy as np


def start():
    readImage()


def readImage():

    image = cv.imread('Flower.jpg')

    st = image.shape

    if len(st) == 3:
        modifyPx(image)

    else:
        print("Image can't reload...")


def modifyPx(image):
    x = int(input("X: "))
    y = int(input("Y: "))
    z = int(input("Color Attributes: "))

    cv.imshow("Before ", image)
    cv.waitKey(0)
    cv.destroyAllWindows()

    px = image.item(x, y, z)
    print("Image Value: ", x, y, z)
    print("Pixel Value: ", px)

    image.itemset((x, y, z), 200)
    px = image.item(x, y, z)
    print("Modified Pixel Value: ", px)

    dimention(image)


def dimention(image):

    size = image.shape

    x = 1000
    y = 1000

    if size[0] > x and size [1] > y:
        print("Invalid Image Dimention!")

    else:
        imagetype(image)


def imagetype(image):
    dtype = image.dtype
    print("Image Data Type: ", dtype)

    imagesize(image)


def imagesize(image):

    rqrdsize = 2000000
    size = image.size

    if size <= rqrdsize:
        print("Image Size Validated!")
        cv.imshow("After", image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    else:
        print("Image Size Invalid!")


start()
