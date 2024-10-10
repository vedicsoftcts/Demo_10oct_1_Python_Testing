import DClass1
import unittest

#emp3 = DClass1.employee("Madhu", 33)
#emp3.display()
# Unit test class
class TestEmployee(unittest.TestCase):

    # Test case to check employee initialization
    def test_employee_init(self):
        emp = DClass1.employee("Ravi", 44)
        self.assertEqual(emp.name, "Ravi")
        self.assertEqual(emp.age, 44)

    # Test case to check diplay() method output
    def test_employee_display(self):
        emp = DClass1.employee("Vijay", 23)
        expected_output = "Hello, I am Vijay, my age is 23"
        self.assertEqual(emp.display(), expected_output)

    # Test case for an edge case with age as zero
    def test_employee_age_zero(self):
        emp = DClass1.employee("John", 0)
        self.assertEqual(emp.age, 0)

    # Test case for negative age (which could be an invalid input)
    def test_employee_negative_age(self):
        emp = DClass1.employee("Doe", -5)
        self.assertEqual(emp.age, -5)

    # Test case for empty name input
    def test_employee_empty_name(self):
        emp = DClass1.employee("", 30)
        self.assertEqual(emp.name, "")
        self.assertEqual(emp.display(), "Hello, I am , my age is 30")


# Running the tests if the script is executed directly
if __name__ == '__main__':
    unittest.main()
