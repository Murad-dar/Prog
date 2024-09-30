#include <stdio.h>

int calc_sum_digits(int number)
{
    int sum = 0;
    int rest;
    while(number != 0){
        rest = number % 10;
        sum = sum + rest;
        number = number / 10;
    } 
    return sum;
}


int main()
{
    int a, b;
    printf("Enter a -> ");
    scanf("%d", &a);
    printf("Enter b -> ");
    scanf("%d", &b);
   

    if (!a && !b)
        return 0;

    int sum_a = calc_sum_digits(a);
    int sum_b = calc_sum_digits(b);
    
    if (sum_a > b)
        printf("sum_a = %d\n", sum_a);
    if (sum_a == b)
        printf("sum_b = %d\n", sum_b);
    if (sum_a < b)
        printf("sum_b + b = %d\n", sum_b + b);

    return 0;
}
