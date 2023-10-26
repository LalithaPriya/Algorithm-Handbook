// Given an array and integer k, return true;   if nums[i] == nums[j] and abs(i-j) <= k 
//                                      fasle;  otherwise
// similar to above problem

// Approach1: by iterating through array 2 times 
// i.e i = 0 to n
//     j = max(i-k,0) j<i
//  Time Complexity is O(n min(n,k))

// Approach2: Using BST for sliding window          //may use treeset or treemap in java
//           Time Complexity: O(n min(n,k))

// Approach3: with HashTable; TC -  O(n)
// --> loop through array,
//   --> search current element in the hash
//   --> if found, return true
//   --> put current in hashtable 
//   -->if size exceeds k, then remove first or oldest element

class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i< nums.length; i++) {
            if (set.contains(nums[i])) {
                return true;
            }
            set.add(nums[i]);
            if (set.size() > k) {
                set.remove(nums[i-k]);
            }
        }
        return false;
    }
}
