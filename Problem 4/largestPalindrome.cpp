#include <iostream>
#include <string>
#include <algorithm>
using namespace std;


void findLargestPal (int numA, int numB, double largestPal) {

  //cout << "Find Largest Pal  RUnning\n";

  cout << "Number A BEFORE: " + to_string(numA) + "\n";
  cout << "Number B BEFORE " + to_string(numB) + "\n";

  // We keeping testing NumA and NumB until they are longer than 3 digits
  while (numA <= 999) {
    while (numB <= 999) {
      // Multipling the NumA and B together to find their product
      int palTest = numA * numB;

      string tempStr = to_string(palTest);

      cout << "\n"
           << "Sum Result: " + to_string(palTest)
           << "\n";

      // Converting the palTest result into a string, and using substr to
      // split the string into two halves. The string will ALWAYS be 6 digits,
      // So we can hard code the numbers in
      string numPartA = to_string(palTest).substr(0, 3);
      cout << "Pal Test After Subtraction: " + to_string(palTest) + "\n";
      string numPartB = to_string(palTest).substr(4, 6);

      cout << "Number Part A: " + numPartA + "\n";
      cout << "Number Part B: " + numPartB + "\n";

      // Reversing the second  half of the split to be compared
      reverse(begin(numPartB), end(numPartB));

      // Comparing the two halves together, to see if they're the same
      if (numPartA == numPartB) {
        // If they are the same, we then see if the sum of the two parts is
        // larger than the currently largest sum, we replace it
        if (palTest > largestPal) {
          cout << "Currently Largest Pal: " + to_string(largestPal) + "\n";
          cout << "Testing Pal: " + to_string(palTest) + "\n";
          largestPal = palTest;
        }
        // Increment NumB
        numB++;
      }
      // Incrementing numA and Resetting numB
      numA++;
      numB = 100;
    }
    // Return the result
    cout << to_string(largestPal) + "\n";
  }
}


int main () {
  int numA = 100;
  int numB = 100;

  findLargestPal(numA, numB, 0);

  cout << "Result!!";


}
