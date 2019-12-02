string = "def even_judgment(i):\n"
judgment = """    if i == {}:
        return {}\n"""
for i in range(int(input())+1):
    string += judgment.format(i, i%2 == 0)
string += """    return '知らん'\n"""
with open("./even_judgment.py", mode="w") as f:
    f.write(string)
