import os

class MovieCatalogue:

    file_path = 'movies.txt'

    @classmethod
    def add_movie(cls, movie):
        with open(cls.file_path, 'a', encoding='utf8') as file:
            file.write(f'{movie.name}\n')

    @classmethod
    def movie_list(cls):
        with open(cls.file_path, 'r', encoding='utf8') as file:
            print('Movies Catalogue'.center(50,'-'))
            print(file.read())


    @classmethod
    def delete_movies(cls):
        os.remove(cls.file_path)
        print(f'Deleted file: {cls.file_path}')
