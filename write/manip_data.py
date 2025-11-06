def addmovie():
    user_title_movie = input("Choisissez le nom de votre film ")
    user_annee_prod_movie = input("Choisissez l'année de production: ")
    user_genre_movie = input("Choisissez le genre du film: ")
    user_age_limit = input("Choisissez l'age limit du film: ")
    return user_title_movie, user_annee_prod_movie, user_genre_movie, user_age_limit
