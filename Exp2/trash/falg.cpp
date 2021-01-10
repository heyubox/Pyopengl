/*
author：fish1996
date:2016/03/09
*/
 
#define GLUT_DISABLE_ATEXIT_HACK  
#include<math.h>  
#include<stdio.h>  
#include<gl/glut.h>  
const GLfloat PI = 3.1415926536f;//定义PI  
 
 
//(cx,cy)为五角星中心坐标，（mx,my)为其中一顶点坐标  
void drawStar(GLfloat cx, GLfloat cy, GLfloat mx, GLfloat my)
{
    int i, j;
 
    GLfloat length = sqrt((mx - cx)*(mx - cx) + (my - cy)*(my - cy));//计算外点极坐标半径  
    const GLfloat cos1 = cos(PI*0.4), sin1 = sin(PI*0.4);//计算得到常量 cos72°，sin72°的值  
    GLfloat cos2 = (mx - cx) / length; //计算得到初始点极坐标的cos，sin值  
    GLfloat sin2 = (my - cy) / length;
    const GLfloat cos3 = cos(PI*0.2), sin3 = sin(PI*0.2);//计算得到常量 cos36°，sin36°的值  
    GLfloat length2 = length*cos1/cos3;//计算内点极坐标半径  
    GLfloat point[10][2];//定义存储坐标信息的数组  
    GLfloat tmp_cos, tmp_sin;
 
    point[0][0] = mx, point[0][1] = my;
 
    //计算五个外点的坐标点，存入偶数下标  
    for (i = 1; i < 5; i++) {
        //利用极坐标旋转公式计算新坐标  
        tmp_cos = cos1*cos2 - sin1*sin2;
        tmp_sin = sin1*cos2 + cos1*sin2;
        point[2 * i][0] = cx + length*tmp_cos;
        point[2 * i][1] = cy + length*tmp_sin;
        cos2 = tmp_cos;
        sin2 = tmp_sin;
    }
 
    cos2 = (mx - cx) / length;
    sin2 = (my - cy) / length;
 
    //计算五个内点的坐标点，存入奇数下标  
    for (i = 0; i < 5; i++) {
        //利用极坐标旋转公式计算新坐标  
        if (i == 0) {
            tmp_cos = cos2*cos3 - sin2*sin3;
            tmp_sin = sin2*cos3 + cos2*sin3;
        }
        else {
            tmp_cos = cos1*cos2 - sin1*sin2;
            tmp_sin = sin1*cos2 + cos1*sin2;
        }
        point[i * 2 + 1][0] = cx + length2*tmp_cos;
        point[i * 2 + 1][1] = cy + length2*tmp_sin;
        cos2 = tmp_cos;
        sin2 = tmp_sin;
    }
 
    //设置黄色  
    glColor3f(1, 1, 0);
 
    //绘制五个三角形  
    glBegin(GL_TRIANGLES);
    for (i = 0; i < 5; i++) {
        for (j = 1; j <= 3; j++) {
            glVertex2fv(point[(2 * i + j) % 10]);
        }
    }
    glEnd();
 
    //绘制五边形  
    glBegin(GL_POLYGON);
    for (i = 0; i < 5; i++) {
        glVertex2fv(point[2 * i + 1]);
    }
    glEnd();
}
 
void display()
{
    glClear(GL_COLOR_BUFFER_BIT);//清除颜色缓存  
    //设置红色  
    glColor3f(1, 0, 0);
 
    //绘制红旗  
    glBegin(GL_QUADS);
    glVertex2f(-0.9, 0.6);
    glVertex2f(0.9, 0.6);
    glVertex2f(0.9, -0.6);
    glVertex2f(-0.9, -0.6);
    glEnd();
 
    //绘制星星  
    drawStar(-0.60, 0.30, -0.78, 0.36);
    drawStar(-0.30, 0.48, -0.24, 0.48);
    drawStar(-0.18, 0.36, -0.24, 0.36);
    drawStar(-0.18, 0.18, -0.18, 0.24);
    drawStar(-0.30, 0.06, -0.24, 0.06);
 
    glutSwapBuffers();//交换缓冲区  
}
 
int main(int argc, char *argv[])
{
    glutInit(&argc, argv);//对glut的初始化  
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE);//初始化显示模式:RGB颜色模型，双缓冲  
    glutInitWindowPosition(10, 10);//设置窗口位置  
    glutInitWindowSize(400, 400);//设置窗口大小  
    glutCreateWindow("五星红旗");//设置窗口标题  
    glutDisplayFunc(display);//注册绘制回调函数  
    glutMainLoop();// glut事件处理循环  
    return 0;
}
 