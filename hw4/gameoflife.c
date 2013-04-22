#include "mpi.h"
#include <stdio.h>
#include <stdlib.h>

#define IS_ODD(x)  ((x % 2))


void life(int *outgoing, int *incoming, int my_ID, int buff_count, int num_procs, int rows, int dir) {
    int next;
    int prev;
    MPI_Status stat; 
    if (dir == 1) {
        next = (my_ID + 1) % num_procs;
        prev = ((my_ID == 0) ? (num_procs - 1) : (my_ID - 1));
    } else {
        next = next + prev;
        prev = next - prev;
        next = next - prev;
    }
    
    if (IS_ODD(my_ID)) {
        printf("ID: %d message send...\n", my_ID);
        MPI_Send(outgoing, buff_count, MPI_INT, next, 3, MPI_COMM_WORLD);    
        printf("ID: %d message receiving...", my_ID);
        MPI_Recv(incoming, buff_count, MPI_INT, prev, 3, MPI_COMM_WORLD, &stat);
    } else {
        printf("ID: %d message send...\n", my_ID);
        MPI_Recv(incoming, buff_count, MPI_INT, prev, 3, MPI_COMM_WORLD, &stat);
        printf("ID: %d message receiving...", my_ID);
        MPI_Send(outgoing, buff_count, MPI_INT, next, 3, MPI_COMM_WORLD);
    }
}
void update(int low, int high, int *up, int *down) {
    int i;
    int j;
    int count = 0;

    for (i = low; i < high; i++) {
        for (j = 0; j < dimension; j++) {
            count = 0;
            count += global_grid[(i - 1) % dimension][(j - 1) % dimension];
            count += global_grid[(i - 1) % dimension][j];
            count += global_grid[(i - 1) % dimension][(j + 1) % dimension];
            count += global_grid[i][(j - 1) % dimension];
            count += global_grid[i][(j + 1) % dimension];
            count += global_grid[(i + 1) % dimension][(j - 1) % dimension];
            count += global_grid[(i + 1) % dimension][j];
            count += global_grid[(i + 1) % dimension][(j + 1) % dimension];
    
    }
}
void slice(int *src, int *dest, int from, int to) {
    int i;
    for (i = from; i < to; i++) {
        dest[i - from] = src[i];
    }
}

void copyto(int *src, int *dest, int from, int to) {
    int i;
    for (i = from; i < to; i++) {
        dest[i] = src[i - from];
    }
}

int main(int argc, char **argv){
 /* Global constant data */
    const int dimension = 16;     // assume a square grid
    int my_grid[ 256 ] = { 
                            0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                            0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,
                            1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,
                            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 
                        };
    int *temp_grid;
    int ID;
    int num_procs = 0;
    int low = 0, high = 0;
    int *outgoing, *up, *down, *incoming;
    int i;
    double t0;
    int itr = 0;
    MPI_Status stat; 

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &ID);
    MPI_Comm_size(MPI_COMM_WORLD, &num_procs);
    
    if (num_procs != 1 && num_procs != 2 && num_procs != 4 && num_procs != 8 && num_procs != 16) {
        printf("Only support 1/2/4/8/16 processors\n");
        fflush(stdout);
        MPI_Abort(MPI_COMM_WORLD, 1);
    }
    int rows = dimension / num_procs;   
    low = ID * rows;
    high = low + rows;
    
    /* printf("THIS IS ID: %d\nprocs: %d\nlow: %d\nhigh: %d\n", ID, num_procs, low, high); */
    
    outgoing = (int *) malloc(dimension * sizeof(int));
    up = (int *) malloc(dimension * sizeof(int));
    down = (int *) malloc(dimension * sizeof(int));
    incoming = (int *) malloc(dimension * sizeof(int));
    
    for (itr = 0; itr < 64; i++) {
        MPI_Barrier(MPI_COMM_WORLD);
        slice(global_grid, outgoing, low * dimension, (low + 1) * dimension);
        life(outgoing, up, ID, dimension, num_procs, rows, 1); 
        slice(global_grid, outgoing, (high - 1) * dimension, high * dimension);
        life(outgoing, down, ID, dimension, num_procs, rows, 0);
        // XXX not correct, should update all the rows 
        copyto(up, global_grid, ((low - 1) % dimension) * dimension, low * dimension);
        copyto(down, global_grid, high * dimension, ((high + 1) % dimension) * dimension)
        update(low, high);
        if (ID == 0) {
            for (i = 1; i < num_procs; i++) {
                MPI_Recv(incoming, dimension, MPI_INT, i, 3, MPI_COMM_WORLD, &stat);
                // XXX

            }
        }
    }

                MPI_Send(x, dimension, MPI_INT, 0, 3, MPI_COMM_WORLD);
    /* printf("low: %d, high: %d up: ", low, high); */
    /* for (i = 0; i < dimension; i++) { */
    /*     printf("%d ", up[i]); */
    /* } */
    /* printf("\n"); */

    /* printf("low: %d, high: %d down: ", low, high); */
    /* for (i = 0; i < dimension; i++) { */
    /*     printf("%d ", down[i]); */
    /* } */
    /* printf("\n"); */

    t0 = MPI_Wtime();
    MPI_Finalize();
}
