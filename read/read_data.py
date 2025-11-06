import csv

def read_movie():
    fichier = open("./read/data/movies.csv", "rt")
    lecteurCSV = csv.reader(fichier, delimiter=",")
    for ligne in lecteurCSV:
        print(', '.join(ligne))
    fichier.close()

def read_movie_by_title(title):
    with open("./read/data/movies.csv", "rt") as fichier:
        lecteurCSV = csv.reader(fichier, delimiter=",")
        for ligne in lecteurCSV:
            if title.lower() in ligne[1].lower():
                print(', '.join(ligne))

if __name__ == '__main__':
    pass

# file_path3 = "E:/developpement web/TEST/python/POO/lesson 14 - writing files/output.csv"

# with open(file_path3, "w", newline="") as file: #newine avoid an enter between
#     writer = csv.writer(file) #writer provide method for csv file
#     for row in employee:
#         writer.writerow(row)
#     print(f"csv file {file_path3} was created")