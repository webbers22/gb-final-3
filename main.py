from complex_number import ComplexNumber
from calculator import Calculator
from operation_factory import OperationFactory
from logger import Logger

logger = Logger.get_instance()

if __name__ == "__main__":
    num1 = ComplexNumber(2, 3) # Комплексное число 1
    num2 = ComplexNumber(4, 5) # комплексное число 2

    calc = Calculator()
    factory = OperationFactory()

    operation = factory.create_operation('*') # Указываем какое действие будем проводить +, *, /
    result = getattr(calc, operation)(num1, num2)
    logger.log(f"Addition result: {result.real} + {result.imaginary}i")
