# l-system settings
gens = 10
axiom = 'A'
charcter_1, rule_1 = 'A', 'AB'
charcter_2, rule_2 = 'B', 'A'

def apply_rules(axiom):
    result = ''
    for character in axiom:
        if character == charcter_1:
            result += rule_1
        else:
            result += rule_2
    return result

for gen in range(gens):
    input()
    print(f'generation {gen}: {axiom}')
    axiom = apply_rules(axiom)
print(len(axiom))