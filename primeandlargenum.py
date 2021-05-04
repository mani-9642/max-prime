class prime:
    @staticmethod
    def primenum():
        a = []
        num = int(input("Enter the Limit value : "))
        for x in range(num):
            k = int(input("Enter the numbers : "))
            if k==2 or k==3 or k==5:
                print(k,"Prime Number")
            elif k%2==0 or k%3==0 or k%5==0:
                print(k,"Not a Prime")
            else:
                print(k,"prime number")
            a.append(k)
        print("Maximum number is",max(a),"\t","Minimum number is",min(a))
prime.primenum()