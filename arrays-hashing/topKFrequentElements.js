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
    // loop backwards through helper array (largest count to smallest count)
    for (let i = helper.length -1; i < 1; i--) {
      // loop through each value in nested array
      for (num of helper[i]) {
        // push that value to results array
        result.push(num);
        // if length of result array = k, return
        if (result.length === k) {
          return result;
        }
      }
    }
};