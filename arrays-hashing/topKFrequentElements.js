/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
 var topKFrequent = function(nums, k) {
    // create result array
    let result = [];
    // create helper array
    let helper = [];
    // loop and fill with unique empty arrays
    for (let i = 0; i < nums.length + 1; i++) {
      helper[i] = [];
    }
    // create dictionary to hold integers and their frequency as key:value pairs
    let numCount = {};
    // loop through nums array
    for (const num of nums) {
      // check if num exists as key in numCount, if yes increment, if no create it with value of 1
      numCount[num] ? numCount[num]++ : numCount[num] = 1;
    }
    // loop through dictionary items
    for (const [key, val] of Object.entries(numCount)) {
      // push num to value(array) of helper array at index [count]
      helper[val].push(key);
    }
};