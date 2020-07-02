# Flappy_bird_Game
## 根据教程《Python入门到精通》游戏编程，编写Flappy_Bird
### 简介
1. 这个程序是在教程上看着很有意思的一个小东西，代码量不大，游戏还蛮有意思的，就想着模仿着写一下
2. 整个程序基于的是python生态的pygame库，据说已经很老，过时了（反正对我来说都难，哼，😕）
3. test.py和pygame_test.py可以不用管，那是写代码写到一半我碰到对语法和库的用法不确定的时候写的测试程序，通过Print看一下输出结果

### 难点解析
1. 原本教程上的一些程序结构不是很合理，做了一些微型调整
2. 没有找教材中的推荐素材，自己在爱给网上找了点
3. 由于素材不一样，参数设置上就需要对pygame.Rect(x,y,width,height)的定义有点理解，不能完全照抄参数
4. 值得记住的是所有的surface对象都可以直接得到get_rect或者get_width等，方便定位
5. 需要了解pygame.display.flip()的意义，不能画一次就flip一下画面会不停闪烁的
6. 与教材不同，我加了点花样：
    * 管道数量增多了点
    * 上管道和下管道的间距会随机变化
    * 小鸟速度会递增
    * 可以重新开始游戏
    
### 总结与展望
1. 这个小游戏其实对我个人成长没有太大帮助，（倒是学到了Python跟C一样全局变量所有函数都能用，定义在前的函数才能用；想想也是，毕竟解释器一行一行下来的），不过对我学习计算机写代码
   的兴趣方面很有帮助
2. 解决了一个sRGB瞎吉儿警告的问题，原来是png格式的图片颜色检查变严格了,可以通过magick（一个软件的命令行指令）重新载入输出一下就行了
3. 按理来讲应该做一个开始界面和难度选择界面啥的，那难度不同对源码肯定又影响，我代码写的有点死不是很符合开闭原则（功能添加开放，修改代码关闭），肯定很麻烦，后期要多注意
4. 下一个程序，打算用Flasky框架写个小web程序，还是基于教程
5. 讲真，不管怎么说，写代码还是一个：理解语法->读代码->抄代码->改代码->写代码 的过程，抄人家的其实不可耻（开源是种值得鼓励的精神嘛）,重点在于有自己的理解，有知识上的增长，
   这也是学习普遍的过程，哪有刚刚看完教材就能各种解题的呀，不都是听老师解析，抄老师的答案和解析，才会自己做吗？
6. 时刻告诫自己：
    * 不要松懈
    * 不要焦虑浮躁
    * 保持心态，锻炼身体
    * 不要对抄教程代码抵触，自己也就是个普通人，端着干嘛（手动狗头🐶）
    * 加油加油😎
