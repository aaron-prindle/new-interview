#include<stdio.h>

void reverseString(char* str){
  char tmp;
  char* left = str;
  char* right = str;
  while(*right){
    printf("%c\n", *right);
    right++;
  }
  right--;
  while(left<right){
    tmp = *left;
    *left = *right;
    *right = tmp;
    *left++;
    *right--;
  }
}

int main(){
  char* test = (char*)"hello";
  reverseString(test);
}

