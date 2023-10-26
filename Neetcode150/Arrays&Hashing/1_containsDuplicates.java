// Given an array , find if it contains duplicates or not. return true if it contails duplicates else false.
//constrains : 1<= arr.len <= 10^5
//               -10^9 <num <= 10^9

// Approach 1: (naive linear search):
//   with 2 loops to check , i.e we will get n(n-1)/2 pairs of integers to check , so time complexity O(n2);
//   Time limit exceeded, Generally TLE occurs if an algorithm is O(n2), but IDE can handle n upto 10^4. TLE occurs when >= 10^5.
    
// Approach2: use sorting technique, will be done by time complexity O(n log n) , i.e O(nlogn) --> sorting and iterating through array O(n).

// Approach3: Hashing technique  (either by using Bineary search tree or Hash table)          BST - search() --> O(log n)       HashTable ==> search() --> O(1)
//                                                                                                  insert() --> O(log n)                     insert() --> O(1)

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>(nums.length);
        for (int n: nums) {
            if ( set.contains(n)) {
                return true;
            }
            set.add(n);        
        }
    return false;    
    }
}

//  Note: if n is not very large then approach2 runs faster than approach3. WHY? Hash table has some overhead in maintaining property.


    
