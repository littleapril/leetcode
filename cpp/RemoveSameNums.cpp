class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int len=nums.size();
        if(len==0)
            return 0;
        int a=0;
        for(int i=0;i<len;i++){
            if(nums[i]!=nums[a]){
                ++a;
                nums[a]=nums[i];
            }
        }
        return ++a;
    }
};
