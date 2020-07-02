import pygame


class Background(object):
    def __init__(self):
        self.__backgroundSize = 10

    def get_backgroundSize(self):
        return self.__backgroundSize

    def set_backgroundSize(self, newSize):
        self.__backgroundSize = newSize


def changeSize():
    print('进入函数体')
    background.set_backgroundSize(30)
    print('执行完函数体')
    return background.get_backgroundSize()

class Test(object):
    def __init__(self, score):
        self.score = score
        self.score += 1

    def add(self):
        self.score += 1

if __name__ == "__main__":
    background = Background()
    print(changeSize())
    score = 0
    isinstance1 = Test(score)
    isinstance2 = Test(score)
    print(score)
    print(isinstance1.score)
    print(isinstance2.score)
    rect = pygame.Rect(0,20,20,30)
    print(list(rect))
# 经过检验得知上面这一小部分中的background实例属于全局变量因此可以在函数中访问,而且还会变量提前

