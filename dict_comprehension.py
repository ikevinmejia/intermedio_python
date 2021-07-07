import math

def run():
    # my_dict = {i:i**3 for i in range(101) if i % 3 != 0}
    # print(my_dict)

    # Reto

    my_dict={i:round(math.sqrt(i),2) for i in range(1000)}
    print(my_dict)

if __name__=="__main__":
    run()