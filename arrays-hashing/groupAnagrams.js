/**
 * @param {string[]} strs
 * @return {string[][]}
 */
 var groupAnagrams = function(strs) {
  let result = {}; // create result dict
  // loop through each str
  for (const str of strs) {
      // create array of 26 zeroes, one for each letter;
      let charCount = new Array(26).fill(0);
      // for each char of current str find utf-16 charcode and -97 so it maps to its index value in count array.
      for (const char of str) charCount[char.charCodeAt()-97]++;
      // join array so that you can use it as a unique key
      let key = count.join('#');
      // check if unique key exists in dict: if so, push the current str into its array value pair, if not create an array with current str
      res[key] ? res[key].push(str) : res[key] = [str];
  };
  // return array of object values
  return Object.values(result);
};