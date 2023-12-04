"""Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

print("\t\tGiven a string s consisting of words and spaces, return the length of the last word in the string.")

def lengthOfLastWord(a):
	l = 0
	x = a.strip()

	for i in range(len(x)):
		if x[i] == " ":
			l = 0
		else:
			l += 1
	return l


# Driver code
if __name__ == "__main__":
	inp = "Hello World "
	print("The length of last word is",
		lengthOfLastWord(inp))



Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]"""



print("\t\tGiven an integer numRows, return the first numRows of Pascal's triangle.")
def pascal_triangle(n):
    trow = [1]
    
    y = [0]
    
    for x in range(max(n, 0)):
        
        print(trow)
        
        
        trow = [l + r for l, r in zip(trow + y, y + trow)]
    
    
    return n >= 1

pascal_triangle(5) 
