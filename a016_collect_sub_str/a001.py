class Solution:
    def __init__(self):
        self.path = []
        self.rst = []
        self.string = ""

    def entry(self, string):
        self.string = string
        self.solve(0)

    def solve(self, i):
        if i == len(self.string):
            self.rst.append(self.path.copy())
            return

        self.solve(i + 1)

        self.path.append(self.string[i])
        self.solve(i + 1)
        self.path.pop(-1)

        return

    def print(self):
        for elem in self.rst:
            print(f'"{"".join(elem)}"')


def tst_1():
    sol = Solution()
    sol.entry("abc")
    sol.print()


if __name__ == "__main__":
    tst_1()
