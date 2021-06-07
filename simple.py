import time 

starttime=time.time() 

def main():
     while True:
          print("Hello World!")
          # Print Hello World every 30 seconds.
          time.sleep(30.0 - ((time.time() - starttime) % 30.0))

if __name__ == "__main__":
     main()
