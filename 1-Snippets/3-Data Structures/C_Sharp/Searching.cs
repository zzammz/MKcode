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
        // searching
        // ----------------------------------------
        public class DataStructure
        {
            public DataStructure()
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

            public bool LinearSearch(int iSearch, int[] iList)
            {
                int fullcount = iList.Count();
                bool returnresult = false;
                for (int ii = 0; ii < iList.Count(); ii++)
                    if (iSearch == iList[ii])
                    {
                        returnresult = true;
                        break;
                    }

                return returnresult;
            }

            public bool BinarySearchLinear(int iSearch, int[] iList)
            {
                Console.WriteLine("BinarySearchLinear");
                bool returnresult = false;

                showArray(iList);
                Array.Sort(iList);
                showArray(iList);

                if (iList.Count() == 0)
                    return returnresult;

                int min = 0;
                int max = iList.Count() - 1;

                while (min <= max)
                {
                    int mid = (min + max) / 2;

                    if (iList[mid] == iSearch)
                        return true;
                    else if (iSearch < iList[mid])
                        max = mid - 1;
                    else
                        min = mid + 1;
                }

                return returnresult;
            }

            private int BinarySearchRecursiveProc(int iSearch, int[] iList, int min, int max)
            {
                int mid = (min + max) / 2;

                if (iList[mid] == iSearch)
                    return mid;
                else if (iSearch < iList[mid])
                    max = mid - 1;
                else
                    min = mid + 1;

                if (max < min)
                    return -1;

                return BinarySearchRecursiveProc(iSearch, iList, min, max);
            }

            public bool BinarySearchRecursive(int iSearch, int[] iList)
            {
                Console.WriteLine("BinarySearchRecursive");
                bool returnresult = false;
                showArray(iList);
                Array.Sort(iList);
                showArray(iList);

                if (iList.Count() == 0)
                    return returnresult;

                returnresult = BinarySearchRecursiveProc(iSearch, iList, 0, iList.Count() - 1) == -1 ? false : true; 

                return returnresult;
            }
        }



        // ----------------------------------------
        // Main
        // ----------------------------------------
        static void Main(String[] args)
        {

            // Data struc linear search
            DataStructure ds = new DataStructure();
            int[] iilist = { 2, 4, 6, 8, 10, 1, 3, 5, 7, 9, -1 };
            int iisearch = 6;
            bool searchresult = false;
            searchresult = ds.LinearSearch(iisearch, iilist);
            Console.WriteLine("search for: " + iisearch);
            Console.WriteLine("search result: " + searchresult);


            // Data struc bin search
            DataStructure ds = new DataStructure();
            int[] iilist = { 2, 4, 6, 8, 10, 1, 3, 5, 7, 9, -1 };
            int iisearch = 4;
            bool searchresult = false;
            searchresult = ds.BinarySearchLinear(iisearch, iilist);
            Console.WriteLine("--- result---");
            Console.WriteLine("search for: " + iisearch);
            Console.WriteLine("search result: " + searchresult);

            searchresult = ds.BinarySearchRecursive(iisearch, iilist);
            Console.WriteLine("--- result---");
            Console.WriteLine("search for: " + iisearch);
            Console.WriteLine("search result: " + searchresult);



        }
    }

