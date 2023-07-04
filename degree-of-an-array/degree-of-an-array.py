class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        res=[]
        count={}
        start={}
        end={}
        for i,n in enumerate(nums):
            if n not in start:
                start[n]=i
            end[n]=i
            count[n]=1+count.get(n,0)
        maxi=max(count.values())
        for i,j in count.items():
            if j==maxi:
                size=end[i]-start[i]+1
                res.append(size)

        return min(res)