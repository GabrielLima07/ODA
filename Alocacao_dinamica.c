// Projeto 09
#include <stdio.h>
#include <stdlib.h>

int main() {
    // declaração do ponteiro
    int *ptr, i; 
    // atribuindo ao ponteiro o tamanho de 22 inteiros
    ptr = (int *) calloc(22, sizeof(int)); 
    // realocando ao ponteiro o tamanho de 50 inteiros
    ptr = (int *) realloc(ptr, 50 * sizeof(int));

    // exibição dos bits do vetor
    for (i = 0; i < 50; i++) {
        printf(" ptr[%d] = %d\n", i, ptr[i]);
    }

    // liberação do ponteiro
    free(ptr);

    return 0;
}