#include <stdio.h>
#include <math.h>
int main (){
    double h, x = 0;
    FILE *graph;
    printf("Enter h:");
    scanf("%lf", &h);
    graph = fopen("graphik.txt", "w");
    for (double x = 0; x <= 2; x = x + h){
        if(x <= 1){
            fprintf(graph, "%lf\t%lf\n", x, cos(x + pow(x,3)));
            printf("%lf\t%lf\n", x, cos(x + pow(x,3)));
        }else{
            fprintf(graph, "%lf\t%lf\n", x, exp(pow(-x,2)) - pow(x,2) + 2*x);
            printf("%lf\t%lf\n", x, exp(pow(-x,2)) - pow(x,2) + 2*x );
        }
    }
    fclose(graph);
    return 0;
}