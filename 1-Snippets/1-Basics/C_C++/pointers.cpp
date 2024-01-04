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
void TestPointer(void) // ptr to array
{
	ShowFuncName("TestPointer");
	#define ARRAY_LEN	3
	int ar2[ARRAY_LEN] = {7, 19, 11};
	int *iptr = NULL;

	iptr = ar2;
	for (int ii=0; ii<ARRAY_LEN; ii++, iptr++)
	{
		printf("up via counter: ii=%d  val=%d\n", ii, ar2[ii]);
		printf("up via ptr: ii=%d  val=%d\n", ii, *iptr);
	}
	printf("\n");
	iptr = &ar2[ARRAY_LEN-1];
	for (int ii=ARRAY_LEN-1; ii>=0; ii--, iptr--)
	{
		printf("down via ptr: ii=%d  val=%d\n", ii, *iptr);
	}
	printf("\n");
	iptr = ar2;
	while (iptr<=&ar2[ARRAY_LEN-1])
	{
		printf("up via ptr: val=%d\n", *iptr);
		iptr++;
	}
}
void TestPtr2CharArray(void)
{
	ShowFuncName("TestPtr2CharArray");
	const int iMaxSize = 3;
	const char *avengers[iMaxSize] = {"Iron man", "Hulk", "Thor"};
	for (int ii=0; ii<iMaxSize; ii++)
		printf("ii=%d  name=%s\n", ii, *(avengers+ii) );
}

void TestPtr2Ptr(void)
{
	ShowFuncName("TestPtr2Ptr");
	int var = 42;
	int *ptr;
	int **pptr;
	ptr = &var;
	pptr = &ptr;
	printf("var=%d ptr=%d  pptr=%d\n", var, *ptr, **pptr);
}

#define GETPTR_MAX	3
int *TestGetPtrProc(void)
{
	ShowFuncName("GetPtrTest");
	static int ar2[GETPTR_MAX] = {7, 12, 42};
	return ar2;
}
void TestGetptrMain(void)
{
	ShowFuncName("TestGetptrMain");
	int *ptr = TestGetPtrProc();
	for (int ii=0; ii<GETPTR_MAX; ii++)
		printf ("ii=%d  val=%d\n", ii, *(ptr+ii));
}
void Testtime(void)
{
	ShowFuncName("Testtime");
	time_t now = time(0);

	// convert now to string form
	char *dt = ctime(&now);
	printf("the local date/time is: %s\n", dt);

	// convert now to tm struct for UTC
	tm *gmtm = gmtime(&now);
	dt = asctime(gmtm);
	printf("The UTC date/time is: %s\n", dt);
}


int main (void)
{

	TestPointer();
	TestPtr2CharArray();
	TestPtr2Ptr();
	TestGetptrMain();



