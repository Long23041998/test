import time

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"Time left: {i} seconds")
        time.sleep(1)

    print("Countdown complete!")

if __name__ == "__main__":
    seconds = int(input("Enter the number of seconds to count down: "))
    countdown(seconds)
