#_*_coding:utf-8_*_
import jpype
from Fighting import Fighting
def Main():
    jvmPath = jpype.get_default_jvm_path()
    jarpath = "F:\\sikuli\\sikulixapi.jar"
    classpath = "-Djava.class.path=" + jarpath
    jpype.startJVM(jvmPath, classpath)
    print("初始化JAVA虚拟机".center(50, "*"))
    fighting = Fighting()
    playnum = 1
    while playnum <=4:
        fighting.gotoRoom()
        fighting.entry()
        fighting.autoattack()
        fighting.resolve()
        fighting.choosePlay()
        playnum+=1
    jpype.shutdownJVM()
    print("关闭JAVA虚拟机".center(50, "*"))

if __name__ == "__main__":
    Main()




