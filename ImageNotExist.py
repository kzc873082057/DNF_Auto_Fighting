#_*_coding:utf-8_*

class ImageNotExist(Exception):
    def __init__(self,*args,**kwargs):
        super(ImageNotExist,self).__init__(*args,**kwargs)
