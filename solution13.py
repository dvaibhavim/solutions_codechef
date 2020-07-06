# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 21:03:27 2020

Input
The first line of the input file contains an integer T, the number of test cases. T test cases follow. Each test case consists of exactly 2 lines. 
The first line of each test case contains two space separated integers N and C, the total number of elephants and the total number of candies in the 
Zoo respectively. The second line contains N space separated integers A1, A2, ..., AN.

Output
For each test case output exactly one line containing the string Yes if it possible to make all elephants happy and the string No otherwise. Output 
is case sensitive. So do not print YES or yes.
"""
'''
result = []
for tc in range(int(input())):
    elephant, candy = input().split(' ')
    ele_candy = list(map(int,input().split(' ')))
    rem = int(candy)
    for i in range(int(elephant)):
        if ele_candy[i]>=i:
            rem = rem - max(ele_candy[i],i)
    if rem<0:
        result.append("No")
    else:
        result.append("Yes")
for i in result:
    print(i)    
    
    
    #include <bits/stdc++.h>
using namespace std;
#define ll		long long
#define w(t)	int t; cin>>t; while(t--)
#define FIO 	ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl	"\n"
#define f(a,b,c) for(int a=b;a<c;a++)
#define inp_arr	int n;cin>>n;int arr[n];f(i,0,n)cin>>arr[i];
int main()
{
	FIO
	w(t) {
		ll n, c, a, k = 0;
		cin >> n >> c;
		for (int i = 0; i < n; i++) {
			cin >> a;
			k += a;
		}
		if (k <= c)
			cout << "Yes" << endl;
		else
			cout << "No" << endl;
	}
	return 0;
}
    '''
    
t=int(input())
for i in range(t):
    n,c=map(int,input().split())
    a=[int(x) for x in input().split()]
    cook=0
    j=0
    while(cook<=c and j<n):
       
        cook+=a[j]
        j+=1
    if(cook<=c):
        print('Yes')
    else:
        print('No')    