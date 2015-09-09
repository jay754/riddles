#include <iostream>
#include <stdlib.h>

struct Node{
  int value;
  struct Node *next;
};

struct Linkedlist{
  struct Node *head;
};

struct Linkedlist* createLinkedlist(){
  struct Linkedlist* list = (struct Linkedlist*)(malloc(sizeof(struct Linkedlist)));
  list->head = NULL;
  return list;
}

void addNode(struct Linkedlist* list, int element){
  struct Node* temp = (struct Node*)malloc(sizeof(struct Node));
  temp->value = element;
  temp->next = list->head;
  list->head = temp;
}

void deleteNode(struct Linkedlist* list, int element){
  struct Node* currentNode = list->head;
  struct Node* prev = NULL;
  int found = 0;

  while (found == 0){
    if (currentNode->value==element){
      found = 1;
    }
    else{
      prev = currentNode;
      currentNode = currentNode->next;
    }
  }

  if(prev == NULL){
    list->head = currentNode->next;
  }
  else{
    prev->next = currentNode->next;
  }
}

int containsNode(struct Linkedlist* list, int element){
  struct Node* currentNode = list->head;
  int found = 0;

  while(found == 0){
    if(currentNode->value == element){
      found = 1;
      return found;
    }
    else{
      currentNode = currentNode->next;
    }
  }

  return found;
}

void display(struct Linkedlist* list){
  struct Node* currentNode = list->head;

  while(currentNode != NULL){
    std::cout << currentNode->value << std::endl;
    currentNode = currentNode->next;
  }
}

int main(){
  struct Linkedlist* list = createLinkedlist();
  addNode(list, 23);
  addNode(list, 4);
  display(list);
  deleteNode(list, 4);
  display(list);
  return 0;
}
