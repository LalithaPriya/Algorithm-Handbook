st = []
string =  "sample"
print(st)
# for c in reversed(string): # reverse in iteration
for c in range(len(string)-1,-1,-1):
    print(string[c])
    st.append(string[c])
print(st)
