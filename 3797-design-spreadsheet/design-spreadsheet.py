class Spreadsheet:

    def __init__(self, rows: int):
        self.spreadsheet = [[0] * 26 for _ in range(rows)]

    def _parse_cell(self, cell: str):
        col, row = re.match(r"([A-Z]+)(\d+)", cell).groups()
        col = ord(col) - ord('A')
        row = int(row) - 1
        return row, col

    def setCell(self, cell: str, value: int) -> None:
        row, col = self._parse_cell(cell)
        self.spreadsheet[row][col] = value

    def resetCell(self, cell: str) -> None:
        row, col = self._parse_cell(cell)
        self.spreadsheet[row][col] = 0

    def getValue(self, formula: str) -> int:
        tokens = re.findall(r"([A-Za-z]+\d+|\d+|[+\-*/])", formula.lstrip("="))
        
        total = 0
        current_op = '+'

        for token in tokens:
            if token in "+-*/":
                current_op = token
                continue
            
            if token.isdigit():
                value = int(token)
            else:
                r, c = self._parse_cell(token)
                value = self.spreadsheet[r][c]
            
            if current_op == '+':
                total += value
            elif current_op == '-':
                total -= value
            elif current_op == '*':
                total *= value
            elif current_op == '/':
                total //= value

        return total


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)