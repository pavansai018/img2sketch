import cv2
import numpy as np

def dodgeV2(image,mask):
  return cv2.divide(image,255-mask,scale=256)


def pencil_sketch(source_path, destination_path):
  source_photo = cv2.imread(source_path)
  scale_percent = 0.60

  width = int(source_photo.shape[1]*scale_percent)
  height = int(source_photo.shape[0]*scale_percent)

  dim = (width,height)

  resized = cv2.resize(source_photo,dim,interpolation = cv2.INTER_AREA)
    
  kernel_sharpening = np.array([[-1,-1,-1],[-1, 9,-1],[-1,-1,-1]])
    
  sharpened = cv2.filter2D(resized,-1,kernel_sharpening)
    
  gray = cv2.cvtColor(sharpened , cv2.COLOR_BGR2GRAY)

  inv = 255-gray
    
  gauss = cv2.GaussianBlur(inv,ksize=(15,15),sigmaX=0,sigmaY=0)
    
    
  pencil_photo = dodgeV2(gray,gauss)
    
  cv2.imwrite(destination_path,pencil_photo)
  #cv2.imwrite("/home/pavan/Desktop/resized.jpg",resized)
  #cv2.imwrite("/home/pavan/Desktop/gauss.jpg",gauss)
  #cv2.imwrite("/home/pavan/Desktop/inv.jpg",inv)
  #cv2.imwrite("/home/pavan/Desktop/gray.jpg",gray)
  #cv2.imwrite("/home/pavan/Desktop/sharpened.jpg",sharpened)

if __name__ == "__main__":
  pencil_sketch("/home/pavan/Desktop/x5.jpg", "/home/pavan/Desktop/y5.jpg")

