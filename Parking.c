#include <stdio.h>

int main() { int m; //printf("Type a number and press enter: \n"); 

  // Get and save the number the user types
  scanf("%d", &m); int u; scanf("%d", &u); /* 2D array declaration*/
  int d[m][u]; /*Counter variables for the loop*/
  int i, j, p, t = 0, c = 0; for(i=0; i<m; i++) { for(j=0;j<u;j++) {
         //printf("Enter value for disp[%d][%d]:", i, j);
         scanf("%d", &d[i][j]); c+=d[i][j];} if (t < c) { t = c; p = m;// i==m-1 && j > 0
} c = 0;} // Print the number the user typed
  //printf("Your number is: %d", myNum);
return p;}
