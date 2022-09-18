from Domain.Movie import Movie
from Service.MovieCatalogue import MovieCatalogue as mc

option = None
while option != 4:
    try:
        print('Options: ')
        print('1. Add Movie')
        print('2. List Movies')
        print('3. Delete Movies Catalogue')
        print('4. Exit')
        option = int(input('Type your option (1-4):'))

        if option == 1:
            movie_name = input('Add a Movie: ')
            movie = Movie(movie_name)
            mc.add_movie(movie)
        elif option == 2:
            mc.movie_list()
        elif option == 3:
            mc.delete_movies()

    except Exception as e:
        print(f'Error {e}')
        option = None
else:
    print('Exiting program...')