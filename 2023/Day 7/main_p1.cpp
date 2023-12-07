#include <bits/stdc++.h>
#define fi first
#define sc second

using namespace std;

int hand_type(string hand)
{
    int type = 1;
    unordered_map<char, int> cards;
    for (auto c: hand) cards[c]++;
    for (auto p: cards){
        if (p.sc >= 4) type = p.sc + 3; // Five of a Kind and Four of a Kind
        else if (p.sc == 3){
            if (type == 2) type = 5; // Full House
            else type = 4; // Three of a Kind
        }
        else if (p.sc == 2){
            if (type == 2) type = 3; // Two Pair
            else if (type == 4) type = 5; // Full House
            else type = 2; // One Pair
        }
    }
    return type;
}

bool comp(pair<string, int> &LHS, pair<string, int> &RHS)
{
    if (hand_type(LHS.fi) == hand_type(RHS.fi)){
        for (int i = 0; i < 5; i++){
            if (LHS.fi[i] != RHS.fi[i]) return LHS.fi[i] < RHS.fi[i];
        }
        return true;
    }
    return hand_type(LHS.fi) < hand_type(RHS.fi);
}

int main()
{
    freopen("input.txt", "r", stdin);

    const int n = 1000;
    pair<string, int> l[n+1];
    long p1_sum = 0;

    for (int i = 1; i <= n; i++){
        cin >> l[i].fi >> l[i].sc;
        for (int j = 0; j < 5; j++){
            switch (l[i].fi[j])
            {
                case 'T':
                    l[i].fi[j] = 'L';
                    break;
                case 'J':
                    l[i].fi[j] = 'M';
                    break;
                case 'Q':
                    l[i].fi[j] = 'N';
                    break;
                case 'K':
                    l[i].fi[j] = 'O';
                    break;
                case 'A':
                    l[i].fi[j] = 'P';
                    break;
                default:
                    break;
            }
        }
    }

    sort(l+1, l+n+1, comp);
    for (auto p: l){
        cout << p.fi << " " << p.sc << endl;
    }
    for (int i = 1; i <= n; i++){
        p1_sum += l[i].sc * i;
    }

    cout << "Part 1: " << p1_sum << "\n";
}