#include <iostream>
#include <algorithm>
using namespace std;

int main(int argc, char const *argv[]) {
int a[5]={1,2,3,4,5};
int k=2;
for(int i=0;i<5;i++){
  cout<<a[(i+k)%5]<<" ";
}
}
