users ={
    "gaurav":{
        "Inception", "Titanic", "Avatar", "Interstellar", "The Dark Knight",
        "The Matrix", "Gladiator", "The Lion King", "Frozen", "Coco"
    },
    "sham":{
        "Titanic", "Avatar", "The Avengers", "Iron Man", "Captain America",
        "Thor", "Black Panther", "Doctor Strange", "Spider-Man", "Guardians of the Galaxy"
    },
    "sumit":{
        "Inception", "The Dark Knight", "Interstellar", "Memento", "Dunkirk",
        "Tenet", "The Prestige", "Shutter Island", "Se7en", "Fight Club"
    },
    "ajay":{
        "The Dark Knight", "Titanic", "Avatar", "Joker", "The Batman",
        "Man of Steel", "Justice League", "Aquaman", "Wonder Woman", "Suicide Squad"
    },
    "pawan": {
        "Frozen", "Coco", "Moana", "Zootopia", "Inside Out",
        "Toy Story", "Finding Nemo", "Up", "Monsters, Inc.", "Ratatouille"
    },
    "suraj":{
        "Gladiator", "Braveheart", "Troy", "300", "Alexander",
        "Kingdom of Heaven", "Ben-Hur", "Spartacus", "Hercules", "Clash of the Titans"
    },
    "rakesh":{
        "The Matrix", "The Matrix Reloaded", "The Matrix Revolutions", "John Wick", "John Wick 2",
        "John Wick 3", "Constantine", "Speed", "Point Break", "The Devil’s Advocate"
    },
    "chandu":{
        "The Lion King", "Aladdin", "Beauty and the Beast", "Mulan", "Pocahontas",
        "Tarzan", "Hercules", "Frozen", "Cinderella", "Sleeping Beauty"
    },
    "mahesh": {
        "Avengers: Endgame", "Avengers: Infinity War", "Iron Man", "Captain Marvel", "Black Panther",
        "Doctor Strange", "Spider-Man: No Way Home", "Shang-Chi", "Eternals", "Ant-Man"
    }
}

def similarity(users1 , users2):
    set1 , set2 = users["gaurav"], users["sham"]
    return len(set1 & set2)/ len(set1 | set2)

def recommend(target_user):
    scores = {}
    for other_user in users:
        if other_user != target_user:
            scores[other_user] = similarity(target_user, other_user)

    best_match = max(scores, key=scores.get)
    recommendations = users[best_match] - users[target_user]

    return best_match, recommendations
def show_menu():
    print("\n=== Movie Recommendation System ===")
    print("1. View all users")
    print("2. Add new user")
    print("3. Get recommendations")
    print("4. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            for user, movies in users.items():
                print(f"{user}: {movies}")

        elif choice == "2":
            name = input("Enter user name: ")
            movies = input("Enter movies (comma-separated): ").split(",")
            users[name] = set([m.strip() for m in movies])
            print(f"User {name} added successfully!")

        elif choice == "3":
            name = input("Enter user name to get recommendations: ")
            if name in users:
                best_user, recs = recommend(name)
                print(f"\nMost similar user to {name}: {best_user}")
                print(f"Recommendations for {name}: {recs}")
            else:
                print("User not found!")

        elif choice == "4":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
