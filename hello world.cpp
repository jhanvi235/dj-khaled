#include <iostream>
using namespace std;

class chef
{
    public:
  void dish()
  { 
    cout<<" pasta"<<endl;
  }
};
class italian_chef:public chef
public:
{
    void dish ()
{
    cout<<"Pizza"<< endl;
}

};
int main ()
{
   italian_chef ic1
   
   ic1.dish()
    
    return 0;
}
