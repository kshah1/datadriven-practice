def the_squeeze(s: str):
    
    if not s:
        return ""
        
    current = s[0]
    count = 1
    result = ""
    
    for i in range(1, len(s)):
        if current == s[i]:
            count += 1
        else:
            result += current + str(count)
            current = s[i]
            count = 1
            
    result += current + str(count)
    
    if len(s) <= len(result):
        return s
    
    return result
