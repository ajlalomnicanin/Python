import math

# Zadaci
usd = float(input())
bgn = usd * 1.79549
print(str(bgn) + " bgn.")

#
radians = float(input())
angle = radians * 180 / math.pi
print(angle)

#
deposite_amount = float(input())
term_of_the_deposit = int(input())
annual_interest_rate = float(input())/100
amount = deposite_amount + term_of_the_deposit * ((deposite_amount * annual_interest_rate) / 12)
print(amount)

#
number_pages = int(input())
pages_read_hour = int(input())
number_of_days = int(input())

hours = number_pages / pages_read_hour
hours_per_day = hours / number_of_days
print(round(hours_per_day, 0))

#
package_of_pens = int(input())
package_of_markers = int(input())
list_of_detergent = int(input())
percentage = int(input())

total_price = 5.8 * package_of_pens + 7.2 * package_of_markers + 1.2 * list_of_detergent
discounted_price = total_price * (100 - percentage)/100
print(discounted_price)

#
nylon = int(input())
paint = int(input())
paint_thinner = int(input())
hours = int(input())

nylon_price = (nylon + 2) * 1.5
paint_price = (paint * 0.1) * 14.5
paint_thinner_price = paint_thinner * 5

total_price_mat = nylon_price + paint_price + paint_thinner_price + 0.4
price_per_hour = total_price_mat + 0.3
total_price_of_everything = total_price_mat + price_per_hour * hours

#
chickens = int(input())
fish = int(input())
vegetarian_menu = int(input())

total_price = chickens * 10.35 + fish * 12.4 + vegetarian_menu * 8.5
desert = total_price * 0.2

total_total_price = total_price * desert + 2.5
print(total_total_price)



