# Write your solution here
def chessboard(length):
    index=0
    while index<length:
        o=0
        while o<length:
            if (index+o)%2==0:
                print('1', end="")
            else:
                print('0',end="")
            o+=1
        print()
        index+=1
# Testing the function
if __name__ == "__main__":
    chessboard(3)
