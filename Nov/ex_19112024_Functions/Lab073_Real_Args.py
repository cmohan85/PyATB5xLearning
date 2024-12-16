#  Pizza Lovers

# Toppings - mushroom, panner, olives, corn, pineapple, jalapeno

def make_pizza(*toppings):
    print(toppings)
    for i in toppings:
        print(i)

kchenna = make_pizza("tomato", 'olives')
Krishna = make_pizza('pineapple', 'olives', 'corn', 'panner')
Mohan = make_pizza('tomato')