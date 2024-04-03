class GenNums:
    def generator(self):
        self.value = 0
        print("start generator")
        while self.value < 20:
            yield self.value

            self.value += 1
            print("increase value gen")
