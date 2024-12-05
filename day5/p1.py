import re
def split_page_ordering_rules_updates(input):

    # ordering_rules part
    # we get every couple of numbers having pattern "XX|YY"
    ordering_rules_list = [item.split("|") for item in re.findall(r"\d+\|\d+",input)]
    # we create a dictionary having key being the "XX" and the values every "YY"
    ordering_rules = {}
    for key,value in ordering_rules_list:
        if key not in ordering_rules:
            ordering_rules[key] = []
        ordering_rules[key].append(value)

    # update part
    # we get every numbers in the lines having pattern "XX,YY,...."
    updates = [item.split(",") for item in re.findall(r"^\d+(?:,\d+)*$",input, flags=re.MULTILINE)]
    return ordering_rules,updates

def get_corrects_updates(ordering_rules, updates):
    correct_updates = []
    for update in updates:
        correct = True
        n = len(update)
        for i in range(n):
            key = update[i]
            for j in range(i):
                value = update[j]
                # If there is a rule for our current char
                # is there a char before it that is supposed to be after
                if key in ordering_rules and value in ordering_rules[key]:
                    correct = False
        if correct:
            correct_updates.append(update)
    return correct_updates

def calculate_sum_mid_values(updates):
    # sum of mids of a list of lists
    return sum([int(update[int (len(update)/2)]) for update in updates])


if __name__ == "__main__":
    with open("input", "r") as f:
        input = f.read()
    ordering_rules,updates = split_page_ordering_rules_updates(input)
    updates = get_corrects_updates(ordering_rules,updates)
    
    result = calculate_sum_mid_values(updates)
    print(f"Total is: {result}")