class Solution {
public:
    int romanToInt(string s) {
        map<char,int> ss = {{'I',1},{'V',5},{'X',10},{'L',50},{'C',100},{'D',500},{'M',1000}};
        int len = s.length();
        int sum = 0;
        if (len==1)
            return ss[s[0]];
        for(int i=0;i<len-1;i++){
            if (ss[s[i]]<ss[s[i+1]])
                sum -=ss[s[i]];
            else
                sum +=ss[s[i]];
        }
        sum +=ss[s[len-1]];
        return sum;                
    }
};
