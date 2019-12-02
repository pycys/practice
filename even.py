string = "def even_judgment(i):\n"
true = """    if i == {}:
        return True\n"""
false = """    if i == {}:
        return False\n"""
for i in range(int(input())+1):
    string += true.format(i) if i%2 == 0 else false.format(i)
string += """    return '知らん'\n"""
with open("./even_judgment.py", mode="w") as f:
    f.write(string)