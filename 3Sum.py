res = []
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        x = nums[i]+nums[j]
        for k in range(j+1,len(nums)):
            if nums[k] == 0-x:
                res.append([nums[i],nums[j],nums[k]])
return res