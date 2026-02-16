#Two.py 
import one
print("Top level code in TWO .py")

one.func()

if __name__ == "__main__":
    print("THIS is under main of TWO .py running directly..")
else:
    print("Under two.py called/imported")
