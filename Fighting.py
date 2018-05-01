#_*_coding:utf-8_*
from FindImage import FindImage
import Key
from Analog_Buttons import AnalogButton
from ImageNotExist import ImageNotExist
import time
class Fighting(object):
    itemNotIsExist = True
    def __init__(self):
        self.findimage = FindImage('.\\image\\',(0,0,1070,660))
        print("初始化FindImage".center(50, "*"))
        self.analogbutton = AnalogButton()
        self.attackArrayKey = [Key.DIK_X,Key.DIK_A,Key.DIK_X,Key.DIK_S,Key.DIK_X,Key.DIK_D,Key.DIK_X,Key.DIK_F,Key.DIK_X,Key.DIK_G,Key.DIK_H]
        self.pick_up = [Key.DIK_Z,Key.DIK_X,Key.DIK_X,Key.DIK_X,Key.DIK_X,Key.DIK_X,Key.DIK_X,Key.DIK_X]
    def autoattack(self):
        count = 1
        round = 1
        while True:
            if  self.itemNotIsExist:
                self.analogbutton.PressKeyAndReleaseKeyArray(self.attackArrayKey)
                item = self.findimage.find("Item.jpg")
                if item and count < 5:
                    print("找到Item{0}".center(50,'*').format(count))
                    count += 1
                    self.itemNotIsExist = False
                again = self.findimage.find("Again.jpg")
                if again and round <= 16:
                    print("第{}轮挑战结束".center(50,'*').format(round))
                    count = 1
                    round += 1
                    if round > 16:
                        print("返回主城".center(50, '*'))
                        self.analogbutton.BackCity(True)
                        time.sleep(5)
                        return True
                    self.analogbutton.Again(again)
                    time.sleep(8)
                    self.analogbutton.PressKeyAndReleaseKey(Key.DIK_SPACE)
                    time.sleep(2)
                    self.analogbutton.PressKeyAndReleaseKey(Key.DIK_SPACE)
            elif not self.itemNotIsExist:
                self.analogbutton.PressKeyAndReleaseKeyArray(self.pick_up)
                self.itemNotIsExist = True
            else:
                raise Exception('未知错误')
    def resolve(self):
        Resolve = self.findimage.find("Resolve.jpg")
        self.findimage.click(Resolve)
        self.analogbutton.PressKeyAndReleaseKey(Key.DIK_K)
        time.sleep(0.2)
        self.analogbutton.PressKeyAndReleaseKey(Key.DIK_K)
        time.sleep(0.2)
        self.analogbutton.PressKeyAndReleaseKey(Key.DIK_RETURN)
        time.sleep(0.2)
        self.analogbutton.PressKeyAndReleaseKey(Key.DIK_A)
        time.sleep(0.2)
        self.analogbutton.PressKeyAndReleaseKey(Key.DIK_RETURN)
        time.sleep(4)
        self.analogbutton.PressKeyAndReleaseKey(Key.DIK_ESCAPE)
        print("执行完resolve".center(50, '*'))

    def gotoRoom(self):
        self.analogbutton.PressKeyDown(Key.DIK_K)
        time.sleep(1.5)
        self.analogbutton.PressKeyUp(Key.DIK_K)
        time.sleep(0.2)
        self.analogbutton.PressKeyDown(Key.DIK_J)
        time.sleep(2.1)
        self.analogbutton.PressKeyUp(Key.DIK_J)
        time.sleep(0.2)
        self.analogbutton.PressKeyDown(Key.DIK_I)
        time.sleep(2.1)
        self.analogbutton.PressKeyUp(Key.DIK_I)
        time.sleep(0.2)
        self.analogbutton.PressKeyDown(Key.DIK_L)
        time.sleep(3.2)
        self.analogbutton.PressKeyUp(Key.DIK_L)
        time.sleep(0.2)
        self.analogbutton.PressKeyDown(Key.DIK_K)
        time.sleep(1)
        self.analogbutton.PressKeyUp(Key.DIK_K)
        time.sleep(0.2)
        self.analogbutton.PressKeyDown(Key.DIK_L)
        time.sleep(1)
        self.analogbutton.PressKeyUp(Key.DIK_L)
        print("执行完gotoRoom".center(50,'*'))

    def entry(self):
        time.sleep(1)
        self.analogbutton.PressKeyAndReleaseKey(Key.DIK_SPACE)
        time.sleep(6)
        self.analogbutton.PressKeyAndReleaseKey(Key.DIK_SPACE)
        print("执行完entry".center(50, '*'))

    def choosePlay(self):
        time.sleep(0.2)
        self.analogbutton.PressKeyAndReleaseKey(Key.DIK_ESCAPE)
        Choose = self.findimage.find("Choose.jpg")
        self.findimage.click(Choose)
        self.findimage.click(Choose)
        time.sleep(5)
        self.analogbutton.PressKeyAndReleaseKey(Key.DIK_RIGHT)
        time.sleep(0.2)
        self.analogbutton.PressKeyAndReleaseKey(Key.DIK_RETURN)
        time.sleep(5)
        self.analogbutton.PressKeyAndReleaseKey(Key.DIK_RETURN)
        print("执行完choosePlay".center(50, '*'))






















