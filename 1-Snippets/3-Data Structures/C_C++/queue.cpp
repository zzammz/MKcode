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


// ------------------ queue
class MKQueue
{
	private:
		struct MQStruct
		{
			int q_data;
			MQStruct *qp_next, *qp_prev;
		};
		MQStruct *qp_head, *qp_tail, *qp_tmp, *qp_current;
		int q_count;
	public:
		MKQueue(void);
		~MKQueue(void);
		bool Push(int newval);
		int Pop(void);
		int GetCount(void);
		void ShowAll(void);
		void AddQueueBulk(int icount);
		void EmptyQueue(void);
};

MKQueue::MKQueue(void)
{
	qp_head = qp_tail = qp_tmp = qp_current = NULL;
	q_count = 0;
}
MKQueue::~MKQueue(void)
{

}
int MKQueue::GetCount(void)
{
	return q_count;
}
bool MKQueue::Push(int newval)
{
	bool returnval = false;
	qp_tmp = new MQStruct();

	if (qp_tmp)
	{
		qp_tmp->q_data = newval;
		qp_tmp->qp_prev = qp_tmp->qp_next = NULL;
		qp_tail = qp_tmp;
		if(q_count==0)
		{
			qp_head = qp_tmp;
			qp_current = qp_tmp;
		}
		else
		{
			qp_current->qp_next = qp_tmp;
			qp_tmp->qp_prev = qp_current;
			qp_current = qp_tmp;
		}
		q_count++;
		returnval = true;
	}

	return returnval;
}
void MKQueue::ShowAll(void)
{
	ShowFuncName("ShowAll");
	printf("Showing %d members\n", GetCount());
	qp_tmp = qp_head;
	while (qp_tmp)
	{
		printf("  q data: %d\n", qp_tmp->q_data);
		qp_tmp = qp_tmp->qp_next;
	}
}

void MKQueue::AddQueueBulk(int icount)
{
	ShowFuncName("AddQueueBulk");
	for (int ictr=0; ictr<icount; ictr++)
	{
		printf("Adding %d\n", ictr);
		if(Push(ictr+200))
		{
			printf("  Successfuly added %d\n", ictr);
		}
		else
		{
			printf("  ERR: failed to add %d\n", ictr);
			break;
		}
	}
}
int MKQueue::Pop(void)
{
	int returnval = -1;
	if (qp_current)
	{
		returnval = qp_current->q_data;
		qp_tmp = qp_current->qp_prev;
		delete qp_current;
		qp_current = qp_tmp;
		qp_current->qp_next = NULL;
		q_count--;
	}
	return returnval;
}

void MKQueue::EmptyQueue(void)
{
	ShowFuncName("EmptyQueue");
	qp_current = qp_head;
	while(qp_current)
	{
		qp_tmp = qp_current;
		qp_current = qp_current->qp_next;
		printf("deleting %d\n", qp_tmp->q_data);
		delete qp_tmp;
	}
	q_count = 0;
	qp_head = NULL;
}
void Test_Queue(void)
{
	ShowFuncName("Test_Queue");
	MKQueue *mkq = new MKQueue();
	mkq->AddQueueBulk(5);
	printf("queue count: %d\n", mkq->GetCount());
	mkq->ShowAll();
	printf("\npop=%d\n", mkq->Pop());
	mkq->ShowAll();
	mkq->EmptyQueue();
	mkq->ShowAll();
	printf("\n\n");
}



int main (void)
{

	Test_Queue();

}


