
#include <stdio.h>
#include <stdlib.h>


void pname(const char *msg)
{
	printf("\n====== %s\n", msg);
}

//------------------- TREE

struct TREENODE
{
	int t_data;
	TREENODE *tptr_left, *tptr_right;
};

struct TREENODE *TreeNewNode(int new_val)
{
	TREENODE *tmpptr = (TREENODE *) malloc (sizeof(TREENODE));
	if (tmpptr)
	{
		tmpptr->tptr_left = tmpptr->tptr_right = NULL;
		tmpptr->t_data = new_val;
	}
	return tmpptr;
}


void TreePrintPreOrder(TREENODE *treeptr)
{
	if (treeptr==NULL)
		return;
	printf("%d ", treeptr->t_data);
	TreePrintPreOrder(treeptr->tptr_left);
	TreePrintPreOrder(treeptr->tptr_right);
}

void TreePrintInOrder(TREENODE *treeptr)
{
	if (treeptr==NULL)
		return;
	TreePrintInOrder(treeptr->tptr_left);
	printf("%d ", treeptr->t_data);
	TreePrintInOrder(treeptr->tptr_right);
}

void TreePrintPostOrder(TREENODE *treeptr)
{
	if (treeptr==NULL)
		return;
	TreePrintPostOrder(treeptr->tptr_left);
	TreePrintPostOrder(treeptr->tptr_right);
	printf("%d ", treeptr->t_data);
}


void test_tree(void)
{
	/* Let us create following tree 
            1
          /    \ 
         2       3
        / \     /  \ 
       4    5   6   7   */

	pname("test_tree");
	TREENODE *root = TreeNewNode(1);
	root->tptr_left = TreeNewNode(2);
	root->tptr_right = TreeNewNode(3);
	root->tptr_left->tptr_left = TreeNewNode(4);
	root->tptr_left->tptr_right = TreeNewNode(5);
	root->tptr_right->tptr_left = TreeNewNode(6);
	root->tptr_right->tptr_right = TreeNewNode(7);
	
	printf("\n--- TREE ---\n");
	printf("\npre order traversal of tree\n");
	TreePrintPreOrder(root);

	printf("\n--- TREE ---\n");
	printf("\nin order traversal of tree\n");
	TreePrintInOrder(root);

	printf("\n--- TREE ---\n");
	printf("\npost order traversal of tree\n");
	TreePrintPostOrder(root);
}



//------------------- BST

TREENODE * InsertBST (TREENODE *treeptr, int new_val)
{
	if (treeptr==NULL)
		return TreeNewNode(new_val);
	
	if(new_val < treeptr->t_data)
		treeptr->tptr_left = InsertBST(treeptr->tptr_left, new_val);
	else if (new_val > treeptr->t_data)
		treeptr->tptr_right = InsertBST(treeptr->tptr_right, new_val);
	return treeptr;
}


TREENODE * SearchBST(TREENODE * rootptr, int key_val)
{
	if (rootptr==NULL || rootptr->t_data == key_val)
		return rootptr;
	if (key_val > rootptr->t_data)
		return SearchBST(rootptr->tptr_right, key_val);
	
	return SearchBST(rootptr->tptr_left, key_val);
}

void test_BST(void)
{
/* Let us create following BST 
              50 
           /     \ 
          30      70 
         /  \    /  \ 
       20   40  60   80 */

	pname("\ntest_BST");
	TREENODE * root = NULL;
	root = InsertBST(root, 50);
	InsertBST(root, 30);
	InsertBST(root, 20);
	InsertBST(root, 40);
	InsertBST(root, 70);
	InsertBST(root, 60);
	InsertBST(root, 80);

	printf("\n--- BST ---\n");
	printf("\npre order traversal of tree\n");
	TreePrintPreOrder(root);

	printf("\n--- TREE ---\n");
	printf("\nin order traversal of tree\n");
	TreePrintInOrder(root);

	printf("\n--- TREE ---\n");
	printf("\npost order traversal of tree\n");
	TreePrintPostOrder(root);
	
	TREENODE * searchptr = SearchBST(root, 40);
	if (searchptr != NULL)
		printf("\nsearchval=%d\n", searchptr->t_data);
	else
		printf("\nnot found\n");

}



int main()
{
	test_tree();
	test_BST();

	return 0;
}
