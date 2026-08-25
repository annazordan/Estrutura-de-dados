#include <stdio.h>

int vetor[5] = {2,3,5,4,1};

int main(){
int aux;
int qtd = 5;
int j;
int troca = 0; //Cria a variável que vai controlar os passos para trás (da direita para a esquerda) na parte já ordenada do vetor.

printf("\nVetor Original: "); //Um loop que começa no índice 0 e vai até o 4 (i < qtd).
for(int i = 0; i < qtd; i++){ //A cada rodada, o printf mostra o número que está naquela posição do vetor formatado dentro de colchetes. 
	printf(" [%i] ", vetor[i]); //O %i avisa que o computador deve colocar um número inteiro ali.
}

for(int i=1; i < qtd; i++){ //Ele parte do índice 1 (o segundo elemento, que é o 3) porque o primeiro (5) já é considerado ordenado sozinho.
aux = vetor[i]; //Pega o elemento atual que queremos colocar no lugar certo e o guarda em segurança na variável aux.
j = i - 1; //Define que a nossa comparação deve começar pelo elemento que está imediatamente à esquerda do atual (i - 1).
while(j >= 0 && aux < vetor[j]){ /*O loop de comparação. Ele continuará rodando e empurrando os números para o lado enquanto:
								j >= 0: Ainda estivermos dentro dos limites do vetor (sem passar do primeiro elemento).
								aux < vetor[j]: O número guardado na nossa "mão" (aux) for menor do que o número do vetor na posição j.*/
vetor[j+1] = vetor[j]; //(Dentro do while) Copia o elemento maior para a posição da direita (j+1). Isso abre o espaço na memória que precisamos.			 
j--;
 troca++;				   //(Dentro do while) Subtrai 1 de j. Isso faz o algoritmo olhar para o próximo número mais à esquerda na próxima rodada do while.						 
}
vetor[j+1] = aux;
//Quando o while termina (porque achou alguém menor ou chegou no início), o espaço correto foi aberto.
}
				//Essa linha coloca o valor salvo em aux de volta no vetor na posição exata dele.
		printf("\nVetor Ordenado: ");
	for(int i =0; i <qtd; i++){
		printf(" [%i] ",vetor[i]);
	}
	printf("Trocas => [%i]", troca);
}
