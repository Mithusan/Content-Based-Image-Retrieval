import numpy as np
import time
from pathlib import Path
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as img


def concatenate(list):  # function to concatenate barcodes
    result = ''
    for element in list:
        result += str(element)
    return result


def hammingDistance(str1, str2):  # function to calculate hamming distance
    i = 0
    count = 0
    while i < len(str1):
        if str1[i] != str2[i]:
            count += 1
        i += 1
    return count

# Barcode Generator
startBar = time.time()  # Measuring time for barcodes to generate
barcodes = []  # Array to hold barcodes
paths = []  # Array to hold path to images
pathList = Path("MNIST_DS").glob('**/*.jpg') #Defining path to data set

for path in pathList:

    path_in_str = str(path) # converting path to image to string
    paths.append(path_in_str) # saving paths to paths array
    arr = np.array(Image.open(path_in_str).convert('P')) #Creating array out of images

    # getting sums
    sumRow = np.sum(arr, axis=1).tolist()
    sumCol = np.sum(arr, axis=0).tolist()
    sumDig1 = [np.trace(arr, offset=i) for i in range(-np.shape(arr)[0] + 2, np.shape(arr)[1] - 1)]
    sumDig2 = [np.trace(np.fliplr(arr), offset=i) for i in range(-np.shape(np.fliplr(arr))[0] + 2, np.shape(np.fliplr(arr))[1] - 1)]  # order is slightly different than example

    # getting averages
    avgRow = np.average(sumRow).round(0)
    avgCol = np.average(sumCol).round(0)
    avgDig1 = np.average(sumDig1).round(0)
    avgDig2 = np.average(sumDig2).round(0)

    tempBarcode = []  # empty array for barcodes to be in before being concatenated
    for i in range(len(sumRow)):
        if sumRow[i] >= avgRow:
            tempBarcode.append(1)
        else:
            tempBarcode.append(0)

    for i in range(len(sumDig1)):
        if sumDig1[i] >= avgDig1:
            tempBarcode.append(1)
        else:
            tempBarcode.append(0)

    for i in range(len(sumCol)):
        if sumCol[i] >= avgCol:
            tempBarcode.append(1)
        else:
            tempBarcode.append(0)

    for i in range(len(sumDig2)):
        if sumDig2[i] >= avgDig2:
            tempBarcode.append(1)
        else:
            tempBarcode.append(0)

    barcodes.append(concatenate(tempBarcode))
endBar = time.time() # getting elapsed time

# Search Algorithm
hits = 0  # number of hits
minVal = 128  # Current minimum hamming distance
minIndex = -1  # Current index of image with lowest distance
testHam = 128  # hamming distance between two barcodes
startSearch = time.time()  # Measuring time for search algorithm

for barcodeSearchIndex in range(len(barcodes)): # Search algorithm
    for i in range(len(barcodes)): # Iterating thorough all the barcodes
        if i != barcodeSearchIndex: # Checking to see if barcode isn't reference barcode
            testHam = hammingDistance(barcodes[barcodeSearchIndex], barcodes[i]) # Getting hamming distance
            if testHam < minVal: # Check to find minimum hamming distance
                minVal = testHam
                minIndex = i
    if barcodeSearchIndex == 1: # getting time for one search
        firstSearch = time.time()
        # End time for first one
    if paths[barcodeSearchIndex][9] == paths[minIndex][9]: # Check to see if its hit or not
        hits += 1
    # Outputting images
    image1 = img.imread(paths[barcodeSearchIndex])
    image2 = img.imread(paths[minIndex])
    plt.subplot(2, 2, 1)
    plt.title("Base Image")
    plt.imshow(image1)
    plt.subplot(2, 2, 2)
    plt.title("Found Image")
    plt.imshow(image2)
    plt.show()
    minVal = 128
    minIndex = -1

# Time Calculations
endSearch = time.time() # End time for entire search
searchFirst = firstSearch - startSearch
searchTime = endSearch - startSearch

# Output statements
print("Accuracy", hits)
print("First Search time: ", searchFirst)
print("Search time: ", searchTime)
