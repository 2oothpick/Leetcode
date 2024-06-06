function removeDuplicates(nums) {
    pset = new Set(nums)
    nums.splice(0, nums.length)
    pset.forEach((value) => {
        nums.push(value)
    })
    return nums.length
}
