// http://www.geeksforgeeks.org/splay-tree-set-1-insert/
// http://cslibrary.stanford.edu/110/BinaryTrees.html

// Full credit to the above links for their work

#include <iostream>
#include <stdlib.h>

struct Node{
  int key;
  struct Node* left;
  struct Node* right;
};

struct Node* createNode(int key){
  struct Node* node = (struct Node*)malloc(sizeof(struct Node));
  node->key = key;
  node->right = NULL;
  node->left = NULL;
  return node;
}

struct Node* insert(struct Node* node, int key){
  if (node == NULL){
    return createNode(key);
  }

  if(key < node->key){
    if(node->left == NULL){
      node->left = createNode(key);
    }
    else{
      node->left = insert(node->left, key);
    }
  }
  else if(key > node->key){
    if(node->right == NULL){
      node->right = createNode(key);
    }
    else{
      node->right = insert(node->right, key);
    }
  }

  return node;
}

struct Node* getMinimum(struct Node* node){
  struct Node* current = node;

  while(current->left == NULL){
    current = node->left;
  }

  return current;
}

struct Node* getMaximum(struct Node* node){
  struct Node* current = node;

  while(current->right == NULL){
    current = node->right;
  }

  return current;
}

struct Node* deleteNode(struct Node* node, int key){
  if (node == NULL){
    return node;
  }

  if(key < node->key){
    node->left = deleteNode(node->left, key);
  }
  else if(key > node->key){
    node->right = deleteNode(node->right, key);
  }
  else{
    if(node->left == NULL){
      struct Node* temp = node->right;
      free(node);
      return temp;
    }
    else if(node->right == NULL){
      struct Node* temp = node->left;
      free(node);
      return temp;
    }

    struct Node* temp = getMinimum(node->right);
    node->key = temp->key;
    node->right = deleteNode(node->right, temp->key);
  }

  return node;
}

struct Node* rightRotate(struct Node* node){
  struct Node* temp = node->left;
  node->left = temp->right;
  temp->right = node;
  return temp;
}

struct Node* leftRotate(struct Node* node){
  struct Node* temp = node->right;
  node->right = temp->left;
  temp->left = node;
  return temp;
}

struct Node* splay(struct Node* node, int key){
  if(node == NULL){
    return node;
  }

  if (node->key > key){
    if (node->left == NULL){
      return node;
    }

    if(node->left->key > key){
      node->left->left = splay(node->left->left, key);
      node = rightRotate(node);
    }
    else if(node->left->key < key){
      node->left->right = splay(node->left->right, key);

      if (node->left->right == NULL){
        node->left = leftRotate(node->left);
      }
    }

    if(node->left == NULL){
      return node;
    }
    else{
      return rightRotate(node);
    }
  }

  else{
    if(node->right == NULL){
      return node;
    }

    if(node->right->key > key){
      node->right->left = splay(node->right->left, key);

      if(node->right->left != NULL){
        node->right = rightRotate(node->right);
      }
    }
    else if(node->right->key < key){
      node->right->right = splay(node->right->right, key);
      node = leftRotate(node);
    }
  }

  if(node->right == NULL){
    return node;
  }
  else{
    return leftRotate(node);
  }
}

struct Node* search(struct Node* root, int key){
    return splay(root, key);
}

int size(struct Node* root){
  return size(root->left) + size(root->right) + 1;
}

/*
  Inverse method will change left values to the right
*/

void inverseTree(struct Node* node){
  if(node != NULL){
    struct Node* temp;

    inverseTree(node->left);
    inverseTree(node->right);

    temp = node->left;
    node->left = node->right;
    node->right = temp;
  }
}

/*

the whole point of bst is to have the right node greater
than the value. And the left node less than the value.

Hence getting the max of left and the min of the right
and checking if

The max(left) is greater than the node means that its a binary tree
and not a bst

same goes for the right. If the min(right) is less than node key
than it is binary tree and not a bst.
 */

int isBST(struct Node* node){
  if(node == NULL){
    return true;
  }

  if(node->left != NULL && getMaximum(node->left)->key > node->key){
    return false;
  }
  if(node->right != NULL && getMinimum(node->right)->key <= node->key){
    return false;
  }
  if(!isBST(node->left) || !isBST(node->right)){
    return false;
  }
  return true;
}

// this is to check whether a node is a leaf
// this can simply be obtained by checking if both
// left and right keys are null

int isLeaf(struct Node* node){
  if(node->right == NULL and node->left == NULL){
    return true;
  }
  return false;
}

void preOrder(struct Node* node){
  if (node != NULL){
    std::cout << node->key << std::endl;
    preOrder(node->left);
    preOrder(node->right);
  }
}

void inOrder(struct Node* node){
  if (node != NULL){
    inOrder(node->left);
    std::cout << node->key << std::endl;
    inOrder(node->right);
  }
}

void postOrder(struct Node* node){
  if (node != NULL){
    postOrder(node->left);
    postOrder(node->right);
    std::cout << node->key << std::endl;
  }
}

// Just to print the Tree

void printTree(struct Node* node){
  if(node != NULL){
    printTree(node->left);
    std::cout << node->key << std::endl;
    printTree(node->right);
  }
}

int main(){
  struct Node* root = createNode(100);

  root->left = createNode(50);
  root->right = createNode(200);
  root->left->left = createNode(40);
  root->left->left->left = createNode(30);
  root->left->left->left->left = createNode(20);

  root = search(root, 20);
  preOrder(root);
  // insert(root, 30);
  // insert(root, 20);
  // insert(root, 40);
  // insert(root, 70);
  // insert(root, 60);
  // insert(root, 80);
  // inOrder(root);
  //
  // deleteNode(root, 40);
  // inOrder(root);
  return 0;
}
