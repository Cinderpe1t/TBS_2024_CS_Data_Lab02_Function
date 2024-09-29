"""
Name: Angelina Kim
Date: Fall 2024
Purpose: A Choose-Your-Own-Adventure game where the user simulates an escape
        (or failure to escape) from their captors.
"""

import textwrap
from typing import Tuple
from typing import Union

class Player:
    """Stores player information"""
    def __init__(self) -> None:
        self.game_stage = ""
    
    def set_game_stage(self, stage:str = "Start") -> str:
        """Set player's game stage"""
        self.game_stage = stage
        return self.game_stage 

    def append_game_stage(self, stage:str = "") -> str:
        """Append player's game stage"""
        self.game_stage += stage
        return self.game_stage 
    
# Satisfies 6
def print_string_line(string_to_repeat:str, number_of_string:int = 80, 
                      line_end = "\n") -> None:
    """Print a decoration and separation line"""
    for i in range(number_of_string):
        # Satisfies 1
        print(string_to_repeat, end = "")
    print(line_end, end = "")
    return None

# Satisfies 8, 9
def print_title(decoration_string:str, /, **string_setup:int) -> None:
    """Print game title"""
    string_width = 80
    string_height = 1
    if 'string_width' in string_setup:
        string_width = string_setup["string_width"]
    if 'string_height' in string_setup:
        string_height = string_setup["string_height"]
    
    # Satisfies 4, 5, 6A
    for i in range(string_height):
        print_string_line(string_to_repeat = decoration_string, 
                          number_of_string = string_width)
    
    # Satisfies 1, 2, 4
    print("The Escape from the Kingdom - A Quest for Survival", 
          "by Angelina Kim", sep = "\n", end = "\n")
    print("")
    
    # Satisfies 2, 3, 6B
    for i in range(string_height):
        print_string_line(decoration_string, string_width, "\n")
    print("Welcome to the game")
    return None

# Satisfies 7
def print_story(*paragraphs:str, line_width:int = 80, 
                line_spacing:int = 1) -> None:
    """Print long series of paragraphs with wrap around"""
    for paragraph in paragraphs:
        # Satisfies 1
        paragraph_wrapped = textwrap.wrap(paragraph, width = line_width)
        for line in paragraph_wrapped:
            print(line)
        for i in range(line_spacing):
            print("")
    return None

# Satisfies 7, 11, 12
def get_response(*choices: Tuple[Union[int, str], str]) \
                    -> (Union[int, str], str):
    """Print user choices and collect user response"""
    # Print choices
    for item in choices:
        (index, choice) = item
        print(str(index), ") ", choice)
    choice = ""

    # Input loop
    while choice == "":
        try:
            response = input("Enter your choice: ")
            for pair in choices:
                # If string
                if type(pair[0]) == str:
                    # Compare lowercase
                    if str.lower(pair[0]) == str.lower(response):
                        choice = pair[1]
                        response = str.lower(response)
                # If integer
                elif type(pair[0]) == int:
                    if pair[0] == int(response):
                        choice = pair[1]
            # If response does not match out of the choices
            if choice == "":
                print("Your input", response, "is invalid")
        except ValueError as e:
            print("!!! That's not a valid input")
    return (response, choice)

# Satisfies 13
def illegal_function_call_restricted_position() -> None:
    """Demonstrate illegal function call with keyword on position parameter"""
    print_string_line("!", 80, "\n")
    print("Function test")
    print("Illegal function call with keyword for a restricted position "\
          "parameter")
    print("try: ")
    print('    print_title(decoration_string = "*")')
    # Satisfies 13
    try: 
        print_title(decoration_string = "*")
    except TypeError as e:
        print("!!! Function parameter is incorrect:")
        print(e)
    print("End of function test")
    print_string_line("!", 80, "\n")
    return None
    
# Satisfies 14
def illegal_function_call_restricted_keyword() -> None:
    """Demonstrate illegal function call with parameter on keyword parameter"""
    print_string_line("!", 80, "\n")
    print("Function test")
    print("Illegal function call with position for a restricted keyword "\
          "parameter")
    print("try:")
    print("     print_congratulation(3, 1)")
    # Satisfies 14
    try: 
        print_congratulation(3, 1)
    except TypeError as e:
        print("!!! Function parameter is incorrect:")
        print(e)
    print("End of function test")
    print_string_line("!", 80, "\n")
    return None

# Satisfies 10 
def print_congratulation(*, column_of_cup = 1, row_of_cups = 1) -> None:
    """Print congratulation message"""
    # Set cup data
    cup=[]
    cup.append(" ____________________ ")
    cup.append(" |                  | ")
    cup.append("(| CONGRATULATIONS! |)")
    cup.append(" |                  | ")
    cup.append("  \\                 / ")
    cup.append("   `-——————————————'  ")
    cup.append("   _|_____________|_  ")
    
    # Repeat cut as defined by the parameters
    for i in range(row_of_cups):
        for cup_row in cup:
            for j in range(column_of_cup):
                # Satisfies 1
                print(cup_row, end="")
            print()
    return None

# Main setup
def main():
    # Catch keyboard interruption
    try:
        player = Player()
        try: 
            player.set_game_stage(stage = "Start")
        except TypeError as e:
            print("!!! Function parameter is incorrect:")
            print(e)

        # Main game loop
        while player.game_stage != "End": 
            match player.game_stage:
                case "Start":
                    # Print title
                    # Satisfies 1
                    print_title("*", string_width = 80)

                    # Satisfies #13
                    illegal_function_call_restricted_position()
                    player.set_game_stage("Q1")

                case "Q1":
                    print_string_line("-")
                    line1 = "You wake up in a dark prison. A troll bangs on "\
                        "the bars of your cell."
                    line2 = '“Wake up! It’s time to fight.”'
                    line3 = "He offers you 3 options: a glowing sword, a "\
                        "beautiful shield, or a stone. The only information "\
                        "you receive is that you will be fighting the world's "\
                        "most powerful wizard."
                    print_story(line1, line2, line3)
                    (response, choice) = get_response((1, "Sword"), \
                                                      (2, "Shield"), \
                                                      (3, "Stone"))
                    player.append_game_stage("," + choice)

                case "Q1,Sword":
                    print_string_line("-")
                    line1 = "You choose SWORD."
                    line2 = "As you enter the arena, you see that your "\
                        "opponent is a small, bearded man (think Dumbledore "\
                        "in Harry Potter). Do you make the first move?"
                    print_story(line1, line2)
                    (response, choice) = get_response(("a", "Yes"), \
                                                      ("b", "No"))
                    player.append_game_stage("," + choice)

                case "Q1,Sword,Yes":
                    print_string_line("-")
                    line1 = "You choose to make the first move."
                    line2 = '”YAHHHH!” you scream as you run towards the '\
                        'wizard. Suddenly, a bright light beams out of your '\
                        'sword and flashes by the side of the wizard. You are '\
                        'confused. Everyone is confused. Except the troll who '\
                        'offered you the sword before the match. You try to '\
                        'swing again, and another bright light shines out of '\
                        'the sword, hitting just above the wizard’s head. The '\
                        'entire crowd is silent. Because instead of hitting '\
                        'the wizard, the light engulfs the king in flames. A '\
                        'group of soldiers begin to run to you.'
                    line3 = "What do you do?"
                    print_story(line1, line2, line3)
                    (response, choice) = \
                        get_response(("a", "Fight the soldiers"), 
                                     ("b", "Run away"))
                    player.append_game_stage("," + choice)
                    if response == "b":
                        player.set_game_stage("Run away")

                case "Q1,Sword,Yes,Fight the soldiers":
                    print_string_line("-")
                    line1 = "Though your sword seems very formidable, the "\
                        "guards overpower you, and you are executed by the "\
                        "queen within minutes."
                    print_story(line1)
                    player.set_game_stage("Game over")

                case "Run away":
                    print_string_line("-")
                    line1 = "You try to run away, but you encounter 3 tunnels "\
                        "on your way out. The first tunnel on the left emits "\
                        "a rotten-egg smell, the second is bright red, and "\
                        "the third is completely silent. Which tunnel do you "\
                        "select?"  
                    print_story(line1)
                    (response, choice) = get_response((1, "First"), \
                                                      (2, "Second"), \
                                                      (3, "Third"))
                    player.append_game_stage("," + choice)

                case "Run away,First":
                    print_string_line("-")
                    line1 = "As you walk into the dark tunnel, you suddenly "\
                        "get the feeling of being watched. You continue to "\
                        "sprint down the tunnel, tripping over the sticks (or "\
                        "bones?) of objects you cannot see. You step into a "\
                        "large, musty cavern with many stalactites."
                    line2 = "As you peer deeper into the cave, the top of the "\
                        "cave begins to close down on you."
                    line3 = "You step into the maws of a dragon and are eaten "\
                        "and digested within minutes"
                    print_story(line1)
                    player.set_game_stage("Game over")

                case "Run away,Second":
                    print_string_line("-")
                    line1 = "As you walk into the dark tunnel, a strong, iron "\
                        "scent engulfs you. Was the red on the walls blood? "\
                        "You start to run out of the tunnel, but a dull "\
                        "object hits your head from behind you, and the world "\
                        "fades into black."
                    print_story(line1)
                    player.set_game_stage("Game over")

                case "Run away,Third":
                    print_string_line("-")
                    line1 = "As you walk in, you lose all capability to see "\
                        "because of the darkness. You continue, but there "\
                        "seems to be no light at the end of the tunnel "\
                        "(literally). Do you keep on walking or turn around?"
                    print_story(line1)
                    (response, choice) = \
                        get_response(("a", "Keep on walking"), 
                                     ("b", "Turn around"))
                    player.append_game_stage("," + choice)

                case "Run away,Third,Keep on walking":
                    print_string_line("-")
                    line1 = "You keep on walking for hours (or is it days? "\
                        "You have no way to keep track of time here). "\
                        "Suddenly, a pinprick of light beams down from ahead "\
                        "of you. You race towards it, and find an abandoned "\
                        "ladder and a hole leading to fresh air."
                    line2 = "You eagerly climb the ladder, entering a homey "\
                        "village where you can recuperate and begin your new "\
                        "life."
                    print_story(line1, line2)
                    player.set_game_stage("End of game")

                case "Run away,Third,Turn around":
                    print_string_line("-")
                    line1 = "As soon as you turn around, you encounter a "\
                        "group of soldiers searching for you. Though your "\
                        "weapon seems very formidable, the guards overpower "\
                        "you, and you are slaughtered within minutes."
                    print_story(line1)
                    player.set_game_stage("Game over")

                case "Q1,Sword,No":
                    print_string_line("-")
                    line1 = "You don’t make the first move. Instead, you "\
                        "watch as the wizard beams out a bright green light "\
                        "from his palms. As the light approaches you, you "\
                        "slash out with your sword, which somehow makes the "\
                        "light bounce back to the wizard and hit him in the "\
                        "face."
                    line2 = "You decide not to swing again—perhaps out of "\
                        "worry for the poor wizard, who seems to be "\
                        "incapacitated on the ground. You are crowned as the "\
                        "next champion!"
                    print_story(line1, line2)
                    player.set_game_stage("End of game")

                case "Q1,Shield":
                    print_string_line("-")
                    line1 = "You choose Shield."
                    line2 = "As you enter the arena, you see that your "\
                        "opponent is a small, bearded man (think Dumbledore "\
                        "in Harry Potter). Do you make the first move?"
                    print_story(line1, line2)
                    (response, choice) = get_response(("y", "Yes"), \
                                                      ("n", "No"))
                    player.append_game_stage("," + choice)

                case "Q1,Shield,Yes":
                    print_string_line("-")
                    line1 = "You choose to make the first move. But how do "\
                        "you attack someone with a shield? You throw the "\
                        "shield to the wizard, hoping that you can become the "\
                        "next Captain America—but to no avail. The shield "\
                        "thunks into the ground, and you suddenly feel your "\
                        "insides ripping out of your body (thanks to the "\
                        "wizard’s powerful spell which flips your skin inside "\
                        "out)."
                    line2 = "Your dying body is left to rot in the arena."
                    print_story(line1, line2)
                    player.set_game_stage("Game over")

                case "Q1,Shield,No":
                    print_string_line("-")
                    line1 = "You don’t make the first move. Instead, you lift "\
                        "up the shield to protect yourself as a bright ball "\
                        "of green light from the wizard skyrockets toward "\
                        "you. The light bounces off the shield and hits just "\
                        "above the wizard’s head. The entire crowd is silent. "\
                        "Because instead of hitting the wizard, the light "\
                        "engulfs the king in flames. A group of soldiers "\
                        "begin to run to you."
                    line2 = "What do you do?"
                    print_story(line1, line2)
                    (response, choice) = \
                        get_response(("a", "Fight the soldiers"),
                                     ("b", "Run away"))
                    if response == "b":
                        player.set_game_stage("Run away")

                case "Q1,Shield,No,Fight the soldiers":
                    print_string_line("-")
                    line1 = "Though your shield seems very formidable, the "\
                        "guards overpower you, and you are executed by the "\
                        "queen within minutes."
                    print_story(line1)
                    player.set_game_stage("Game over")

                case "Q1,Stone":
                    print_string_line("-")
                    line1 = "You choose STONE."
                    line2 = "As you enter the arena, you see that your "\
                        "opponent is a small, bearded man (think Dumbledore "\
                        "in Harry Potter). Do you make the first move?"
                    print_story(line1, line2)
                    (response, choice) = get_response(("y", "Yes"), \
                                                      ("n", "No"))
                    player.append_game_stage("," + choice)

                case "Q1,Stone,Yes":
                    print_string_line("-")
                    line1 = "You choose to make the first move."
                    line2 = "But fighting with a stone is a bit awkward... "\
                        "You try to throw the stone at the wizard’s head in a "\
                        "Pokéball-esque style, but you miss and it sadly "\
                        "plops on the ground beside the wizard. You suddenly "\
                        "feel your insides ripping out of your body (thanks "\
                        "to the wizard’s powerful spell which flips your "\
                        "skin inside out)"
                    line3 = "Your dying body is left to rot in the arena."
                    print_story(line1, line2, line3)
                    player.set_game_stage("Game over")

                case "Q1,Stone,No":
                    print_string_line("-")
                    line1 = "You don’t make the first move. Instead, you hold "\
                        "your stone and cower awkwardly to protect yourself "\
                        "as a bright ball of green light from the wizard "\
                        "skyrockets toward you. The light bounces off the "\
                        "shield and hits just above the wizard’s head. The "\
                        "entire crowd is silent. Because instead of hitting "\
                        "the wizard, the light engulfs the king in flames. A "\
                        "group of soldiers begin to run to you."
                    line2 = "What do you do?"
                    print_story(line1, line2)
                    (response, choice) = \
                        get_response(("a", "Fight the soldiers"), 
                                     ("b", "Run away"))
                    player.append_game_stage("," + choice)
                    if response == "b":
                        player.set_game_stage("Run away")

                case "Q1,Stone,No,Fight the soldiers":
                    print_string_line("-")
                    line1 = "Though your mysterious stone seems very "\
                        "formidable, the guards overpower you, and you are "\
                        "executed by the queen within minutes."
                    print_story(line1)
                    player.set_game_stage("Game over")
                
                # Win the game
                case "End of game":
                    print_string_line("-")
                    print_congratulation(column_of_cup = 3, row_of_cups = 1)
                    #Satisfies #14
                    illegal_function_call_restricted_keyword()
                    player.set_game_stage("Play again") 
                
                # Lose the game
                case "Game over":
                    print_string_line("-")
                    print_string_line("X")
                    print("GAME OVER")
                    print_string_line("X")
                    player.set_game_stage("Play again") 

                # Play again question
                case "Play again":
                    print_string_line("-")
                    line1 = "Play again?"
                    print_story(line1)
                    (response, choice) = get_response(("y", "Yes"), \
                                                      ("n", "No"))
                    match response:
                        case "y":
                            player.set_game_stage("Start")
                        case "n":
                            player.set_game_stage("End")

    except KeyboardInterrupt as e:
        print("\n")
        print("!!! Keyboard interruption:", e)
        print_string_line("X")
        print("GAME OVER")
        print_string_line("X")

if __name__=="__main__":
    main()