import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import matplotlib.cm
from vectors import *
from math import *

def normal(face):
    return(cross(subtract(face[1], face[0]), subtract(face[2], face[0])))


blues = matplotlib.cm.get_cmap('Blues')

def shade(face,color_map=blues,light=(1,2,3)):
    return color_map(1 - dot(unit(normal(face)), unit(light)))

light = (1,2,3)
faces = [
    [(1,0,0), (0,1,0), (0,0,1)],
    [(1,0,0), (0,0,-1), (0,1,0)],
    [(1,0,0), (0,0,1), (0,-1,0)],
    [(1,0,0), (0,-1,0), (0,0,-1)],
    [(-1,0,0), (0,0,1), (0,1,0)],
    [(-1,0,0), (0,1,0), (0,0,-1)],
    [(-1,0,0), (0,-1,0), (0,0,1)],
    [(-1,0,0), (0,0,-1), (0,-1,0)],
]

pygame.init() # 启动pygame
display = (400,400)
window = pygame.display.set_mode(display,DOUBLEBUF|OPENGL) 
# 要求PyGame在400像素×400像素的窗口中显示我们的图形
# 让PyGame知道我们的图形使用的是OpenGL，并声明我们想使用名为double-buffering的内置优化，它对我们理解目标来说并不重要


gluPerspective(45, 1, 0.1, 50.0)    # 描述我们在场景中的视角，其中视线角度为45°，纵横比为1。这意味着垂直单位和水平单位会显示为相同的大小。为了优化性能，通过0.1和50.0这两个数对z坐标的渲染进行限制：距离观察者50.0单位以上或0.1单位以下的对象均不显示。
glTranslatef(0.0,0.0, -5)   # 表示我们将在从原点沿z轴向上5个单位处来观察场景，这意味着场景将沿向量(0, 0, -5)向下移动
glEnable(GL_CULL_FACE)  # 会开启一个OpenGL选项，自动隐藏背对观察者的多边形
glEnable(GL_DEPTH_TEST)     # 能够确保渲染离我们最近的多边形
glCullFace(GL_BACK)     # 启用一个OpenGL选项，自动隐藏面向我们但位于其他多边形之后的多边形

degrees_per_second = 360./5
degrees_per_millisecond = degrees_per_second / 1000


clock = pygame.time.Clock()    # 初始化时钟，测量pygame的时间进度  
while True:
    milliseconds = clock.tick()
    glRotatef(milliseconds * degrees_per_millisecond, 1,1,1)
    for event in pygame.event.get():     
        if event.type == pygame.QUIT:   # 在每次迭代中，检查PyGame接收的事件并在用户关闭窗口时退出
            pygame.quit()
            quit()

    clock.tick()    #  指示时钟已经花费的时间
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glBegin(GL_TRIANGLES)   # 告诉OpenGL我们将要绘制三角形  
    for face in faces:
        color = shade(face,blues,light)
        for vertex in face:
            glColor3fv((color[0],
                        color[1],
                        color[2]))   #   根据阴影设置每个面（三角形）顶点的颜色
            glVertex3fv(vertex)    #  指定当前三角形的下一个顶点
    glEnd()
    pygame.display.flip()   # 向PyGame指示动画的最新帧已经准备就绪，可以显示
   