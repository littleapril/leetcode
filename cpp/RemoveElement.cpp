class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int i = 0;
        for(int j=0;j<nums.size();j++){
            if (nums[j]!= val){
                nums[i] = nums[j];
                i++;
            }
        }
        return i;
    }
};

=================================================================
    
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int i = 0;
        int j = nums.size();
        while (i<j){
            if (nums[i]==val)
                nums[i] = nums[--j];
            else
                i++;
        }
        return j;
    }
};
