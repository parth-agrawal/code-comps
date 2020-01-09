"""
https://codeforces.com/contest/1270/problem/D
"""

from sys import stdout


def interact(q):
    
    submission = "?"

    for i in q:
        submission = submission + " " + str(i[0])
    print(submission)
    stdout.flush()
    result = input().split()
    return result

def one_bool(test):
    true_count = 0

    num = None

    for n in test:
        if n[1] == True:
            true_count += 1
            num = test.index(n) + 1
            
    
    if true_count > 1:
        return False, num
    elif true_count == 1:
        return True, num
    else:
        print("Error: trues are 0")
        return False, num



def main():
    console = input().split()
    n = int(console[0])
    k = int(console[1])
    
    m = None

    # check to make sure it's not n + 1

    arr = []
    # generates a 2d array
    for i in range(1, n + 1):
        arr.append([i, True])
    
    print(arr)

    # picks first query array
    query = arr[:k]

    print(query)
    # check this index - k+1 may be out of range

    # iterates through different indices in the query

    last_output = interact(query)
    
    for q_ind in range(1, k+1):
        query[-q_ind][0] += 1
        output = interact(query)
        if output == last_output:
            query[-q_ind][1] = False
        
        drumroll = one_bool(query)
        if drumroll[0]:
            m = drumroll[1]
            print("!" + " " + str(m))
            break
        last_output = output    



main()