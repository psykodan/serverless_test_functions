import cv2
scale_percent=100
for loop in range(20):
      imagePath = "img.jpg"

      # Read the image
      img = cv2.imread(imagePath)

      scale_percent = scale_percent + 100 # percent of original size
      width = int(img.shape[1] * scale_percent / 100)
      height = int(img.shape[0] * scale_percent / 100)
      dim = (width, height)
      # resize image
      resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
      name = "img{}.jpg".format(loop)
      cv2.imwrite(name,resized)
      #print('Resized Dimensions : ',resized.shape)