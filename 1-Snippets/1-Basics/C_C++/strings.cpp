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


void TestString(void)
{
	ShowFuncName("TestString");
	char mystr[] = "Hello darkness my old friend";
	char *cptr;
	cptr = strstr(mystr, "my");
	if (cptr)
		ShowMsg("found");
	else
		ShowMsg("not found");
	ShowMsg("");

}


int main (void)
{

	TestString();

}


