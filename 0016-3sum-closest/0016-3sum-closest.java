class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int s = nums[0]+nums[1]+nums[2];

        for(int i =0;i<nums.length-2;i++){
            int l =i+1;
            int r  =nums.length-1;
            while(l<r){
                int c = nums[i]+nums[l]+nums[r];
                if(Math.abs(s-target)>Math.abs(c-target))
                    s =c;
                if(c>target)
                    r--;
                else if(c<target)
                    l++;
                else
                    return c;
            }
        }
        return s;
        
    }
}