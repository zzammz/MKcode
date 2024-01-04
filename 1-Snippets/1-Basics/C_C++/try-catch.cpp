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


// ----- try catch
void Test_TryCatch(void)
{
	ShowFuncName("Test_TryCatch");
	int mynum = 42;
	try
	{
		throw 20;
	}
	catch (int e)
	{
		printf("error %d\n", e);
	}

	// exception handling
	int x = 10;
	int y = 0;
	try
	{
		int z = x/y;
		//cout << "z=" << z << "\n";
	}
	catch (const char *msg)
	{
		cout << "ERR: " << msg << "\n";
	}
}


int main (void)
{

	Test_TryCatch();

}


