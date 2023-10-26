// same as contains_duplicatesII but with extra condition
// 1. i!=j
// 2. abs(i-j) <= indexDiff
// 3. abs(nums[i]-nums[j]) <= valueDiff

// Approach1:
// can follow linear search but will get TLE 
//   for i in 0 to n:
//     for j in max(i-k,0) to < i
//       if abs(nums[i]-nums[j]) <= valueDiff
//         return true

// Approach 2: using BST (as BST takes O(logn) time to search or insert element)
//   If we use another datastructure, we need to sort the data structure to satisfy the condition 3. 

class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int indexDiff, int valueDiff) {
        
        TreeSet<Long> set = new TreeSet<>();

        for ( int  i = 0; i< nums.length; i++) {
            Long floor = set.floor( 1L * nums[i]);
            if ( floor!= null && nums[i] - floor <= valueDiff) {
                return true;
            }
            Long ceil = set.ceiling(1L * nums[i]);
            if ( ceil!= null && ceil - nums[i] <= valueDiff) {
                return true;
            }
            set.add(1L * nums[i]);
            if (set.size() > indexDiff) {
                set.remove(1L * (nums[i-indexDiff]));
            }
        }
    return false;
    }

}
  
