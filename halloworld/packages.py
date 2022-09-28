# are a other way to organize our codes
# is a container for different modules
# for example our first one will be ecommerce
# you can import a directory or a package in two ways
# the first is the whole thing

#####
# import ecommerce.shipping
# ecommerce.shipping.calc_shipping()  # this is the longer method

# the other method
# from ecommerce.shipping import calc_shipping
# calc_shipping()
   # Or
from ecommerce import shipping
shipping.calc_shipping()