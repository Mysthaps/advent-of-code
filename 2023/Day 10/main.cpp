#include <bits/stdc++.h>
#define fi first
#define sc second

using namespace std;

const int n = 140;
map<char, vector<pair<int, int>>> dirs = {
    {'-', {{0, 1}, {0, -1}}},
    {'|', {{1, 0}, {-1, 0}}},
    {'L', {{-1, 0}, {0, 1}}},
    {'J', {{-1, 0}, {0, -1}}},
    {'7', {{1, 0}, {0, -1}}},
    {'F', {{1, 0}, {0, 1}}},
    {'S', {{0, 1}, {0, -1}, {1, 0}, {-1, 0}}},
    {'.', {}}
};

char l[142][142];
pair<int, int> st;
queue<pair<int, int>> q;
int c[142][142];

int p1 = 0;

int main()
{
    freopen("input.txt", "r", stdin);

    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= n; j++){
            cin >> l[i][j];
            c[i][j] = -1;
            if (l[i][j] == 'S'){
                st = {i, j};
                c[i][j] = 0;
            }
        }
    }

    q.push(st);
    while (q.size()){
        int i = q.front().fi, j = q.front().sc;
        q.pop();

        for (auto dir: dirs[l[i][j]]){
            int x = i + dir.fi, y = j + dir.sc;
            //cout << "current: " << i << " " << j << " to " << x << " " << y << endl;
            if (find(dirs[l[x][y]].begin(), dirs[l[x][y]].end(), make_pair(-dir.fi, -dir.sc)) != dirs[l[x][y]].end() && c[x][y] == -1){
                c[x][y] = c[i][j] + 1;
                p1 = max(p1, c[x][y]);
                q.push(make_pair(x, y));
            }
        }
    }

    /*for (int i = 1; i <= n; i++){
        for (int j = 1; j <= n; j++){
            cout << c[i][j] << " ";
        }
        cout << endl;
    }*/

    cout << "Part 1: " << p1 << "\n";
    //cout << "Part 2: " << p2_sum << "\n";
}