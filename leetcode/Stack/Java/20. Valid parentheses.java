//https://leetcode.com/submissions/detail/116353682/

// Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
// determine if the input string is valid.

// The brackets must close in the correct order, "()" and "()[]{}" are all valid 
// but "(]" and "([)]" are not.



class Solution {
    public boolean isMatch(char c1, char c2){
        if ((c1 == '(' && c2 == ')') || (c1 =='[' && c2 == ']') || (c1 == '{' && c2 == '}')){
            return true;
        }else{
            return false;
        }
    }
    public boolean isValid(String s) {
        Stack stack = new Stack();
        
        //you must close the last before the next
        for(int i= 0; i < s.length() ; i++){
            if(!stack.empty() && isMatch((char)stack.peek(), s.charAt(i))){
                stack.pop();
            }else{
                stack.push(s.charAt(i));    
            }
        }
        
        if (stack.empty())
            return true;
        else
            return false;
        
    }
}