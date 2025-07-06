movies = [("28 years later", "Danny Boyle", 2025, 60000000)]

movie_name = input("Please enter your movie's name: ")
director = input("Please enter the director of this movie: ")
release_year = int(input("Please enter the year of this movie: "))
budget = int(input("Please enter the budget of this movie: "))

new_movie = (movie_name, director, release_year, budget)
print(f"{new_movie[0]}, {new_movie[2]}")

movies.append(new_movie)
print(movies[0])
print(movies[-1])

# movies.remove(movies[0])
# movies.pop(0)
del movies[0]
print(movies)
