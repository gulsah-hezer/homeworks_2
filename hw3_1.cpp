#include <iostream>

using namespace std;

int main()
{
//prime olup olmad���n� anlamak i�in test
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
//buaraya kadar prime testi yapt�k, �imdi prime p den k���k bir a girmesini sa�layaca��z:
if (isprime==true)
{
 cout << "p is  prime, you can start to calculation now!" << endl;
 cout << "please enter positive number a which is less than p!" << endl;
                          cin>>a;
if (a<p){
//buraya kadar a n�n k���k olup olmamas�n� test ettik,
// �imdi verilen prime p ile olu�turulan multiplication group i�in a n�n order� n� bulaca��z:
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
// buraya kadar a n�n sahip olabilece�i order de�erlerini inceledik.�imdi en k���k de�erin as�l order olaca��n� s�ylememiz gerek.

}






    return 0;
}
