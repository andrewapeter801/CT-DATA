def describe_pet(pet_name, animal_type="cat"):
    """Display information about a pet."""
    return "My " + animal_type + "'s name is " + pet_name.title() + "."
print(describe_pet(pet_name="Kink"))