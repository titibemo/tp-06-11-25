import csv

def addmovie(user_title_movie, user_annee_prod_movie, user_genre_movie, user_age_limit):
        modified_data = []
        id = 0

        with open("read/data/movies.csv", "r", newline="", encoding="utf-8") as csv_file: 
            csv_reader = csv.reader(csv_file)
            for i, line in enumerate(csv_reader):
                modified_data.append(line)
                id = i
            new_movie = [id+1, user_title_movie, user_annee_prod_movie, user_genre_movie, user_age_limit]
            modified_data.append(new_movie)

        with open("read/data/movies.csv", "w", encoding="utf-8", newline="") as csv_file_write:
            writer = csv.writer(csv_file_write) 
            writer.writerows(modified_data)


def updatemovie(idMovie):
    user_title_movie = input("modification titre - Choisissez le nom de votre film ")
    user_annee_prod_movie = input("modification année - Choisissez l'année de production: ")
    user_genre_movie = input("modification genre - Choisissez le genre du film: ")
    user_age_limit = input("modification age - Choisissez l'age limit du film: ")

    modified_data = []
    id = 0

    with open("read/data/movies.csv", "r", newline="", encoding="utf-8") as csv_file: 
        csv_reader = csv.reader(csv_file)
        for i, line in enumerate(csv_reader):
            id = i
            if id == idMovie-1:
                line = [id+1, user_title_movie, user_annee_prod_movie, user_genre_movie, user_age_limit]
                print("ok")
            modified_data.append(line)

    with open("read/data/movies.csv", "w", encoding="utf-8", newline="") as csv_file_write:
        writer = csv.writer(csv_file_write) 
        writer.writerows(modified_data)

    
if __name__ == '__main__':
    pass

def deletemovie(idMovie):

    modified_data = []

    with open("read/data/movies.csv", "r", newline="", encoding="utf-8") as csv_file: 
        csv_reader = csv.reader(csv_file)
        for i, line in enumerate(csv_reader):
            modified_data.append(line)
        modified_data.pop(idMovie-1)
        print(modified_data)
        for i, line in enumerate(modified_data):
            if i == 0:
                continue
            line[0] = i
        print(modified_data)
            
    with open("read/data/movies.csv", "w", encoding="utf-8", newline="") as csv_file_write:
        writer = csv.writer(csv_file_write) 
        writer.writerows(modified_data)

    
if __name__ == '__main__':
    pass