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



// STL
void Test_sorting(void)
{
	int arr[] = {3, 5, 1, 8, 2};
	std::sort(std::begin(arr), std::end(arr));
	//for (int ii : arr)
	for (int ii=0; ii<5; ii++)
		std::cout << arr[ii] << " ";
	cout << "\n";
}

int main (void)
{

	Test_sorting();
}


