# Content-Based-Image-Retrieval (CBIR)

### Algorithm Explanation In Detail:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
The algorithm's purpose is to create a barcode to present handwritten digits. I
would achieve this by making multiple functions to generate barcodes and additional
steps as it advances. The barcode would be based on the Radon barcode that employs
binarization. I used a Radon barcode to convert the images into a binary code, where "1"
represents a greater mean and a "0" represents a lesser mean. The algorithm primarily
focuses on images with a size of 28x28.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
The algorithm would employ projections specific angles of 0, 45, 90, and 180
when looking at the handwritten images creating many arrays. The function would
calculate the sum of the array based on the angles previously mentioned. The first array
would store the binary digits and scan through the given amount of projections. The array
can additionally be a smaller size to ensure and maintain accuracy.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
A search algorithm was created where multiple values were defined. This
algorithm is used to determine the most corresponding image in the dataset. I would
set variables for the number of hits, the minimum hamming distance, the distance
between the two barcodes and the current image with the lowest distance. The algorithm
iterates through all the barcodes to ensure that it was not a barcode from reference.
Hamming distance would be calculated using a function defined in the algorithm. The
Hamming distance would provide a comparison of two binary sets. The function includes
a while loop using the function "len" inside. The parameter would be a variable defined
by the function. The last step of the algorithm would be to determine if the algorithm is a
hit.

<br>

### Required Measurements and Analysis
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
The algorithm generated a hit ratio of 50%, meaning that half of the searches were hits.
Calculating the hit ratio was very easy as there were 100 total searches, making the
amount of hits achieved the hit ratio percentage.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Both the Barcode_Generator and Search_Algorithm contains a for loop nested within
another for loop. Therefore, the Big-O time complexity of both is O(n<sup>2</sup>). Although the
Barcode_Generator inner loop does not go from 0 to N, it still has a Big-O of O(n<sup>2</sup>) times
a constant value, and in Big-O complexities, constant factors are dropped. For the
Search_Algorithm, both inner and outer loops go from 0 to N (length of barcodes),
generating a time complexity of O(n<sup>2</sup>).
