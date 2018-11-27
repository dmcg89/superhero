import random

#integer division in weapon

class Hero:
	def __init__(self, name, health=100):
		self.name = name
		self.abilities = list()
		self.armors = list()
		self.start_health = health
		self.health = health
		self.deaths = 0
		self.kills = 0

	def add_ability(self, ability):
		self.abilities.append(ability)

	def add_armor(self, armor):
		self.armors.append(armor);

	def attack(self):
		total = 0
		for i in self.abilities:
			total += i.attack()
		return total

	def defend(self):
		total = 0
		for i in self.armors:
			total += i.defend()
		return total

	def take_damage(self, damage_amt):
		self.health -= damage_amt
		if self.health < 0:
			self.deaths += 1
		return self.deaths

	def add_kill(self, num_kills):
		self.kills += num_kills



class Armor:
	def __init__(self, name, defense):
		self.name = name
		self.defense = defense

	def defend(self):
		return random.randint(0, defense)

class Abilities:
	def __init__(self, name, strength):
		self.name = name
		self.strength = strength

	def attack(self):
		low = self.strength // 2
		return random.randint(0, self.strength)

	def update_attack(self, attack_strength):
		self.strength = attack_strength

class Weapon(Abilities):
	def attack(self):
		return random.randint(self.strength//2, self.strength)


class Team:
	def __init__(self, team_name):
		self.name = team_name
		self.heroes = list()

	def add_hero(self, Hero):
		self.heroes.append(Hero)

	def remove_hero(self, name):
		# 1. loop through the list of Heroes
		# 2. look at each one, and compare
		# 3. if the name == Hero.name
		# 4. then if it does match, remove it
		print("hey")
		if not len(self.heroes) > 0:
			return 0

		else:
			for hero in self.heroes:
				if hero.name == name:
					self.heroes.remove(hero)
				else:
					return 0




				# self.heroes.remove[i]

		# if len(self.heroes) > 0:
		# 	# print("YOLO!!!!!!!")
		# 	print(self.heroes)
		# 	self.heroes.remove(name)
		# 	return self.heroes

	def find_hero(self, name):
		for i in self.heroes:
			if i == name:
				return i
		return 0

	def view_all_heroes(self):
		for i in self.heroes:
			print(i.name)

	def update_kills(self, kills):
		rm = kills % len(self.heroes)
		self.heroes[0].add_kill(rm)
		kills = kills / len(self.heroes)
		for i in self.heroes:
			i.add_kill(kills)

	def attack(self, other_team):
		total_attack = 0
		kills = 0
		for i in self.heroes:
			total_attack += i.attack()
		kills = other_team.defend(total_attack)
		self.update_kills(kills)

	def deal_damage(self, damage):
		damage = damage / len(self.heroes)
		kills = 0
		for i in self.heroes:
			kills += i.take_damage(damage)
		return kills

	def defend(self, damage_amt):
		total_defense = 0
		kills = 0
		for i in self.heroes:
			total_defense += i.defend()
		damage_amt -= total_defense
		if damage_amt > 0:
			kills += self.deal_damage(damage_amt)
		return kills

	def revive_heroes(self, health=100):
		for i in self.heroes:
			i.health = health

	def stats(self):
		for i in self.heroes:
			print(i.name + " Kills/Deaths: " + str(i.kills) + "/" + str(i.deaths))

class Arena:
	def __init__(self):
		self.team_one = None
		self.team_two = None

	def user_input(self, prompt):
		user_input = input(prompt)
		return user_input

	def build_team_one(self):
		hero1 = Hero(self.user_input("HERO NAME: "))
		ability_name1 = self.user_input("POWER: "),
		power1 = len(ability_name1) * random.randint(1, 5) * 10
		ability1 = Abilities(ability_name1, power1)
		hero1.add_ability(ability1)
		weapon1 = Weapon(self.user_input("WEAPON: "), random.randint(1, 5) * 10)
		hero1.add_ability(weapon1)

		hero2 = Hero(self.user_input("HERO NAME: "))
		ability_name2 = self.user_input("POWER: "),
		power2 = len(ability_name2) * random.randint(1, 5) * 10
		ability2 = Abilities(ability_name2, power2)
		hero2.add_ability(ability2)
		weapon2 = Weapon(self.user_input("WEAPON: "), random.randint(1, 5) * 10)
		hero2.add_ability(weapon2)


		self.team_one = Team(self.user_input("TEAM NAME: "))
		self.team_one.add_hero(hero1)
		self.team_one.add_hero(hero2)

	def build_team_two(self):
		hero1 = Hero(self.user_input("HERO NAME: "))
		ability_name1 = self.user_input("POWER: "),
		power1 = len(ability_name1) * random.randint(1, 5) * 10
		ability1 = Abilities(ability_name1, power1)
		hero1.add_ability(ability1)
		weapon1 = Weapon(self.user_input("WEAPON:"), random.randint(1, 5) * 10)
		hero1.add_ability(weapon1)

		hero2 = Hero(self.user_input("HERO NAME: "))
		ability_name2 = self.user_input("POWER: "),
		power2 = len(ability_name2) * random.randint(1, 5) * 10
		ability2 = Abilities(ability_name2, power2)
		hero2.add_ability(ability2)
		weapon2 = Weapon(self.user_input("WEAPON: "), random.randint(1, 5) * 10)
		hero2.add_ability(weapon2)


		self.team_two = Team(self.user_input("TEAM NAME: "))
		self.team_two.add_hero(hero1)
		self.team_two.add_hero(hero2)

	def team_battle(self):
		deaths1 = 0
		deaths2 = 0

		while deaths1 < len(self.team_one.heroes) and deaths2 < len(self.team_two.heroes):
			self.team_one.attack(self.team_two)
			self.team_two.attack(self.team_one)
			for i in self.team_one.heroes:
				deaths1 += i.deaths
			for i in self.team_two.heroes:
				deaths2 += i.deaths

	def show_stats(self):
		print(self.team_one.name + " stats:")
		self.team_one.stats()
		print(self.team_two.name + " stats:")
		self.team_two.stats()

	def play_again(self):
		answer = self.user_input("Play again (y/n)? ")
		if answer == "y" or answer == "Y":
			self.team_one.revive_heroes()
			self.team_two.revive_heroes()
			game_loop(self)
#
# arena = Arena()
# arena.build_team_one()
# arena.build_team_two()



def game_loop(arena):
	arena.team_battle()
	arena.show_stats()
	arena.play_again()

# game_loop(arena)
