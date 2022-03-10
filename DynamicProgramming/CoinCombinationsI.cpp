#include <bits/stdc++.h>
using namespace std;

int main(){
    long long int n,x,mod;
    mod = pow(10,9) + 7;
    cin>>n>>x;
    vector <long long int>dp(x+1,0);
    vector <long long int>coins(n);
    dp[0] = 1;
    for (int i= 0; i<n;i++){
        cin >> coins[i];
    }

    for (int i = 1; i <=x;i++){
        for (auto coin : coins){
            if(i - coin >=0){
                dp[i] += dp[i-coin];
                dp[i] = dp[i]%mod;
            }
        }
    }
    cout << dp[x] <<endl;
    return 0;
}