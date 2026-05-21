class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        #creating an Hashtable and storing the prefixes of arr1
        my_pref=set()
        for num in arr1:
            while num>0:
                my_pref.add(num)
                num//=10
#let the maximum lenght of prefix be zero
        max_len=0
#comparing with arr2
        for num in arr2:
# first finding the length of the numbers
            curr_len=0 
            temp=num
            while temp>0:
                curr_len+=1
                temp//=10
#Now check the prefixes
            while num>0:
                if num in my_pref:
                    max_len=max(max_len,curr_len)
                    break 
                num//=10 # Chop off the last digit
                curr_len-=1 # The prefix is now 1 digit shorter
        return max_len




                