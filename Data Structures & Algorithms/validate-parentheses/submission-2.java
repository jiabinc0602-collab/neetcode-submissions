class Solution {
    public boolean isValid(String s) {
        Stack<Character> brackets = new Stack<>();
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if(c == '[' || c== '(' || c == '{'){
                brackets.push(c);
            }
            else{
                if(brackets.isEmpty()){
                    return false;
                }
                char popped = brackets.pop();
                if((c == ')' && popped != '(') || 
                (c == ']' && popped != '[') || 
                (c == '}' && popped != '{')){
                    return false;
                }
            }
        }
        return brackets.isEmpty();
    }
}
