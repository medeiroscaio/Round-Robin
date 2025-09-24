from processo import Processo
from collections import deque

# Define o quantum do Round Robin
QUANTUM = 2

# Lista de processos com: pid, tempo de chegada (arrivalTime), e tempo de execução (burstTime)
processos = [
    Processo("P1", 0, 10),
    Processo("P2", 1, 5),
    Processo("P3", 2, 8)
]

# Fila de prontos (ready queue)
ready_queue = deque()

# Tempo atual da simulação
current_time = 0

# Adiciona todos os processos à fila de prontos 
for p in processos:
    ready_queue.append(p)

# Início da simulação
print(f"Simulacao Round Robin (Quantum = {QUANTUM}):")

# continua enquanto houver processos na fila
while ready_queue:

    # Pega o próximo processo da fila
    current_process = ready_queue.popleft()

    # Calcula o tempo de execução desta rodada 
    time_to_run = min(QUANTUM, current_process.burstTimeRemaining)

    # Armazena o tempo de início da execução atual
    start_time = current_time

    # Atualiza o tempo restante de CPU para esse processo
    current_process.burstTimeRemaining -= time_to_run

    # Atualiza o tempo global da simulação
    current_time += time_to_run

    # Mostra qual processo está sendo executado e o tempo restante
    print(f"[{start_time} - {current_time}]: Executando {current_process.pid}. Restante: {current_process.burstTimeRemaining}")

    # Verifica se o processo terminou
    if current_process.burstTimeRemaining == 0:
        current_process.isComplete = True
        completion_time = current_time

        # Calcula Turnaround Time (tempo total de vida do processo)
        turnaround_time = completion_time - current_process.arrivalTime

        # Calcula Waiting Time (tempo de espera)
        waiting_time = turnaround_time - current_process.burstTime

        print(f"  -> {current_process.pid} CONCLUIDO. WT= {waiting_time} TAT = {turnaround_time} CT = {completion_time}")
    else:
        # Se não terminou, volta para o fim da fila
        ready_queue.append(current_process)

# Fim da simulação
print("\nFinalizacao da simulacao.")
