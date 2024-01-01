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
        // OOP
        // ----------------------------------------
        public class Fruit
        {
            private string color = "";
            public Fruit()
            {
                color = "no color";
            }
            public Fruit(string newcolor)
            {
                color = newcolor;
            }
            public void setcolor(string newcolor)
            {
                color = newcolor;
            }
            public string getcolor()
            {
                return color;
            }
        }

        public class Guava : Fruit
        {
            //private string type = "";
            public Guava()
            {
                setcolor("green");
            }
        }

        // ----------------------------------------
        // searching
        // ----------------------------------------

        // ----------------------------------------
        // stack
        // ----------------------------------------
       
        // ----------------------------------------
        // collections
        // ----------------------------------------
        


        // ----------------------------------------
        // Main
        // ----------------------------------------
        static void Main(String[] args)
        {

            string[] mycars = { "toyota", "honda", "ford" };
            foreach (string ii2 in mycars)
                Console.WriteLine(ii2);
            string[] mycars2;
            mycars2 = new string[] { "one", "two", "thre" };
            foreach (string ii3 in mycars2)
                Console.WriteLine(ii3);

            mycar obj2 = new mycar();
            obj2.setcolor("pink");
            Console.WriteLine(obj2.getcolor());

            string name1 = "james";
            string name2 = "bond";
            string name3 = $"my full name is: {name1} {name2}";
            Console.WriteLine(name3);

            Car myobj = new Car();
            myobj.setcolor("red");
            Console.WriteLine(myobj.color);

            string name1 = "john";
            string name2 = "doe";
            string name3 = $"my full name is: {name1} {name2}";
            Console.WriteLine(name3);
            
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



