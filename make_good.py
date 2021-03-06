""" 
https://codeforces.com/contest/1270/problem/C

Let's call an array a1,a2,…,am of nonnegative integer numbers good if a1+a2+⋯+am=2⋅(a1⊕a2⊕⋯⊕am), where ⊕ denotes the bitwise XOR operation.

For example, array [1,2,3,6] is good, as 1+2+3+6=12=2⋅6=2⋅(1⊕2⊕3⊕6). At the same time, array [1,2,1,3] isn't good, as 1+2+1+3=7≠2⋅1=2⋅(1⊕2⊕1⊕3).

You are given an array of length n: a1,a2,…,an. Append at most 3 elements to it to make it good. Appended elements don't have to be different. It can be shown that the solution always exists under the given constraints. If there are different solutions, you are allowed to output any of them. Note that you don't have to minimize the number of added elements!. So, if an array is good already you are allowed to not append elements.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1≤t≤10000). The description of the test cases follows.

The first line of each test case contains a single integer n (1≤n≤105) — the size of the array.

The second line of each test case contains n integers a1,a2,…,an (0≤ai≤109) — the elements of the array.

It is guaranteed that the sum of n over all test cases does not exceed 105.

Output
For each test case, output two lines.

In the first line, output a single integer s (0≤s≤3) — the number of elements you want to append.

In the second line, output s integers b1,…,bs (0≤bi≤1018) — the elements you want to append to the array.

If there are different solutions, you are allowed to output any of them.

"""
def main():

    for t in range(0, int(input())):
        n = input()
        arr = list(map(int, input().split()))
        
        bin_arr = []
        for x in arr:
            bin_arr.append(num_bin(x))
        
        xor_sum = bin_arr[0]
        add_count = 0
        nums_added = []
        
        for x in range(1, len(bin_arr)):
            xor_sum = x_or(xor_sum, bin_arr[x])

        if bin_num(xor_sum) == sum(arr)/2:
            print("0")
            print("")
        else:
            print("2")
            print(bin_num(xor_sum), bin_num(xor_sum)+sum(arr))


        


def num_bin(num):
    
    el = num
    count = 0
    count_list = []
    while True:
        el = el // 2
        if el >= 1:
            count += 1
            continue
        
        count_list.append(count)

        if (num - 2**count > 0):
            num = num - 2**count
            el = num
            count = 0
            continue
        else:
            break

    binary = []  

    for n in range(0, max(count_list) + 1):
        binary.append(0)
    for i in count_list:
        binary[-(i+1)] = 1

    if num == 0:
        binary = [0]

    return binary
 
def bin_num(b):
    num = 0
    for x in range(0, len(b)):
        if(b[-(x+1)] == 1):
            num = 2**x + num
    return num 


def x_or(num1, num2):
    new_arr = []
    flag = False
    diff = len(num2)-len(num1)

    # if the first number is actually bigger than the second
    if len(num1) >= len(num2):
        diff = len(num1)-len(num2)
        flag = True
    

    
    # append big array's elements at start
    
    if(flag):
        for i in range(0, diff):
            new_arr.insert(i, num1[i])
        for i in range(0, len(num2)):
            if num1[i + diff] != num2[i]:
                new_arr.append(1)
            else:
                new_arr.append(0)
    else:
        for i in range(0, diff):
            new_arr.insert(i, num2[i])
        for i in range(0, len(num1)):
            if num2[i + diff] != num1[i]:
                new_arr.append(1)
            else:
                new_arr.append(0)
    return new_arr
    

main()








