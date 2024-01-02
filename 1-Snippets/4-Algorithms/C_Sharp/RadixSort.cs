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


            public void RadixSort(int[] iList)
            {
                Console.WriteLine("\nradix sort");
                showArray(iList);

                int ictr, jctr;
                int[] tmplist = new int[iList.Length];

                for (int shift=31; shift>-1; shift--)
                {
                    jctr = 0;
                    for (ictr=0; ictr<iList.Length; ++ictr)
                    {
                        bool move = (iList[ictr] << shift) >= 0;
                        if (shift == 0 ? !move : move)
                            iList[ictr - jctr] = iList[ictr];
                        else
                            tmplist[jctr++] = iList[ictr];
                    }
                    Array.Copy(tmplist, 0, iList, iList.Length - jctr, jctr);
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

            int[] ilist5 = { 2, 4, 6, 8, 10, 1, 3, 5, 7, 9, -1 };
            mks.RadixSort(ilist5);

        }
    }



