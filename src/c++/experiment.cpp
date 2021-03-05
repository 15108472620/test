#include <iostream>
#include <cmath>
using namespace std;
class quadrangle
{
private:
    int x,x1,x2,y1,y2;
    int length1,length2,length3,length4;
public:
    quadrangle(){
        this->x=Rand();
        this->x1=Rand();
        this->x2=Rand();
        while(this->x2==this->x1){
            this->x2=Rand();
        };
        this->y2=Rand();
        this->y1=0;
        if(this->x1 > this->x2){
            Line(0,0,this->x2,this->y2);
            Line(this->x2,this->y2,this->x1,this->y1);
            Line(this->x1,this->y1,this->x,0);
            Line(0,0,this->x,0);
            this->length1=this->x;
            this->length2=sqrt(this->x2^2+this->y2^2);
            this->length3=this->x1-this->x2;
            this->length4=sqrt((this->x-this->x1)^2+this->y2^2);
        }
        else if {
            Line(0,0,this->x1,this->y1);
            Line(this->x1,this->y1,this->x2,this->y2);
            Line(this->x2,this->y2,this->x,0);
            Line(0,0,this->x,0);
            this->length1=this->x;
            this->length2=sqrt(this->x1^2+this->y2^2);
            this->length3=this->x2-this->x1;
            this->length4=sqrt((this->x-this->x2)^2+this->y2^2);
        }
    }
}
int Rand(){
    Random ro = new Random();
    int iResult;
    int iUp=10;
    int iDown=1;
    iResult=ro.Next(iDown,iUp);
    return iResult;
}
int Line(int x1,int y1,int x2,int y2){
    HDC hDC;
    MoveToEx(hDC,x1,y1,NULL);
    LineTo(hDC,x2,y2);
}
void quadrangle(){
    int x=Rand();
    int x1=Rand();
    int x2=Rand();
    while(x2==x1){
        x2=Rand();
    };
    int y2=Rand();
    int y1=0;
    if(x1>x2){
        Line(0,0,x2,y2);
        Line(x2,y2,x1,y1);
        Line(x1,y1,x,0);
        Line(0,0,x,0);
    }
    else {
        Line(0,0,x1,y1);
        Line(x1,y1,x2,y2);
        Line(x2,y2,x,0);
        Line(0,0,x,0);
    }
}
ostream& operator <<(ostream& os, const quadrangle& a)
{
    return os << a << std::endl;
}
int main(){
    int result=1;
    while(result==1){
        quadrangle quad;
        cout << "下底边："<< quad.length1 << endl;
        cout << "左侧边："<< quad.length2 << endl;
        cout << "上底边："<< quad.length3 << endl;
        cout << "右侧边："<< quad.length4 << endl;
        mianji=(quad.length1+quad.length3)*quad.y2/2;
        cout << "请输入结果";
        cin >> in;
        if(mianji==in)
            cout << "计算结果正确" << endl;
        else 
            cout << "计算结果错误" << endl;
        cout << "请输入是否继续，1：继续，0：停止";
        cin >> result;
    }
    return 0;
}