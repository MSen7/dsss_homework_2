import unittest
from math_quiz import Generate_Random_Number, Generate_Random_Arithmetic_Operator,Arithmetic_Operations


class TestMathGame(unittest.TestCase):

    def test_function_Generate_Random_Number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = Generate_Random_Number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_Generate_Random_Arithmetic_Operator(self):
            operator = Generate_Random_Arithmetic_Operator()
            expected_operators = {'+', '-', '*'}
            self.assertIn(operator, expected_operators, f"Unexpected operator: {operator}")
        

    def test_Arithmetic_Operations(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5,2,'-','5 - 2',3),(5,2,'*','5 * 2',10)
            ]
        
            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                
                with self.subTest(num1=num1, num2=num2, operator=operator):
                    message, answer = Arithmetic_Operations(num1, num2, operator)
                    self.assertEqual(message, expected_problem, f"Unexpected problem: {message}")
                    self.assertEqual(answer, expected_answer, f"Unexpected answer: {answer}")

if __name__ == "__main__":
    unittest.main()
