from write.models.Movie import Movie
from read.read_data import read_movie
from write.manip_data import addmovie, updatemovie, deletemovie

def nav():
    print("====== GESTION BIBLIOTHEQUE ======")
    print("====== 1. Voir les films ======")
    print("====== 2. ajouter un film ======")
    print("====== 3. modifier un film ======")
    print("====== 4. supprimer un film ======")
    print("====== 0. Quitter ======")

def main():
    pass
    # all_movie = [
    #     Movie("a", "b", "c", "d"),
    # ]1


    

    while True:
        nav()
        user_input = input("Que voulez vous faire ? :")
        match user_input:
            case "1":
                read_movie()        
            case "2":
                addmovie()
            case "3":
                user_input = int(input("selectionner le numéro du film à modifier: "))
                updatemovie(user_input)
            case "4":
                user_input = int(input("selectionner le numéro du film à effacer: "))
                deletemovie(user_input)
            case "0":
                print("🖐️  Merci et bonne journée")
                exit()

if __name__ == '__main__':
    main()