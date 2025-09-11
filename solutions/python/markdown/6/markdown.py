from re import match, sub


def header(line):
    splits = match(r"(#+) (.*)", line)
    hnum = len(splits.group(1))
    return f"<h{hnum}>{splits.group(2)}</h{hnum}>"


def bullets(lines):
    listed = ""

    while lines and lines[0].startswith("*"):
        line = lines.pop(0).lstrip("* ")
        listed += "<li>" + scan(line) + "</li>"

    listed = "<ul>" + listed + "</ul>"

    rest = ""
    
    if lines:
        rest = "".join(scan(line) for line in lines)
        rest = "<p>" + rest + "</p>"

    return listed + rest


def scan(line):
    line = sub(r"__(.*?)__", r"<strong>\1</strong>", line)
    line = sub(r"_(.*?)_", r"<em>\1</em>", line)
    return line


def parse(markdown):
    start = markdown[0]
    lines = markdown.splitlines()
    parsed = ""

    while lines:
        if lines[0].startswith("#"):
            parsed += header(lines.pop(0))
        elif lines[0].startswith("*"):
            parsed += bullets(lines)
            break
        else:
            parsed += scan(lines.pop(0))

    return (
    parsed if start in "#*"
    else "<p>" + parsed + "</p>"
    )
