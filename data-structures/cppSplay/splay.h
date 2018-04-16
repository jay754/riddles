#include <iostream>
#include <stdlib.h>

struct Node{
  int key;
  struct Node* left;
  struct Node* right;
};

struct Node* createNode(int key);
struct Node* insert(struct Node* node, int key);
struct Node* getMinimum(struct Node* node);
struct Node* deleteNode(struct Node* node, int key);
struct Node* rightRotate(struct Node* node);
struct Node* leftRotate(struct Node* node);
struct Node* splay(struct Node* node, int key);
struct Node* search(struct Node* root, int key);
void inverseTree(struct Node* node);
int isBST(struct Node* node);
int isLeaf(struct Node* node);
void preOrder(struct Node* node);
void inOrder(struct Node* node);
void postOrder(struct Node* node);
void printTree(struct Node* node);
