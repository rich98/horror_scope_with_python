import random

# Define the zodiac signs
zodiac_signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']

# Read the predictions from the file
with open('predictions.txt', 'r') as f:
    predictions = [line.strip() for line in f]

# Generate the horror scopes
for sign in zodiac_signs:
    prediction = random.choice(predictions)
    print(f"{sign}: {prediction}")
