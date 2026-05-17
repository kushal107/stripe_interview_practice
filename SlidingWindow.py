nums = [3, 1, 2, 7, 4, 2, 1, 1, 5]
k = 8

left = curr = right = ans = 0

while right < len(nums):
    curr = curr + nums[right]
    while curr > k:
        curr = curr - nums[left]
        left = left + 1
    if ans < right - left + 1:
        ans = right - left + 1
    #ans = max(ans,right-left+1)
    right = right + 1

print(ans)

