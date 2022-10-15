# enumerate
L = [1,2,3,4,9,8,7]

for id, el in enumerate(L):
    print('Индекс элемента:',id,'сам элемент',el,' из списка L')
# тот же код без enumerate
print()

for id in range(len(L)):
    print('Индекс элемента:',id,'сам элемент',L[id],' из списка L')