import csv

max_sales = 0
best_selling_book = None
with(open('Bestseller - Sheet1.csv', 'r', encoding='utf-8')) as file:
    csv_reader = csv.reader(file)
    file.readline()

    for row in csv_reader:
        current_sales = float(row[4])
        if current_sales > max_sales:
            max_sales = current_sales
            best_selling_book = row


output_file_path = 'best_selling_book.csv'
with(open('../best_seller_info.csv', 'w', newline='')) as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Book','Author','Sales in million'])
    csv_writer.writerow([best_selling_book[0], best_selling_book[1], best_selling_book[4]])

print(output_file_path)