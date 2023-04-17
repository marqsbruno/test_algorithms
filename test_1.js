/* Create an algorithm that runs through a one-dimensional array containing letters and numbers: [ “a”, 10, “b”, “hola”, 122, 15]
Get an array containing just the letters
Get an array containing just the numbers
Get the highest number from the array above */

const array = ["a", 10, "b", "hola", 122, 15, 664]

//a
function filterLetters(array){
  let newArray_a = []
  for(let i=0; i <= array.length; i++) { 
    if ( typeof array[i] === "string" && array[i].length < 2 ) {
      newArray_a.push(array[i])
      }
  }
  return newArray_a
}

//b

function filterNumbers(array) {
  let newArray_b = []
  for(let i=0; i <= array.length; i++) { 
    if ( typeof array[i] === "number" ) {
      newArray_b.push(array[i])
    }
  }
  return newArray_b
}

//c

function filterMaxNumber(array) {
  // reutilizo a função de filtrar por números
  const arrayNumbers = filterNumbers(array)

  let maxNumber = 0
  for(let i=0; i <= array.length; i++) { 
	  if(arrayNumbers[i] > maxNumber) {
      maxNumber = arrayNumbers[i]
    }
  }
  return maxNumber
}

console.log('a:', filterLetters(array))
console.log('b:', filterNumbers(array))
console.log('c:', filterMaxNumber(array))