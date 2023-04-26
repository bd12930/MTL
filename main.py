# Python code to
# demonstrate readlines()
import csv
import sys
sys.stdout.reconfigure(encoding='utf-8')

#     kata_baru[0] = {
#         kanji: "容易", gambar: "648422", pinyin: "Róngyì", meaning: "easy",
#         contoh: "语法 很 容易"};
# Define data
data = [
    (1, "A towel,", 1.0),
    (42, " it says, ", 2.0),
    (1337, "is about the most ", -1),
    (0, "massively useful thing ", 123),
    (-2, "an interstellar hitchhiker can have.", 3),
]

# Write CSV file
# with open("test.csv", "wt") as fp:
#     writer = csv.writer(fp, delimiter=",")
#     # writer.writerow(["your", "header", "foo"])  # write header
#     writer.writerows(data)

# Read CSV file
with open("test.csv") as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"')
    # next(reader, None)  # skip the headers
    # data_read = [row for row in reader]
    counter = 0
    for row in reader:
        print(f'kata_baru[{counter}] = ''{')
        print(f'kanji:"{row[0]}",gambar:"{row[1]}",pinyin:"{row[2]}",meaning:"{row[3]}",')
        print(f'contoh:"{row[4]}"''};')
        counter += 1
# print("容易")

#     kata_baru[0] = {
#         kanji: "容易", gambar: "648422", pinyin: "Róngyì", meaning: "easy",
#         contoh: "语法 很 容易"};