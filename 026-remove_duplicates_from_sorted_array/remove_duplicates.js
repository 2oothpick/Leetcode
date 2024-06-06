function removeDuplicates(nums) {
    nums.filter((value, index) => {
        // index of a duplicate element
        const replIdx = nums.indexOf(value, index + 1)
        const revReplIdx = nums.lastIndexOf(value, index - 1)
        if (replIdx !== -1) {
            nums.splice(replIdx, 1)
        } else if(index != 0 && revReplIdx !== -1) {
            nums.splice(revReplIdx, 1)
        }
        return nums
    })
    return nums.length

}

nums = [1,1,1,1]
console.log(removeDuplicates(nums))
console.log(nums)
/* let index = 0
console.log(nums.indexOf(0, ))
 */