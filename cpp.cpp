#include <iostream>
using namespace std;

int main(int argc, char const *argv[]) {
  int n;
  cin>>n;
  int x=0;
  int y=1;
  int ans=0;
  while(n--){
    if(ans==0){
      ans=y;
      cout<<ans<<" ";
    }
    else{
    ans=x+y;
    cout<<ans<<" ";
    x=y;
    y=ans;
    }
  }
    cout<<endl;
        return 0;
}
