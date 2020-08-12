#include <iostream>

using namespace std;

int main()
{
//prime olup olmadýðýný anlamak için test
int p,i,a,k,s;
int x=1;
bool isprime=true;
bool order;

    cout << "please enter prime number p" << endl;
    cin>>p;

             for(i=2;i<p;i++)
                    {
                       if(p % i == 0)
                              {
                                isprime=false;
                                cout << "p is not prime, please enter another number!" << endl;
                                break;
                              }
                        else continue;


                    }
//buaraya kadar prime testi yaptýk, þimdi prime p den küçük bir a girmesini saðlayacaðýz:
if (isprime==true)
{
 cout << "p is  prime, you can start to calculation now!" << endl;
 cout << "please enter positive number a which is less than p!" << endl;
                          cin>>a;
if (a<p){
//buraya kadar a nýn küçük olup olmamasýný test ettik,
// þimdi verilen prime p ile oluþturulan multiplication group için a nýn orderý ný bulacaðýz:
                             for (s=1;s<p;s++){

                                          for(k=1;k<=s;k++)
                                          {

                                                     x=a*x;

                                          }//cout<<"x is:"<<x<<endl;
                                                    if(x%p!=1)
                                                    {
                                                       x=1;
                                                       continue;
                                                      //cout << "order of a in set of congruence class mod p is not:" <<s<< endl;

                                                    }
                                                  else  {cout <<"order of a in set of congruence class mod p is :" <<s<< endl;
                                                   break;
                                                    x=1;
                            }



}
}else
cout << "a is not smaller than p, please enter number again!" << endl;
// buraya kadar a nýn sahip olabileceði order deðerlerini inceledik.þimdi en küçük deðerin asýl order olacaðýný söylememiz gerek.

}






    return 0;
}
