class DrawRulerByRecursion:

    def __init__(self, num_inches, major_length):
        self.num_inches = num_inches
        self.major_length = major_length
        self.draw_ruler()

    def draw_ruler(self):
        """Draw English ruler with given number of inches, major tick length."""
        self.draw_line(self.major_length, "0")  # draw inch 0 line
        for j in range(1, 1 + self.num_inches):
            self.draw_interval(self.major_length - 1)
            self.draw_line(self.major_length, str(j))

    @staticmethod
    def draw_line(tick_length, tick_label=""):
        """Draw one line with given tick length(followed by optional label)."""
        line = "-" * tick_length
        if tick_label:
            line += " " + tick_label
        print(line)

    def draw_interval(self, center_length):
        """Draw tick interval based upon a central tick length."""
        if center_length > 0:  # stop when length drops to 0
            self.draw_interval(center_length - 1)  # recursively draw top ticks
            self.draw_line(center_length)  # draw center tick
            self.draw_interval(center_length - 1)  # recursively draw bottom ticks


if __name__ == '__main__':
    def main():
        DrawRulerByRecursion(3, 6)


    main()
