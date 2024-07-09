class Solution {
public:
    int reverse(int n) {
        long long ans=0;
        while(n!=0){
            ans=ans*10+n%10;
            n/=10;
        }
        if(n<0){ans=ans*(-1);}
        if(abs(ans)>2147483648)
        {
            ans=0;
        }
        return ans;
    }
};