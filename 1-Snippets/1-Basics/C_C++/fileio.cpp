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

// ---- fileio
void Test_Fileio(void)
{
	FILE *fp;
	printf("--- opening file for writing\n");
	fp = fopen("test.txt", "w+");
	if(fp)
	{
		fprintf(fp, "This is a test line\n");
		fclose(fp);
	}
	else
		printf("error opening file for writing\n");

	printf("--- opening file for reading\n");
	fp = fopen ("test.txt", "r");
	if (fp)
	{
		char read_line[255];
		fgets(read_line, 255, fp);
		printf("%s\n", read_line);
		fclose(fp);
	}
	else
		printf("error opening file for reading\n");
}


int main (void)
{


	Test_Fileio();

}


