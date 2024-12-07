import re

def next_operation(current_total, remaining_numbers):
    next_operand = remaining_numbers.pop(0)

    for op in ['+', '*', '||']:
        if op == '+':
            total = current_total + next_operand
        elif op == '*':
            total = current_total * next_operand
        else:
            total = int(str(current_total) + str(next_operand))

        if len(remaining_numbers) == 0:
            if total == test_value:
                return True
        else:
            if total <= test_value and next_operation(total, remaining_numbers):
                return True

    remaining_numbers.insert(0, next_operand)
    return False


with open('input.txt', 'r') as f:
    equations = f.read().split('\n')

# use recursion to handle items in input list one at a time
calibration_result = 0
for eq in equations:
    input_numbers = list(map(int, re.findall(r'\d+', eq)))
    test_value = input_numbers.pop(0)

    if next_operation(input_numbers[0], input_numbers[1:]):
        calibration_result += test_value
print(calibration_result)
