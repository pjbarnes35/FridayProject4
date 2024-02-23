import random

def generate_powerball_numbers():
    """Generate and print PowerBall numbers."""
    print("Welcome to the PowerBall number generator!")

    # Ask if the user wants PowerBall numbers
    response = input("Would you like some PowerBall numbers? (yes/no): ").lower()

    if response == "yes":
        # Generate the first five white ball numbers
        white_ball_1 = random.randint(1, 69)
        white_ball_2 = random.randint(1, 69)
        white_ball_3 = random.randint(1, 69)
        white_ball_4 = random.randint(1, 69)
        white_ball_5 = random.randint(1, 69)
        
        # Generate the red PowerBall number
        red_ball = random.randint(1, 26)
        
        # Print the generated numbers with appropriate spacing
        print(f"\nYour PowerBall numbers are: {white_ball_1}  {white_ball_2}  {white_ball_3}  {white_ball_4}  {white_ball_5}    {red_ball}\n")
    else:
        print("No problem, maybe next time!")

    print("Goodbye!")

# Call the function to generate PowerBall numbers
generate_powerball_numbers()
