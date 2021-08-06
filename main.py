from actions import move, choose_random_action

def q_update(state, action, next_state, rw, q_matrix, alpha, gamma):
    # Atualiza a utilidade relacionada ao estado state e a ação action
    # Recompensa atual + utilidade esperada da melhor ação possível do proximo estado.
    estimate_q = rw[state] + gamma * max(q_matrix[next_state][0], q_matrix[next_state][1], q_matrix[next_state][2], q_matrix[next_state][3])

    # Ajusta a q_matrix considerando o valor atual da qualidade e o desvio em relação a estimativa estimate_q
    q_value = q_matrix[state][action] + alpha * (estimate_q - q_matrix[state][action])

    return q_value

num_states = 12 # 0..11
num_actions = 4 # 0..3

actions_names = ['u', 'd', 'l', 'r']

# Exemplo: No modelo q_matrix[2][0] -> Qualidade de andar para cima no estado 3
# Actions -> 0: up | 1: down | 2: left | 3: right

# Inicializa q_matrix com zeros
q_matrix = [[0 for x in range(num_actions)] for y in range(num_states)]

# insere os valores de estados terminais
for i in range (len(q_matrix[11])):
    q_matrix[11][i] = 1
for i in range (len(q_matrix[10])):
    q_matrix[10][i] = -1
for i in range (len(q_matrix[9])):
    q_matrix[9][i] = 0.2

alpha = 0.5
gamma = 1

# array de recompensas
#R = -0.4
R = -0.04
rw = [R for i in range(num_states)]
rw[11] = 1
rw[10] = -1
rw[9] = 0.2

for i in range(100):
    # cada iteração representa uma exploração do ambiente a partir do estado inicial
    state = 0
    terminal = True

    while (terminal):
        # escolher uma ação qualquer
        action_trial = choose_random_action()

        # Aplicar a ação e observar o estado alcançado
        next_state = move(state, action_trial)
        print(state, actions_names[action_trial], next_state)

        # Atualizar a utilidade relacionada ao estado state e açãoe escolhida
        q_matrix[state][action_trial] = q_update(state, action_trial, next_state, rw, q_matrix, alpha, gamma)

        # Atualizar estado atual
        state = next_state

        # teste de parada
        if (state == 11):
            terminal = False
        if (state == 10):
            terminal = False
        if (state == 9):
            terminal = False

    print ("fim do loop ", i)

def max_col(matrix, num_states):
    max_cols = [-1 for x in range(num_states)]
    for i in range(len(matrix)):
        max_q = -9999
        for j in range(len(matrix[i])):
            if (matrix[i][j] >= max_q):
                max_q = matrix[i][j]
                max_cols[i] = j
    
    return max_cols

# imprimir a política retornada
policy = max_col(q_matrix, num_states)

# printar a policy
print(actions_names[policy[2]], actions_names[policy[5]], actions_names[policy[8]], "+1")
print(actions_names[policy[1]], "*"                     , actions_names[policy[7]], "-1")
print(actions_names[policy[0]], actions_names[policy[3]], actions_names[policy[6]], "+0.2")

    