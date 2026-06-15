class Solution {
    public int singleNumber(int[] nums) {
        HashSet<Integer> h1 = new HashSet<>();
        for(int i = 0; i < nums.length; i++){
            if(!h1.contains(nums[i])){
                h1.add(nums[i]);
            }
            else{
                h1.remove(nums[i]);
            }
        }
        int sum = 0;
        for(int j : h1){
            sum+=j;
        }
        return sum;
    }
}
