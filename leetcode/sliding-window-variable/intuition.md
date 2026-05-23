## My intuition

Given a function:
```python
def func(nums: list[int]):
    start = 0
    max_ = 0 # max or min of whatever you wish to find
    occurences = {} # or another data structure

    for end in range(len(nums)):
        occurences[nums[end]] = occurences.get(nums[end], 0) + 1

        while occurences is not valid: # if the invariant is false, or when the window is invalid, shrink it until it is valid
            occurences[nums[start]] -= 1
            if occurences[nums[start]] == 0:
                occurences.pop(nums[start]) # in more general terms, remove nums[start] from occurences
            start += 1
        
        # Here, the invariant must be valid. Hence take the max or min of whatever I want to find. The key intuition is the invariant is ALWAYS true here!
        max_ = max(max_, end - start + 1)
    
    return max_

```
## Idea

Keep growing the window until the invariant becomes false. When it becomes false, shrink the window until it becomes valid


## Definitions

Invariant - a condition that is ALWAYS true at a specific point in code, no matter the iteration or input. It's a fixed truth