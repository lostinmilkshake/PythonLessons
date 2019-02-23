with open("test2.4.1input.txt", "r") as finput, open("test2.4.1output.txt", "w") as foutput:
    lines = finput.read().rsplit()
    lines.reverse()
    lines = "\n".join(lines)
    print(lines)
    for i in lines:
        foutput.write(i)
