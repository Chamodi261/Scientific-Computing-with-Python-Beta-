NUMBER_OF_DISKS = 5
A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []
C = []

def move(n, source, auxiliary, target):
    """
    Move the top n disks from the source tower to the target tower using the auxiliary tower.
    
    Parameters:
    - n (int): Number of disks to move.
    - source (list): The source tower from which disks will be moved.
    - auxiliary (list): The auxiliary tower used during the movement.
    - target (list): The target tower to which disks will be moved.
    """
    if n <= 0:
        return
    
    # Move n - 1 disks from the source to the auxiliary tower, so they are out of the way
    move(n - 1, source, target, auxiliary)
    
    # Move the nth disk from the source to the target
    target.append(source.pop())
    
    # Display the current state of towers
    print("State of Towers:", A, B, C, '\n')
    
    # Move the n - 1 disks that were moved to the auxiliary tower onto the target
    move(n - 1, auxiliary, source, target)

# Initiate the call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, A, B, C)
