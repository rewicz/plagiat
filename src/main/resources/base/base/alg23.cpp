    function getRandom(min,max) {
        var myRandom = max+1;
        while (myRandom > max) {
            myRandom = parseInt(Math.random()*(max-min+1) + min);
        }
        return myRandom;
    }