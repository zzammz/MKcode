
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

	public void LinearsearchTest()
	{
		int[] intArray = { 2, 4, 6, 8, 10, 1, 3, 5, 7, 9, -1 };
		int iSearch = 19;

		for (int ii : intArray)
		{
			if (ii == iSearch)
			{
				System.out.println ("found");
				return;
			}
		}
		System.out.println ("not found");
	}

	private void ShowArray (int[] thearray)
	{
		for (int ii : thearray)
			System.out.print(ii + " ");
		System.out.println("");
	}
	public boolean BinarysearchlinearTest()
	{
		int[] iilist = { 2, 4, 6, 8, 10, 1, 3, 5, 7, 9, -1 };
        int iisearch = 4;

        System.out.println("\nlinear binary search");
		ShowArray(iilist);
		Arrays.sort(iilist);
		ShowArray(iilist);
		System.out.println("search for: " + iisearch);

		if (iilist.length == 0)
			return false;

		int min = 0;
		int max = iilist.length - 1;
		while (min <= max)
		{
			int mid = (min+max)/2;
			if (iilist[mid] == iisearch)
				return true;
			else if (iisearch < iilist[mid])
				max = mid - 1;
			else 
				min = mid + 1;
		}
		return false;
	}
	private int BinarysearchrecursiveProc(int iSearch, int[] iList, int min, int max)
	{
		int mid = (min + max)/2;
		if (iList[mid] == iSearch)
			return mid;
		else if (iSearch < iList[mid])
			max = mid - 1;
		else
			min = mid + 1;
		if (max < min)
			return -1;

		return BinarysearchrecursiveProc(iSearch, iList, min, max);
	}
	public boolean BinarysearchrecursiveTest()
	{
		int[] iilist = { 2, 4, 6, 8, 10, 1, 3, 5, 7, 9, -1 };
        int iisearch = 4;
        boolean returnresult = false;
        System.out.println("\nrecursive binary search");
		ShowArray(iilist);
		Arrays.sort(iilist);
		ShowArray(iilist);
		System.out.println("search for: " + iisearch);

		if (iilist.length == 0)
			return returnresult;

		returnresult = BinarysearchrecursiveProc(iisearch, iilist, 0, iilist.length-1) == -1 ? false: true;

		return returnresult;
	}



}

public class AllSearching
{

	public static void main (String[] args)
	{
		//System.out.println("Hello world!");

		FreshJuice juice = new FreshJuice();
		juice.size = FreshJuice.FreshJuiceSize.MEDIUM;
		System.out.println("size: " + juice.size);

		TestMe tm = new TestMe();

		tm.LinearsearchTest();
		boolean abc = tm.BinarysearchlinearTest();
		System.out.println("binary linear search: " + abc);
		boolean abc2 = tm.BinarysearchrecursiveTest();
		System.out.println("binary recursive search: " + abc2);
	

	}
}