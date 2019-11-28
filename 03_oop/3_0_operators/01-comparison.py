class Apple:
    def __init__(self, weight):
        self.weight = weight


    def __eq__(self, b):
        return self.weight == b.weight 


    def __lt__(self, b):
        return self.weight < b.weight


if __name__=='__main__':
    a1 = Apple(2)
    a2 = Apple(2)


    print(a1 < a2)
