
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
	public void LoopsTest()
	{
		for (int ii=0; ii<10; ii++)
			System.out.println("ii= " + ii);

		int[] intA = {10, 20, 30, 40};
		for (int xx : intA)
			System.out.println("xx= " + xx);

		String[] stringA = {"Allen", "Becky", "Cindy"};
		for (String yy : stringA)
			System.out.println("yy= " + yy);

		int intB = 10;
		String stringC = (intB==10 ? "Yes" : "No");
		System.out.println("Is intB 10? " + stringC);
	}
	public void TryTest()
	{
		int[] intA = {10, 20, 30};
		try
		{
			System.out.println("intA[5]= " + intA[5]);
		}
		catch (ArrayIndexOutOfBoundsException e)
		{
			System.out.println("error: array out of bounds");
		}
		catch (Exception e1)
		{
			System.out.println("error: something else went wrong");
		}
		finally
		{
			System.out.println("finally here");
		}		
	}

}

public class OOPtest
{

	public static void main (String[] args)
	{
		FreshJuice juice = new FreshJuice();
		juice.size = FreshJuice.FreshJuiceSize.MEDIUM;
		System.out.println("size: " + juice.size);

		TestMe tm = new TestMe();
		tm.LoopsTest();
		tm.TryTest();

	}
}