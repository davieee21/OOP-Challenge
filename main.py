from pet import Pet

# Create a pet instance
my_pet = Pet("Buddy")

# Interact with your pet
my_pet.get_status()
print("\nFeeding pet...")
my_pet.eat()
my_pet.get_status()

print("\nPlaying with pet...")
my_pet.play()
my_pet.get_status()

print("\nPutting pet to sleep...")
my_pet.sleep()
my_pet.get_status()

print("\nTraining pet to roll over...")
my_pet.train("roll over")
my_pet.show_tricks()

