def speed():
    distance= int(input("Enter the distance covered: "))

    time = int(input("Enter the time taken: "))

    if(time != 0):
        speed = distance / time
        return speed
    else:
        print("Time can't be zero, enter a valid time taken")
        return None

result = speed()
if result is not None:
    print(f"Speed= ",result)