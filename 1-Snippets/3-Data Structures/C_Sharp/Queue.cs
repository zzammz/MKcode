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
        // queue
        // ----------------------------------------
        public class mkQueue
        {
            ArrayList mksAL;
            int mksCount = 0;
            public mkQueue()
            {
                mksAL = new ArrayList();
                mksCount = 0;
            }

            public void Push(int newval)
            {
                mksAL.Add(newval);
                mksCount++;
            }
            public int Pop()
            {
                if (mksCount == 0)
                    return -1;

                int valread = Convert.ToInt16(mksAL[0]);
                mksAL.RemoveAt(0);
                mksCount--;
                return valread;
            }
            public void mksShow()
            {
                Console.WriteLine("showing queue");
                for (int ii = 0; ii < mksCount; ii++)
                    Console.WriteLine(mksAL[ii]);
                Console.WriteLine("");
            }
        }



        // ----------------------------------------
        // Main
        // ----------------------------------------
        static void Main(String[] args)
        {


            // queue
            mkQueue mymks = new mkQueue();
            mymks.mksShow();
            mymks.Push(42);
            mymks.Push(23);
            mymks.Push(57);
            mymks.mksShow();
            int tmpval = mymks.Pop();
            Console.WriteLine(tmpval);
            mymks.mksShow();


        }
    }


