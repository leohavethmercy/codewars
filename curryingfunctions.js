// let multiplyAll = array => number => {
//     let arrayTwo = []
//     for (let i = 0; i < array.length; i++) { 
//       arrayTwo.push(array[i] * number )     
//     }
//     return arrayTwo
// }


//  console.log(multiplyAll([1, 2, 3])(2))

 // After looking at solutions realized that .map()
 // is the cleaner, efficient solution

 let multiplyAll = (array) => (numbers) => {
     return array.map(x => x * numbers)
 }

 console.log(multiplyAll([1, 2, 3])(2))
