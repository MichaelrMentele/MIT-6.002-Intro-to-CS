s = 'bobobobstqfbobbdobboobobobobbmb'
count = 0
index = int(0)

for char in s:
    #print index
    if char in ['b']:
        index += 1
        #print str(index) + ' 1'
        
        for char in s[index]:
            if char in ['o']:
                index += 1
                #print str(index) + ' 2'
                
                for char in s[index]:
                    if char in ['b']:
                        count += 1
                        #print ' 3'
                        index = 0
            else:
                index = 0
                
         
    
    index = 0
    #print index
                
               
                    
                        
        

print "Number of times bob occurs is: " + str(count)