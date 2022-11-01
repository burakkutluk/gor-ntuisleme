
import cv2 as cv
import numpy as np

def Inverting(Image):

    Height = Image.shape[0]
    Width = Image.shape[1]
    Channels = Image.shape[2]

    Size = (Height,Width,Channels)

    new = np.zeros(Size,np.uint8)

    for x in range(0,Height):
        for y in range(0,Width):
            for z in range(0,Channels):
                new[x,y,z]= 255 - Image[x,y,z]

    return new

def main():
    Input_Image = cv.imread("indir-1.png")
    yeni_resim =Inverting(Input_Image)

    cv.imwrite("yeni_resim.png",yeni_resim)


    cv.imshow("indir-1.png",Input_Image)
    cv.imshow("yeni_resim.png",yeni_resim)
    cv.waitKey(0)


if __name__ =='__main__':
    main()

