class Solution {
    public int[] resultArray(int[] nums) {
        List<Integer> a = new ArrayList<>();
        List<Integer> b = new ArrayList<>();
        a.add(nums[0]);
        b.add(nums[1]);
        for(int i = 2; i < nums.length; i++){
            if(a.get(a.size() - 1) > b.get(b.size() - 1)){
                a.add(nums[i]);
            }
            else{
                b.add(nums[i]);
            }
        }
        a.addAll(b);
        int [] ans = new int[a.size()];
        int r = 0;
        for (int i: a){
            ans[r++] = i;
        }
        return ans;
    }
}