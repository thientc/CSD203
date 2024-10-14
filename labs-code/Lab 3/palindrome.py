def isPalindrome(string):
  	#termination condition: the string is one character or less
    if (len(string) <= 1):
        return True
    if (string[0] == string[-1]):
        return isPalindrome(string[1:-1])
    else:
        return False
p = list(input())
for i in range(len(p)):
    if p[i] == p[len(p)-1-i]:
        continue
    else:
         print("NOT PALINDROME")
         break
else:
    print("PALINDROME")