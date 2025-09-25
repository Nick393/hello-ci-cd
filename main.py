def main():
    print("Hello from hello-ci-cd!")
    num1=input("enter a number: ")
    num2=input("Enter another number: ")
    add(num1,num2)
    
    print(sum)
def add(num1,num2):
    sum=int(num1)+int(num2)
    return sum

if __name__ == "__main__":
    main()
