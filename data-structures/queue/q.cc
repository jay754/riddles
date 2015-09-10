#include <iostream>
#include <stdlib.h>

struct Q{
  int first;
  int last;
  int count;
  int size[100];
};

struct Q* createQ(){
  struct Q* q = (struct Q*)malloc(sizeof(struct Q));
  q->first = 0;
  q->last = 100-1;
  q->count = 0;

  return q;
}

void push(struct Q* q, int element){
  q->last = (q->last+1) % 100; // this ensures everytime that the queue is pushed onto the first
  q->size[q->last] = element;
  q->count++;
}

int pop(struct Q* q){
  int last;
  if(q->count > 0){
    last = q->size[q->first];
    q->first = (q->first+1) % 100;
    q->count--;
  }
  return last;
}

bool empty(struct Q* q){
  if(q->count == 0){
    return true;
  }
  return false;
}

int main(){
  struct Q* q = createQ();
  // std::cout << empty(q) << std::endl;

  push(q, 10);
  push(q, 30);
  push(q, 40);

  // std::cout << pop(q) << std::endl;
  // std::cout << pop(q) << std::endl;

  for(int i=0; i<q->count;i++){
    std::cout << q->size[i] << std::endl;
  }

  // std::cout << q->count << std::endl;
}
