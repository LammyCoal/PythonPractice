import csv

highest_sales = 0
highest_sales_book = None

with open('Bestseller - Sheet1.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    file.readline()

    for row in csv_reader:
        sales = float(row[4])
        if sales > highest_sales:
            highest_sales = sales
            highest_sales_book = row
            print(highest_sales_book)

with open('Bestseller_info.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Book','Author','Sales in million'])
    csv_writer.writerow([highest_sales_book[0],highest_sales_book[1],highest_sales_book[4]])


#Another example on csv writing and reading

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]

try:
    with open('packing_list.csv', 'r',encoding='utf-8') as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            print(row)
except FileNotFoundError:
    print('Packing list not found.Creating a new one')

    with open('packing_list.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)