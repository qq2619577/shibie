import cv2  as cv
import time







def main():
    big_img = cv.imread('./2.png',0)
    small_img = cv.imread('./1.png',0)

    result = cv.matchTemplate(big_img,small_img, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    h,w = small_img.shape

    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv.rectangle(big_img, top_left, bottom_right, 255, 2)


    cv.imshow('big_img', big_img)
    cv.waitKey(0)
    cv.destroyAllWindows()




if __name__ == '__main__':
    main()