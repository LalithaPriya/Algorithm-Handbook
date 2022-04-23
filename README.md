# Algorithm-Handbook

FacebookInterviewQnts:
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
 
