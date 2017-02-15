/**
 * @param {number} n
 * @return {boolean}
 */
var canWinNim = function(n) {
    var originalN = n;
    var dict = {
        "0": false,
        "1": true,
        "2": true,
        "3": true
    };
    while (true) {
        if (dict.hasOwnProperty(n.toString())) {
            dict[originalN.toString()] = dict[n.toString()];
            return dict[n.toString()];
        }
        n = n - 4;
    }
};
// Time limit exceeded on above implementation, but it gets the correct answer

/**
 * @param {number} n
 * @return {boolean}
 */
var canWinNim = function(n) {
    return n % 4 !== 0;
};
// Memoization was too complicated for this problem, from reasoning, the only way to lose
// (as long as each player is playing optimally) is to leave the other person with a 
// multiple of 4 stones, which means the only way to lose is to start with a multiple of 4 
// stones. 