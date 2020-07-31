from PIL import Image, ImageChops
import cv2
import numpy
#Read orignal images 
orignal = cv2.imread("1.jpg")
duplicate = cv2.imread("1.jpg")

img1 = Image.open("1.jpg")
img2 = Image.open("1.jpg")

#Display images
#plt.imshow(orignal)
#plt.show()

# Get Difference
image1 = orignal.shape
image2 = duplicate.shape

difference =cv2.subtract(image1,image2)
diff = ImageChops.subtract(img1,img2)
print(difference)

result=not numpy.any(difference)
if result is True:
    print("Same")
    
else:
    print("not Same")
    cv2.imwrite("result.jpg",difference)
    diff.show()

#cv2.imshow("Difference",difference)
#plt.imshow(difference)
#plt.show()
#cv2.waitKey(0)
#cv2.destroyAllWindows()
