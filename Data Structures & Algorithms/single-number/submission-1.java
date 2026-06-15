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
        return h1.iterator().next();
    }
}
