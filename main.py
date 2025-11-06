from write.models.Movie import Movie
from read.read_data import read_movie
from write.manip_data import addmovie, updatemovie, deletemovie
from write.exceptions import InvalidNumberException, InvalidAgeLimitException, InvalidGenreException, InvalidTitleException, InvalidYearException

##### nav
def nav():
    print("====== GESTION BIBLIOTHEQUE ======")
    print("====== 1. Voir les films ======")
    print("====== 2. ajouter un film ======")
    print("====== 3. modifier un film ======")
    print("====== 4. supprimer un film ======")
    print("====== 0. Quitter ======")

##### exception
def is_title_valid():
    user_title_movie = input("Choisissez le nom de votre film ")

    if user_title_movie.isspace():
        raise InvalidTitleException.InvalidTitleException("Le titre n'est un titre !") 
    else:
        return user_title_movie
    
def is_annee_valid():
    user_annee_prod_movie = input("Choisissez l'année de production: ")

    if user_annee_prod_movie.isspace():
        raise InvalidTitleException.InvalidTitleException("l'année n'est pas valide !") 
    elif not user_annee_prod_movie.isdigit():
        raise InvalidTitleException.InvalidTitleException("l'année n'est pas valide !") 
    else:
        return int(user_annee_prod_movie)
    
def is_genre_valid():
    user_genre_movie = input("Choisissez le GENRE de votre film ")

    if user_genre_movie.isspace():
        raise InvalidTitleException.InvalidTitleException("Le genre n'ets pas bon !") 
    elif not user_genre_movie.isalpha():
        raise InvalidTitleException.InvalidTitleException("l'age n'est pas valide !") 
    else:
        return user_genre_movie
    
def is_age_valid():
    user_age_limit = input("Choisissez le nom de votre film ")

    if user_age_limit.isspace():
        raise InvalidTitleException.InvalidTitleException("l'age n'est pas valide !") 
    elif not user_age_limit.isdigit():
        raise InvalidTitleException.InvalidTitleException("l'age n'est pas valide !") 
    else:
        return int(user_age_limit)

def is_valid_number():
    user_input = input("selectionner le numéro du film: ")

    if user_input.isdigit():
        return user_input
    else:
        raise InvalidNumberException.InvalidNumberException("La valeur inscrite n'est pas un numéro")

def main():
    while True:
        nav()
        user_input = input("Que voulez vous faire ? :")
        match user_input:
            case "1":
                read_movie()        
            case "2":
                try:
                    user_title_movie = is_title_valid()
                    user_annee_prod_movie = is_annee_valid()
                    user_genre_movie = is_genre_valid()
                    user_age_limit = is_age_valid()
                except InvalidTitleException.InvalidTitleException as e:
                    print(e)
                except InvalidYearException.InvalidYearException as e:
                    print(e)
                except InvalidGenreException.InvalidGenreException as e:
                    print(e)
                except InvalidAgeLimitException.InvalidAgeLimitException as e:
                    print(e)
                else:
                    addmovie(user_title_movie, user_annee_prod_movie, user_genre_movie, user_age_limit)
            case "3":
                try:
                    user_input = is_valid_number()
                except InvalidNumberException.InvalidNumberException as e:
                    print(e)
                else:
                    updatemovie(user_input)
            case "4":
                try:
                    user_input = is_valid_number()
                except InvalidNumberException.InvalidNumberException as e:
                    print(e)
                else:
                    deletemovie(user_input)
            case "0":
                print("🖐️  Merci et bonne journée")
                exit()
            case _:
                print("entrée inconnue...")

if __name__ == '__main__':
    main()