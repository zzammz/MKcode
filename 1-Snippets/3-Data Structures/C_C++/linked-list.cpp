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


// --------- linked list
void Test_DynamicAlloc(void)
{
	char *cVal = NULL;
	cVal = new char;
	*cVal = 'W';
	cout << "cVal= " << *cVal << "\n";
	delete cVal;

	char *sVal = NULL;
	sVal = new char[10];
	sVal[0] = 'G';
	sVal[1] = 'o';
	sVal[2] = '\0';
	cout << "sVal= " << sVal << "\n";
	delete sVal;
}

void Test_LinkedList(void)
{
	struct EMPLOYEES
	{
		int code;
		EMPLOYEES *listPrev, *listNext;
	};

	EMPLOYEES *ptrHead = NULL;
	EMPLOYEES *ptrTail = NULL;
	EMPLOYEES *ptrTmp = NULL;
	EMPLOYEES *ptrPrev = NULL;
	int empcount = 5;
	int ictr = 0;

	// generate linked list
	for (ictr=0; ictr<empcount; ictr++)
	{
		ptrTmp = new EMPLOYEES;

		if (!ptrTmp)
		{
			empcount = ictr - 1;
			break;
		}
		ptrTail = ptrTmp;
		ptrTmp->listPrev = ptrTmp->listNext = NULL;
		ptrTmp->code = 100 + ictr;
		if (ictr==0)
			ptrHead = ptrTmp;
		else
		{
			ptrTmp->listPrev = ptrPrev;
			ptrPrev->listNext = ptrTmp;
		}
		ptrPrev = ptrTmp;
	}

	// show contents from start via count
	printf ("show contents from start via count\n");
	ptrTmp = ptrHead;
	for (ictr=0; ictr<empcount; ictr++)
	{
		printf ("%d: code=%d\n", ictr, ptrTmp->code);
		ptrTmp = ptrTmp->listNext;
	}

	// show contents from start via ptr
	printf ("show contents from start via ptr\n");
	ptrTmp = ptrHead;
	ictr=0;
	while (ptrTmp)
	{
		printf ("%d: code=%d\n", ictr, ptrTmp->code);
		ptrTmp = ptrTmp->listNext;
		ictr++;
	}

	printf ("show contents from end via ptr\n");
	ptrTmp = ptrTail;
	ictr = empcount-1;
	while(ptrTmp)
	{
		printf ("%d: code=%d\n", ictr, ptrTmp->code);
		ptrTmp = ptrTmp->listPrev;
		ictr--;
	}
}

class LinkedList
{
	private:
		struct EMPLOYEES
		{
			int code;
			EMPLOYEES *listPrev, *listNext;
		};
		EMPLOYEES *ptrHead, *ptrTail, *ptrTmp, *ptrPrev, *ptrNext;
	public:
		LinkedList(void);
		~LinkedList(void);
		int employee_count;
		int employee_max_count;
		bool AddEmployee(int newCode);
		void AddEmployeeBulk(int icount);
		void ShowEmployeeCount(void);
		void ShowContentStartCount(void);
		void ShowContentStartPtr(void);
		void ShowContentEndPtr(void);

};
LinkedList::LinkedList(void)
{
	ptrHead = NULL; 
	ptrTail = NULL;
	ptrTmp = NULL;
	ptrPrev = NULL;
	ptrNext = NULL;
	employee_count = 0;
	employee_max_count = 5;
}
LinkedList::~LinkedList(void)
{

}
bool LinkedList::AddEmployee(int newCode)
{
	//ShowFuncName("  AddEmployee");
	if (employee_count == employee_max_count) // already reached the max
	{
		printf ("ERR: too many employees\n");
		return false;
	}
	ptrTmp = new EMPLOYEES;
	ptrTmp->listPrev = ptrTmp->listNext = NULL;
	ptrTmp->code = newCode;
	if(!ptrTmp)
	{
		printf ("ERR: failed to instantiate EMPLOYEE\n");
		return false;
	}
	ptrTail = ptrTmp;
	if(employee_count == 0)
	{
		ptrHead = ptrTmp;
	}
	else
	{
		ptrTmp->listPrev = ptrPrev;
		ptrPrev->listNext = ptrTmp;
	}
	ptrPrev = ptrTmp;

	return true;
}
void LinkedList::AddEmployeeBulk(int icount)
{
	ShowFuncName("::AddEmployeeBulk");
	employee_count = 0;
	printf("icount=%d  employee_max_count=%d\n", icount, employee_max_count);
	for (int ictr=0; ictr<icount; ictr++)
	{
		printf("Adding employee %d\n", ictr);
		if(!AddEmployee(ictr+100))
			break;
		else
			employee_count++;
		printf("   ... employee added successfully\n");
	}	
}
void LinkedList::ShowEmployeeCount(void)
{
	printf("\nemployee count=%d\n\n", employee_count);
}
void LinkedList::ShowContentStartCount(void)
{
	ShowFuncName("::ShowContentStartCount");
	ptrTmp = ptrHead;
	for (int ictr=0; ictr<employee_count; ictr++)
	{
		printf("%d: code=%d\n", ictr, ptrTmp->code);
		ptrTmp = ptrTmp->listNext;
	}
}
void LinkedList::ShowContentStartPtr(void)
{
	ShowFuncName("::ShowContentStartPtr");
	ptrTmp = ptrHead;
	int ictr=0;
	while (ptrTmp)
	{
		printf("%d: code=%d\n", ictr, ptrTmp->code);
		ptrTmp = ptrTmp->listNext;
		ictr++;
	}
}
void LinkedList::ShowContentEndPtr(void)
{
	ShowFuncName("::ShowContentEndPtr");
	ptrTmp = ptrTail;
	int ictr=employee_count;
	while (ptrTmp)
	{
		printf("%d: code=%d\n", ictr, ptrTmp->code);
		ptrTmp = ptrTmp->listPrev;
		ictr--;
	}
}

void Test_LinkedListClass(void)
{
	LinkedList *llPtr = new LinkedList();
	llPtr->ShowEmployeeCount();
	llPtr->AddEmployeeBulk(5);
	llPtr->ShowEmployeeCount();
	llPtr->ShowContentStartCount();
	llPtr->ShowContentStartPtr();
	llPtr->ShowContentEndPtr();
}

int main (void)
{

	Test_LinkedList();
	Test_LinkedListClass();

}


