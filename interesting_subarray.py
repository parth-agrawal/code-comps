"""

https://codeforces.com/contest/1270/problem/B

For an array a of integers let's denote its maximal element as max(a), and minimal as min(a). We will call an array a of k integers interesting if max(a)−min(a)≥k. For example, array [1,3,4,3] isn't interesting as max(a)−min(a)=4−1=3<4 while array [7,3,0,4,3] is as max(a)−min(a)=7−0=7≥5.

You are given an array a of n integers. Find some interesting nonempty subarray of a, or tell that it doesn't exist.

An array b is a subarray of an array a if b can be obtained from a by deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end. In particular, an array is a subarray of itself.

Input
The first line contains integer number t (1≤t≤10000). Then t test cases follow.

The first line of each test case contains a single integer n (2≤n≤2⋅105) — the length of the array.

The second line of each test case contains n integers a1,a2,…,an (0≤ai≤109) — the elements of the array.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅105.

Output
For each test case, output "NO" in a separate line if there is no interesting nonempty subarray in a.

Otherwise, output "YES" in a separate line. In the next line, output two integers l and r (1≤l≤r≤n) — bounds of the chosen subarray. If there are multiple answers, print any.

You can print each letter in any case (upper or lower).
"""


def main():
    from sys import stdin
    # console = iter(stdin.read().split("\n"))
    console = iter(("3\n5\n1 2 3 4 5\n4\n2 0 1 9\n2\n2019 2020").split("\n"))
    for t in range(0, int(next(console))):

        n = int(next(console))

        arr = list(map(int, next(console).split()))

        flag = False
        for i in range(1,len(arr)):
            current = arr[i]
            last = arr[i-1]
            if current - last != 1:
                flag = True
                break
        
        if flag:
            print("YES")
            print(arr.index(min(arr)), " ", arr.index(max(arr)) + 1) 
        else:
            print("NO")
main()