class Solution {
public:
    int lengthOfLastWord(string s) {
        if(s==" " || s.size()==0)
            return 0;
        int len=s.size();
        int count=0;
        for(int i=len-1;i>=0;i--){
            if(s[i]!=' ')
                count++;
            else{
                if(s[i]==' '&& count!=0)
                    return count;
            }
        }
        return count;
    }
};
