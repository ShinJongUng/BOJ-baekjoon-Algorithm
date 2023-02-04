#include <stdio.h>

int main(void) {
    int maxb = 100;
    int ecob = 20;
    double t, p;
    scanf("%lf %lf", &t, &p);
    double result;
    if (p >= ecob) {
        double dpd = (maxb - p) / t;
        result = ((p - ecob) / dpd) + (ecob / (dpd / 2));
    }
    else {
        double dpd = ((maxb - ecob) + (ecob - p) * 2) / t;
        result = p / (dpd / 2);
    }
    printf("%.5lf\n", result);
    return 0;
}


