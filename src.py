import pyperclip

# Open the file and read its contents
with open("gecko.txt", "r+") as f:
    contents = f.read()
    lines = contents.splitlines()
    clipboard = pyperclip.paste()
    for i, line in enumerate(lines):
        if "$Second gecko" in line:
            lines[i+1] = clipboard
            break
    new_contents = '\n'.join(lines)
    f.seek(0)
    f.write(new_contents)
    f.truncate()