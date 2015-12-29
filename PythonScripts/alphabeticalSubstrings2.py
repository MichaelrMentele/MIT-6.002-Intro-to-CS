def parse_stringAlphabetic(s):
    
    i = 0
    j = 0
    temp = str(s[i])
    
    string_list = []
    index = 1
   
       
    while True:
        j = i + 1
        if s[i] <= s[j]:
            temp += str(s[j])
            i += 1
            print temp
        else:
            i = j
            string_list[index] = temp
            index += 1
            temp = str(s[i])
        
        if j >= len(s):
            break
            
    return max(string_list)
            
        
        

       
            