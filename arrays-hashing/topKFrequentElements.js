/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
 var topKFrequent = function(nums, k) {
    // create result array;
    let result = [];
    // create dictionary to hold integers and their frequency as key:value pairs
    let numCount = {};
    // loop through nums array
    for (const num of nums) {
      // check if num exists as key in numCount, if yes increment, if no create it with value of 1
      numCount[num] ? numCount[num]++ : numCount[num] = 1;
    }
    

};