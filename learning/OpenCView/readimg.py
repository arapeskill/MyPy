import cv2 as cv

img = cv.imread(r"D:\Data\PythonData\MyPy\learning\OpenCView\Photos\cat.jpg")

cv.imshow("Cat", img)
cv.waitKey(0)
cv.destroyAllWindows()
