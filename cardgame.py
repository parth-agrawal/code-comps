# https://codeforces.com/contest/1270/problem/A

"""
Input
Each test contains multiple test cases. The first line contains the number of test cases t (1≤t≤100). The description of the test cases follows.

The first line of each test case contains three integers n, k1, k2 (2≤n≤100,1≤k1≤n−1,1≤k2≤n−1,k1+k2=n) — the number of cards, number of cards owned by the first player and second player correspondingly.

The second line of each test case contains k1 integers a1,…,ak1 (1≤ai≤n) — the values of cards of the first player.

The third line of each test case contains k2 integers b1,…,bk2 (1≤bi≤n) — the values of cards of the second player.

It is guaranteed that the values of all cards are different.

Output
For each test case, output "YES" in a separate line, if the first player wins. Otherwise, output "NO" in a separate line. You can print each letter in any case (upper or lower).

"""


def main():
    
    from sys import stdin
    
    console = iter(stdin.read().split("\n"))
    # console = iter(("2\n2 1 1\n2\n1\n5 2 3\n2 3\n1 4 5").split("\n"))

    t = int(next(console))

    # iterates over test cases
    for i in range(0, t):
        nkline = next(console).split()

        n, k1, k2 = (int(nkline[0]), int(nkline[1]), int(nkline[2]))
        p1_cards = list(map(int,next(console).split()))
        p2_cards = list(map(int,next(console).split()))

        if max(p1_cards) == n:
            print("YES")
        else:
            print("NO")


main()      
    
