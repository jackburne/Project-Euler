#include <iostream>
#include <string>
#include <math.h>
using namespace std;


void findFactor(double numToFactor, double currDivisor, double largestDivisor) {
  // Storing the number we want to factor
  double numFactor = numToFactor;

  // While our current divisor is less than the number we are factoring,
  while (currDivisor <= numToFactor) {

    // We also run a loop that performs a modulo of our number to factor
    // and our current divisor. If it's not 0, we increment the current
    // divisor (We need to use fmod from math.h because "%" isn't declared
    // for doubles)
    while (fmod(currDivisor, numToFactor) != 0) {
      currDivisor += 1;
    }

    // if our current divisor is larger than our currently Largest Divisor,
    if (currDivisor >= largestDivisor) {

      // Then we set the current divisor to BE our largest...
      largestDivisor = currDivisor;
      // and set our new number to factor to be the current factor divided by
      // the current divisor
      numToFactor = numToFactor / currDivisor;
      // We then reset our current divisor to be 2
      currDivisor = 2;
    } else {

      break;
    }

    continue;
  }

  cout << "Largest possible prime for " + to_string(numFactor) + " is: " + to_string(largestDivisor);
}


int main() {
  double numToFactor = 600851475143;
  double currDivisor = 2;
  double largestDivisor = 0;

  findFactor(numToFactor, currDivisor, largestDivisor);
}
