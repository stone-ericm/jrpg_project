def gender(self):
  while True:
    choice = input("What is the player's gender?\n[M]ale\n[F]emale\n[O]ther\n").lower()
    if choice in self.genders:
      return choice
    
def intro(self):
  #GameState.location = "Lalivero"
  print('''This is the world of Weyard. For an age the world has been at peace, with magic and the djinn in harmony with the people. This peace has been upheld thanks to the tireless efforts of a nameless watchman. The mantle has been passed from generation to generation in relative secrecy. All anyone knows, or really cares to know, is that the watchman is the strongest in the land, able to keep the djinn themselves in line, and is responsible for the peace that all enjoy.

Parents tell their children stories of a mythical time before the watchman when monsters roamed the countryside and djinn, who controlled one region or another, fought bloody wars. Of course, this was long before anyone can remember and many wonder if it wasn't always like it is now.

But something has changed. The djinn have become restless, seizing towns throughout the world. They have created new monsters to terrorize travelers, destroying trade routes, and isolating the people in ways they haven't seen this age.

But hope remains. The people of Lalivero have seen {do} watching from atop the Babi Lighthouse, contemplating his course of action...'''.format(**self.gender))
  return input("What is the watchman's name?\n")