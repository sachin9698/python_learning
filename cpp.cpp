#include<iostream>
#include<algorithm>
using namespace std;

int main(int argc, char const *argv[]) {
  int a[10];
  for (int i = 0; i < 10; i++) {
    cin>>a[i];
  }
  sort(a,a+10);
  for (int i = 0; i < 10; i++) {
    cout<<a[i]<<" ";
  }
  cout<<endl;
  return 0;
}
