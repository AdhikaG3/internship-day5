class InstagramAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
        self.__followers = []
        self.__archived_reels = ["Travel Reel", "Food Reel"]

    # Getter to check followers
    def get_followers(self):
        return self.__followers

    # Setter to add follower
    def add_follower(self, name):
        self.__followers.append(name)
        print(name, "is now following", self.username)

    # View archived reels with password
    def view_archived_reels(self, password):
        if password == self.__password:
            print("Archived Reels:", self.__archived_reels)
        else:
            print("Wrong password. Access denied.")

    # Update password with validation
    def update_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password updated successfully.")
        else:
            print("Old password is incorrect.")


# Creating object
account = InstagramAccount("user_01", "insta123")

account.add_follower("Adhika")
account.view_archived_reels("insta123")
account.update_password("insta123", "newpass456")
