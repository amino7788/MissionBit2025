import csv

# Reads movie data from file
movies = []

with open("sports.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        movies.append(row)


# Pick one movie by index number, minimum 0 to length of all movies
def pick_movies():
    try:
        number = int(input(f"Enter the movie number (0 to {len(movies) - 1}): "))
        if 0 <= number < len(movies):
            movie = movies[number]
            print("Title:", movie[1])
            print("Genres:", movie[5])
            print("Rating:", movie[6])
            try:
                rating = float(movie[6])
                if rating >= 8:
                    print("Great movie!")
                elif rating >= 5:
                    print("Okay movie")
                else:
                    print("Not worth watching")
            except:
                print("No rating")
        else:
            print("Number out of range.")
    except:
        print("Invalid input, please enter a number.")


# Show average rating of all movies, finds total ratings +'d up / by length of all movie ratings
def show_average(movies):
    ratings = []
    for movie in movies:
        try:
            rating = float(movie[6])
            ratings.append(rating)
        except:
            continue
    if len(ratings) > 0:
        print("The average rating:", sum(ratings) / len(ratings))
    else:
        print("No ratings found.")


# Shows highest rated movie, iterates thru all ratings & replaces best rating & compares against all other
def show_best():
    best_rating = 0
    best_movie = None
    for movie in movies:
        try:
            rating = float(movie[6])
            if rating > best_rating:
                best_rating = rating
                best_movie = movie
        except:
            continue
    if best_movie:
        print("Best movie:", best_movie[1])
        print("Rating:", best_movie[6])
    else:
        print("No ratings found.")


# Show movies by genre, depending on if genre makes found true/false
def find_by_genre():
    genre = input("Type a genre to look for: ")
    found = False
    for movie in movies:
        if genre.lower() in movie[5].lower():
            print("Title:", movie[1])
            print("Genres:", movie[5])
            print("Rating:", movie[6])
            found = True
    if not found:
        print("No movies found with that genre.")


# Main while loop, else-ifs for choice selections & all functions called
while True:
    print("\nMovie Pick")
    print("1 - Pick a movie by number")
    print("2 - Show average rating")
    print("3 - Show best movie")
    print("4 - Find movies by genre")

    choice = input("Pick an option (1-4): ")

    if choice == "1":
        pick_movies()
    elif choice == "2":
        show_average(movies)
    elif choice == "3":
        show_best()
    elif choice == "4":
        find_by_genre()
    else:
        print("Not a choice.")

    again = input("Do you want to do something else? (yes/no): ")
    if again.lower() == ("no" or "n"):
        print("Bye!")
        break

    # Improvements: Add if-else statement for answering yes to again, add strip to remove any spaces & better formatting generally
