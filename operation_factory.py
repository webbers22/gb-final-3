class OperationFactory:
    def create_operation(self, operation):
        if operation == '+':
            return 'add'
        elif operation == '*':
            return 'multiply'
        elif operation == '/':
            return 'divide'
        else:
            return None