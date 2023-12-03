#include <bits/stdc++.h>

using namespace std;

bool chrcheck(char c, bool sym, bool gear)
{
    if (gear) return (c == '*');
    bool num = (c - 48 >= 0 && c - 48 <= 9);
    if (sym) return (c != '.' && num != true);
    else return (num);
}

int main()
{
    freopen("input.txt", "r", stdin);

    char f[142][142];
    pair<int, int> g[142][142];
    int p1_sum = 0;
    int p2_sum = 0;
    int cur = 0;
    bool check;
    bool gearcheck;
    vector<pair<int, int>> gears;

    for (int i = 0; i <= 141; i++){
        for (int j = 0; j <= 141; j++){
            f[i][j] = '.';
            g[i][j] = {1, 0};
        }
    }

    for (int i = 1; i <= 140; i++){
        for (int j = 1; j <= 140; j++){
            cin >> f[i][j];
        }
    }

    for (int i = 1; i <= 140; i++){
        for (int j = 1; j <= 140; j++){
            cin >> f[i][j];
            if (chrcheck(f[i][j], false, false)){
                cur = cur * 10 + (f[i][j] - 48);
                for (int x = -1; x <= 1; x++){
                    for (int y = -1; y <= 1; y++){
                        if (chrcheck(f[i+x][j+y], true, false)) check = true;
                        if (chrcheck(f[i+x][j+y], false, true) && !gearcheck) { gears.push_back({i+x, j+y}); gearcheck = true; }
                    }
                }
            }
            else {
                if (check) {
                    p1_sum += cur;
                    for (auto p : gears){
                        g[p.first][p.second].first *= cur;
                        g[p.first][p.second].second += 1;
                        cout << p.first << " " << p.second << endl;
                    }
                }
                cur = 0;
                check = false;
                gears.clear();
                gearcheck = false;
            }
        }
    }

    for (int i = 1; i <= 140; i++){
        for (int j = 1; j <= 140; j++){
            if (g[i][j].second == 2) p2_sum += g[i][j].first;
        }
    }

    cout << "Part 1: " << p1_sum << "\n";
    cout << "Part 2: " << p2_sum << "\n";
}