def header(line):
    hnum = 0
    for char in line:
        if char != "#":
            break
        hnum += 1
    hnum = "h" + str(hnum)
    return f"<{hnum}>{line.lstrip('# ')}</{hnum}>"


def bullets(lines):
    items = ""

    while lines and lines[0].startswith("*"):
        line = lines.pop(0).lstrip("* ")
        items += "<li>" + scan(line) + "</li>"

    items = "<ul>" + items + "</ul>"

    lines = "".join(lines)
    if lines:
        lines = "<p>" + lines + "</p>"

    return items + lines


def scan(line):
    line = line.split()
    scanned = []

    for word in line:

        if word.startswith("__"):
            word = "<strong>" + word.lstrip("_")
        elif word.startswith("_"):
            word = "<em>" + word.lstrip("_")

        if word.endswith("__"):
            word = word.rstrip("_") + "</strong>"
        elif word.endswith("_"):
            word = word.rstrip("_") + "</em>"

        scanned.append(word)

    return " ".join(scanned)


def parse(markdown):
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
