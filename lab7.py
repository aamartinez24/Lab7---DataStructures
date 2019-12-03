def edit_dist(str1, str2):
    return _edit_dist(str1, str2, len(str1), len(str2))

def _edit_dist(str1, str2, m, n):
    if m == 0:
        return n
    
    if n == 0:
        return m
    
    if str1[m-1] == str2[n-1]:
        return _edit_dist(str1, str2, m-1, n-1)
    
    return 1 + min(_edit_dist(str1, str2, m-1, n-1), _edit_dist(str1, str2, m, n-1), _edit_dist(str1, str2, m-1, n))

def main():
    print("input the first word")
    str1 = input()
    print("input the second word")
    str2 = input()
    print(edit_dist(str1, str2))
    
    
main()