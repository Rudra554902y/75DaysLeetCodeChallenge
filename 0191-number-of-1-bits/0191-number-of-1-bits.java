class Solution {
    public int hammingWeight(int n) {
        int c=0;
        while(n>0){
            int x=n&-n;
            n=n^x;
            c+=1;
        }
        return c;
    }
}