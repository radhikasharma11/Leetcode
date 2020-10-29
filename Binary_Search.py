# iterative Approach
class Solution:
    def iter_binsearch(self, nums, target):
        low,high = 0, len(nums)-1
        mid = 0

        while low <= high:
            mid = (high+low)//2

            if nums[mid]<target:
                low = mid+1
            elif nums[mid]>target:
                high = mid-1
            else:
                return mid
        return -1

    def recur_binsearch(self, nums, low, high, target):
        if high >= low:
            mid = (high+low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return self.recur_binsearch(nums, mid+1, high, target)
            else:
                return self.recur_binsearch(nums, low, mid-1, target)
        else:
            return -1


s = Solution()
nums = [-1,0,3,5,9,12]
target = 9
low = 0
high = len(nums)-1
while True:
    inp = input("Choose 1 or 2: ")
    if inp == '1':
        result_iter = s.iter_binsearch(nums,target)
        print("You chose Iterative methode for BinSearch. Result generated from iteration: %s " %result_iter)
        break
    elif inp == '2':
        result_recur = s.recur_binsearch(nums, low, high, target)
        print("You chose Recursive method for BinSearch. Result generated from recursion: %s " %result_recur)
        break
    else:
        print("Wrong choice entered")

