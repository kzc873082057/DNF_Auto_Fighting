#_*_coding:utf-8_*
from C_SendKey import PressKey,ReleaseKey
import time
class AnalogButton(object):
    interval = 0.15
    DIK_F10 = 0x44
    DIK_F12 = 0x58
    def __index__(self):
        super(AnalogButton,self).__init__()
    def PressKeyAndReleaseKey(self,Keyboardcode):
        PressKey(Keyboardcode)
        time.sleep(AnalogButton.interval)
        ReleaseKey(Keyboardcode)

    def PressKeyAndReleaseKeyArray(self,KeyboardArray):
        for keyboar in KeyboardArray:
            self.PressKeyAndReleaseKey(keyboar)

    def PressKeyDown(self,Keyboardcode):
        PressKey(Keyboardcode)
    def PressKeyUp(self,Keyboardcode):
        ReleaseKey(Keyboardcode)

    def Again(self,flag):
        if (flag):
            self.PressKeyAndReleaseKey(AnalogButton.DIK_F10)
            return 1
        else:
            return -1

    def BackCity(self,flag):
        if (flag):
            self.PressKeyAndReleaseKey(AnalogButton.DIK_F12)
            return 1
        else:
            return -1



