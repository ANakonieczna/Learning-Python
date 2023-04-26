import random
from replit import clear
from game_data import data
from art import logo,vs
print(logo)

def answer(data_A,data_B):
  print(f"Compare A: {data[data_A]['name']}, a {data[data_A]['description']}, from {data[data_A]['country']}.")
  
  print(vs)
  
  print(f"Against B: {data[data_B]['name']}, a {data[data_B]['description']}, from {data[data_B]['country']}.")
  
  AorB = input("Who has more followers? Type 'A' or 'B': ").upper()
  return AorB

score = 0
end = False
info = False
data_A = random.randint(0,len(data)-1)

while not end:
  clear()
  print(logo)

  if info == True:
    print(f"You're right! Current score: {score}.")
    info = False

  data_B = random.randint(0,len(data)-1)
  if data_B == data_A:
    data_B = random.randint(0,len(data)-1)

  AorB = answer(data_A,data_B)
  
  if (AorB == 'A' and data[data_A]['follower_count'] > data[data_B]['follower_count']) or (AorB == 'B' and data[data_B]['follower_count'] > data[data_A]['follower_count']):
    score += 1
    info = True
  else:
    end = True
    print(f"Sorry, that's wrong. Final score: {score}.")

  data_A = data_B
