import cv2
import numpy as np

def dog(image, sigma, k, gamma):
    s1 = sigma
    s2 = k*sigma
    im1 = cv2.GaussianBlur(image, (0, 0), s1)
    im2 = gamma*cv2.GaussianBlur(image, (0, 0), s2)
    return (im1 - gamma*im2)

def xdog(image, sigma, k, gamma, epsilon, phi):
    aux = dog(image, sigma, k, gamma)
    for i in range(len(aux)):
        for j in range(len(aux[0])):
            if aux[i][j] >= epsilon:
                aux[i][j] = 1
            else:
                ht = np.tanh(phi*(aux[i][j] - epsilon))
                aux[i][j] = 1 + ht
    return aux*255

def reparam(image, sigma, k, gamma, p, epsilon, phi):
    s1 = sigma
    s2 = k*sigma
    im1 = cv2.GaussianBlur(image, (0, 0), s1)
    im2 = gamma*cv2.GaussianBlur(image, (0, 0), s2)
    sharpened = ((1 + p)*(im1)) - (p*im2)
    for i in range(len(sharpened)):
        for j in range(len(sharpened[0])):
            if sharpened[i][j] >= epsilon:
                sharpened[i][j] = 1
            else:
                ht = np.tanh(phi*(sharpened[i][j] - epsilon))
                sharpened[i][j] = 1 + ht
    return sharpened*255

image = cv2.imread("./data/img_celeba/000001.jpg", cv2.IMREAD_GRAYSCALE)
result = reparam(image, 0.50,  1.6, 1, 21.7, 79.5, 100.017)
cv2.imwrite('result2.jpg', result)
