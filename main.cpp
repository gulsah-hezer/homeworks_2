#include <iostream>
using namespace std;


int main()
{
int a,b,q,x,lastx,y,lasty,temp,temp1,temp2,temp3;
cout<<"please enter a positive number a"<<endl;
cin>>a;
cout<<"please enter a positive integer b"<<endl;
cin>>b;


 if (b>a){// in here, we switch them.
           temp=a;
           a=b;
           b=temp;
        }
x=0;
y=1;
lastx=1;
lasty=0;
 while(b!=0){
             q=a/b;
             temp1=a%b;
             a=b;
             b=temp1;
             //up to here, we calculated gcd as an a.
             temp2=x;
             x=lastx-q*x;
             lastx=temp2;

             temp3=y;
             y=lasty-q*y;
             lasty=temp3;
            }
cout<<"gcd(a,b)"<<a<<endl;
cout<<"x="<<lastx<<endl;
cout<<"y="<<lasty<<endl;
return 0;

}
