import pyperclip

with open("gecko.txt", "r+") as f:
    contents = f.read()
    start_index = contents.find("$Second gecko")
    if start_index == -1:
        print("Second gecko not found in file")
    end_index = contents.find('\n', start_index)
    if end_index == -1:
        end_index = len(contents)
    clipboard = pyperclip.paste()
    new_contents = contents[:start_index] + clipboard + contents[end_index:]
    f.seek(0)
    f.write(new_contents)
    f.truncate()