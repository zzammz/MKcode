
import java.io.FileInputStream;
import java.io.FileOutputStream;

import java.util.*;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

import java.util.ArrayList;
import java.util.List;

class FreshJuice
{
	enum FreshJuiceSize {SMALL, MEDIUM, LARGE}
	FreshJuiceSize size;
}

class TestMe
{

	private void ShowArray (int[] thearray)
	{
		for (int ii : thearray)
			System.out.print(ii + " ");
		System.out.println("");
	}

	public void BubblesortTest()
	{
		int[] intArray = { 2, 4, 6, 8, 10, 1, 3, 5, 7, 9, -1 };
		int iTmp=0;
		System.out.println("\nbubble sort");
		ShowArray(intArray);
		for (int ii=0; ii<intArray.length-1; ii++)
		{
			for (int jj=0; jj<intArray.length-1-ii; jj++)
			{
				if (intArray[jj] > intArray[jj+1])
				{
					iTmp = intArray[jj];
					intArray[jj] = intArray[jj+1];
					intArray[jj+1] = iTmp;
				}
			}
		}
		ShowArray(intArray);
	}
	public void SelectionSort()
	{
		int[] intArray = { 2, 4, 6, 8, 10, 1, 3, 5, 7, 9, -1 };
		int iTmp=0;
		int iIndex=0;
		System.out.println("\nselection sort");
		ShowArray(intArray);

		for (int ii=0; ii<intArray.length; ii++)
		{
			iIndex = ii;
			for (int jj=ii; jj<intArray.length; jj++)
			{
				if (intArray[jj]<intArray[iIndex])
					iIndex = jj;
			}
			iTmp = intArray[ii];
			intArray[ii] = intArray[iIndex];
			intArray[iIndex] = iTmp;
		}
		ShowArray(intArray);
	}
	public void InsertionsortTest()
	{
		int[] intArray = { 2, 4, 6, 8, 10, 1, 3, 5, 7, 9, -1 };
		int iTmp=0;
		int my_pos=0;
		int my_cursor=0;
		System.out.println("\ninsertion sort");
		ShowArray(intArray);

		for (int ii=0; ii<intArray.length; ii++)
		{
			my_cursor = intArray[ii];
			my_pos = ii;
			while (my_pos>0 && intArray[my_pos-1]>my_cursor)
			{
				intArray[my_pos] = intArray[my_pos-1];
				my_pos--;
			}
			intArray[my_pos] = my_cursor;
		}
		ShowArray(intArray);
	}


}

public class SortingAll
{

	public static void main (String[] args)
	{
		//System.out.println("Hello world!");

		FreshJuice juice = new FreshJuice();
		juice.size = FreshJuice.FreshJuiceSize.MEDIUM;
		System.out.println("size: " + juice.size);

		TestMe tm = new TestMe();

		//tm.BubblesortTest();
		//tm.SelectionSort();
		//tm.InsertionsortTest();

	}
}