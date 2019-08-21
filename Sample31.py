n = raw_input('Enter a String :')
rev = n[::-1]
if n == rev:
    print n,'is Palindrome'
else:
    print n,'is not Palindrome'