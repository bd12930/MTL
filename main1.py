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
        print(f'<div class="carousel-item container-fluid">')
        print(f'<h2 class="testimonial-text1" >“{row[0]}” </h2>')
        print(f'<img class="testimonial-image1" src="http://bishun.strokeorder.info/characters/{row[1]}.gif" alt="budi">')
        print(f'<em>{row[3]}</em>')
        print(f'<div class="carousel-caption d-none d-md-block">')
        print(f'<h2 class="testimonial-text3" >{row[4]}</h2>')
        print('</div></div>')

        print(f'<div class="carousel-item container-fluid">')
        print(f'<h2 class="testimonial-text2">“{row[0]}”</h2>')
        print(f'<img class="testimonial-image2" src="http://bishun.strokeorder.info/characters/{row[1]}.gif" alt="budi">')
        print(f'<em>{row[2]}</em></div>')

        print(f'<div class="carousel-item container-fluid">')
        print(f'<img class="testimonial-image2" src="http://bishun.strokeorder.info/characters/{row[1]}.gif" alt="budi">')
        print('</div>')

# print("容易")

#     kata_baru[0] = {
#         kanji: "容易", gambar: "648422", pinyin: "Róngyì", meaning: "easy",
#         contoh: "语法 很 容易"};