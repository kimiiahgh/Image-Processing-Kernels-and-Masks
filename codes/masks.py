import cv2
from matplotlib import pyplot as plt
img = cv2.imread('Image.jpg')
mask = cv2.imread('mask.png')
methods = ['cv2.TM_CCORR','cv2.TM_CCORR_NORMED',
           'cv2.TM_CCOEFF','cv2.TM_CCOEFF_NORMED', 
           'cv2.TM_SQDIFF','cv2.TM_SQDIFF_NORMED']
m=["Correlation","Normilized corr","Coefficient","Normalized Coeff","Squere Diff","Normalized Squer Diff"]

result=[0 for i in range(0,6)]
res=cv2.matchTemplate(img,mask,cv2.TM_CCORR)
#print(res)
w, h = mask.shape[:-1]
j=100
for i in range(len(methods)):
    img2=img
    method = eval(methods[i])
    result[i] = cv2.matchTemplate(img,mask,method)
    print ((methods[i],result[i]))
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result[i])
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(img2,top_left, bottom_right, 255, 2)
    plt.figure(j)
    plt.subplot(121),plt.imshow(result[i])
    plt.title(m[i]), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img2)
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(method)
    plt.show(block=False)
    j+=100
