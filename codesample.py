def sort(width, height, length, mass):
    """
    Sort a package into STANDARD, SPECIAL, or REJECTED stacks
    based on its dimensions and mass.
    
    Parameters:
    - width (cm), height (cm), length (cm): dimensions of the package
    - mass (kg): weight of the package
    
    Returns:
    - str: "STANDARD", "SPECIAL", or "REJECTED"
    """
    volume = width * height * length
    is_bulky = volume >= 1_000_000 or max(width, height, length) >= 150
    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return "REJECTED"
    return "SPECIAL" if is_bulky or is_heavy else "STANDARD"


# Test cases
if __name__ == "__main__":
    tests = [
        (50, 50, 50, 5), 
        (200, 50, 50, 5), 
        (50, 50, 50, 25),  
        (200, 200, 50, 25),   
        (150, 150, 150, 19), 
        (100, 100, 100, 20), 
    ]

    for w, h, l, m in tests:
        print(f"Package({w}x{h}x{l}, {m}kg) -> {sort(w, h, l, m)}")
