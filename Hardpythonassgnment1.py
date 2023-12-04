
"""Input: n = 13
Output: 6

Input: n = 0
Output: 0

print(" \t \t Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.")

def countDigitOne(n):
    countr = 0;
    for i in range(1, n + 1):
        str1 = str(i);
        countr += str1.count("1");
 
    return countr;
 
# Driver Code
n = 13;
print("The no of 1 in digital count is 13 :- ", countDigitOne(n));
 
n = 0;
print("The no of 1 in digital count is 0 :- ", countDigitOne(n));












Input: s = "aacecaaa"
Output: "aaacecaaa"   """


print("You are given a string s. You can convert s to a palindrome by adding characters in front of it.Return the shortest palindrome you can find by performing this transformation.")
 
def ispalindrome(s):
 
    l = len(s)
     
    i = 0
    j = l - 1
    while i <= j:
     
        if(s[i] != s[j]):
            return False
        i += 1
        j -= 1
     
    return True

if __name__ == "__main__":
     
    s = "aacecaaa"
    cnt = 0
    flag = 0
     
    while(len(s) > 0):
        if(ispalindrome(s)):
            flag = 1
            break
         
        else:
            cnt += 1
            s = s[:-1]
     
    
    if(flag):
        print(cnt)

