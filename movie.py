import json


class Recommender:
    def __init__(self, filename):
        self.user_data = {}
        with open(filename, "rt") as file:
            self.movie_data = json.load(file)
        self.parse_list()

    def add_user_movie(self, user, movie):
        if user not in self.user_data:
            self.user_data[user] = {movie}
        else:
            self.user_data[user].add(movie)

    def parse_list(self):
        for userdata in self.movie_data:
            if userdata[2] > 3:
                self.add_user_movie(userdata[0], userdata[1])

    def find_similar_users(self, username):
        similar_users = []
        user_movies = self.user_data[username]
        for checked_user, checked_data in self.user_data.items():
            if not user_movies.isdisjoint(checked_data):
                similar_users.append(checked_user)
        return similar_users

    def get_movies_from_users(self, user_list: list):
        movies = set()
        for user in user_list:
            movies.update(self.user_data[user])
        return movies

    def get_movies_watched_by_user(self, user_name):
        return [x[1] for x in self.movie_data if x[0] == user_name]

    def exclude_watched(self, user_name, movies: set):
        movies_watched = self.get_movies_watched_by_user(user_name)
        return movies.difference(movies_watched)

    def recommend(self, user_name):
        similar_users = self.find_similar_users(user_name)
        possible_movies = self.get_movies_from_users(similar_users)
        return self.exclude_watched(user_name, possible_movies)


def start():
    Netflix = Recommender("moviedata.json")
    print(Netflix.recommend("Dennis"))

if __name__ == "__main__":
    start()
