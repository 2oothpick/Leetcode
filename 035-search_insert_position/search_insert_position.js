var searchInsert = function (nums, target) {
    if (!nums.includes(target)) {
        if (target < 0) {
            return 0
        }
        for (i = 0; i <= nums.length; i++) {
            if (target === 0 && nums.at(0) >= 0) {
                return 0
            }
            if (target > nums[i] && target < nums[i + 1]) {
                return (i + 1)
            } else if (target > (nums[i - 1] || 0) && target < nums[i + 1]) {
                return 0
            } else if (target > nums.at(-1)) {
                return nums.length
            }
        }
    } else if (nums.includes(target)) {
        return nums.indexOf(target)
    } else {
        return 0
    }

};