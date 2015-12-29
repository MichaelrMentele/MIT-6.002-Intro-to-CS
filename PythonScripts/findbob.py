#findbob
s = 'bobobobstqfbobbdobboobobobobbmb'

index = 0
count = 0

while index<len(s):
    if s.startswith('bob', index, len(s)):
        count += 1
    index += 1

print "Number of times bob occurs is: " + str(count)
    