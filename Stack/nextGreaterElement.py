st = []
arr = [1, 3, 5, 4, 7]
arr2 = [4, 3, 5, 4, 7]
# for i in range(len(arr)):
#     print(arr[i])
st.append(7)
for i in range(len(arr)-1, -1, -1):
    print(arr[i])
    if(len(st) != 0 and st[0] > arr[i]):
        st.pop()
    nge[i] = -1 if len(st) == 0 else nge[i] = st[-1]

print(nge)
