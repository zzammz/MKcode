// See https://aka.ms/new-console-template for more information

// .Net 5 style
using System;
using Microsoft.VisualBasic;

using System.Collections;
using System.Collections.Generic;

using System.Text.RegularExpressions;
using static System.Net.Mime.MediaTypeNames;

namespace hw
{
    /*
    struct MyStruct
    {
        public string aname;
        public int anum=0;
    }*/

    public class Car
    {
        public string color="";

        public void setcolor(string newcolor)
        {
            color = newcolor;
        }
    }

    public class mycar
    {
        string colorval = "";
        public void setcolor (string newcolor)
        {
            colorval = newcolor;
        }
        public string getcolor()
        {
            return colorval;
        }
    }


    internal class Program
    {

        static void PrintSomething(string astring)
        {
            Console.WriteLine("printing str: " + astring);
        }

        static void PrintSomething(int intval)
        {
            Console.WriteLine("printing val: " + intval);
        }

        static void printall(params string[] sentence)
        {
            for (int ii = 0; ii < sentence.Length; ii++)
                Console.WriteLine(sentence[ii] + " ");
        }

        static int mymin(params int[] myval)
        {
            int resultmin = int.MaxValue;
            for (int ii = 0; ii < myval.Length; ii++)
                if (myval[ii] < resultmin)
                    resultmin = myval[ii];

            return resultmin;

        }


        // ----------------------------------------
        // Main
        // ----------------------------------------
        static void Main(String[] args)
        {

            // string format writing

            int anumber = 42;
            Console.WriteLine("number is {0}", anumber);

            int[] jojo = new int[] { 4, 6, 8, 10, 2, 5, 7, 9, 1, 3 };
            foreach (int ii in jojo)
                Console.WriteLine("ii is {0}", ii);


            Console.WriteLine(".Net 5: Hello, World!");

            Console.WriteLine(".Net 5: howdy");


            int iNum = 10;
            float fNum = 12.34f;
            string strMsg = "Hello World";
            Console.WriteLine("iNum=" + iNum + "    fNum=" + fNum);
            Console.WriteLine(strMsg.ToUpper());

            const int ciNum = 15;
            Console.WriteLine(ciNum);

            int ii = 42;
            float ff = 1.2f;
            string ss = "yo man";
            Console.WriteLine("  int= " + ii + "  float= " + ff + "  string= " + ss);
            string ss2 = "yes here";
            Console.WriteLine(ss2.ToUpper());
            //Console.WriteLine("yes");



            string strOne = " Hello darkness my old friend   ";
            string strTwo = strOne.Substring(3);
            Console.WriteLine("[" + strOne + "]");
            Console.WriteLine("[" + strTwo + "]");
            Console.WriteLine("[" + strTwo.Trim() + "]");
            int indexstr = strOne.IndexOf('e', 0);
            Console.WriteLine(indexstr);
            int ii = strOne.IndexOf('o', 0);
            string iis = Convert.ToString(ii);
            Console.WriteLine("loc is= " + ii);
            string mymsg = String.Format(" the result it {0} really!", iis);
            Console.WriteLine(mymsg);

            int intOne = 24;
            Console.WriteLine(Convert.ToString(intOne));


            var strname = "Mike";
            var strthree = String.Format("my name is {0}", strname);
            Console.WriteLine(strthree);

            int whichmin = Math.Min(5, 10);
            Console.WriteLine(whichmin);
            Console.WriteLine(strname.Length);

            string fname = "Mike";
            string lname = "Craig";
            string fullname = $"my full name is: {fname}  {lname}";
            Console.WriteLine(fullname);


            string fullname = "John Doe";
            int charpos = fullname.IndexOf(" ");
            string lastname = fullname.Substring(charpos+1);
            Console.WriteLine(lastname);



            Console.WriteLine(5 > 10);

            int inum = 5;
            string strresult = (inum > 5) ? "greater" : "smaller";
            Console.WriteLine(strresult);

            string onename = "James Bond";
            int ipos = onename.IndexOf(" ");
            Console.WriteLine(ipos);
            string onename2 = onename.Substring(ipos + 1);
            Console.WriteLine(onename2);

            int ii = 5;
            string iicheck = (ii > 5) ? "No" : "Yes";
            Console.WriteLine(iicheck);


            //string[] cars = { "volvo", "ford", "mazda" };  // static
            string[] cars;   // dynamic def
            cars = new string[] { "gm", "kia", "bmw" }; // dynamic def
            foreach (string ii in cars)
            {
                Console.WriteLine(ii);
            }

            string[] mycars = { "toyota", "honda", "ford" };
            foreach (string ii2 in mycars)
                Console.WriteLine(ii2);
            string[] mycars2;
            mycars2 = new string[] { "one", "two", "thre" };
            foreach (string ii3 in mycars2)
                Console.WriteLine(ii3);


            //string ival;
            int ictr = 0;
            foreach (string ival in cars)
            {
                Console.WriteLine(Convert.ToString(ictr) + " --- " +  ival);
                PrintSomething(ictr);
                PrintSomething(ival);
                ictr++;
            }

            Console.Read();
 

            try
            {
                int[] mynums = { 1, 2, 3 };
                Console.WriteLine(mynums[10]);
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
            finally
            {
                Console.WriteLine("finally");
            }


            string astring = "12a";
            try
            {
                int anum = int.Parse(astring);
                Console.WriteLine(anum);
            }
            catch (Exception)
            {
                Console.WriteLine("some error");
            }
            finally
            {
                Console.WriteLine("good to be here");
            }


            try
            {
                int[] myint = { 1, 2, 3 };
                Console.WriteLine(myint[10]);
            }
            catch (Exception e)
            {
                Console.WriteLine("something happened");
            }
            finally
            {
                Console.WriteLine("finally here");
            }

            string string2 = "12a";
            try
            {
                int ii5 = int.Parse(string2);
            }
            catch (Exception e)
            {
                Console.WriteLine("some other error");
            }
            finally
            {
                Console.WriteLine("at other finally");
            }


            // arrays
            string[] cars2 = { "ford", "gm", "toyota", "honda" };
            Console.WriteLine(cars2.Length);
            string[] cars3;
            cars3 = new string[] { "a", "b" };
            Console.WriteLine(cars3.Length);
            for (int ii = 0; ii < cars2.Length; ii++)
                Console.WriteLine(cars2[ii]);
            Array.Sort(cars2);
            for (int ii = 0; ii < cars2.Length; ii++)
                Console.WriteLine(cars2[ii]);

            string astring = "12a";
            int newval;
            bool issuccess = int.TryParse(astring, out newval);
            Console.WriteLine(issuccess);
            if (issuccess)
                Console.WriteLine("success");
            else
                Console.WriteLine("not good");


            //enum Level { Low, Medium, High };
            //Level myl = Level.Medium;
            //Console.WriteLine(myl);



            string[] cars = { "volvo", "ford", "toyota", "honda" };
            foreach (string ii in cars)
            {
                Console.WriteLine(ii);
            }

            Console.WriteLine();

            Array.Sort(cars);

            foreach (string ii in cars)
            {
                Console.WriteLine(ii);
            }

            Console.WriteLine("length of array is {0}", cars.Length);

            printall("hello darkness my old friend");


            int[] somenums = { 1, 2, 3, -6, 12, 15 };
            Console.WriteLine(mymin(somenums));

            int[] ii6 = { -4, 5, 9, 10, -5 };
            Console.WriteLine(mymin(ii6));



            ArrayList myAL = new ArrayList(5);
            myAL.Add(5);
            myAL.Add("Hello");
            myAL.Add(3.14);
            myAL.Add(100);
            myAL.Add("bye");
            for (int ii = 0; ii < myAL.Count; ii++)
                Console.WriteLine(myAL[ii]);
            Console.WriteLine();

            myAL.Remove(100);
            for (int ii = 0; ii < myAL.Count; ii++)
                Console.WriteLine(myAL[ii]);
            Console.WriteLine();

            foreach (object oo in myAL)
                Console.WriteLine(oo);
 
            ArrayList myal = new ArrayList(5);
            myal.Add(5);
            myal.Add("green");
            myal.Add(1.2);
            myal.Add("blue");
            myal.Add(77);
            for (int ii = 0; ii < myal.Count; ii++)
                Console.WriteLine(myal[ii]);
            myal.Remove(1.2);
            for (int ii = 0; ii < myal.Count; ii++)
                Console.WriteLine(myal[ii]);

            MyStruct ms2;
            ms2.aname = "howdy";
            ms2.anum = 45;
            Console.WriteLine(ms2.aname);
            Console.WriteLine(ms2.anum);

            DateTime dt2 = new DateTime(2023, 5, 31);
            Console.WriteLine(dt2.DayOfWeek);



        }
    }

    class mystudent
    {
        public int s_id { get; set;  }
        public string s_name { get; set; }
        public float s_gpa { get; set; }
        public mystudent(int id, string name, float gpa)
        {
            this.s_id = id;
            this.s_name = name;
            this.s_gpa = gpa;
        }
    }

}



