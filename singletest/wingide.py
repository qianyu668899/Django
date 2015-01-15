class simple:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def test(self):
        print self.x + self.y

if __name__ == "__main__":
    sol = simple(1, 2)
    sol.test()