
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

}

public class SelectionSort
{

	public static void main (String[] args)
	{
		//System.out.println("Hello world!");

		FreshJuice juice = new FreshJuice();
		juice.size = FreshJuice.FreshJuiceSize.MEDIUM;
		System.out.println("size: " + juice.size);

		TestMe tm = new TestMe();

		tm.SelectionSort();

	}
}