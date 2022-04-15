# Algorithm-Handbook

FacebookInterviewQnts:
  1.  Valid Palindrome (should consists alphanumeric, and case insensitive) —> in Java, check with Character.isLetterOrDigit(char) and check the total           Sentence
  2. Find Triplets (a+b+c =0 ) —> Iterate in 2 loops with Hashset to find the 3rd number 
  3. Valid parenthesis —> Stack , push all the open parenthesis , pop by checking the close parenthesis from the stack
  4. Reverse K group Nodes in LL —> Recursive for K nodes in full LL, track the previous and next pointer and swap the nodes
  5.  Merge Intervals (start, end)(s1,e1),(s2,e2) (e1>s2 && e2>=s2 —> (s1,e2)) —>  sort the input and push into stack and check if e1>s2 then edit and push
