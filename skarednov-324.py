def check(line):
    if re.fullmatch(line, line[::-1]):
        return "YES"
    else:
        return "NO"


