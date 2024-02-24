import random

# Define the zodiac signs
zodiac_signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']

# Define the horror-themed predictions
predictions = [
    "You will encounter a ghost from your past.",
    "A vampire will cross your path today.",
    "Beware of full moons - a werewolf might be lurking.",
    "Your future is haunted by specters of uncertainty.",
    "A zombie apocalypse is nearer than you think.",
    "Your spirit will be tested by a poltergeist.",
    "An old curse will resurface.",
    "A witch will cast a spell on you.",
    "You will be visited by a creature from another dimension.",
    "A dark shadow looms over your destiny.",
    "An eerie silence will fall upon you.",
    "Your fate is intertwined with a phantom."
]

# Generate the horror scopes
for sign in zodiac_signs:
    prediction = random.choice(predictions)
    print(f"{sign}: {prediction}")
