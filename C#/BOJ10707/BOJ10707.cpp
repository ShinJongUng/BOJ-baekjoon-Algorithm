#include <bits/stdc++.h>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr), cout.tie(nullptr);

	int a, b, c, d, p;
	cin >> a >> b >> c >> d >> p;
	cout << min(a*p, b+max(0, p-c)*d) << '\n';

	return 0;
}