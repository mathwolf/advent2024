import re

with open('input.txt', 'r') as f:
    equations = f.read().split('\n')

calibration_result = 0
for eq in equations:
    input_numbers = list(map(int, re.findall(r'\d+', eq)))
    test_value = input_numbers.pop(0)

    # try all possible placements of operators between numbers
    # operators are encoded as a binary number with 0 representing +
    # and 1 representing *
    operator_placements = 2 ** (len(input_numbers) - 1)
    for j in range(operator_placements):
        operator_code = str(bin(j)[2:])
        # pad operator code with leading zeros
        pad = len(input_numbers) - 1 - len(operator_code)
        operator_code = '0' * pad + operator_code

        total = input_numbers[0]
        for k, op in enumerate(operator_code, start=1):
            if op == '0':
                total += input_numbers[k]
            else:
                total *= input_numbers[k]
        
        if total == test_value:
            calibration_result += test_value
            break
print(calibration_result)
