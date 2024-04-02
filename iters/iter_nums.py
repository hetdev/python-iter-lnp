class IterNums:


    def __iter__(self):
        print("iterr")
        self.a = 1

        return self

    def __next__(self):
        print("nextt")
        if self.a < 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
