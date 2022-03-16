let multiplyAll = array => number => {
    let arrayTwo = []
    for (let i = 0; i < array.length; i++) {
      let add = 0
      add = array[i] * number   
      arrayTwo.push(add)     
    }
      return arrayTwo
  }


 console.log(multiplyAll([1, 2, 3])(2))