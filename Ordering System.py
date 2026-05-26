import tkinter as tk 

#create menu
menu={
      "Burger":500,
      "Pizza":300,
      "Alfredo":100,
      "Spaghetti":800,
      "Biryani":200,
      "Water":60,
      "Pepsi":80,
      "Lassi":180}
#empty cart dictionary
cart={}

#function to add items in cart
def add_to_cart(item):
    if item in cart:
        cart[item]+=1
    else:        
        cart[item]=1
    update_display()
        
def update_display():
    display.delete("1.0",tk.END)
    total=0
    for item in cart:
        qty=cart[item]
        price=menu[item]
        subtotal=qty*price
        total+=subtotal
        
        display.insert(tk.END, f"{item}x{qty}=Rs.{subtotal}\n")
    display.insert(tk.END,f"\nTotal=Rs. {total}")    

#function to clear the cart
def clear_cart():
    cart.clear()
    update_display()
    
root=tk.Tk()
root.title("ORDER SYSTEM-CART VERSION")
tk.Label(root,text="Select Items",
         font=("Arial",14)).pack(pady=10)

#create buttons for each item
for item in menu:
    tk.Button(root,text=item,width=15,
    command=lambda i=item: add_to_cart(i)).pack(pady=5)
    
display=tk.Text(root,height=8,width=50,bg="pink")
display.pack(pady=10)

#create buttons
tk.Button(root,text="Clear Cart",command=clear_cart).pack(pady=5)
tk.Button(root,text="Exit",command=root.destroy).pack(pady=5)    
root.mainloop()