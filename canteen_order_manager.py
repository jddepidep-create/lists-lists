order =[]

for i in range(1,6):
    orders = input("what is your order")
    order.append(orders)

print(f"Orig Orders:{order}")
add = input("Additional order:")
order.append(add)
priority = input("Priority order: ")
order.insert(0,priority)
print(f"Order: {order}")
search = input("serch")
if search not in order:
    print("invalid")
else:
    print(order.count(search))
    print(order.index(search))

cancel = input("Cancel an order")
if cancel not in order:
    print("NO ORDER")
else:
    order.remove(cancel)

print("removing last order because i hate you")
print(order.pop())

print("sorting A for apol B for bol")
order.sort()
print(order)
num = len(order)
print(f"Num {num}")
print(f"Final roders: {order}")

