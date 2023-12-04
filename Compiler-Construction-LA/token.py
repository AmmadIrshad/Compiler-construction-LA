from classpart import ClassPart

class Token:
    def __init__(self, class_part, value, line_number):
        self.ClassPart = class_part
        self.Value = value
        self.LineNumber = line_number

    def to_csv_string(self):
        return f"{self.LineNumber},{self.ClassPart},{self.Value}\r\n"

    def __str__(self):
        return f"LINE NUMBER: {self.LineNumber}\t\tCLASS PART: {self.ClassPart}\t\t\t\t\t\tVALUE: {self.Value}\r\n"
