#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  gl.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-06-15 09:29:02
#  Last Modified:  2018-06-15 09:30:25
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def drawFunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glRotatef(0.1, 5, 5, 0)  #(角度,x,y,z)
    glutWireTeapot(0.5)
    #刷新显示
    glFlush()


#使用glut初始化OpenGL
glutInit()
#显示模式:GLUT_SINGLE无缓冲直接显示|GLUT_RGBA采用RGB(A非alpha)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
#窗口位置及大小-生成
glutInitWindowPosition(0, 0)
glutInitWindowSize(400, 400)
glutCreateWindow(b"first")
#调用函数绘制图像
glutDisplayFunc(drawFunc)
glutIdleFunc(drawFunc)
#主循环
glutMainLoop()
