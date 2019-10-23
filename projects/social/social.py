import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()
    
    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for user in range(0, numUsers):
            self.addUser(user)
        # Create friendships
        totalFriendships = numUsers * avgFriendships
        times_to_call_addFriendship = totalFriendships // 2
        userIds = range(1, numUsers + 1)
        
        print("Times Friends", times_to_call_addFriendship)
        
        friends = []
        for user in userIds:
            for friend in range(user + 1 , numUsers + 1):
                friends.append((user, friend))

        friends_to_make = friends[0:times_to_call_addFriendship]
        #shuffle the list
        random.shuffle(friends)
        print("FRIENDS", friends)
        # (10, 2) ----> friends has 45 possible friendships
        #but we want to call self.addFriendship 10 times, to make
        #20 total friendships so we only take 10 friendship combos
        #from the front of our list
        for friendship in friends_to_make:
            self.addFriendship(friendship[0], friendship[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        #look for userId and a list of friends
        if userID in self.friendships:
            for idx in range
        return visited

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
