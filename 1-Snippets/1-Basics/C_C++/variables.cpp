#include <stdio.h>
#include <iostream>
#include <cstring>
using namespace std;



// ----------------- show vals
void ShowMsg(const char *msg)
{
	printf ("%s\n", msg);
}

void ShowVals (int ishow)
{
	printf ("show vals: %d\n", ishow);
}

void ShowVals(int *ishow)
{
	printf ("show vals: (*)\n");
	printf ("show vals: %d\n", *ishow);
	//*ishow++;
}
void ShowFuncName(const char *funcname)
{
	printf("\n----- %s\n", funcname);
}

// -------------- passing int
void IncrementInt(int *ii) // pass by pointer
{
	ShowMsg("print *int");
	*ii = 7;
}
/*
void IncrementInt(int ii) // pass by value
{
	ShowMsg("print int");
	ii = 8;
}
*/
void IncrementInt(int &ii) // pass by reference
{
	ShowMsg("print &int");
	ii = 9;
}


int main (void)
{
	printf ("Hello World!\n");
	std::cout << "Hello Again!" << "\n";

	// int passing
	int xx = 5;
	printf ("before: xx=%d\n", xx);
	IncrementInt(&xx);
	printf ("after: xx=%d\n", xx);

	IncrementInt(xx);
	printf ("after: xx=%d\n", xx);


}


