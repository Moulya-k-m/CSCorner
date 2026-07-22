def reve(s):
   if len(s)==0:
      return s
   else:
      return reve(s[1:])+s[0]
   
string=input("Enter a string")
print(reve(string))