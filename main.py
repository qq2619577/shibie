import cv2  as cv
import time
import pyautogui as pg
import numpy as np

def get_img():

    img = pg.screenshot(region=[0, 0, 1920, 1080])  # x,y,w,h
    
    # img = Image.fromarray(np.uint8(img))
    # img.save('screenshot3.png')
    img = cv.cvtColor(np.asarray(img), cv.COLOR_RGB2BGR)  # cvtColor用于在图像中不同的色彩空间进行转换,用于后续处理。
    cv.imwrite('2.png', img)




def main():
    big_img = cv.imread('2.png')
    small_img = cv.imread('1.png')

    # 确保读取成功
    if big_img is None or small_img is None:
        print("请检查图像路径是否正确")
        exit()

    # 获取模板的高度和宽度
    h, w = small_img.shape[:2]

    # 使用 TM_SQDIFF_NORMED 进行模板匹配
    result = cv.matchTemplate(big_img, small_img, cv.TM_SQDIFF_NORMED)

    # 找到最佳匹配的位置
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    # 计算最佳匹配的左上角坐标
    top_left = min_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)


    pg.moveTo(top_left[0]+w/2, top_left[1]+h/2)  # 移动鼠标到匹配结果的中心位置
    # 在匹配结果中绘制矩形框
    cv.rectangle(big_img, top_left, bottom_right, (0, 255, 0), 2)

    # 显示结果
    cv.imshow('Matched Result', big_img)
    cv.waitKey(0)
    cv.destroyAllWindows()




if __name__ == '__main__':
    time.sleep(2)
    get_img()
    main()