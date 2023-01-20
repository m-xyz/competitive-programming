#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int n = 8;
int ans = 0;
vector<int> col(n);
vector<int> diag1(n);
vector<int> diag2(n);


void search(int y){
	if(y == n){
		ans++;
		return;
	}

	for(int i = 0; i < n; i++){
		if(col[i] || diag1[i + y] || diag2[i - y + n - 1]) continue;
		col[i] = diag1[i + y] = diag2[i - y + n - 1] = 1;
		search(y + 1);
		col[i] = diag1[i + y] = diag2[i - y + n - 1] = 0;
	}
}



int main(){

	search(0);

	cout << ans << endl;

	return 0;
}
