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
        // collections
        // ----------------------------------------
        public class MKcollections
        {
            public void MKarraylist()
            {
                ArrayList al = new ArrayList();
                al.Add(7);
                al.Add(1);
                al.Add(3);
                al.Add(42);
                al.Add(8);
                al.Add(9);
                al.Add(2);
                al.Add(-1);
                Console.WriteLine("\noriginal");
                foreach (int ii in al)
                    Console.WriteLine(ii);
                al.Sort();
                Console.WriteLine("\nsorted");
                foreach (int ii in al)
                    Console.WriteLine(ii);
            }

            public void MKhashtable()
            {
                Hashtable ht = new Hashtable();
                ht.Add("001", "michael");
                ht.Add("002", "pam");
                ht.Add("003", "dwight");
                ht.Add("004", "jim");
                ht.Add("005", "angela");
                ht.Add("006", "oscar");
                if (ht.ContainsValue("stanley"))
                    Console.WriteLine("This student name is already in the list");
                else
                    ht.Add("007", "stanley");


                ICollection key = ht.Keys;
                foreach (string k in key)
                    Console.WriteLine(k + ": " + ht[k]);

            }

            public void MKsortedlist()
            {
                SortedList ht = new SortedList();
                ht.Add("001", "michael");
                ht.Add("002", "pam");
                ht.Add("003", "dwight");
                ht.Add("004", "jim");
                ht.Add("005", "angela");
                ht.Add("006", "oscar");
                if (ht.ContainsValue("stanley"))
                    Console.WriteLine("This student name is already in the list");
                else
                    ht.Add("007", "stanley");


                ICollection key = ht.Keys;
                foreach (string k in key)
                    Console.WriteLine(k + ": " + ht[k]);

            }

            public void MKstack()
            {
                Stack st = new Stack();
                st.Push('A');
                st.Push('B');
                st.Push('C');
                st.Push('D');
                st.Push('E');

                Console.WriteLine("\nCurrent stack");
                foreach (char cc in st)
                    Console.WriteLine(cc + " ");
                st.Pop();

                Console.WriteLine("\nNew stack");
                foreach (char cc in st)
                    Console.WriteLine(cc + " ");

            }


            public void MKqueue()
            {
                Queue mkq = new Queue();
                mkq.Enqueue('A');
                mkq.Enqueue('B');
                mkq.Enqueue('C');
                mkq.Enqueue('D');

                Console.WriteLine("\nCurrent queue");
                foreach (char cc in mkq)
                    Console.WriteLine(cc + " ");

                mkq.Dequeue();

                Console.WriteLine("\nNew queue");
                foreach (char cc in mkq)
                    Console.WriteLine(cc + " ");

            }
        }



        // ----------------------------------------
        // Main
        // ----------------------------------------
        static void Main(String[] args)
        {


            // collections
            MKcollections mkc = new MKcollections();
            //mkc.MKarraylist();
            //mkc.MKhashtable();
            //mkc.MKsortedlist();
            //mkc.MKstack();
            mkc.MKqueue();


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



            // hashtable
            Hashtable mytable = new Hashtable();
            mystudent st1 = new mystudent(1, "Allan", 2);
            mystudent st2 = new mystudent(2, "Becky", 3);
            mystudent st3 = new mystudent(3, "Cindy", 4);

            mytable.Add(st1.s_id, st1);
            mytable.Add(st2.s_id, st2);
            mytable.Add(st3.s_id, st3);



            // dict
            string mytext = System.IO.File.ReadAllText(@"/Users/muzzammilkhan/Desktop/MKhome/Dev/Csharp/hw/mytextfile.txt");
            Console.WriteLine("text is {0}", mytext);
            Console.ReadKey();


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



