
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

	public void CollectionsTest()
	{
		Vector v = new Vector(0,1);
		System.out.println ("size= "+v.size() + " capacity= " + v.capacity());

		v.addElement(2);
		v.addElement(4.22);
		//v.addElement( new Double(2.1));
		System.out.println ("size= "+v.size() + " capacity= " + v.capacity());

		Enumeration vEnum = v.elements();
		while(vEnum.hasMoreElements())
			System.out.print(vEnum.nextElement() + " ");
		System.out.println();
	}
	public void StackTest()
	{
		Stack st = new Stack();
		st.push(3);
		st.push(6);
		st.push(3.4);
		st.push(9);
		int aa = (int) st.pop();
		System.out.println("pop= "+aa);
	}
	public void DictTest()
	{
		Dictionary<Integer, Integer> dictionary = new Hashtable<>();
		dictionary.put(1, 11);
		dictionary.put(2, 22);
		Enumeration<Integer> enumeration = dictionary.keys();
		while(enumeration.hasMoreElements())
			System.out.println(enumeration.nextElement());
	}
	public void ListTest()
	{
		List<String> a1 = new ArrayList<>();
		a1.add("Daniel");
		a1.add("Cory");		
		a1.add("Rami");
		System.out.println("members: " + a1);
	}
	public void QueueTest()
	{
		Queue<Integer> q = new LinkedList<>();
		q.add(7);
		q.add(3);
		q.add(9);
		q.add(2);
		System.out.println("queue: " + q);
		int num1 = q.remove();
		System.out.println("removed: " + num1);
		System.out.println("queue: " + q);
	}
	public void MapTest()
	{
		Map<String, String> m1 = new HashMap<>();
		m1.put("Daniel", "21");
		m1.put("Cory", "30");
		m1.put("Rami", "25");
		System.out.println("map " + m1);
	}


	private void ShowArray (int[] thearray)
	{
		for (int ii : thearray)
			System.out.print(ii + " ");
		System.out.println("");
	}



}

public class DataStruct
{

	public static void main (String[] args)
	{
		//System.out.println("Hello world!");

		FreshJuice juice = new FreshJuice();
		juice.size = FreshJuice.FreshJuiceSize.MEDIUM;
		System.out.println("size: " + juice.size);

		TestMe tm = new TestMe();

		tm.CollectionsTest();
		tm.StackTest();
		tm.DictTest();
		tm.ListTest();
		tm.QueueTest();
		tm.MapTest();

	}
}