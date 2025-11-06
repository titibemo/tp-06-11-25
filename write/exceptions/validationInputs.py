from write.exceptions import InvalidNumberException, InvalidAgeLimitException, InvalidGenreException, InvalidTitleException, InvalidYearException

def is_title_valid():
    user_title_movie = input("Choisissez le nom de votre film ")

    if user_title_movie.isspace():
        raise InvalidTitleException.InvalidTitleException("Le titre n'est un titre !") 
    else:
        return user_title_movie
    
def is_annee_valid():
    user_annee_prod_movie = input("Choisissez l'année de production: ")

    if user_annee_prod_movie.isspace():
        raise InvalidYearException.InvalidYearException("l'année n'est pas valide !") 
    elif not user_annee_prod_movie.isdigit():
        raise InvalidYearException.InvalidYearException("l'année n'est pas valide !") 
    else:
        return int(user_annee_prod_movie)
    
def is_genre_valid():
    user_genre_movie = input("Choisissez le GENRE de votre film ")

    if user_genre_movie.isspace():
        raise InvalidGenreException.InvalidGenreException("Le genre n'ets pas bon !") 
    elif not user_genre_movie.isalpha():
        raise InvalidGenreException.InvalidGenreException("l'age n'est pas valide !") 
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
        raise InvalidAgeLimitException.InvalidAgeLimitException("La valeur inscrite n'est pas un numéro")
    
if __name__ == '__main__':
    pass