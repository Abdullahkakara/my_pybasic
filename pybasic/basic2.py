product_name = "sugar"
product_name = "egg"
product_name = "bottle"
product_name = "water"
product_name = "pin"
product_name = "Mobile"
Product_name = "Book"
Product_name = "Brash"
product_name = "Pen"
product_name = "Pad"

quan1 = 5
quan2 = 20
quan3 = 2
quan4 = 3
quan5 = 5 
quan6 = 70
quan7 = 40
quan8 = 52
quan9 = 90
quan10 = 82


price1 = 150
price2 = 10
price3 = 40 
price4 = 40
price5 = 8
price6 = 7000
price7 = 450
price8 = 32
price9 = 7
price10 = 210

total_price1 = price1 * quan1
total_price2 = price2 * quan2
total_price3 = price3 * quan3
total_price4 = price4 * quan4
total_price5 = price5 * quan5
total_price6 = price6 * quan6
total_price7 = price7 * quan7
total_price8 = price8 * quan8
total_price9 = price9 * quan9
total_price10 = price10 * quan10

print(total_price1,total_price2,total_price3,total_price4,total_price5,total_price6,total_price7,total_price8,total_price9,total_price10)

discount = 10

total = total_price1 + total_price2 + total_price3 + total_price4 + total_price5 + total_price6 + total_price7 + total_price8 + total_price9 + total_price10

total_after_discount = total-(total * discount)/100

print(total)
print(total_after_discount)