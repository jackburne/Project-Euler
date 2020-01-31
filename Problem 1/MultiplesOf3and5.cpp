#include <iostream>
using namespace std;

// Main Function for finding multiples of 3 and 5
void findMultiples(int sum) {
  // For loop that will iterate over x, adding 1 each loop until
  // it equals 1000
  for (int x = 0; x < 1000; x++) {
    // Checking if x is evenly divisible by 3
    if ((x % 3) == 0) {
      // If it is, then we add it to the sum
      sum += x;
      // Next we check if x is evenly divisible by 5
    } else if ((x % 5) == 0) {
      // If it is, we add it to the sum
      sum += x;
    }
  }

  cout << sum;
}


//Main loop for calling the "Find Multiples" function
int main() {
  // Creating the sum variable that will be used to store our
  // result
  int sum = 0;
  // Calling the findMultiples function and parsing the sum variable
  findMultiples(sum);
  return 0;
}
