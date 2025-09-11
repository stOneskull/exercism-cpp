import re

def header(line):
    #split it into the hashes and the rest
    # hashsplitter = re.compile(r"(#+) (.*)")
    # splits = hashsplitter.match(line)
    splits = re.match(r"(#+) (.*)", line)
    hnum = len(splits.group(1))
    return f"<h{hnum}>{splits.group(2)}</h{hnum}>"
    
    # hnum = 0
    # for char in line:
        # if char != "#":
            # break
        # hnum += 1
    # hnum = "h" + str(hnum)
    # return f"<{hnum}>{line.lstrip('# ')}</{hnum}>"


def bullets(lines):
    items = ""

    while lines and lines[0].startswith("*"):
        line = lines.pop(0).lstrip("* ")
        items += "<li>" + scan(line) + "</li>"

    items = "<ul>" + items + "</ul>"
    lines = "<p>" + "".join(lines) + "</p>" if lines else ""

    return items + lines


def scan(line):
    line = re.sub(r"__(.*?)__", r"<strong>\1</strong>", line)
    line = re.sub(r"_(.*?)_", r"<em>\1</em>", line)
    return line
    
    # scanA = [
    # "<strong>" + word.lstrip("_") if word.startswith("__")
    # else "<em>" + word.lstrip("_") if word.startswith("_")
    # else word for word in line.split()
    # ]

    # scanB = [
    # word.rstrip("_") + "</strong>" if word.endswith("__")
    # else word.rstrip("_") + "</em>" if word.endswith("_")
    # else word for word in scanA
    # ]

    # return " ".join(scanB)


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
