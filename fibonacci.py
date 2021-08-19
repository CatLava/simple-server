# This is a fibonacci sequence practice
'''The fibonacci sequence is a recursive function that calls itself
to get a number in the instance. For instance, the 5th number in the fibonacci
sequence allows for calling f(0), f(1). f(2)'''

def fibonacci_seq(n):
    if n==0 or n==1:
        return n
    else:
        return fibonacci_seq(n-1) + fibonacci_seq(n-2)

print(fibonacci_seq(10))


# Create a class out of it
# This using caching to speed up processes

class Fib_seq:
    def __init__(self):
        self.cache = []
        self.cache.append(0)
        self.cache.append(1)

    def __call__(self, i):
        newfib = 0

        if isinstance(i, int) and i >= 0:
            if i == 0 or i ==1:
                return self.cache[i]

            elif i >= len(self.cache):
                newfib = self.__call__(i-1) + self.__call__(i-2)
                self.cache.append(newfib)

            else:
                newfib = self.cache[i-1] + self.cache[i-2]

            return self.cache[i]

        else:
            raise ValueError("Invalid input")

new = Fib_seq()

print(new(10))
