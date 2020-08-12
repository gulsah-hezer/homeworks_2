#include <iostream>

using namespace std;
gcd(int a,int b)
{
    if (b==0)
        {return a;}
    else
        return gcd(b,a%b);

}
number(int sayi)
{
  return 1;
}

int main()
{
   int d,i,n,k;
   int t=0;
    cout << "please enter positive integer n:" << endl;
    cin>>n;
    for(i=1;i<n;i++)
    {    cout << "n is:" <<n<< endl;
          cout << "i is:" <<i<< endl;
        d=gcd(i,n);
     cout << "gcd is:" <<d<< endl;

       if (d==1)
       {
       k=number(i);
       cout << "k is:" <<k<< endl;
        t=t+k;

       }
      else cout << "they are not coprime" << endl;
    }
     cout <<"order of G=(Zn*,.)=" << "order of set of congruence class mod" <<n<<" is=" <<t<< endl;
    return 0;
}

