class FindTriplets {
    public List<List<Integer>> threeSum(int[] nums) {
       int  m= 0;
       List<List<Integer>> arr = new ArrayList<List<Integer>>();
       //List<Integer> a1 = new ArrayList<Integer>();

       for (int i=0;i<nums.length-1;i++){
        HashSet<Integer> st = new HashSet<Integer>();
           for(int j=i+1;j<nums.length;j++){
               int sum = nums[i]+nums[j];
               if(st.contains(-sum)){
                   List<Integer> a1 = new ArrayList<Integer>();
                   a1.add(nums[i]);
                   a1.add(nums[j]);
                   a1.add(-sum);
                   arr.add(a1);

               }else{
                   st.add(nums[j]);
               }
           }
       }
     return arr;
    }
}
