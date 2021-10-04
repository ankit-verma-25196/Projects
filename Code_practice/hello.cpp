// Dynamic Programmming in c++ - https://www.codechef.com/UADPIP01/problems/BLJUMP
// jump over buildings

#include<iostream>
#include<vector>
using namespace std;
int main()
{
int t;
cin>>t;
while(t--){
	long long int n,k;
	cin>>n>>k;
	vector<int> h(n);
	for(int i=0;i<n;i++)
	{
		cin>>h[i];
	}

	cout<<n<<k;
	for(int i=0;i<n;i++)
	{
		cout<<h[i];
	}

	vector<int> dp(n,inf);
	dp[0] = 0;
	
	for(int i=1;i<n;i++)
	{
		for(int j=1;j<=k;j++)
		{
			if(i-j < 0) break;
			dp[i] = min(dp[i],dp[i-j]+abs(h[i]-h[i-j]));
		}
	}
	cout<<dp[n-1]<<endl;

}
cout<<"hello";
return 0;
}
