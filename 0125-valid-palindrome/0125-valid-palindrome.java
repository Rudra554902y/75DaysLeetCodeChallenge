class Solution {
    public boolean isPalindrome(String s) {
        // s=s.replaceAll("[^a-zA-Z0-9]","").toLowerCase();
        int start=0,end=s.length() -1;
        while (start<=end){
            while(start<=end && !Character.isLetterOrDigit(s.charAt(start))){
                start++;
            }
            while(start<=end && !Character.isLetterOrDigit(s.charAt(end))){
                end--;
            }
            if(start<=end){
                char c1=Character.toLowerCase(s.charAt(start));
                char c2=Character.toLowerCase(s.charAt(end));
                if(c1!=c2){
                    return false;
                }
                start++;
                end--;
            }
        }
        return true;
    }
}