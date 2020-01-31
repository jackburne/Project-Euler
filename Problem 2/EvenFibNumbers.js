
function main () {
  let sum = 0
  getFibNumbers(sum)
}

function getFibNumbers (sum) {
  let a = 1
  let b = 1
  let c = a + b

  while (sum <= 4000000) {
    if ((c % 2) === 0) {
      sum += c
    }
    a = b
    b = c
    c = a + b
  }

  console.log(sum.toString())
}

main()
