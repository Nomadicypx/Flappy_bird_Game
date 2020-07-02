import pygame
import time
import sys
import random

size = width, height = 720, 640
pipeLength = 640
pipeWidth = 54


def processImage(image_url):
    image = pygame.image.load(image_url)
    image = pygame.transform.flip(image, True, False)
    image = pygame.transform.smoothscale(image, (width // 10, height // 6))
    return image


class Bird(object):
    def __init__(self):
        self.status = 0
        self.statusImageList = [processImage('bird_normal.png'), processImage('bird_jump.png'),
                                processImage('bird_dead.png')]
        self.statusImage = self.statusImageList[self.status]
        self.birdRect = pygame.Rect(65, 50, 20, 30)
        self.birdX = 65
        self.birdY = 50
        self.jump = False
        self.jumpSpeed = 10
        self.gravity = 1
        self.dead = False
        self.movingSpeed = 5

    def reNew(self):
        self.status = 0
        self.birdRect = pygame.Rect(65, 50, 20, 30)
        self.birdX = 65
        self.birdY = 50
        self.jump = False
        self.jumpSpeed = 10
        self.gravity = 1
        self.dead = False
        self.movingSpeed = 5

    def birdUpadate(self):
        if self.dead:
            self.status = 2
            self.statusImage = self.statusImageList[self.status]
        elif self.jump:
            self.status = 1
            self.statusImage = self.statusImageList[self.status]

        if self.jump:
            self.jumpSpeed -= 1
            if self.jumpSpeed <= 0:
                self.status = 0
                self.statusImage = self.statusImageList[self.status]
            self.birdY = self.birdY - self.jumpSpeed
            # self.birdY = max(self.birdY, 0)
        else:
            self.gravity += 0.2
            self.birdY += self.gravity
        self.birdRect[1] = self.birdY
        self.movingSpeed += random.uniform(0, 0.01)  # TODO： 这里需要设根据难度设置一下


class Pipeline(object):
    def __init__(self, bird, position, score_target):
        self.position = position
        self.score = score_target
        self.wallx = size[0] + self.position
        self.pipeUp = pygame.image.load('pipe.png')
        self.pipeDown = pygame.image.load('pipe.png')
        self.bird = bird
        self.length = self.getLength()  # length[0] 代表上面管道露出来的长度，Length [1] 是下面管道露出来的长度
        self.upy = 0 - pipeLength + self.length[0]
        self.downy = pipeLength - self.length[1]
        self.flag = True  # 是否等待经过小鸟

    def reNew(self):
        self.score.score = 0
        self.flag = True
        self.wallx = size[0] + self.position
        self.length = self.getLength()  # length[0] 代表上面管道露出来的长度，Length [1] 是下面管道露出来的长度
        self.upy = 0 - pipeLength + self.length[0]
        self.downy = pipeLength - self.length[1]

    def updatePipeline(self):
        self.wallx -= self.bird.movingSpeed
        if (self.wallx < self.bird.birdX) and self.flag:
            self.score.score += 1
            self.flag = False  # 这个柱子在刷新前已经不会再计数了
        if self.wallx < -60:
            self.wallx = size[0]
            self.flag = True
            self.length = self.getLength()
            self.upy = 0 - pipeLength + self.length[0]
            self.downy = pipeLength - self.length[1]

    def getLength(self):
        UpLength = random.randrange(10, size[1] // 2 - 30)
        DownLength = size[1] - UpLength - random.randrange(150, 200)
        return UpLength, DownLength


class Score(object):
    def __init__(self, score):
        self.score = score


def createMap(screen, background, bird, pipe_list, font):
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    for i in pipe_list:
        screen.blit(i.pipeUp, (i.wallx, i.upy))
        screen.blit(i.pipeDown, (i.wallx, i.downy))
    screen.blit(bird.statusImage, (bird.birdX, bird.birdY))
    screen.blit(font.render(str(pipe_list[0].score.score), -1, (255, 255, 255)), (size[0] // 2, size[1] // 10))
    bird.birdUpadate()
    for i in pipe_list:
        i.updatePipeline()
    pygame.display.flip()


def checkDead(bird, pipe_instance):
    upPipeDistric = pygame.Rect(pipe_instance.wallx, 0, pipeWidth, pipe_instance.length[0])
    downPipeDistric = pygame.Rect(pipe_instance.wallx, size[1] - pipe_instance.length[1], pipeWidth,
                                  pipeline_instance.length[1])
    if upPipeDistric.colliderect(bird.birdRect) or downPipeDistric.colliderect(bird.birdRect):
        bird.dead = True
        return True
    else:
        return False


def getResult(screen):
    final_text1 = "Game Over"
    final_text2 = "You have got " + str(score.score)
    ft1_font = pygame.font.SysFont(None, 70)
    ft2_font = pygame.font.SysFont(None, 50)
    ft1_surf = ft1_font.render(final_text1, 1, (243, 3, 36))
    ft2_surf = ft2_font.render(final_text2, 1, (253, 177, 6))
    restart = pygame.image.load('restart.png')
    restart = pygame.transform.smoothscale(restart, (40, 40))
    try:
        screen.blit(ft1_surf, (size[0] // 2 - ft1_surf.get_width() // 2, size[1] // 5))
        screen.blit(ft2_surf, (size[0] // 2 - ft2_surf.get_width() // 2, size[1] // 3))
        screen.blit(restart, (size[0] // 2 - restart.get_width() // 2, size[1] // 2 - 50))
    except Exception as e:
        pass
    pygame.display.flip()
    return list(pygame.Rect(size[0] // 2 - restart.get_width() // 2, size[1] // 2 - 50, restart.get_width(),
                            restart.get_height()))


def checkButton(button_position, mouse_postion):
    if (mouse_postion[0] < button_position[0] + button_position[2] and mouse_postion[0] > button_position[0]) and (
            mouse_postion[1] < button_position[1] + button_position[3] and mouse_postion[1] > button_position[1]
    ):
        return True
    else:
        return False


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('flappy bird game')
    background = pygame.image.load('background.jpg')
    background = pygame.transform.smoothscale(background, size)
    clock = pygame.time.Clock()
    bird_instance = Bird()
    score = Score(0)
    pipeline_instance = Pipeline(bird_instance, 0, score)
    pipeline_instance2 = Pipeline(bird_instance, size[0] // 2, score)
    pipeline_instance_list = [pipeline_instance, pipeline_instance2]
    font = pygame.font.SysFont(None, 50)
    while True:
        time.sleep(0.01)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and (not bird_instance.dead):
                bird_instance.jump = True
                bird_instance.gravity = 5
                bird_instance.jumpSpeed = 12
        dead = False
        for pipeline_instance in pipeline_instance_list:
            if checkDead(bird_instance, pipeline_instance):
                dead = True
                break
        if dead:
            button_position = getResult(screen)
            bird_instance.status = 2
            bird_instance.statusImage = bird_instance.statusImageList[bird_instance.status]
            screen.fill((254, 255, 255))
            screen.blit(background, (0, 0))
            for i in pipeline_instance_list:
                screen.blit(i.pipeUp, (i.wallx, i.upy))
                screen.blit(i.pipeDown, (i.wallx, i.downy))
            screen.blit(bird_instance.statusImage, (bird_instance.birdX, bird_instance.birdY))
            screen.blit(font.render(str(pipeline_instance_list[0].score.score), -1, (255, 255, 255)),
                        (size[0] // 2, size[1] // 10))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_postion = event.pos
                    mouse_postion = list(mouse_postion)
                    if checkButton(button_position, mouse_postion):
                        bird_instance.reNew()
                        for pipeline_instance in pipeline_instance_list:
                            pipeline_instance.reNew()

        else:
            createMap(screen, background, bird_instance, pipeline_instance_list, font)

    pygame.quit()
