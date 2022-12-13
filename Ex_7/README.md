# Music Scores (very hard)


<img width="1347" alt="Screen Shot 2022-12-13 at 11 45 43" src="https://user-images.githubusercontent.com/74509202/207283675-a22e14b1-7382-414a-b415-84c2e590c3ff.png">


You are provided with scanned images of the scores in black and white encoded in a simple, yet efficient, form of RLE (Run-Length Encoding): the DWE (Doctor Who Encoding) algorithm.
In the DWE, consecutive pixels of the same color are encoded using a letter (B for black pixels, W for white pixels) followed by a space followed by the number of pixels of that color.

For example: W 5 B 20 W 16 means 5 white pixels, followed by 20 black pixels, followed by 16 white pixels.

Encoding is done from top to bottom. When the image width is known, reconstructing the original image is straightforward.
 
Within the images, the scores and notes have various sizes. To fully understand the challenge at hand, you should check all the images from this    page  . They correspond to the challenge tests further down. 

All the test cases are contained within these 12 images and if your code can process them all, then you are good to go!

INPUT:
Line 1: the width W and height H of the image in pixels.
Line 2: the image encoded from top to bottom using the DWE algorithm: several couples of "C L" separated by spaces. C is the color of the pixels (either B for black or W for white), L is the number of contiguous pixels of the same color (may encompass multiple image lines).
 
OUTPUT:
Notes read from left to right separated by space characters.
Each note is composed of two characters. First the note itself: A B C D E F or G. Then its type: H for a half note or Q for a quarter note. There is no distinction between the first C and the second C (same goes for D, E, F, G).
#### link to solution: https://www.codingame.com/ide/puzzle/music-scores 

-----------------------------------------------------------------------------------------------------------------------------------------------------------

## Q1: According to this result, it can concluded that cvxpy library more fast than cvxpy library
