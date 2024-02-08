"""8. Write a python script to check whether two given strings are identical,
 first string
comes before the second in dictionary order or first string comes after the second
string in dictionary order using match case statement"""


str1=input("Enter a frist string here: ")
str2=input("Enter a second string here: ")

match str1,str2:
    case (s1,s2) if (s1==s2):
        print("These strings are identical")
    case (s1,s2) if s1<s2:
        print(f'"{s1}" comes before "{s2}" in dictionary order.')
    case (s1,s2) if s1>s2:
        print(f'"{s1}" comes after "{s2}" in dictionary order.')        
