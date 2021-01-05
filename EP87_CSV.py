import csv
def readCSV():
    with open('Demo3.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            # ส่วนในการแสดงข้อมูล
            else:
                print(f'\t{row[0]} is my friend {row[1]} is movie feb, and adopt {row[2]}.')
                line_count += 1
        print(f'Processed {line_count} lines.')

def writeCSV():
    with open('employee_file.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # ส่วนการเพิ่มข้อมูล
        employee_writer.writerow(['Max Chans', 'Business Development', 'April'])
        employee_writer.writerow(['Rattana Lek', 'Sale', 'Febuary'])
        employee_writer.writerow(['Arkom Ex', 'Marketing', 'August'])

writeCSV()