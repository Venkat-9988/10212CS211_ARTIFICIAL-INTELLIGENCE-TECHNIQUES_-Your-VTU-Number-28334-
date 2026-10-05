# TASK 7
# Monkey Banana Problem using Goal Stack Planning

class MonkeyBanana:
    def __init__(self):
        # Initial state
        self.monkey_position = "door"
        self.box_position = "corner"
        self.banana_position = "middle"
        self.monkey_on_box = False
        self.has_banana = False

    def display_state(self):
        print("\nCurrent State:")
        print("Monkey position :", self.monkey_position)
        print("Box position    :", self.box_position)
        print("Banana position :", self.banana_position)
        print("Monkey on box   :", self.monkey_on_box)
        print("Has banana      :", self.has_banana)

    def walk(self, position):
        self.monkey_position = position
        print("Action: Monkey walks to", position)

    def push_box(self, position):
        self.box_position = position
        self.monkey_position = position
        print("Action: Monkey pushes the box to", position)

    def climb(self):
        if self.monkey_position == self.box_position:
            self.monkey_on_box = True
            print("Action: Monkey climbs onto the box")
        else:
            print("Cannot climb: Monkey is not near the box")

    def grasp(self):
        if (self.monkey_on_box and
            self.box_position == self.banana_position):
            self.has_banana = True
            print("Action: Monkey grasps the banana")
        else:
            print("Cannot grasp the banana")

    def solve(self):
        print("===================================")
        print("     MONKEY BANANA PROBLEM")
        print("     GOAL STACK PLANNING")
        print("===================================")

        print("\nInitial State:")
        self.display_state()

        print("\nPlanning and Actions:")
        print("----------------------------")

        # Step 1: Move monkey to the box
        if self.monkey_position != self.box_position:
            self.walk(self.box_position)

        # Step 2: Move box below the banana
        if self.box_position != self.banana_position:
            self.push_box(self.banana_position)

        # Step 3: Climb onto the box
        if not self.monkey_on_box:
            self.climb()

        # Step 4: Grasp the banana
        if not self.has_banana:
            self.grasp()

        # Final state
        print("\n===================================")
        print("           FINAL STATE")
        print("===================================")
        self.display_state()

        # Goal test
        print("\nGoal Test:")
        if self.has_banana:
            print("SUCCESS!")
            print("Goal achieved: Monkey has the banana.")
        else:
            print("FAILURE!")
            print("Goal not achieved.")


# Create object and solve the problem
problem = MonkeyBanana()
problem.solve()
