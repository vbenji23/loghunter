from loghunter.parser import read_log

lines = read_log("samples/auth.log")
print(f"{len(lines)} lignes lues")

for line in lines:
    print(line)
