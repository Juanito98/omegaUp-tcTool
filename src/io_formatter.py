class IOFormatter:

    def LINE(self, *args) -> None:
        self.printToFile(" ".join(str(a) for a in args) + "\n")

    def LINES(self, *args) -> None:
        for i in range(len(args[0])):
            self.LINE(*[a[i] for a in args])

    def GRID(self, grid) -> None:
        for row in grid:
            self.LINE(*row)

    def setInputFile(self, f) -> None:
        self.f = f

    def printToFile(self, s: str) -> None:
        self.f.write(s)
