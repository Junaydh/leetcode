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

    // create dictionary to hold integers and their frequency as key:value pairs
    let numCount = {};

    // loop through nums array
    for (const num of nums) {
      // check if num exists as key in numCount, if true increment, if false create it with value of 1
      numCount[num] ? numCount[num]++ : numCount[num] = 1;
    }

    // populate helper array with numcount entries
    helper = [...numCount.entries()];

    // sort helper array by frequency in descending order
    helper.sort((a, b) => b[1] - a[1]);

    // loop through helper array
    for (let i = 0; i < k; i++) {
      // push integer value into results array
      result.push(helper[i][0]);
    }
    // return result array
    return result;
};