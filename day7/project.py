movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

new_movie_count = int(input("Please enter how many movies you wish to add: "))

for _ in range(new_movie_count):
    name = input("Please enter your movie name: ")
    budget = int(input("Please enter the movie budget: "))
    new_movie = name, budget
    movies.append(new_movie)

print()

total_budget = 0
for movie in movies:
    total_budget += movie[-1]
average_budget = total_budget / len(movies)
print(f"The average budget of the movies is: ${average_budget}")

higher = 0
for movie in movies:
    diff = movie[-1] - average_budget
    if diff > 0:
        higher += 1
        print(f"The {movie[0]} has ${diff} higher than the average budget")
print(f"There are {higher} movies have the higher budget than the average budget")
