class Context:
    def __init__(self, buffer, start, end):
        self.buffer = buffer
        self.start = start
        self.end = end

    def __str__(self):
        result = ""
        line, column = 0, 0

        for buffer_line in self.buffer:
            for char in buffer_line:
                if (line, column) == self.start:
                    result += "["

                result += char

                if (line, column) == self.end:
                    result += "]"

                column += 1
            line += 1

            return result
