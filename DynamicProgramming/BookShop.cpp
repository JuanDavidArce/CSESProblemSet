
#include <bits/stdc++.h>
using namespace std;




int dp(int money, int pages[], int price[], int n)
{
	int i, w;
	vector<vector<int>> K(n + 1, vector<int>(money + 1));


	for(i = 0; i <= n; i++)
	{
		for(w = 0; w <= money; w++)
		{
			if (i == 0 || w == 0)
				K[i][w] = 0;
			else if (price[i - 1] <= w)
				K[i][w] = max(pages[i - 1] +
								K[i - 1][w - price[i - 1]],
								K[i - 1][w]);
			else
				K[i][w] = K[i - 1][w];
		}
	}
	return K[n][money];
}


int main()
{
    int n, money ;
    cin >> n >> money;
	int price[n]; 
	int pages[n];
	
	for (int i = 0; i< n; i++){
        cin >> price[i];
    }
    for (int i = 0; i< n; i++){
        cin >> pages[i];
    }
	
	cout << dp(money, pages, price, n)<<endl;
	
	return 0;
}

