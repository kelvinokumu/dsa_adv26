def nests():
    for i in range(10):
        print("Outer loop Inside I ")
        for j in range(10-i):
            print(f"Inside {j}")

nests()