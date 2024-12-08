### part 1 of the day 7 of adventofcode
### https://adventofcode.com/2024/day/7

import itertools

# Get every possible expressions for every operators
def getEveryPossibleExpressions(everyOperators,operations):
    everyOperations = []
    for operators in everyOperators:
        everyOperations.append(getPossibleExpressions(everyOperators,operations))
    return everyOperations

# get every possible expressions for a given operator list
def getPossibleExpressions(possible_operators,operations):
    possible_expressions = []
    for ops in itertools.product(operations, repeat=len(possible_operators)-1):
        expression_parts = []
        for number, op in itertools.zip_longest(possible_operators, ops, fillvalue=''):
            expression_parts.append(str(number))
            if op:
                expression_parts.append(op)
        possible_expressions.append(expression_parts)
    return possible_expressions

# Get every possible evaluation of an expression_list
def evaluateExpressions(expression_list):
    possible_outcomes = []
    expression_list=expression_list[0]
    for expression in expression_list:
        i = 0
        n = len(expression)
        outcome_of_current_expression = [int(expression[0])]
        while i+2<n:
            if expression[i+1] == "*":
                outcome_of_current_expression.append(outcome_of_current_expression[i//2]*int(expression[i+2]))
            else:
                outcome_of_current_expression.append(outcome_of_current_expression[i//2]+int(expression[i+2]))
            i+=2
        possible_outcomes.append(outcome_of_current_expression[-1])
    return possible_outcomes

# Parse the input, splitting the target values and the operators
def parse_input(input):
    target_values, everyOperators = [],[]
    for line in input:
        line = line.split()
        target_values.append(int(line[0][:-1]))
        everyOperators.append(list(map(int,line[1:])))
    return target_values,everyOperators

# calculate the calibration result
def calculate_calibration_result(target_value,possible_outcomes):
    if target_value in possible_outcomes:
        return target_value
    return 0

if __name__ == "__main__":
    with open("input", "r") as f:
        input = f.readlines()
    target_values,everyOperators = parse_input(input)
    operations = ['+', '*']
    result = 0
    i=0
    for operators in everyOperators:
        possible_expressions = getEveryPossibleExpressions(operators,operations)
        possible_outcomes = evaluateExpressions(possible_expressions)
        result+= calculate_calibration_result(target_values[i],possible_outcomes)
        i+=1
    print(f"Total is: {result}")


