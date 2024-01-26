import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.0 .Created by Althaf")
    while True:
        x = input("Enter What you want to speak: ")
        if x == "q":
            break;
        command = f"say {x}"
        os.system(command)

