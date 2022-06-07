import cv2
import numpy as np
img = cv2.imread(r'TO_PATH_IMAGES',cv2.IMREAD_UNCHANGED)

HEIGHT = len(img)
WIDTH = len(img[0])

print(HEIGHT, WIDTH)
print(img.ndim)

# アルファチャンネルが存在しなかったら追加する
if img.ndim == 3:
    img = cv2.cvtColor(img, cv2.COLOR_RGB2RGBA)

for h in range(HEIGHT):
    for w in range(WIDTH):
        
        b, g, r, a = img[h, w]
        if b == 36 and g == 28 and r == 237:
            img[h, w] = 250, 250, 250,255
            # print(img[h, w])
            continue
        # img[h, w] = 9, 71, 233,179

cv2.imwrite(r'SAVE_TO_PATH_IMAGES',img)

print('完了')