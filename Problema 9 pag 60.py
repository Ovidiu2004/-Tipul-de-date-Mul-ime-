A=set(input('Dati litere mari ale alfabetului - A:'))
B=set(input('Dati litere mari ale alfabetului - B:'))
print(A)
print(B)
print('Intersectia multimilor A si B ->',A.intersection(B))
print('Reuniunea multimilor A si B ->',A.union(B))
print('Diferenta multimilor A si B ->',A.difference(B))
print('Diferenta multimilor B si A ->',B.difference(A))