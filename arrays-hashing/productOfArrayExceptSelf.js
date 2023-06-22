/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var productExceptSelf = function(nums) {
    // create answer array
    let answer = []

    // create counter variable
    let count = 0;

    // create variable to hold product
    let product = 0;
    // while length of answer array isnt equal to length of nums array
    while (answer.length !== nums.length) {
      // loop through nums array
      for (let i = 0; i < nums.length; i++) {
        // check if count is same as current itteration var
        if (i === count) {
          // if so, continue to next iteration
          continue;
        }
        // if not, calculate product
        product  *= nums[i];
      }
      // push final product to answer array
      answer.push(product);
      // increment counter
      count++;
      // reset product value
      product = 1;
    }
    // return answer array
    return answer;
};