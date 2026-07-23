class order:
    def __init__(self,items,price):
        self.items=items
        self.price=price

    def __gt__(self,it2):
        return self.price > it2.price

it1=order("book",200)
it2=order("pen",10)

print(it1 > it2)
