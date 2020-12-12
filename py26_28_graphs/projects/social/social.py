import random


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif (
            friend_id in self.friendships[user_id]
            or user_id in self.friendships[friend_id]
        ):
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_friendship2(self, user_id, friend_id):
        if user_id == friend_id:
            return False
        elif (
            friend_id in self.friendships[user_id]
            or user_id in self.friendships[friend_id]
        ):
            return False

        self.friendships[user_id].add(friend_id)
        self.friendships[friend_id].add(user_id)
        return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_of_users, avg_num_of_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # these lines reset our graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # add users to the graph
        for i in range(1, num_of_users):  # start @ 1 to match id
            self.add_user(f"User {i}")

        target_friendships = num_of_users * avg_num_of_friendships
        total_friendships = 0

        while total_friendships < target_friendships:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)
            # from our amended add_friendship to return boolean
            if self.add_friendship2(user_id, friend_id):
                # inc by 2 since we're adding friendship to both users
                total_friendships += 2

        """
        # generate all combinations of friendships
        possible_friendships = []  # this is the performance bottleneck

        # loop through our users dict
        for user_id in self.users:
            # take advantage of sequential ids to avoid duplicates
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))  # tuple of friendship

        random.shuffle(possible_friendships)  # built-in method for shuffling!

        # b/c we're adding friendships in both directions, we need to floor divide by 2 (avoid floats)
        for i in range(num_of_users * avg_num_of_friendships // 2):
            friendship = possible_friendships[i]
            # self.add_friendship(friendship[0], friendship[1])
            self.add_friendship(*friendship)  # equivalent to ^^ as it unpacks the tuple
        """

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}

        q = [user_id]

        while len(q) > 0:
            user = q.pop(0)

            if user not in visited:
                visited[user] = list(self.friendships[user])

                for friend in self.friendships[user]:
                    q.append(friend)

        return visited


if __name__ == "__main__":
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    # connections = sg.get_all_social_paths(1)
    # print(connections)
