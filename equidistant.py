# nums = range(1, 10)
nums = [11, 12, 13, 21, 22, 23, 31, 32, 33]
equi_digits = []


for a in nums:
    if nums[-2] == a:
        continue
    for b in nums[nums.index(a) + 1 :]:
        if nums[-1] == b:
            continue
        for c in nums[nums.index(b) + 1 :]:
            if (b - a) == (c - b):
                equi_digits.append(f"{a}-{b}-{c}")
                

print(len(equi_digits))                
print(equi_digits)