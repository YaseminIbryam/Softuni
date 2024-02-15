electrons = int(input())
shell = 1
electron_distribution = []
while True:
    max_electrons_per_shell = 2 * shell ** 2
    if electrons >= max_electrons_per_shell:
        electrons_in_shell = max_electrons_per_shell
    elif electrons > 0:
        electrons_in_shell = electrons
    else:
        break
    electron_distribution.append(electrons_in_shell)
    electrons -= electrons_in_shell
    shell += 1
print(electron_distribution)
