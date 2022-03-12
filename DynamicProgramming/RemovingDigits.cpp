#include <bits/stdc++.h>
using namespace std;


vector<int> getDigits(int n){
    vector<int>digits;
    while (n/10 >0)
    {
        if (n%10 != 0){
        digits.push_back(n%10);

        }
        n = n/10;

    }
    digits.push_back(n);
    return digits;

}

vector <int>dp(1000000,1e9);

int solver(int n){
    if (n == 0){
        return 0;
    }else if(n < 10){
        return 1;
    }else if(dp[n]!= 1e9){
        return dp[n];
    }else{
        for (auto digit:getDigits(n)){
            dp[n] = min(dp[n],solver(n-digit) + 1);

        }
        return dp[n];
    }
}


int main(){
    int n ;
    cin>>n;
    cout << solver(n) <<endl;
    return 0;
}