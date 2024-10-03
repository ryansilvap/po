import pulp

# Entrada do usuário para o número de variáveis
num_variaveis = int(input("Insira o número de variáveis: "))

# Cria o problema de maximização
prob = pulp.LpProblem("Simplex_Maximizacao", pulp.LpMaximize)

# Cria as variáveis de decisão dinamicamente
variaveis = [pulp.LpVariable(f'x{i}', lowBound=0) for i in range(1, num_variaveis + 1)]

# Coeficientes da função objetivo
coef_obj = []
for i in range(num_variaveis):
    coef = float(input(f"Insira o coeficiente da variável {i+1} na função objetivo: "))
    coef_obj.append(coef)

# Função objetivo
prob += pulp.lpSum(coef_obj[i] * variaveis[i] for i in range(num_variaveis)), "FO"

# Restrições
num_restricoes = int(input("Insira o número de restrições: "))
for i in range(num_restricoes):
    coef_restricao = []
    print(f"Restrição {i+1}:")
    for j in range(num_variaveis):
        coef = float(input(f"Insira o coeficiente da variável {j+1} na restrição {i+1}: "))
        coef_restricao.append(coef)
    relacao = input(f"Insira a relação (<=, >=, ou =) para a restrição {i+1}: ")
    value = float(input(f"Insira o valor da restrição {i+1}: "))

    if relacao == "<=":
        prob += pulp.lpSum(coef_restricao[j] * variaveis[j] for j in range(num_variaveis)) <= value
    elif relacao == ">=":
        prob += pulp.lpSum(coef_restricao[j] * variaveis[j] for j in range(num_variaveis)) >= value
    elif relacao == "=":
        prob += pulp.lpSum(coef_restricao[j] * variaveis[j] for j in range(num_variaveis)) == value

# Resolve o problema
prob.solve()

# Imprime o resultado
#print("Status:", pulp.LpStatus[prob.status])
print("Valor ótimo:", pulp.value(prob.objective))
for v in variaveis:
    print(f"{v.name} =", pulp.value(v))
