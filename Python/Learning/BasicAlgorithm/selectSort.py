def sel_sort(list_in):
    list_out=list_in
    length=len(list_in)
    for k in range(0,length):
        p=list_in[k]
        for j in range(k,length-1):
            if list_out[j]>p:
                list_out[k]=j
                list_out[j]=p
