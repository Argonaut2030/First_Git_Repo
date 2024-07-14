def order_pizza(size, *toppings, **extras):
    order = f"A {size} pizza with {', '.join(toppings)}."
    if extras:
        extra_details = ", ".join([f"{key}: {value}" for key, value in extras.items()])
        order += f" With extra {extra_details}."
    return order

print(order_pizza("large", "pepperoni", "mushrooms"))  # Output: A large pizza with pepperoni, mushrooms.
print(order_pizza("medium", crust="thin", cheese="double"))  # Output: A medium pizza with extra cheese. Thin crust.
