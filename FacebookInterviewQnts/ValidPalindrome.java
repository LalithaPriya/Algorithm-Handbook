class ValidPalindrome {
    public boolean isPalindrome(String s) {
        boolean flag = false;
        char[] ch = new char[s.length()];
        int k=0;
       for(int i=0;i<s.length();i++){
            if((Character.isLetterOrDigit(s.charAt(i)))){
                ch[k++]=s.charAt(i);
            }
        }  
        int i=0,j=k-1;
        int x=k-1;
        for(int z=0;z<k;z++){
            if(Character.isLowerCase(ch[z])==true){
                ch[z] = Character.toUpperCase(ch[z]);
             }
        }

        for(int z=0;z<k/2;z++){
            System.out.println(ch[z]+"  "+ch[x]);
            if(ch[z]!=ch[x]){
                flag = true;
                System.out.println(ch[z]+"  "+ch[x]);
            }x--;
        }
        
        // for(int m=0;m<k;m++)
        //  System.out.print(ch[m]);
        // System.out.print(k/2);

        return !flag;
    }
}
