class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        post = [1]
        counter = -1

        for i in range(len(nums) - 1):
            pre.append(nums[i]*pre[i])

            post.append(nums[counter]*post[i])
            print("nums ", nums[counter])
            print("post ", post[i])
            counter -= 1
        flipped_list = post[::-1]
        #print(flipped_list)
        #print(pre)

        ans = []
        for i in range(len(pre)):
            ans.append(pre[i] * flipped_list[i])
        return ans
        