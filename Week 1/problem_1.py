s = 'azcbobobegghakl'
vowels = 'aeiou'

def main():
    count = 0
    for vowel in s:
        if vowel in vowels:
            count += 1
            
    print("Number of vowels: ", count)
''' 


def main():
    a = s.count("a")
    e = s.count("e")
    i = s.count("i")
    o = s.count("o")
    u = s.count("u")
    print(a+e+i+o+u)
    '''
    
main()