import INTexam
class Product:
    def __init__(self, price, product_name, category, unit ):
        self.price = price
        self.category = category
        self.product_name = product_name
        self.unit = unit
        
    
    def is_edible (self, category: str) -> bool:
        if self.category != 'household chemicals':

            return True
        else:

            return False

    
    def price_total (self):
        n = INTexam.intexam(input('Введите номер товара(начало с 1): '))
        product_total_price = 0
        print (self.price)
        product_total_price = counts[n] * products[n].price

        return product_total_price

    def get_info(self) -> str:

        return f'{self.product_name} {self.price} for {self.unit}. '


class Cart:
    def __init__(self):
        self.products = list()
        self.counts = list()
    
    def put(self, product: Product, count: int):
        if not isinstance(product, Product):
            raise TypeError (f'product {product} is not Product instance')
        if not isinstance(count, int):
            raise TypeError (f'count {count} is not integer' )

        self.products.append(product)
        self.counts.append(count)

    def total(self):
        total_var = 0.0
        for count, product in zip(self.counts, self.products):
            total_var += count * product.price

        return total_var


    def totally_edible(self):
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

apple = Product(15.90, 'Apple', 'edible', '1 kg') 
banana = Product(32.90, 'Banana', 'edible', '1 kg')
bread = Product(24.48, 'Bread', 'edible', '1 piece')
beet = Product(7.90, 'Bbeet', 'edible', '1 kg')
carrot = Product(9.90, 'Ccarrot', 'edible', '1 kg')
chicken_meat = Product(65.35, 'Cchicken_meat', 'edible', '1 kg')
cheese = Product(130.90, 'Cheese', 'edible', '1 kg')
cow_meat = Product(159.13, 'Cow_meat', 'edible', '1 kg')
milk = Product(26.13, 'Milk', 'edible', '1 liter')
pork_meat = Product(118.33, 'Pork_meat', 'edible', '1 kg')
pickle = Product(34.90, 'Pickle', 'edible', '1 kg')
potato = Product(8.90, 'Potato', 'edible', '1 kg')
salt = Product(6.00, 'Salt', 'edible', '1 kg')
tomato = Product(37.90, 'Tomato', 'edible', '1 kg') 

beer = Product(32.80, 'Beer', 'alcohol', '1 liter')
champagne = Product(349, 'Champagne', 'alcohol', 'three quarters liter')
cider = Product(38.70, 'Cider', 'alcohol', '1 liter')
cognac = Product(374, 'Cognac', 'alcohol', 'half liter')
moonshine = Product(70, 'Moonshine', 'alcohol', '1 liter')
rum = Product(198, 'Rum', 'alcohol', 'half liter')
vine = Product(142, 'Vine', 'alcohol', 'three quarters liter')
vodka = Product(89.40, 'Vodka', 'alcohol', 'half liter')
whiskey = Product(458, 'Whiskey', 'alcohol', 'half liter')

pipe_cleaning = Product(24.75, 'Pipe_cleaning', 'household chemicals', '100 grams')
toilet_cleaner = Product(72.44, 'Toilet_cleaner', 'household chemicals', '1 liter')
capsules_for_washing = Product(161.30, 'Capsules_for_washing', 'household chemicals', '10 pieces')
dishwashing_detergent = Product(32, 'Dishwashing_detergent', 'household chemicals', 'half liter')
refresh_the_air = Product(69.65, 'Refresh_the_air', 'household chemicals', 'half liter')
hygiene_unit_for_toilet = Product(65.80, 'Hygiene_unit_for_toilet', 'household chemicals', '100 grams') 
means_for_removing_stains_and_reinforcing_washing_powder = Product(83, 'Means_for_removing_stains_and_reinforcing_washing_powder', 'household chemicals', 'half liter')
whiteness = Product(22.20, 'Whiteness', 'household chemicals', '1 kg')
washing_powder = Product(55.10, 'Washing powder', 'household_chemicals', '1 kg')

while True:
    products, counts = [None], [None]
    product = eval(input('Введите продукт, который хотите положить в корзину: ').lower())
    count = INTexam.intexam(input('Введите количество этого продукта: '))
    cart.put(product, count)
    products.append(product), counts.append(count)

    user_input = input('Хотите положить еще товар в корзину? "Yes", "No"').title()
    print(user_input)
    if user_input == 'No':
        break
  
print(cart.products, cart.counts)
print(product.price_total())
print(cart.total())
cart.totally_edible()