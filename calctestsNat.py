import unittest
from calculator import Calculator
#from calculatorNat import Calculator


class TestStringMethods(unittest.TestCase):

    def test_add(self):
        c = Calculator()
        self.assertEqual(c.add(3, 3), 6)


    def test_add2(self):
        c = Calculator()
        self.assertEqual(c.add(12, -10), 2)

    def test_add3(self):
        c = Calculator()
        self.assertEqual(c.add(5, 8), 13)

    def test_sub(self):
        c = Calculator()
        self.assertEqual(c.sub(9, 3), 6)

    def test_sub2(self):
        c = Calculator()
        self.assertEqual(c.sub(9, 1), 8)

    def test_sub3(self):
        c = Calculator()
        self.assertEqual(c.sub(4, 2), 2)

    def test_mul(self):
        c = Calculator()
        self.assertEqual(c.mul(2, 3), 6)

    def test_mul2(self):
        c = Calculator()
        self.assertEqual(c.mul(9, 1), 9)

    def test_mul3(self):
        c = Calculator()
        self.assertEqual(c.mul(4, 4), 16)

    def test_div(self):
        try:
            c = Calculator()
            self.assertEqual(c.div(9, 3), 3)

        except ZeroDivisionError:
            self.currentValue = None
            self.currentMsg = 'Div By Zero'

        except ValueError:
            if self.currentValue <= 0:
                self.currentValue = None
                self.currentMsg = 'Neg Num Error'

    def test_div2(self):
        try:
            c = Calculator()
            self.assertEqual(c.div(9, 3), 3)

        except ZeroDivisionError:
            self.currentValue = None
            self.currentMsg = 'Div By Zero'

            c = Calculator()
            self.assertEqual(c.div(18, 3), 6)

    def test_div3(self):
        try:
            c = Calculator()
            self.assertEqual(c.div(9, 3), 3)

        except ZeroDivisionError:
            self.currentValue = None
            self.currentMsg = 'Div By Zero'

            c = Calculator()
            self.assertEqual(c.div(8, 4), 2)


 #NOT SURE HOW TO TEST THESE YET:  Binary | Octal | Decimal(default) | Hexidecimal
    # def displayModeBin(self):
    #     c = Calculator()
    #     self.assertEqual(c.displayMode(3, 3), 6)

    def test_hex(self):
        c = Calculator()
        c.set_value(44222)
        result = c.displayModeHex()
        self.assertEqual(result, 0xacbe)

    def test_hex2(self):
        c = Calculator(55557)
        self.assertEqual(c.displayModeHex(55555, +2), 0xd905)

    def test_hex3(self):
        c = Calculator()
        self.assertEqual(c.displayModeHex(777, -222), 0x309)





    def test_oct(self):
        c = Calculator()
        self.assertEqual(c.hex(44444, -222), )

    def test_oct2(self):
        c = Calculator()
        self.assertEqual(c.hex(55555, +2), )

    def test_oct3(self):
        c = Calculator()
        self.assertEqual(c.hex(777, -222), )





    def test_bin(self):
        c = Calculator()
        self.assertEqual(c.hex(44444, -222), )

    def test_bin2(self):
        c = Calculator()
        self.assertEqual(c.hex(55555, +2), )

    def test_bin3(self):
        c = Calculator()
        self.assertEqual(c.hex(777, -222), )


if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    unittest.main()
