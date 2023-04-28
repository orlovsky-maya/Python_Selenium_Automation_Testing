"""Locators on Catalog page"""

# Locators for Sauce Labs Backpack product on Products page
backpack_name = '#item_4_title_link .inventory_item_name'
backpack_price = 'div.inventory_item:nth-child(1) > div:nth-child(2)' \
                 ' > div:nth-child(2) > div:nth-child(1)'
backpack_add_button = 'add-to-cart-sauce-labs-backpack'

# Locators for Labs Bike Light product on Products page
bike_light_name = '#item_0_title_link .inventory_item_name'
bike_light_price = 'div.inventory_item:nth-child(2) > div:nth-child(2) > ' \
                   'div:nth-child(2) > div:nth-child(1)'
bike_light_add_button = 'add-to-cart-sauce-labs-bike-light'

# Locators for Sauce Labs Bolt T-Shirt product on Products page
bolt_t_shirt_name = '#item_1_title_link .inventory_item_name'
bolt_t_shirt_price = 'div.inventory_item:nth-child(3) > div:nth-child(2) > ' \
                   'div:nth-child(2) > div:nth-child(1)'
bolt_t_shirt_add_button = 'add-to-cart-sauce-labs-bolt-t-shirt'

# Locators for Sauce Labs Fleece Jacket product on Products page
fleece_jacket_name = '#item_5_title_link .inventory_item_name'
fleece_jacket_price = 'div.inventory_item:nth-child(4) > div:nth-child(2) > ' \
                   'div:nth-child(2) > div:nth-child(1)'
fleece_jacket_add_button = 'add-to-cart-sauce-labs-fleece-jacket'

# Locators for Sauce Labs Onesie product on Products page
onesie_name = '#item_2_title_link .inventory_item_name'
onesie_price = 'div.inventory_item:nth-child(5) > div:nth-child(2) > ' \
                   'div:nth-child(2) > div:nth-child(1)'
onesie_add_button = 'add-to-cart-sauce-labs-onesie'

# Locators for Test.allTheThings() T-Shirt (Red) product on Products page
t_shirt_red_name = '#item_3_title_link .inventory_item_name'
t_shirt_red_price = 'div.inventory_item:nth-child(6) > div:nth-child(2) > ' \
                   'div:nth-child(2) > div:nth-child(1)'
t_shirt_red_add_button = 'add-to-cart-test.allthethings()-t-shirt-(red)'

# Locator fo cart button
cart_button_loc = 'span.shopping_cart_badge'

"""Cart page"""

# Locators for product on Cart page
name_cart = '.inventory_item_name'
price_cart = '.inventory_item_price'
checkout_button_loc = 'checkout'

"""Checkout: Overview page"""

# Locators for product on Overview page
name_overview = '.inventory_item_name'
price_overview = '.inventory_item_price'
finish_button_loc = 'finish'
item_total_loc = '.summary_info .summary_subtotal_label'
