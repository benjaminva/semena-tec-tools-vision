"""
By Abhisek Jana
code taken from https://github.com/adeveloperdiary/blog/tree/master/Computer_Vision/Sobel_Edge_Detection
blog http://www.adeveloperdiary.com/data-science/computer-vision/how-to-implement-sobel-edge-detection-using-python-from-scratch/

Modified by Benjamin Valdes
"""

import numpy as np
import cv2
import argparse
import matplotlib.pyplot as plt
from gaussian_blur import gaussian_blur
from simple_conv import convolution
 
 
def sobel_edge_detection(image, filter, verbose=False):
    """Aplica el filtro de sobel con convoluciones  para 
    obtener las orillas horizontales y verticales, 
    después se mezclan las matrices en una sola imagen
    """
    
    new_image_x = convolution(image, filter)
 
    if verbose:
        plt.imshow(new_image_x, cmap='gray')
        plt.title("Horizontal Edge")
        plt.show()
 
    new_image_y = convolution(image, np.flip(filter.T, axis=0))
 
    if verbose:
        plt.imshow(new_image_y, cmap='gray')
        plt.title("Vertical Edge")
        plt.show()
 
    gradient_magnitude = np.sqrt(np.square(new_image_x) + np.square(new_image_y))

    if verbose:
        plt.imshow(gradient_magnitude, cmap='gray')
        plt.title("Gradient Magnitude")
        plt.show()
 
    gradient_magnitude *= 255.0 / gradient_magnitude.max()
 
    if verbose:
        plt.imshow(gradient_magnitude, cmap='gray')
        plt.title("Gradient Magnitude")
        plt.show()
 
    return gradient_magnitude
 
 
if __name__ == '__main__':
    
    filter = np.array([[-1, 0, 1], #sobel filter/mask/kernel
                       [-2, 0, 2], 
                       [-1, 0, 1]])  

    # obtiene la imagen de la linea de comando "python sobel.py -i img.jpg"
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path of image")
    args = vars(ap.parse_args())

    # cambia la imagen a formato numerico, matriz de 3 dimensiones rgb
    image = cv2.imread(args["image"])
    
    """ preformatea la imagen, la cambia a una sola matriz en escala 
    de grises con efecto blur (borroso) usando el método de Gauss
    """
    image = gaussian_blur(image, 9, verbose=False)
    
    sobel_edge_detection(image, filter, verbose=True)