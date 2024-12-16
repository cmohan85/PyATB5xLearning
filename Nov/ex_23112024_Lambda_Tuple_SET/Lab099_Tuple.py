# Tuple - Collection of Items
# syntax is ()
# Immutable - which can't be changed

my_tuple = (1, 4, 9, 16 , 25)
# my_tuple[3] = 64 # TypeError: 'tuple' object does not support item assignment

#List is mutalbe
shopping_list = ['bread', 'butter', 'panner']
shopping_list[2] = 'milk'
print(shopping_list)

# Real time example of tuple
my_tuple = ('tta.com', 'sedt.live')
my_api_list =  list(my_tuple)
print(my_api_list)
#my_tuple[0] = 'abc.com'  # TypeError: 'tuple' object does not support item assignment

# Real case, where Tuple used
API_URLs = ("https://sedt.live/phython", "https://awesome.com", "https://myworld.com")
print(API_URLs[0])
print(API_URLs[1])