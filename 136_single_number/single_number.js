/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function (nums) {
    let answer = 0
    for (item of nums) {
        answer ^= item
    }
    return answer
};