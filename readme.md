# Escalonador Round Robin

## Descrição da Simulação

Usamos o escalonador **Round Robin** para simular a execução de processos. O funcionamento segue os seguintes passos:

1. Criamos os processos com a classe `Processo`, cada um contendo:

   - Tempo de chegada
   - Tempo de execução total
   - Um identificador único

2. Todos os processos são colocados em uma **fila de prontos**, que funciona de forma **circular**.

3. Definimos um **quantum** (neste caso, **2 unidades de tempo**) e iniciamos o **relógio da simulação** em zero.

4. A cada passo:

   - Retiramos o primeiro processo da fila.
   - Executamos o processo pelo menor tempo entre:
     - O valor do quantum
     - O tempo restante de execução do processo
   - Atualizamos o **relógio global**
   - Exibimos qual processo está sendo executado e quanto tempo ainda falta.

5. Após a execução:

   - Se o processo **terminou**, ele é marcado como concluído e calculamos:
     - `Completion Time` (tempo em que o processo finalizou)
     - `Turnaround Time` (tempo total no sistema: finalização - chegada)
     - `Waiting Time` (tempo total em espera na fila)
   - Caso **não tenha terminado**, ele retorna ao **fim da fila** para aguardar sua próxima vez.

6. O ciclo se repete até que **todos os processos terminem**.

7. Ao final, o programa mostra a **finalização da simulação**.

## Conceito do Escalonador Round Robin

O **Round Robin** é um algoritmo de escalonamento de processos que funciona dividindo o tempo da CPU em pequenas fatias chamadas **quantum**. Seu funcionamento é:

- Cada processo recebe a CPU por um quantum, em ordem sequencial, dentro de uma **fila circular**.
- Quando o tempo do quantum **expira**, o processo em execução é **interrompido** e enviado para o **final da fila**, dando lugar ao próximo.

### Vantagens do Round Robin:

- **Justiça**: todos os processos têm a mesma oportunidade de acesso à CPU.
- **Bom tempo de resposta**: especialmente em sistemas interativos.
- **Preempção**: o sistema pode interromper a execução de um processo antes que ele termine, garantindo alternância e respeitando o quantum.
