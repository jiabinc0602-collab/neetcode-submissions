class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int low = 0;
        int high = numbers.length-1;
        int[] indices = new int[2];
        while (low < high){
            int sum = numbers[low] + numbers[high];
            if (sum == target){
                indices[0] = low + 1;
                indices[1] = high + 1;
                return indices;
            }
            else if(sum < target){
                low++;
            }
            else{
                high--;
            }

        }
        return new int[0];
    }
}
