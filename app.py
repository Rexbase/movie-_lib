menu_prompt = ("\n Enter 'a' - to add movie, 'l' - to see movies, 'f' - to find movie by title, or 'q' - to quit: \n")
movies = []

def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter movie director: ")
    year = input("Enter movie year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })

def show_movies():
    for movie in movies:
        print_movie(movie)


def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Year: {movie['year']}")


def find_movie():
    search__title = input("Enter movie title you're looking for: ")
    for movie in movies:
        if movie['title'] == search__title:
            print_movie(movie)
        else:
            print("The movie is not in the collection")


user_options = {
    "a": add_movie,
    "l": show_movies,
    "f": find_movie
}

def menu():
    selection = input(menu_prompt)
    while selection != 'q':
        if selection in user_options:
            selected_func = user_options[selection]
            selected_func()
        else:
            print("Unkown Command. Please try again!")
        selection = input(menu_prompt)


menu()
