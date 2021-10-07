def insertionsort(nums: list):
    counter = 0
    for idx in range(1, len(nums)):
        shift = 1
        counter += 1
        while shift <= idx and nums[idx - shift] > nums[idx - shift + 1]:
            nums[idx - shift], nums[idx - shift +
                                    1] = nums[idx - shift + 1], nums[idx - shift]
            shift += 1
            counter += 1

    return counter


def selectionsort(nums: list):
    counter = 0
    for start_idx, _ in enumerate(nums):
        min_elem_idx = start_idx
        for idx in range(start_idx + 1, len(nums)):
            counter += 1
            if nums[idx] < nums[min_elem_idx]:
                min_elem_idx = idx

        nums[start_idx], nums[min_elem_idx] = nums[min_elem_idx], nums[start_idx]

    return counter


def mergesort(nums: list):
    counter = 0
    if len(nums) > 1:
        mid = len(nums) // 2

        nums_left = nums[:mid]
        nums_right = nums[mid:]

        counter = mergesort(nums_left) + mergesort(nums_right)

        idx_left = idx_right = idx = 0

        while idx_left < len(nums_left) and idx_right < len(nums_right):
            counter += 1
            if nums_left[idx_left] < nums_right[idx_right]:
                nums[idx] = nums_left[idx_left]
                idx_left += 1
            else:
                nums[idx] = nums_right[idx_right]
                idx_right += 1
            idx += 1

        while idx_left < len(nums_left):
            nums[idx] = nums_left[idx_left]
            idx_left += 1
            idx += 1

        while idx_right < len(nums_right):
            nums[idx] = nums_right[idx_right]
            idx_right += 1
            idx += 1

    return counter


def shellsort(nums: list):
    if len(nums) <= 1:
        return 0

    counter = 0
    gap = 1
    while gap < len(nums) / 3:
        gap = 3 * gap + 1

    while gap >= 1:
        for idx_1 in range(gap, len(nums)):
            for idx_2 in range(idx_1, gap - 1, -gap):
                counter += 1
                if nums[idx_2] >= nums[idx_2 - gap]:
                    break

                nums[idx_2], nums[idx_2 -
                                  gap] = nums[idx_2 - gap], nums[idx_2]
        gap //= 3
    return counter
