nums = [10, 5, 2, 6]
k = 100

left = ans = 0
curr = 1

if k == 1:
    print(0)
    quit()

for right in range(len(nums)):
    curr = curr * nums[right]
    while curr >= 100:
        curr = curr / nums[left]
        left += 1
    
    ans += right - left + 1

print(ans)