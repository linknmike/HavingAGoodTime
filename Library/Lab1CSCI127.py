lenR = int(input("What is the length of the room (in feet)? "))

widR = int(input("What is the width of the room (in feet)? "))

lenT = int(input("What is the length of the table (in feet)? "))

widT = int(input("What is the width of the table (in feet)? "))

space = int(input("How much space is required between tables (in feet)? "))

numL = lenR // (lenT + 2*space)

numW = widR // (widT + space)

numT = numL * numW

seat = int(input("How many people does each table seat? "))

print("This arrangement seats", numT*seat, "people.")
