// Finding Multiples of 3 and 5
function findMultis (sum) {
  // Defining the iterator "i" as specifically a integer
  let i = 0
  // using "i" to loop to 1000, iterating by 1 each time
  for (i = 0; i < 1000; i++) {
    // If "i" modulo 3 leaves a remainder of 0,
    // it is evenly divisible
    if ((i % 3) === 0) {
      // we add the value of "i" to the total sum and
      // continue out of the IF statement
      sum += i
      continue
    // Else, we see if "i" is evenly divisble by 5, again,
    // using the modulo function
    } else if ((i % 5) === 0) {
      // If it is, we add the value of "i" to the total
      // sum number
      sum += i
      continue
    }
  }
  // Once the FOR loop is completed, we print the value of "sum"
  // to the console
  console.log(sum.toString())
}

function main () {
  // Creating the "sum" variable and forcing it to be an integer
  let sum = 0
  // Calling "findMultis", and parsing the value of "sum" to it
  findMultis(sum)
}

main()
