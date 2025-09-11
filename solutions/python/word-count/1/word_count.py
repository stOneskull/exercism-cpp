def word_count(phrase):
    words = ''
    
    for char in phrase.lower():
        if char.isalnum() or char == ' ' or char == "'":
            words += char
        elif char in '\n\t-_,':
            words += ' '
            
    wordlist = words.split()
    
    counts = {}
    
    for word in wordlist:
        if word[0] == "'" and word[-1] == "'":
            wordlist.remove(word)
            wordlist.append(word[1:-1])
            
    for word in wordlist:
        counts[word] = wordlist.count(word)
        
    return counts