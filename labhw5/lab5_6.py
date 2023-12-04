ss = "You said some winds blow forever and I didn't understand"
print(f"원본 문자열: {ss}")

remlist = []
remlist.append("some")
remlist.append("forever")

print(f"삭제할 단어들: {remlist}")
ss2 = ss.split()
for ch in remlist:
    ss2.remove(ch)
    
print(f"삭제 후 남은 단어들: {ss2}")