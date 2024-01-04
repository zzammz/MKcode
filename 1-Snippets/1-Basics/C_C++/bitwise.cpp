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


// ----- bitwise
void Test_Bitwise(void)
{
	int a = 60;
	int b = 13;
	int c = 2;

	printf("a&b=%d\n", a&b);
	printf("a|b=%d\n", a|b);
	printf("a^b=%d\n", a^b);
	printf("~a=%d\n", ~a);
	printf("c<<2=%d\n", c<<2);
	printf("c>>2=%d\n", c>>2);
}


int main (void)
{


	Test_Bitwise();

}


