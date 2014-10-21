/* sample.h */

extern int isprime(int n);
extern int gcd(int x, int y);
extern double cone_volume(double radius, double height);
extern void addv(double *a, double *b, double *c, int n);

/* A C data structure */
typedef struct Point {
    double x,y;
} Point;

extern double distance(Point *p1, Point *p2);
