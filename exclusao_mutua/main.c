#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#define MAX 1000000000
pthread_mutex_t the_mutex;
pthread_cond_t condc, condp;
int buffer[5] = {0, 0, 0, 0, 0};
const clock_t MAXDELAY = 2000000;

void delay(clock_t ticks) { /* a "busy" delay */
  clock_t start = clock();
  do
    ; while (clock() < start + ticks);
}


void imprimir_buffer(){

    printf("----------[");
    for (int i = 0; i < 5; i++){
        printf("%d", buffer[i]);
    }
    printf("]----------\n");
}

void *producer(void *ptr) {
    int i;

    /* usado para sinalizacao */
    /* buffer usado entre produtor e consumidor */
    /* dados do produtor */
    for (i = 1; i <= MAX; i++) {
        pthread_mutex_lock(&the_mutex); /* obtem acesso exclusivo ao buffer */
        while (buffer[0] != 0)
            // Pode acabar a fatia de tempo?
            pthread_cond_wait(&condp, &the_mutex);
            
        for(int j = 0; j < 5; j++){
        printf("Colocando item %d no buffer\n", j + 1);
        buffer[j] = 1; /*coloca item no buffer */
        imprimir_buffer();
        delay(MAXDELAY);
        }

        pthread_cond_signal(&condc); /* acorda consumidor */
        pthread_mutex_unlock(&the_mutex);/* libera acesso ao buffer */
    }

    pthread_exit(0);
}

void *consumer(void *ptr) {
    int i;

    /* quantos numeros produzir */
    /* dados do consumidor */
    for (i = 1; i <= MAX; i++) {
        pthread_mutex_lock(&the_mutex); /* obtem acesso exclusivo ao buffer */
        while (buffer[0] == 0) pthread_cond_wait(&condc, &the_mutex);
        
        for(int j = 4; j >= 0; j--){
        printf("Retirando item %d no buffer\n", j + 1);
       	buffer[j] = 0; /* retira o item do buffer */
       	imprimir_buffer();
        delay(MAXDELAY);
       	}
        /* acorda o produtor */
        pthread_cond_signal(&condp);
        pthread_mutex_unlock(&the_mutex);/* libera acesso ao buffer */
    }
    pthread_exit(0);

}

int main(int argc, char **argv)
{
    pthread_t pro, con;
    pthread_mutex_init(&the_mutex, 0);
    pthread_cond_init(&condc, 0);
    pthread_cond_init(&condp, 0);
    pthread_create(&con, 0, consumer, 0);
    pthread_create(&pro, 0, producer, 0);
    pthread_join(pro, 0);
    pthread_join(con, 0);
    pthread_cond_destroy(&condc);
    pthread_cond_destroy(&condp);
    pthread_mutex_destroy(&the_mutex);
}
