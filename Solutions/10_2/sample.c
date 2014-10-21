/* sample.c */
#include <math.h>

/* A function that determines if an integer is a prime number or not.
   This is just a naive implementation--there are faster ways to do it */

int isprime(int n) {
  int factor = 3;
  /* Special case for 2 */
  if (n == 2) {
    return 1;
  }
  /* Check for even numbers */
  if ((n % 2) == 0) {
    return 0;
  }
  /* Check for everything else */
  while (factor*factor < n) {
    if ((n % factor) == 0) {
      return 0;
    }
    factor += 2;
  }
  return 1;
}

/* Compute the greatest common divisor */
int gcd(int x, int y) {
    int g = y;
    while (x > 0) {
        g = x;
        x = y % x;
        y = g;
    }
    return g;
}

/* Volume of a cone */
double cone_volume(double radius, double height) {
  return (M_PI*radius*radius*height/3.0);
}

/* A C data structure */
typedef struct Point {
    double x,y;
} Point;

double distance(Point *p1, Point *p2) {
   return hypot(p1->x - p2->x, p1->y - p2->y);
}

