/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
    let ans = []
    nums.forEach((value, index) => {
        nums.slice(index + 1).forEach((value1, index1) => {
            if (value + value1 == target) {
                ans.push(index, nums.indexOf(value1, index + 1))
            }
        })
    })
    return ans
};
