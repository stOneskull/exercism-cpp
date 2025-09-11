def recite(start, end):
    verses = end - start + 1
    recital = []
    for verse in range(verses):
        recital += get_verse(start+verse) + [""]
    return recital[:-1]
        
        
def get_verse(num):
    snacks = [
    "fly", "spider", "bird", "cat", 
    "dog", "goat", "cow", "horse",
    ]
    
    feels = [
    "It wriggled and jiggled and tickled inside her.",
    "How absurd to swallow a bird!",
    "Imagine that, to swallow a cat!",
    "What a hog, to swallow a dog!",
    "Just opened her throat and swallowed a goat!",
    "I don't know how she swallowed a cow!",
    ]
    
    verse = [
    f"I know an old lady who swallowed a {snacks[num-1]}."
    ]

    if num == 8:
        return verse + ["She's dead, of course!"]
    
    if num > 1:
        verse.append(feels[num-2])

    for snack in range(num-1, 0, -1):
        why = (
        f"She swallowed the {snacks[snack]}"
        f" to catch the {snacks[snack-1]}" 
        )
        why += (
        "." if snack != 2 else
        " that wriggled and jiggled and tickled inside her."
        )
        verse.append(why)
    
    verse.append(
    "I don't know why she swallowed the fly. Perhaps she'll die."
    )
    
    return verse
    


