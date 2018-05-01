#_*_coding:utf-8_*
import jpype
import os.path
class FindImage(object):
    def __init__(self,bundlePath,tupleRegion):
        '''
        :param bundlePath: 图片路径
        :param tupleRegion: （x,y,w,h）
        '''
        # 设置默认图片搜索路径
        self.FindImagePath = jpype.JPackage('org').sikuli.script.ImagePath
        self.FindImagePath.setBundlePath(bundlePath)
        self.BaseImagePath = self.FindImagePath.getBundlePath()
        #实例化Region对象
        self.Region = jpype.JClass("org.sikuli.script.Region")
        self.ExampleRegion = self.Region(*tupleRegion)
        #设置等待时间
        self.ExampleRegion.setAutoWaitTimeout(0.8)
        #匹配模式类
        self.Pattern = jpype.JClass("org.sikuli.script.Pattern")


    def pathisexist(self,path):
        realpath = os.path.join(self.BaseImagePath,path)
        if not os.path.exists(realpath):
             raise FileNotFoundError("不存在此路径{path}".format(path=realpath))
    def find(self,path):
        '''
        :param path:  要找图片的路径
        :param seconds: 超时时间
        :return: 找到返回Match,找不到返回None
        '''
        self.pathisexist(path)
        return self.ExampleRegion.exists(path)

    def click(self,psmrl):
        '''
        :param psmrl:模式，字符串，匹配，区域或评估为点击点的位置。
        :return:
        '''
        self.ExampleRegion.doubleClick(psmrl)
    def click_1(self):
        self.ExampleRegion.click()

    def mouseMove(self,x,y):
        self.ExampleRegion.mouseMove(x,y)
    def mouseMove_Match(self,PFRML):
        self.ExampleRegion.mouseMove(PFRML)

