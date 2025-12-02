import time

start = time.time()

starting = input("Press enter to start ")


if starting == "":
    print("I have started running the program.")
    print("Delaying the time...")
    print("Proceed..")

else:
    print("Click the correct input")

end = time.time()

print(f"Time taken: {end - start}")