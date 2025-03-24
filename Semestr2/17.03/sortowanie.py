def sort_numbers(nums: list) -> list:
    length = len(nums)
    sorted = False
    while sorted == False:
        sorted = True
        for i in range(length-1):
            if nums[i] > nums[i+1]:
                temp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = temp
                sorted = False
    return nums

liczby = [5,4,3,2,1,0,-1,0,4,2,5,6,2,4,7]

print(sort_numbers(liczby))