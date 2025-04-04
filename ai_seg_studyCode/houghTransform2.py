import numpy as np
import cv2

image = cv2.imread("./projectData/segmentation_results/26309_000_OK_otsu.png")
# 원본 영상을 복사
image2 = image.copy()

# 흑백 영상으로 변환
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# canny edge detection을 이용해 edge 검출
edges = cv2.Canny(gray, 100, 200)

lines = cv2.HoughLinesP(edges, 1, np.pi/180, 25, None, 40, 5)
for line in lines:
    # 검출된 선분 초록색으로 그리기
    x1, y1, x2, y2 = line[0]
    cv2.line(image2, (x1,y1), (x2, y2), (0,255,0), 1)

cv2.imshow("image", image2)
cv2.imshow("edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows() # 모든 창 닫기
cv2.waitKey(1)