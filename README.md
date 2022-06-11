# Algorithm-Handbook

**FacebookInterviewQnts**:
  1.  Valid Palindrome (should consists alphanumeric, and case insensitive) —> in Java, check with Character.isLetterOrDigit(char) and check the total           Sentence
  2. Find Triplets (a+b+c =0 ) —> Iterate in 2 loops with Hashset to find the 3rd number 
  3. Valid parenthesis —> Stack , push all the open parenthesis , pop by checking the close parenthesis from the stack
  4. Reverse K group Nodes in LL —> Recursive for K nodes in full LL, track the previous and next pointer and swap the nodes
  5. Merge Intervals (start, end)(s1,e1),(s2,e2) (e1>s2 && e2>=s2 —> (s1,e2)) —>  sort the input and push into stack and check if e1>s2 then edit and push
  6. Sum of Two Integers without +,- --> loop num1 till 0 from +ve/-ve, with incrementing/decrementing num2 and decrementing/incrementing num1.
  7. validAnagram --> sort both strings and then check in loop, if it breaks return the result.
  8.Remove Nth Node From End of List --> get total nodes count and iterate again till n-k and remove n-k th node
  9.PlusOne-> travesre list in reverse and then increment last digit and carry till first digit 
  10. mergeKLists 
 
**Linked List:**
 1. DetectLoop in LL--> by iterating with 2 pointers, one with normal and other with two at a time, if these two meets at same node --> loop detected else no loop 
 2. Length of loop in LL --> as in above process, count from the node where the pointers meet the increment the count.
 3. Sum of 2 LLs data which represents number, digits stored in data--> reverse the linkedLists and then perform sum and store carrier in temp, if needed add that        carrier to next node. Finally reverse the resulted LinkedList.
 4. Arrange Consonants and Vowels  in linked list as first vowels and then consonents --> 
                  assign a pointer to the first vowel and then iterate till next one and
                  add a new node with vowel next to the first one and 
                  delete the old node and
                  replace the temp pointer with the latest
5. Find the middle of a given linked list: by using Floyd’s slow and fast pointers technique
6. Remove duplicate element from sortedLL: iterate until node.next is not null, while checking if node value and Node.next.value is same then set the pointer to next node.        
7. Reverse a LL in a group of given size: 
  
BST:
 1. LCA in BST --> by using recursion and check if two nodes either lies in left side or right sides, if not then root will be ancestor
 2. Preorder to Inorder BST --> recursive --> As preorder, with 1st as root and check for element with is greater than root(gt), split in to two arrays as root to gt-1 and gt to n.
 3. Check for Identical BSTs without building the trees --> same as above one(2nd), check if root and next min and max values are same in both inputs. If equal then identical.
 4. Sorted array to BST --> Recursive --> pick the middle value in array and from left side array pick the middle and assign it to left child and do ame with right child.
 5. Convert BST to Min Heap --> by using extra space. Store tree values in array while inorder traversal and assign them back in preorder traversal
 6. Shortest distance between two nodes in BST --> similar approach as in one(1st),so check if 2 nodes lies on either right or left, if not then root is LCA. So then check the distance beetween the nodes to root.
 7. Count pairs from two BSTs whose sum is equal to a given value x --> convert two BSTs into two lists, one from preorder and then one in postorder and then iteratre these two arrays and, if i from arr1 and j from arr2 is equal to k then incremt to both iterator
                       if i+j is less than sum, increase arr1 iterator
                       if i+j is greater than sum, increase arr2 iterator

Bit Algos:

 1. Find Element that appears once where every element occurs thrice
        i. by adding the bits in same positions and then mod by 3 for total value. The result will be the unique number in the array.
        ii. By adding all unique values in array then multiply by 3 and then subtract the sum of total array. Then divide by 2 as we need to find unique val.
 2. Detect if two integers have opposite signs: by using XoR, if 2 numbers have different it will return 1 else 0
 3. Count total set bits in all numbers from 1 to n
 4. A Boolean Array Puzzle , where it is a two element array with min one zero element: make both as zero val element:
        --> a[ a[1] ] = a[ a[0] ]
 5. Multiply a given Integer with 3.5, without %,*,/ : 2*x + x + x/2
        to multiply with 2 instead of *, left shift num by 1 and then for divide by 2, right shift by 1
        (2*x + x + x/2) ==> (x<<1 + x+ x>>1)
 6. Find the two non-repeating elements in an array of repeating elements/ Unique Numbers 2

 7. Count number of bits to be flipped to convert A to B: by Using XOR for two numbers
  
DP:
 1. LCS of 3 strings : by using dp table set all values to zero
                       Then if characters in all the three strings matches then set the table value with increment of value in prev index( i-1, j-1,k-1)
                        If not matches, then set tha max value of these ( t[i-1][j][k], t[i][j-1][k], t[i][j][k-1]) 
                        Then return dp length value
