def get_word(prompt):
    """Prompt the user for a word and return it."""
    return input(prompt)

def mad_lib():
    """Generate and display the completed Mad Lib."""
    # Get words from the user
    large_object = get_word("Enter a large object: ")
    large_objects_plural = get_word("Enter large objects (plural): ")
    adjective = get_word("Enter an adjective: ")
    body_part = get_word("Enter a body part: ")
    restaurant = get_word("Enter a restaurant: ")
    first_food = get_word("Enter a food: ")
    second_food = get_word("Enter another food: ")

    # Generate the story with user-provided words
    story = f"I’ve had a very {adjective} day.\n\n"
    story += f"This morning, I dropped a box of {large_objects_plural} on my {body_part}.\n\n"
    story += f"Then, at lunch, I went to {restaurant} for their delicious {first_food},\n"
    story += f"But the waiter brought me {second_food}, which I was not hungry for.\n\n"
    story += f"Finally, on my way home, I was cut off by a van with a large {large_object} strapped to the roof."

    # Display the completed story
    print("\n\n")
    print("=" * 40)  # Visual separator
    print(story)  # Display the story
    print("=" * 40)  # Visual separator

# Call the mad_lib function to run the game
mad_lib()
