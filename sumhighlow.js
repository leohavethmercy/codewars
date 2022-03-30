//Sum without highest and lowest number

// Task
// Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

// The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

// Mind the input validation.

// Example
// { 6, 2, 1, 8, 10 } => 16
// { 1, 1, 11, 2, 3 } => 6

function sumArray(array) {
    let sum = 0;
    array.pop(Math.min(...array))
    array.pop(Math.max(...array))
    for (const num of array) {
        sum += num
        }
    return sum
    }

console.log(sumArray([ -6, 20, -1, 10, -12 ]))
    //  sumArray([ -6, 20, -1, 10, -12 ])  , 3 );

console.log(sumArray([ -6, -20, -1, -10, -12 ]))
    //  sumArray([ -6, -20, -1, -10, -12 ]), -28 );

console.log(sumArray([ 0, 1, 6, 10, 10 ]))
    //  sumArray([ 0, 1, 6, 10, 10 ])      , 17 );

console.log(sumArray([ 6, 2, 1, 8, 10 ]))
    //  sumArray([ 6, 2, 1, 8, 10 ])       , 16 );

console.log('--------')
console.log(sumArray([ 3, 5 ]))
console.log(sumArray([ 3 ]))
console.log(sumArray([ ]))
console.log(sumArray(null))
