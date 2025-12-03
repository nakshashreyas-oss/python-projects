                    # Solution for Arithmetic Formatter

def arithmetic_arranger(problems, display_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes_line = []
    answers_line = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid format."

        operand1, operator, operand2 = parts

        # Check for operator validity
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Check for digit-only operands
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        # Check for operand length
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Determine width of each problem
        width = max(len(operand1), len(operand2)) + 2

        # Build each line
        first_line.append(operand1.rjust(width))
        second_line.append(operator + operand2.rjust(width - 1))
        dashes_line.append('-' * width)

        # Compute and format answer (if requested)
        if display_answers:
            if operator == '+':
                result = str(int(operand1) + int(operand2))
            else:
                result = str(int(operand1) - int(operand2))
            answers_line.append(result.rjust(width))

    # Combine lines with 4 spaces between problems
    arranged_problems = (
        '    '.join(first_line) + '\n' +
        '    '.join(second_line) + '\n' +
        '    '.join(dashes_line)
    )

    if display_answers:
        arranged_problems += '\n' + '    '.join(answers_line)

    return arranged_problems