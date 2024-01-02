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

            public void BubbleSort(int[] iList)
            {
                Console.WriteLine("\nbubble sort");
                showArray(iList);
                for (int ii=0; ii<iList.Length-1; ii++)
                {
                    for (int jj=0; jj<iList.Length-1-ii; jj++)
                    {
                        if (iList[jj] > iList[jj+1])
                        {
                            (iList[jj], iList[jj + 1]) = (iList[jj + 1], iList[jj]);
                        }
                    }
                }
                showArray(iList);
            }

            public void BubbleSort2(int[] iList)
            {
                Console.WriteLine("\nbubble sort2");
                showArray(iList);
                int lenlist = iList.Length;
                bool isswapped = true;
                int xx = -1;
                while (isswapped)
                {
                    isswapped = false;
                    xx++;
                    for(int ictr=1; ictr<lenlist-xx; ictr++)
                    {
                        if (iList[ictr-1] > iList[ictr])
                        {
                            (iList[ictr - 1], iList[ictr]) = (iList[ictr], iList[ictr - 1]);
                            isswapped = true;

                        }
                    }
                }
                showArray(iList);
            }



        // ----------------------------------------
        // Main
        // ----------------------------------------
        static void Main(String[] args)
        {


            // sorting

            MKSorting mks = new MKSorting();
            int[] ilist = { 2, 4, 6, 8, 10, 1, 3, 5, 7, 9, -1 };
            mks.BubbleSort(ilist);

            int[] ilist2 = { 2, 4, 6, 8, 10, 1, 3, 5, 7, 9, -1 };
            mks.BubbleSort2(ilist2);




        }
    }



