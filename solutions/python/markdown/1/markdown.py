def header(line):
    hnum = 0
    for char in line:
        if char != "#":
            break
        hnum += 1
    hnum = "h" + str(hnum)
    return f"<{hnum}>{line.lstrip('# ')}</{hnum}>"


def bullets(lines):
    lines = "".join(
    "<li>" + scan(line.lstrip("* ")) + "</li>"
    for line in lines
    )
    return "<ul>" + lines + "</ul>"


def strong(string, end=False):
    return (
    "<strong>" + string.lstrip("_") if not end
    else string.rstrip("_") + "</strong>"
    )


def italic(string, end=False):
    return (
    "<em>" + string.lstrip("_") if not end
    else string.rstrip("_") + "</em>"
    )


def scan(line):
    line = line.split()
    scanned = []
    
    for word in line:
        
        if word.startswith("__"):
            word = strong(word)
        elif word.startswith("_"):
            word = italic(word)

        if word.endswith("__"):
            word = strong(word, "end")
        elif word.endswith("_"):
            word = italic(word, "end")

        scanned.append(word)
        
    return " ".join(scanned)


def parse_markdown(markdown):
    start = markdown[0]
    lines = markdown.splitlines()
    parsed = ""
    
    for line in lines:
        if line.startswith("#"):
            parsed += header(lines.pop(0))
        elif line.startswith("*"):
            parsed += bullets(lines)
            break
        else:
            parsed += scan(line)

    return (
    parsed if start in "#*"
    else "<p>" + parsed + "</p>"
    )
