// Are You Playing Banjo?

// Create a function which answers the question "Are you playing banjo?".
// If your name starts with the letter "R" or lower 
    // case "r", you are playing banjo!

// The function takes a name as its only argument, 
    //and returns one of the following strings:


    function areYouPlayingBanjo(name) {
        // Implement me
        if (name.startsWith('r') || name.startsWith('R')) {
             return `${name} plays the banjo`
        } else {
            return `${name} does not play banjo`
        }
      }

      console.log(areYouPlayingBanjo("Adam"))
    //   "Adam does not play banjo"
      console.log(areYouPlayingBanjo("Paul"))
    //    "Paul does not play banjo");
      console.log(areYouPlayingBanjo("Ringo"))
    //    "Ringo plays banjo");
      console.log(areYouPlayingBanjo("bravo"))
    //    "bravo does not play banjo");
      console.log(areYouPlayingBanjo("rolf"))
    //    "rolf plays banjo");
    