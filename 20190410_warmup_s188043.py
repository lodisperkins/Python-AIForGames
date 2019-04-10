'''Answer for problem'''
def validate(func, output):
    if func[0](func[1])== output:
        return True
    else:
        return False
'''Tests for function'''
def add(nums):
    return nums[0]+nums[1]
test_true =validate((add,(1,2)),3)
test_false=validate((add,(1,2)),4)
'''This should be true'''
print (test_true)
'''This should be false'''
print (test_false)