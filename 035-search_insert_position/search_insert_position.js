var searchInsert = function (nums, target) {
    let comparr = []
    for (let i = 1; i < 10; i++) {
        comparr.push(i)
    }
    /* nums.forEach((value, index) => {
      comparr[index] = nums[index]
    }) */

    /* const pset = new Set(comparr)
    comparr.splice(0, comparr.length)
    pset.forEach((value)=>comparr.push(value))
    comparr.sort(function(a, b){return a - b}) */
    comparr.splice(0, nums.at(-1))
    let temp = comparr
    comparr = [...nums, ...temp]
    if (target === 0) {
        return 0
    }
    if (!comparr.includes(target)) {
        for (i = 0; i <= comparr.length; i++) {
            if (target > comparr[i] && target < comparr[i + 1]) {
                return (i + 1)
            }
        }
    } else {
        return 0
    }
    return comparr.indexOf(target)
};

console.log(searchInsert([1, 3, 5, 6], 7))
/* let comparr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
let nums = [1, 3, 5, 6]
comparr.splice(0, nums.at(-1))
//console.log(comparr)
let temp = comparr
comparr = [...nums, ...temp]
console.log(comparr) */
