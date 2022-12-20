import pickle


def save_profile(player):
    """Serialize the player and save the data in 'Player_profiles'"""

    with open(f"Player_profiles/{player.name}.dat", 'wb') as file:
        pickle.dump(player, file)
    file.close()


def load_profile(player_name):
    """Deserialize the player profile with name 'player_name'"""
    
    try:
        with open(f"Player_profiles/{player_name}.dat", 'rb') as file:
            data = pickle.load(file)
    except FileNotFoundError:
        return "Profile not found"

    return data