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


            public int XQuickSortProcRec(int[] iList, int lowindex, int highindex)
            {
                //Console.WriteLine("\nquick sort proc rec");
                int index_smaller_element = (lowindex - 1);
                int pivot = iList[highindex];

                for (int jctr = lowindex; jctr < highindex; jctr++)
                {
                    if (iList[jctr] <= pivot)
                    {
                        index_smaller_element++; //increment
                        (iList[index_smaller_element], iList[jctr]) = (iList[jctr], iList[index_smaller_element]);
                    }

                }
                (iList[index_smaller_element + 1], iList[highindex]) = (iList[highindex], iList[index_smaller_element + 1]);
                return (index_smaller_element + 1);
            }


            public int[] XQuickSortProc(int[] iList, int lowindex, int highindex)
            {
                Console.WriteLine("\nquick sort proc");

                int partitionindex = XQuickSortProcRec(iList, lowindex, highindex);
                XQuickSortProc(iList, lowindex, partitionindex - 1);
                XQuickSortProc(iList, partitionindex + 1, highindex);
                return iList;
            }

            public void XQuickSort(int[] iList)
            {
                Console.WriteLine("\nquick sort");
                showArray(iList);
                if (iList.Length == 0)
                    return;
                int startindex = 0;
                int endindex = iList.Length-1;

                XQuickSortProc(iList, startindex, endindex);
                showArray(iList);
            }

            private int QSPartition(int[] iList, int leftindex, int rightindex)
            {
                int pivotindex = iList[leftindex];

                while (true)
                {

                    while (iList[leftindex] < pivotindex)
                        leftindex++;
                    while (iList[rightindex] > pivotindex)
                        rightindex--;

                    if (leftindex < rightindex)
                    {
                        if (iList[leftindex] == iList[rightindex])
                            return rightindex;
                        (iList[leftindex], iList[rightindex]) = (iList[rightindex], iList[leftindex]);
                    }
                    else
                        return rightindex;
                }

            }

            private void QuickSortProc(int[] iList, int leftindex, int rightindex)
            {
                //Console.WriteLine("\nquick sort proc");

                if (leftindex < rightindex)
                {
                    int partitionindex = QSPartition(iList, leftindex, rightindex);

                    if (partitionindex > 1)
                        QuickSortProc(iList, leftindex, partitionindex - 1);

                    if (partitionindex + 1 < rightindex)
                        QuickSortProc(iList, partitionindex + 1, rightindex);
                }
            }


            public void QuickSort(int[] iList)
            {
                Console.WriteLine("\nquick sort");
                showArray(iList);
                if (iList.Length == 0)
                    return;
                int startindex = 0;
                int endindex = iList.Length - 1;

                QuickSortProc(iList, startindex, endindex);
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

            int[] ilist4 = { 2, 4, 6, 8, 10, 1, 3, 5, 7, 9, -1 };
            mks.QuickSort(ilist4);



        }
    }



