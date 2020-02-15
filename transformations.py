import numpy as np
import imageio


def get_image(img):
    if type(img) is str:
        return imageio.imread(img)
    else:
        return img.copy()


def blur(image, blur=32):
    image = get_image(image)

    boxSize = blur
    halfBoxSize = blur//2

    totalRows, totalCols, totalColors = image.shape

    print(totalCols, totalRows, totalColors)

    startRow = halfBoxSize
    startCol = halfBoxSize

    for row in range(startRow, totalRows - halfBoxSize):
        for col in range(startCol, totalCols - halfBoxSize):
            localPixels = image[row - halfBoxSize: row +
                                halfBoxSize+1, col - halfBoxSize: col + halfBoxSize+1]

            image[row, col] = localPixels.mean(axis=(0, 1))

    return image
