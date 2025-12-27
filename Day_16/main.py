from prettytable import PrettyTable

my_table = PrettyTable()
my_table.add_column("Pokemon Name", ['Pikachu', 'Squirtle', 'Charmander'])
my_table.add_column("Type", ["Electric", "Water", "Fire"])

print(my_table)

