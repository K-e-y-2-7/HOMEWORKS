'''
HomeWork 10
===========

Homework9 update. Working with classes.
Сreation of a product selection system. Training using PEP-8.

'''


import NUMexam


class Product:
    '''Class for products in the store.
       Functions are present:
         -create any products; 
         -issue complete information about the product;
         -accept any quantity of one product and issue its total cost;
         -issue information whether the product is edible;
    
    '''

    def __init__(self, price, product_name, category, unit ):
        '''constructor method

        '''
        self.price = price
        self.category = category
        self.product_name = product_name
        self.unit = unit
        
    
    def is_edible (self, category: str) -> bool:
        '''Is edible method.
           
           Issue information whether the product is edible.
           
           :return: booling value.
        
        '''

        if self.category != 'household chemicals':

            return True
        else:

            return False

    
    def price_total (self) -> str:
        '''Price total method.
           
           Multiplies a certain amount of a product and the cost of that product.
           
           :return: total price of some count of product.

        '''

        n = NUMexam.intexam(input('Enter the product number: '))
        n -= 1
        print (n)
        product_total_price = 0
        print (self.price)
        product_total_price = counts[n] * products[n].price
        product_total_price = f'{counts[n]} {products[n].unit} of {products[n].product_name} cost {product_total_price} grn.'
        return product_total_price


    def get_info(self) -> str:
        ''' Method get info. 
            
            Issue complete information about the product.
            
            :return: string of information about product.

        '''

        return f'{self.product_name} {self.price} for {self.unit}. '


class Cart:
    '''The cart class for the products that the user has selected.
       Functions are present:
        -create lists to use class methods;
        -put the user's choice in these lists;
        -calculate the entire value of the item in the cart;
        -check for inedible goods;

    '''

    def __init__(self):
        '''constructor method

           :return: empty list

        '''

        self.products = list()
        self.counts = list()
    

    def put(self, product: Product, count: int):
        ''' Method put.

            Checks if the user's value is valid and then adds it to the lists (to the cart).

            :return: completed list

        '''

        if not isinstance(product, Product):
            raise TypeError (f'product {product} is not Product instance')
        if not isinstance(count, float):
            raise TypeError (f'count {count} is not float. You must enter a number' )

        self.products.append(product)
        self.counts.append(count)


    def total(self):
        ''' Method total.

            Calculate the entire value of the item in the cart.

            :return: string of total price of product in cart.

        '''

        total_var = 0.0
        for count, product in zip(self.counts, self.products):
            total_var += count * product.price
        
        total_var = f'The price of all products in the cart is equal {total_var} grn.'
        
        return total_var


    def totally_edible(self):
        ''' Method totally edible.

            Check for inedible goods.

            :return: string of inedible of product in cart.

        '''
        total_ed = 0 
        for product in self.products:
            print(product.get_info(), f'Is the product edible? =', product.is_edible(product))
            if 'household chemicals' in product.category:
                total_ed += 1
        
        if total_ed >= 1:
            print('not all products are edible')
        else:
            print('all products are edible')

cart = Cart()

# ============================================================================
#                             КАТАЛОГ ТОВАРОВ
# ============================================================================


# ----------------------------------------------------------------------------
#                           СЪЕДОБНЫЕ ПРОДУКТЫ
# ----------------------------------------------------------------------------


apples = Product(15.90, 'Apples', 'edible', 'kg') 
bananas = Product(32.90, 'Bananas', 'edible', 'kg')
bread = Product(24.48, 'Bread', 'edible', 'loaf')
beets = Product(7.90, 'Beet', 'edible', ' kg')
carrots = Product(9.90, 'Carrots', 'edible', 'kg')
chicken_meat = Product(65.35, 'Chicken meat', 'edible', 'kg')
cheese = Product(130.90, 'Cheese', 'edible', ' kg')
cow_meat = Product(159.13, 'Cow meat', 'edible', ' kg')
milk = Product(26.13, 'Milk', 'edible', ' liter')
pork_meat = Product(118.33, 'Pork meat', 'edible', ' kg')
pickled_cucumbers = Product(34.90, 'Pickled cucumbers', 'edible', ' kg')
potatoes = Product(8.90, 'Potatoes', 'edible', ' kg')
salt = Product(6.00, 'Salt', 'edible', ' kg')
tomatoes = Product(37.90, 'Tomatoes', 'edible', ' kg') 


# ----------------------------------------------------------------------------
#                           АЛКОГОЛЬНЫЕ ПРОДУКТЫ
# ----------------------------------------------------------------------------


beer = Product(32.80, 'Beer', 'alcohol', ' liter')
champagne = Product(349, 'Champagne', 'alcohol', 'three quarters liter')
cider = Product(38.70, 'Cider', 'alcohol', ' liter')
cognac = Product(374, 'Cognac', 'alcohol', 'half liter')
moonshine = Product(70, 'Moonshine', 'alcohol', ' liter')
rum = Product(198, 'Rum', 'alcohol', 'half liter')
vine = Product(142, 'Vine', 'alcohol', 'three quarters liter')
vodka = Product(89.40, 'Vodka', 'alcohol', 'half liter')
whiskey = Product(458, 'Whiskey', 'alcohol', 'half liter')


# ----------------------------------------------------------------------------
#                          ПРОДУКТЫ БЫТОВОЙ ХИМИИ
# ----------------------------------------------------------------------------


pipe_cleaning = Product(24.75, 'Pipe_cleaning', 'household chemicals', '100 grams')
toilet_cleaner = Product(72.44, 'Toilet_cleaner', 'household chemicals', ' liter')
capsules_for_washing = Product(161.30, 'Capsules_for_washing', 'household chemicals', '10 pieces')
dishwashing_detergent = Product(32, 'Dishwashing_detergent', 'household chemicals', 'half liter')
refresh_the_air = Product(69.65, 'Refresh_the_air', 'household chemicals', 'half liter')
hygiene_unit_for_toilet = Product(65.80, 'Hygiene_unit_for_toilet', 'household chemicals', '100 grams') 
means_for_removing_stains_and_reinforcing_washing_powder = Product(83, 'Means_for_removing_stains_and_reinforcing_washing_powder', 'household chemicals', 'half liter')
whiteness = Product(22.20, 'Whiteness', 'household chemicals', ' kg')
washing_powder = Product(55.10, 'Washing powder', 'household_chemicals', ' kg')


products, counts = [], []
while True:
    ''' Cycle to fill the cart
    '''
     
    product = eval(input('Enter the product you want to add to cart: ').lower())
    count = NUMexam.floatexam(input('Enter the quantity of this product: '))
    cart.put(product, count)
    products.append(product), counts.append(count)
    user_input = input(
    'Would you like to continue adding products to cart? \
     Enter "Nothing enter" to continue", " "No" to stop": '
    ).title()
    print(user_input)
    if user_input == 'No':
        break


print(cart.products, cart.counts)
print(product.price_total())
print(cart.total())
cart.totally_edible()