import random as rd
import tkinter as tk
import io
import sys

class game:
    def __init__(self, game_number):
        self._game_number = input("Give a number to this game.\n")
        self._teams_number = input("How many people will be playing?\n")
        self._game_teams = []
        for i in range(0, int(self._teams_number)):
            team_name = input(f"Give a name to team {i+1}.\n")  # Prompt for team name
            self._game_teams.append(team(team_name))  # Pass team name when creating team instance
        self._state = self.game_state()

    @property
    def game_number(self):
        return self._game_number

    @game_number.setter
    def game_number(self, value):
        self._game_number = value

    @property
    def teams_number(self):
        return self._teams_number

    @teams_number.setter
    def teams_number(self, value):
        self._teams_number = value

    @property
    def game_teams(self):
        return self._game_teams

    @game_teams.setter
    def game_teams(self, value):
        self._game_teams = value

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    def game_state(self):
        state = "ongoing"
        for i in range(0, int(self._teams_number)):
            if 0 <= int(i) < len(self._game_teams):
                if state == "ongoing":
                    if self._game_teams[int(i)]._team_state == "gaming":
                        state = "ongoing"
                    else:
                        state = "finished"
            else:
                state = "??"
        return state
    
    def game_info(self):
        for team in self._game_teams:
            team.display_team_stats()


class team:
    def __init__(self, name):  # Accept 'name' parameter
        self._name = name  # Assign 'name' to team's name

        self._team_members = []
        fighter_name = input("Give the fighter of your team a name.\n")
        fighter_type = input("Choose fighter type: 1 - Physical Fighter, 2 - Magical Fighter\n")
        if fighter_type == '1':
            self._team_members.append(physical_fighter(fighter_name))
        elif fighter_type == '2':
            self._team_members.append(magical_fighter(fighter_name))
        else:
            print("Invalid fighter type!")

        healer_name = input("Give the healer of your team a name.\n")
        self._team_members.append(super_healer(healer_name))

        paladin_name = input("Give the paladin of your team a name.\n")
        self._team_members.append(paladin(paladin_name))

        self._team_state = self.team_state()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def team_members(self):
        return self._team_members

    @team_members.setter
    def team_members(self, value):
        self._team_members = value

    @property
    def team_state(self):
        return self._team_state

    @team_state.setter
    def team_state(self, value):
        self._team_state = value

    def team_state(self):
        state = "gaming"
        if not self._team_members:
            state = "eliminated"
        else:
            for member in self._team_members:
                if not member.alive:
                    state = "eliminated"
                    break
        return state
    
    def display_team_stats(self):
        print("The team ", self._name, "is", self._team_state, ".\n")
        for i in range(0, 3):
            self._team_members[i].stats_info()

    def select_target(self):
        print(self._name, ", choose a target to use a skill on\n")
        game.game_info()
        target = input("")
        return target

    def select_warrior(self):
        print(self._name, ", Choose a warrior from your team to use one of his skills\n")
        self.display_team_stats()
        warrior = input("")
        return warrior

    def select_skill(self):
        print(self._name, ", choose your warrior's skill\n")
        self.move_warrior.skills_info()
        skill = input("")
        return skill



class skill:
    def __init__(self, name):
        self._name = name
        self._range = None
    @property
    def name(self):
        return self._name
    
    @property
    def range(self):
        return self._range
    def skill_info(self):
        skill_info_str = f"Name: {self._name}\nRange: {self._range}\n"
        return skill_info_str

class attack(skill):
    def __init__(self, name):
        super().__init__(name)
        self._damage = None

    def skill_info(self):
        skill_info_str = super().skill_info()
        skill_info_str += f"Damage: {self._damage}\n"
        return skill_info_str

class simple_attack(attack):
    def __init__(self, name):
        super().__init__(name)
        self._name = "Simple Attack"
        self._damage = 2
        self._range = 2

class physical_attack(attack):
    def __init__(self, name):
        super().__init__(name)
        self._stamina_cost = None

    def skill_info(self):
        skill_info_str = super().skill_info()
        skill_info_str += f"Stamina cost: {self._stamina_cost}\n"
        return skill_info_str

class punch(physical_attack):
    def __init__(self, name):
        super().__init__(name)
        self._name = "Punch"
        self._damage = 4
        self._range = 3
        self._stamina_cost = 5

class kick(physical_attack):
    def __init__(self, name):
        super().__init__(name)
        self._name = "Kick"
        self._damage = 6
        self._range = 4
        self._stamina_cost = 10

class sword_attack(physical_attack):
    def __init__(self, name):
        super().__init__(name)
        self._name = "Sword Slash"
        self._damage = 25
        self._range = 10
        self._stamina_cost = 20

class magical_attack(attack):
    def __init__(self, name):
        super().__init__(name)
        self._mana_cost = None

    def skill_info(self):
        skill_info_str = super().skill_info()
        skill_info_str += f"Mana cost: {self._mana_cost}\n"
        return skill_info_str

class spell(magical_attack):
    def __init__(self, name):
        super().__init__(name)
        self._name = "Spell"
        self._damage = 5
        self._range = 2
        self._mana_cost = 5

class curse(magical_attack):
    def __init__(self, name):
        super().__init__(name)
        self._name = "Curse"
        self._damage = 6
        self._range = 3
        self._mana_cost = 11

class burning_beam(magical_attack):
    def __init__(self, name):
        super().__init__(name)
        self._name = "Burning Beam"
        self._damage = 24
        self._range = 15
        self._mana_cost = 22

class heals_and_buffs(skill):
    def __init__(self, name):
        super().__init__(name)
        self._effect = None

    def skill_info(self):
        skill_info_str = super().skill_info()
        skill_info_str += f"Effect: {self._effect}\n"
        return skill_info_str

class simple_heal(heals_and_buffs):
    def __init__(self, name):
        super().__init__(name)
        self._name = "Simple Heal"
        self._effect = 2
        self._range = 2

class heal(heals_and_buffs):
    def __init__(self, name):
        super().__init__(name)
        self._stamina_cost = None
        self._mana_cost = None

    def skill_info(self):
        skill_info_str = super().skill_info()
        skill_info_str += f"Stamina cost: {self._stamina_cost}\nMana cost: {self._mana_cost}\n"
        return skill_info_str

class life_recovery(heal):
    def __init__(self, name):
        super().__init__(name)
        self._name = "Life Recovery"
        self._stamina_cost = 3
        self._mana_cost = 5
        self._range = 8
        self._effect = 10

class regeneration(heal):
    def __init__(self, name):
        super().__init__(name)
        self._name = "Regeneration"
        self._stamina_cost = 10
        self._mana_cost = 20
        self._range = 5
        self._effect = 20

class buff(heals_and_buffs):
    def __init__(self, name):
        super().__init__(name)
        self._stamina = None
        self._mana = None

    def skill_info(self):
        skill_info_str = super().skill_info()
        skill_info_str += f"Stamina cost: {self._stamina}\nMana cost: {self._mana}\n"
        return skill_info_str

class attack_buff(buff):
    def __init__(self, name):
        super().__init__(name)
        self._name = "Attack Buff"
        self._stamina_cost = 8
        self._mana_cost = 12
        self._range = 7
        self._effect = 2

class defense_buff(buff):
    def __init__(self, name):
        super().__init__(name)
        self._name = "Defense Buff"
        self._stamina_cost = 12
        self._mana_cost = 10
        self._range = 8
        self._effect = 2

class warrior:
    def __init__(self, name):
        self._name = name
        self._health_points = rd.randint(1, 100)
        self._alive = self._health_points > 0
        self._Def = rd.randint(1, 10)
        self._max_health_points = 100
        self._stamina = rd.randint(1, 100)
        self._max_stamina = 100
        self._mana = rd.randint(1, 100)
        self._max_mana_points = 100
        self._skills = []

    @property
    def name(self):
        return self._name

    @property
    def alive(self):
        return self._alive

    def stats_info(self):
        info = [
            f"Name: {self._name}",
            f"Health Points: {self._health_points}/{self._max_health_points}",
            f"Defense: {self._Def}",
            f"Stamina: {self._stamina}/{self._max_stamina}",
        ]
        return info

    def skill_info(self):
        info = []
        for skill in self._skills:
            skill_info = [
                f"Name: {skill.__name__}",
            ]
            info.append(skill_info)
        return info


class fighter(warrior):
    def __init__(self, name):
        super().__init__(name)
        self._AP = rd.randint(1, 10)
        self._Class = "Fighter"
        self._skills.append(simple_attack)

    def stats_info(self):
        info = super().stats_info()
        info.extend([
            f"Attack Points: {self._AP}",
            f"Class: {self._Class}",
        ])
        return info

    def skill_info(self):
        return super().skill_info()


class physical_fighter(fighter):
    def __init__(self, name):
        super().__init__(name)
        self._max_stamina = 200
        self._Class = "Physical Fighter"
        self._skills.extend([punch, kick])

    def stats_info(self):
        return super().stats_info()

    def skill_info(self):
        return super().skill_info()
    


class knight(physical_fighter):
    def __init__(self, name):
        super().__init__(name)
        self._max_stamina = 500
        self._Class = "Knight"
        self._Def *= 1.5
        self._AP *= 1.5
        self._max_health_points = 500
        self._skills.append(sword_attack)

    def stats_info(self):
        return super().stats_info()

    def skill_info(self):
        return super().skill_info()


class magical_fighter(fighter):
    def __init__(self, name):
        super().__init__(name)
        self._mana = rd.randint(0, 100)
        self._max_mana = 100
        self._Class = "Magical Fighter"
        self._skills.extend([curse, spell])
    def stats_info(self):
        info = super().stats_info()
        info.append(f"Mana: {self._mana}/{self._max_mana}")
        return info

    def skill_info(self):
        return super().skill_info()


class mage(magical_fighter):
    def __init__(self, name):
        super().__init__(name)
        self._max_mana = 500
        self._Class = "Mage"
        self._Def *= 1.5
        self._AP *= 1.5
        self._max_health_points = 500
        self._skills.append(burning_beam)

    def stats_info(self):
        return super().stats_info()

    def skill_info(self):
        return super().skill_info()


class healer(warrior):
    def __init__(self, name):
        super().__init__(name)
        self._healing_points = rd.randint(1, 8)
        self._Class = "Healer"
        self._skills.append(simple_heal)

    def stats_info(self):
        info = super().stats_info()
        info.extend([
            f"Healing Points: {self._healing_points}",
            f"Class: {self._Class}",
        ])
        return info

    def skill_info(self):
        return super().skill_info()


class super_healer(healer):
    def __init__(self, name):
        super().__init__(name)
        self._max_stamina = 200
        self._Class = "Super Healer"
        self._skills.extend([life_recovery, regeneration])

    def stats_info(self):
        return super().stats_info()

    def skill_info(self):
        return super().skill_info()


class super_buffer(healer):
    def __init__(self, name):
        super().__init__(name)
        self._max_stamina = 200
        self._Class = "Super Buffer"
        self._skills.extend([attack_buff, defense_buff])

    def stats_info(self):
        return super().stats_info()

    def skill_info(self):
        return super().skill_info()


class paladin(fighter, healer):
    def __init__(self, name):
        fighter.__init__(self, name)
        healer.__init__(self, name)
        self._Class = "Paladin"
        self._skills.extend([simple_attack, simple_heal])

    def stats_info(self):
        fighter_info = super(fighter, self).stats_info()
        healer_info = super(healer, self).stats_info()
        info = fighter_info + healer_info
        return info

    def skill_info(self):
        return super().skill_info()
                                                             

        
##########################################################################################################################
##########################################################################################################################
##                                                                                                                      ##
##   RULES:                                                                                                             ##
##   -----                                                                                                              ##
## print("in this game you ll be playing a 1v1 with a team of warriors\n")                                              ##
## print("each round you ll get to choose the warrior you re going to use\n")                                           ##
## print("your team has 3 warriors whose stats will be defined randomly\n")                                             ##
## print("once you choose the warrior, you ll get to choose one of his skills\n")                                       ##
## print("depending on the class warriors could have various skills\n")                                                 ##
## print("once the skill is selected it ll have effect immediately and the turn will be passed to the opponents\n")     ##
##                                                                                                                      ##
##########################################################################################################################
##########################################################################################################################
class Application:
    def __init__(self, game_instance):
        self.root = tk.Tk()
        self.root.geometry("800x500")
        self.root.config(background="#505050")

        # Set minimum size of the window
        self.root.minsize(800, 500)

        self.game_instance = game_instance

        self.create_widgets()

        self.root.mainloop()

    def create_widgets(self):
        # Create text boxes for displaying information
        self.textbox_left = tk.Text(self.root, height=15, width=30, bg="#353535", fg="#ffffff", font=('Arial', 12))
        self.textbox_left.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.textbox_left.config(state='normal')  # Enable editing

        self.textbox_middle = tk.Text(self.root, height=15, width=30, bg="#353535", fg="#ffffff", font=('Arial', 12))
        self.textbox_middle.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.textbox_middle.config(state='normal')  # Enable editing

        self.textbox_right = tk.Text(self.root, height=15, width=30, bg="#353535", fg="#ffffff", font=('Arial', 12))
        self.textbox_right.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        self.textbox_right.config(state='normal')  # Enable editing

        self.root.grid_rowconfigure(0, weight=1)  # Make the row expandable
        self.root.grid_columnconfigure(0, weight=1)  # Make the columns expandable
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

        self.show_teams()

    def show_teams(self):
        for idx, team in enumerate(self.game_instance.game_teams):
            # Frame for each team
            team_frame = tk.Frame(self.root, bg="#353535")
            team_frame.grid(row=1, column=idx, pady=10)  # Center horizontally

            # Label for team name
            team_label = tk.Label(team_frame, text=team.name, font=('Arial', 18), bg="#353535", fg="#ffffff")
            team_label.pack()

            # Listbox for team members
            team_listbox = tk.Listbox(team_frame, bg="#353535", fg="#ffffff", height=3)
            for team_member in team.team_members:
                team_listbox.insert(tk.END, team_member.name)
            team_listbox.pack()

            # Bind events to listbox
            team_listbox.bind("<Enter>", lambda event, team=team: self.show_team_info(event, team))
            team_listbox.bind("<Leave>", lambda event: self.clear_info_boxes())
            team_listbox.bind("<Button-1>", lambda event, team=team: self.show_player_info(event, team))

    def show_team_info(self, event, team):
        # Get the selected player's name
        selection = event.widget.curselection()
        if selection:
            selected_player = event.widget.get(selection[0])

            # Find the player object
            for team_member in team.team_members:
                if team_member.name == selected_player:
                    player_info = team_member.stats_info()
                    player_info_str = "\n".join(player_info)  # Convert player_info to string
                    self.textbox_left.delete(1.0, tk.END)
                    self.textbox_left.insert(tk.END, player_info_str)
                    break

    def clear_info_boxes(self):
        self.textbox_middle.delete(1.0, tk.END)
        self.textbox_right.delete(1.0, tk.END)

    def show_player_info(self, event, team):
        selection = event.widget.curselection()
        if selection:
            selected_player = event.widget.get(selection[0])

            # Find the player object
            for team_member in team.team_members:
                if team_member.name == selected_player:
                    # Display player info in the left text box
                    self.display_player_info(team_member)
                    # Create buttons for each skill
                    self.create_skill_buttons(team_member)
                    break

    def display_player_info(self, player):

        stdout_capture = io.StringIO()
        sys.stdout = stdout_capture
        

        player.stats_info()


        sys.stdout = sys.__stdout__


        player_info = stdout_capture.getvalue()

        self.textbox_left.delete(1.0, tk.END)
        self.textbox_left.insert(tk.END, player_info)

    def create_skill_buttons(self, player):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.destroy()

        for idx, skill_class in enumerate(player._skills):
            # Create a lambda function that returns a method to create an instance of the skill class
            button_command = lambda cls=skill_class: self.create_skill_instance(cls)
            button = tk.Button(self.root, text=skill_class.__name__, command=button_command)
            button.grid(row=2, column=idx, pady=5, padx=5, sticky="ew")

    def create_skill_instance(self, skill_class):
        # Extract the skill name from the class name
        skill_name = skill_class.__name__.replace('_', ' ')

        # Create an instance of the skill class with the extracted name
        skill_instance = skill_class(skill_name)
        return skill_instance  # Return the skill instance

    def show_skill_info(self, skill_class):
        skill_instance = self.create_skill_instance(skill_class)  # Call create_skill_instance
        skill_info = self.get_skill_info(skill_instance)

        self.textbox_middle.delete(1.0, tk.END)
        self.textbox_middle.insert(tk.END, skill_info)


    def get_skill_info(self, skill_instance):
        stdout_capture = io.StringIO()
        sys.stdout = stdout_capture

        skill_instance.skill_info()

        sys.stdout = sys.__stdout__

        skill_info = stdout_capture.getvalue()
        return skill_info
game1 = game(1)        
Application(game1)