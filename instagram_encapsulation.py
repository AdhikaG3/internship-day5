# Creating account
account = InstagramAccount("adhika_official", "1234")

# Adding followers
account.add_follower("rahul")
account.add_follower("ananya")

# Adding reels
account.add_private_reel("Vacation Reel")
account.add_archived_reel("Old Memories Reel")

# Viewing private reels
account.view_private_reels("rahul")      # allowed
account.view_private_reels("unknown")    # denied

# Viewing archived reels
account.view_archived_reels("1234")      # allowed
account.view_archived_reels("0000")      # denied

# Changing password
account.change_password("1234", "newpass")
