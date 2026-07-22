def lists(items,idx=0):
    if (idx==len(items)):
       return
    else:
       print(items[idx])
       lists(items,idx+1)

fruits=["apple","banana","mango"]
lists(fruits)