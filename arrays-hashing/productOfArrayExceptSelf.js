/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var productExceptSelf = function(nums) {
    // create answer array
    let answer = []
    // create variable to hold product
    let product = 1;
    // outside loop
    for (let i = 0; i < nums.length; i++) {
      // loop through nums array
      for (let k = 0; k < nums.length; k++) {
        // check if count is same as current itteration var
        if (i === k) {
          // if so, continue to next iteration
          continue;
        }
        // if not, calculate product
        product  *= nums[k];
      }
      // push final product to answer array
      answer.push(product);
      // reset product value
      product = 1;
    }
    // return answer array
    return answer;
};