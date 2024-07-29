while True:

    import random

    def emba(s):
        x = ''.join(random.sample(s,len(s)))
        return x

    print(emba(input("Palavra: ")))