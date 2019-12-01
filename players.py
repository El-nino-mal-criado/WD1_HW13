import json

class Player:
    def __init__(self, first_name="Name", last_name="Surname", weight_kg=100, height_cm=180.2): #konstruktor objekta je funkcija init
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

class BasketballPlayer(Player):
    def __init__(self, first_name="Name", last_name="Surname", weight_kg=100, height_cm=180.2, points=0, rebounds=0, assists=0):
        super().__init__(first_name, last_name, weight_kg, height_cm)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

class FootballPlayer(Player):
    def __init__(self, first_name="Name", last_name="Surname", weight_kg=100, height_cm=180.2, goals=0, yellow_cards=0, red_cards=0):
        super().__init__(first_name, last_name, weight_kg, height_cm)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards

def enter_data():
    entry = True
    basketball_players = []
    football_players = []
    while entry:
        type_or_player = input("Whom would you like to enter data for? Choose between (football player or basketball player): ").strip().lower()
        if type_or_player == "basketball player":
            player = BasketballPlayer()
            player.first_name = input("Enter player's first name: ").strip().lower().title()
            player.last_name = input("Enter player's last name: ").strip().lower().title()
            player.height_cm = input("Enter player's height in cm: ").strip()
            player.weight_kg = input("Enter player's weight in kg: ").strip()
            player.points = input("Enter the number of points of the player: ").strip()
            player.rebounds = input("Enter the number of rebounds of the player: ").strip()
            player.assists = input("Enter the number of assists of the player: ").strip()
            basketball_players.append(player)

            reentry = input("Would you like to make another entry (yes/no)? ").strip().lower()
            if reentry == "no":
                entry = False
        elif type_or_player == "football player":
            player = FootballPlayer()
            player.first_name = input("Enter player's first name: ").strip().lower().title()
            player.last_name = input("Enter player's last name: ").strip().lower().title()
            player.height_cm = input("Enter player's height in cm: ").strip()
            player.weight_kg = input("Enter player's weight in kg: ").strip()
            player.goals = input("Enter the number of goals of the player: ").strip()
            player.yellow_cards = input("Enter the number of yellow cards of the player: ").strip()
            player.red_cards = input("Enter the number of red cards of the player: ").strip()
            football_players.append(player)

            reentry = input("Would you like to make another entry (yes/no)? ").strip().lower()
            if reentry == "no":
                entry = False
        else:
            print("ERROR: Please reenter a type of player! Either 'football player' or 'basketball player'!")

    return basketball_players, football_players

def write_to_file(basketball_players, football_players):
    if(len(basketball_players) != 0):
        with open("basketball_players.txt", "a") as output_file:
            for player in basketball_players:
                output_file.write(json.dumps(player.__dict__)+"\n")

    if (len(football_players) != 0):
        with open("football_players.txt", "a") as output_file:
            for player in football_players:
                output_file.write(json.dumps(player.__dict__)+"\n")

if __name__ == "__main__":
    basketball_players, football_players = enter_data()
    write_to_file(basketball_players, football_players)
