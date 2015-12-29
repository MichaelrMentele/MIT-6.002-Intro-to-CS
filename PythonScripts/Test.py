s = 'abcde'
    
i = 0
j = 0
temp = str(s[i])
    
string_list = []
index = 0
   
       
while True:
    j = i + 1
    if s[i] <= s[j]:
        temp += str(s[j])
        i += 1
        
    else:
        i = j
        string_list.append(str(temp));
        index += 1
        temp = str(s[i])
        
    if j >= (len(s) - 1):
        string_list.append(str(temp));
        break
            
print 'Longest substring in alphabetical order is: ' + max(string_list, key = len)
            