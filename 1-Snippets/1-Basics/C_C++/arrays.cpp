#include <stdio.h>
#include <iostream>
#include <cstring>




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



// --------------- arrays & ptrs
void TestArrays(void)
{
	ShowFuncName("TestArrays");
	int array2 [2] [3] = {
		{101, 102, 103},
		{201, 202, 203}
	};
	int a1[3] = {31, 32, 33};

	int *p1;
	p1 = a1;
	printf ("val 1: %d\n", *p1);
	p1++;
	printf ("val 2: %d\n", *p1);
}

int main (void)
{

	TestArrays();

}


