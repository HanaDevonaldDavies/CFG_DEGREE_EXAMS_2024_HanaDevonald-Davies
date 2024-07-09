def no_of_handshakes(no_people):
   
    if not isinstance(no_people, int) or no_people <= 0:
        raise ValueError("Number of people must be a positive integer.")
    
    handshakes = (no_people * (no_people - 1)) // 2
    return handshakes
