def calculate_lift_rounds(n, capacity):
    """
    Function to calculate the number of rounds the lift needs to cover.
    
    Parameters:
    n (int): Total number of people.
    capacity (int): Maximum number of people the lift can carry in one round.
    
    Returns:
    int: The number of rounds required to transport all people to the top floor.
    """
    # Your code here
    return (n + capacity - 1) // capacity
