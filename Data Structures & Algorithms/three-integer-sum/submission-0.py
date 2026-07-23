class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final_list = []
        snums = sorted(nums)
        
        # Change 1: Loop through indices so we can place s and e relative to i
        for i_idx in range(len(snums)):
            i = snums[i_idx]
            
            # Change 2: Set 's' to start immediately after the current 'i'
            s = i_idx + 1
            e = len(snums) - 1
            
            # Change 3: Run the pointers until they meet in the middle
            while s < e:
                current_sum = snums[s] + snums[e]
                
                if -i == current_sum:
                    triplet = [i, snums[s], snums[e]] # Already sorted because snums is sorted
                    if triplet not in final_list:
                        final_list.append(triplet)
                    s += 1
                    e -= 1
                elif current_sum < -i:
                    s += 1 # The sum is too small, move the left pointer up
                else:
                    e -= 1 # The sum is too big, move the right pointer down
                    
        return final_list