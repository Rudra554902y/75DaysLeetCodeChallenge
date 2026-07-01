class Solution {
    public int gcd(int a, int b){
        if (b == 0){
            return a;
        }

        return gcd(b, a % b);
    }
    public int subarrayGCD(int[] nums, int k) {
        int ans = 0;
        for (int i = 0; i < nums.length; i ++){
            if (nums[i] < k){
                continue;
            }
            int g = nums[i];
            if (g == k){
                ans ++;
            }
            for (int j = i + 1; j < nums.length; j ++){
                if (nums[j] < k){
                    break;
                }
                g = gcd(nums[j], g);
                if (g == k){
                    ans ++;
                }
                if (g < k){
                    break;
                }
            }
        }
        return ans;
    }
}