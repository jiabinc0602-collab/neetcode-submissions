class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
        ArrayList<Character> string1 = new ArrayList<>();
        for(int a = 0; a < s.length(); a++){
            string1.add(s.charAt(a));
        }
        ArrayList<Character> string2 = new ArrayList<>();
        for(int b = 0; b < t.length(); b++){
            string2.add(t.charAt(b));
        }

        for(int i = 0; i < string1.size(); i++){
            for(int j = 0; j < string2.size(); j++){
                if(string1.get(i) == string2.get(j)){
                    string2.remove(j);
                    break;
                }
            }
        }
        return string2.isEmpty();
    }
}
