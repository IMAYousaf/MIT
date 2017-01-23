s = 'azcbobobegghakl'
string = 'bob'

def main():
    bob = 0
    for test in s:
        if test in string:
            bob += 1
            
    print("Number of times bob occurs is: ", bob)
    
main()