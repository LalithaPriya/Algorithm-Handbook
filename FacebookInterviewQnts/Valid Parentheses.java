class Solution {
    public boolean isValid(String s) {
        
        char[] chArr = s.toCharArray();
        Stack<Character> st = new Stack<Character>();
        
        for(int i=0;i<chArr.length;i++){
            if(chArr[i]=='{' || chArr[i]=='['|| chArr[i]=='('){
                st.push(chArr[i]);
            }
            else if(chArr[i]=='}' || chArr[i]==']'|| chArr[i]==')'){
                if(st.isEmpty()){
                    return false;
                }
                char ch = st.pop();
                if(chArr[i]=='}' && (ch =='[' || ch =='(')){
                    return false;
                }
                if(chArr[i]==')' && (ch =='[' || ch =='{')){
                    return false;
                }
                if(chArr[i]==']' && (ch =='{' || ch =='(')){
                    return false;
                }
                   
            }else{
                return false;
            }
                 
        
        }
        if(st.isEmpty()){
            return true;
        }
        return false;
    }
}
