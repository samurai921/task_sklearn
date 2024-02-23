import cv2
import numpy as np

def solarize(image, threshold):
    return cv2.bitwise_not(cv2.threshold(cv2.bitwise_not(image), threshold, 255, cv2.THRESH_BINARY)[1])

def log_contrast(image, alpha):
    return (alpha * np.log(1 + image)).astype(np.uint8)

def main():
  
    image = cv2.imread('nature.jpg', cv2.IMREAD_GRAYSCALE)

 
    solarized_image = solarize(image, threshold=127)

   
    log_contrast_image = log_contrast(image, alpha=1.0)


    cv2.imwrite('solarized_image.jpg', solarized_image)
    cv2.imwrite('log_contrast_image.jpg', log_contrast_image)

if __name__ == "__main__":
    main()
