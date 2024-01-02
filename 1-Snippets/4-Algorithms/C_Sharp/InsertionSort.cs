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
        // sorting
        // ----------------------------------------
        public class MKSorting
        {
            public MKSorting()
            {

            }
            public void showArray(int[] iList)
            {
                foreach (int ii in iList)
                {
                    Console.Write(ii);
                    Console.Write(" ");
                }
                Console.WriteLine();

            }


            public void InsertionSort(int[] iList)
            {
                Console.WriteLine("\ninsertion sort");
                showArray(iList);
                for (int ii = 0; ii < iList.Length; ii++)
                {
                    int my_cursor = iList[ii];
                    int my_pos = ii;

                    while (my_pos > 0 && iList[my_pos - 1] > my_cursor)
                    {
                        iList[my_pos] = iList[my_pos - 1];
                        my_pos--;
                    }
                    iList[my_pos] = my_cursor;
                }
                showArray(iList);
            }

        }



        // ----------------------------------------
        // Main
        // ----------------------------------------
        static void Main(String[] args)
        {


            // sorting
 
            MKSorting mks = new MKSorting();

            int[] ilist3 = { 2, 4, 6, 8, 10, 1, 3, 5, 7, 9, -1 };
            mks.InsertionSort(ilist3);


        }
    }



