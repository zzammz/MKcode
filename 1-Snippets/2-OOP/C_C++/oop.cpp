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

// ----------- classes

class Shape
{
public:
	int sides;
	int plane;
	int length;
	Shape(void);
	Shape(int p_sides, int p_plane, int p_length);
	~Shape(void);
	virtual void CalcArea (void) {};
};

Shape::Shape(void)
{
	sides = plane = length = 0;
}

Shape::Shape(int p_sides, int p_plane, int p_length)
{
	this->sides = p_sides;
	this->plane = p_plane;
	this->length = p_length;
}

Shape::~Shape(void)
{
	cout << "Shape destructor called\n";
}

class Rect : public Shape
{
	public:
		Rect(void);
		Rect(int p_sides, int p_plane, int p_length);
		~Rect(void);
		void Show(void);
		void SetVals (int p_sides, int p_plane, int p_length);
		void CalcArea(void);
};

Rect::Rect(void)
{
	this->sides = 4;
	this->plane = 2;
}
Rect::Rect(int p_sides, int p_plane, int p_length)
{
	this->sides = p_sides;
	this->plane = p_plane;
	this->length = p_length;
}
Rect::~Rect(void)
{
	cout << "Rect destructor called\n";
}
void Rect::Show(void)
{
	printf("sides=%d   plane=%d   length=%d\n", this->sides, this->plane, this->length);
}
void Rect::SetVals(int p_sides, int p_plane, int p_length)
{
	this->sides = p_sides;
	this->plane = p_plane;
	this->length = p_length;
}
void Rect::CalcArea(void)
{
	int area = this->length * 2;
	printf ("area=%d\n", area);
}
void Test_RectClass(void)
{
	Rect rect;
	rect.SetVals(5, 3, 2);
	rect.CalcArea();
	rect.Show();
}


int main (void)
{

	Test_RectClass();

}


