#include <iostream>
#include <stdio.h>
#include <stdlib.h>

struct Stack{
  int length;
  int size[100];
};

struct Stack* createStack(){
  struct Stack* stack1 = (struct Stack*)malloc(sizeof(struct Stack));
  stack1->length = 0;
  return stack1;
}

void push(struct Stack* stack1, int element){
  stack1->size[stack1->length++] = element;
}

int pop(struct Stack* stack1){
  return stack1->size[stack1->length--];
}

int main(){
  struct Stack* stack1 = createStack();
  push(stack1, 1);
  push(stack1, 2);
  push(stack1, 3);

  pop(stack1);
  std::cout << stack1->length << std::endl;

  for(int i=0;i<stack1->length;i++){
    std::cout << stack1->size[i] << std::endl;
  }

  return 0;
}
