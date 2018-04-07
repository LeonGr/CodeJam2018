# sample_attack = "6 SCCSSC"
sample_imput = '''
6
1 CS
2 CS
1 SS
6 SCCSSC
2 CC
3 CSCSS
'''

def get_damage(attack):
    strength = 1
    damage = 0
    for char in attack:
        if char == 'C':
            strength *= 2
            # print("Charge the beam, doubling the beam's strength to " + str(strength))
        elif char == 'S':
            damage += strength
            # print("Shoot the beam, doing " + str(strength) + " damage.")

    return damage

def avert_attack(attack):
    max_damage = int(attack.split(" ")[0])
    attack_sequence = attack.split(" ")[1]
    # print('Max damage: ', max_damage)
    # print('Attack sequence: ', attack_sequence)

    if attack_sequence.count('S') > max_damage:
        return 'IMPOSSIBLE'

    swaps = 0

    while get_damage(attack_sequence) > max_damage:

        # print('Damage ' + str(get_damage(attack_sequence)) + ' is too much')

        # reversed_sequence = reversed(attack_sequence)
        sequence_list = [i for i in attack_sequence]

        reversed_sequence = sequence_list[::-1]

        for i, action in enumerate(reversed_sequence):
            # print(i, action)

            if action is 'C' and i is not 0:

                # print('Found first charge not at end at', i)

                if reversed_sequence[i-1] is 'S':

                    # print('Should switch')
                    # print(reversed_sequence)

                    reversed_sequence[i], reversed_sequence[i-1] = reversed_sequence[i-1], reversed_sequence[i]

                    # print(reversed_sequence)

                    normal_sequence = reversed_sequence[::-1]

                    # print('New damage: ', get_damage(normal_sequence))

                    swaps += 1

                    attack_sequence = normal_sequence

    return swaps

# print(sample_imput)

# lines = problem_input.splitlines()

# number_of_tests = int( lines[1] )

# test_cases = lines[2:]

# if not number_of_tests is len(test_cases):
    # print('Error')

# for index, case in enumerate(test_cases):
    # print('Case #' + str(index + 1) + ': ' + str(avert_attack(case)))

t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
  line = input() # read a list of integers, 2 in this case
  print("Case #{}: {}".format(i, avert_attack(line)))
