import cv2 as cv


def resizeFrame(img_temp, scale=0.75):
    height = int(img_temp.shape[0] * scale)
    width = int(img_temp.shape[1] * scale)
    return cv.resizeFrame(img_temp, (width, height))


img = cv.imread(r"D:\Data\PythonData\MyPy\learning\OpenCView\Photos\cat.jpg")

cv.imshow("Cat", img )
cv.waitKey(0)
cv.destroyAllWindows()
