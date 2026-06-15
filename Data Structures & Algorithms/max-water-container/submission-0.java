class Solution {
    public int maxArea(int[] heights) {
        int i = 0;
        int j = heights.length - 1;
        int maxArea = 0;
        while (i < j){
            int h = Math.min(heights[i], heights[j]);
            int area = h * (j - i);

            if (area > maxArea){
                maxArea = area;
            }

            if (heights[i] == h){
                i++;
            }
            else{
                j--;
            }

        }
        return maxArea;
    }
}
