class Solution {
    public boolean isPalindrome(String s) {
        String str = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        int high = str.length() - 1;
        int low = 0;
        while(high > low){
            if(str.charAt(high) != str.charAt(low)){
                return false;
            }
            high--;
            low++;
        }
        return true;
    }
}
