from collections import Counter
def CompanyLogo(S):
    
    N = Counter(s).most_common(3)
    for i in N:
        print(i[0], i[1])
        
if __name__ == '__main__':
    s = ''.join(sorted(list(input())))
    CompanyLogo(s)
