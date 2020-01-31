#include <iostream>
using namespace std;


void getFibNumbers(int sum) {
  int a = 1;
  int b = 1;
  int c = a + b;

  while (sum <= 4000000){
    if ((c % 2) == 0) {
      sum += c;
    }
    a = b;
    b = c;
    c = a + b;
  }
  cout << sum;
}


int main() {
  int sum = 0;
  getFibNumbers(sum);
}
