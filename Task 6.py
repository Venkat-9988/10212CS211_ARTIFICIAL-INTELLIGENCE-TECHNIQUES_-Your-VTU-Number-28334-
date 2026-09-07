colors = ["Red", "Green", "Blue", "Yellow"]


zones = ["A", "B", "C", "D", "E"]


neighbors = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E"],
    "E": ["C", "D"]
}
def is_valid(zone, color, assignment):
    for neighbor in neighbors[zone]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def solve(assignment):
   
    if len(assignment) == len(zones):
        return assignment

    
    for zone in zones:
        if zone not in assignment:
            break

    for color in colors:
        if is_valid(zone, color, assignment):
            assignment[zone] = color

            result = solve(assignment)

            if result:
                return result

            del assignment[zone]

    return None



solution = solve({})


print("CSP Solution:")
for zone in zones:
    print(zone, "->", solution[zone])


//OUTPUT//
CSP Solution:
A -> Red
B -> Green
C -> Blue
D -> Red
E -> Green
