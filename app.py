import random
suites = ["♡","♧","♤","♢"]
values = ["ace","king","queen","jacks","10","9","8","7","6","5","4","3","2"]

random_suites_position=random.randint(0,3)
random_values_position=random.randint(0,12)

generate_card=suites[random_suites_position]+values[random_values_position]

print(generate_card)