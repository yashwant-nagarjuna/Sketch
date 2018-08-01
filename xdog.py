# Difference of Gaussian filter

from scipy.ndimage.filters import gaussian_filter
import cv2
import numpy as np

def dog(image, gamma=1, k=1.6):
    """
    Computes the differnce of Gaussian for an image 
    and returns the image that results from computing dog
    k -> multiplier for second sigma value
    gamma -> multipler for second Gaussian
    """
    # s1 = 0.5
    s1 = 1.6
    s2 = k*s1

    gauss1 =cv2.GaussianBlur(image,(0, 0), s1)
    gauss2 = gamma*cv2.GaussianBlur(image, (0, 0), s2)
    
    result = gauss1 - (gauss2)
    return result


def xdog(image, epsilon=1):
    phi = 10

    """
    Computes the extended difference of gaussian for an image.
    This is done by thresholding. For more info refer the XDoG paper.
    """
#    phi = 1
    

    difference = dog(image, 0.98, 200)/255
    diff = difference*image

    for i in range(0, len(difference)):
      for j in range(0, len(difference[0])):
        if difference[i][j] >= epsilon:
          difference[i][j] = 1
        else:
          ht = np.tanh(phi*(difference[i][j] - epsilon ))
          difference[i][j] = 1 + ht

    return difference*255


image = cv2.imread('SOL.jpg', cv2.IMREAD_GRAYSCALE)
result = xdog(image, 0.26)
cv2.imwrite('result_image.jpg', result)
