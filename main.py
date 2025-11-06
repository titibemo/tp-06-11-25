from write.models.Movie import Movie
from read.read_data import read_movie
from write.manip_data import addmovie, updatemovie, deletemovie
from write.exceptions import InvalidNumberException, InvalidAgeLimitException, InvalidGenreException, InvalidTitleException, InvalidYearException
from write.exceptions.validationInputs import is_title_valid, is_annee_valid, is_genre_valid, is_age_valid, is_valid_number

##### nav
def nav():
    print("====== GESTION BIBLIOTHEQUE ======")
    print("====== 1. Voir les films ======")
    print("====== 2. ajouter un film ======")
    print("====== 3. modifier un film ======")
    print("====== 4. supprimer un film ======")
    print("====== 0. Quitter ======")

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
                    updatemovie(user_input, user_title_movie, user_annee_prod_movie, user_genre_movie, user_age_limit)
            case "4":
                try:
                    user_input = is_valid_number()
                    user_title_movie = is_title_valid()
                    user_annee_prod_movie = is_annee_valid()
                    user_genre_movie = is_genre_valid()
                    user_age_limit = is_age_valid()
                except InvalidNumberException.InvalidNumberException as e:
                    print(e)
                except InvalidTitleException.InvalidTitleException as e:
                    print(e)
                except InvalidYearException.InvalidYearException as e:
                    print(e)
                except InvalidGenreException.InvalidGenreException as e:
                    print(e)
                except InvalidAgeLimitException.InvalidAgeLimitException as e:
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