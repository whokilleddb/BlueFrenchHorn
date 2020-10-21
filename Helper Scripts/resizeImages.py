#!/bin/python3

#Convert Images To Appropriate Sizes For Bot v2.0 (and later versions ?)
from PIL import Image, ImageDraw, ImageFilter

def changeImageSize(maxWidth,maxHeight,image):
    widthRatio  = maxWidth/image.size[0]
    heightRatio = maxHeight/image.size[1]

    newWidth    = int(widthRatio*image.size[0])
    newHeight   = int(heightRatio*image.size[1])

    newImage    = image.resize((newWidth, newHeight))
    return newImage

if __name__="__main__":  
        inputname=input("[+] Enter Path Of Original Image : ")
        outputname=input("[+] Enter Path/Name Of Output Image : ")
        oriFlag=Image.open(inputname)
        resAv=changeImageSize(256,256,oriFlag)
        resAv.save(outputname,quality=95)
        print(f"[+] Resized Image Saved As : {outputname}")
