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
            // tree
            // ----------------------------------------

         public class Node
         {
            public int item;
            public Node? nodeLeft = null;
            public Node? nodeRight = null;

            public Node ()
            {
                //nodeLeft = null;
                //nodeRight = null;
            }
            public void display()
            {
                Console.Write("[");
                Console.Write(item);
                Console.Write("]");
            }
        }

        public class Tree
        {
            public Node? nodeRoot = null;

            public Tree()
            {
                //nodeRoot = null;
            }
            public Tree (int newvalue)
            {
                nodeRoot = new Node();
                nodeRoot.item = newvalue;
            }

            public Node? ReturnRoot()
            {
                return nodeRoot;
            }

            /*
            public void Insert(int newvalue)
            {
                Console.WriteLine("\n100");

                Node nodeNew = new Node();
                nodeNew.item = newvalue;
                if (nodeRoot == null)
                {
                    nodeRoot = nodeNew;
                    Console.WriteLine("101");
                }
                else
                {
                    Console.WriteLine("200");

                    Node nodeCurrent = nodeRoot;
                    Node nodeParent;
                    while (true)
                    {
                        Console.WriteLine("210");

                        nodeParent = nodeCurrent;
                        if (newvalue < nodeCurrent.item)
                        {
                            Console.WriteLine("220");

                            nodeCurrent = nodeCurrent.nodeLeft;
                            if (nodeCurrent == null)
                            {
                                Console.WriteLine("230");

                                nodeParent.nodeLeft = nodeNew;
                                return;
                            }

                        }
                        else
                        {
                            Console.WriteLine("310");

                            nodeCurrent = nodeCurrent.nodeRight;
                            if (nodeCurrent == null)
                            {
                                Console.WriteLine("320");

                                nodeParent.nodeRight = nodeNew;
                                return;

                            }
                        }
                    }

                }
            }
            */


            public void Insert2(int newvalue)
            {
                Console.WriteLine("\n100");

                Node nodeNew = new Node();
                nodeNew.item = newvalue;
                if (nodeRoot == null)
                {
                    Console.WriteLine("110");

                    nodeRoot = nodeNew;
                    return;
                }

                Node nodeCurrent = nodeRoot;

                /*
                while (true)
                {
                    Console.WriteLine("200");

                    Node left = nodeCurrent.nodeLeft;
                    Node right = nodeCurrent.nodeRight;


                    if (nodeCurrent.nodeLeft == null)
                    {
                        Console.WriteLine("210");

                        nodeCurrent.nodeLeft = nodeNew;
                        return;
                    }


                    if (nodeCurrent.nodeRight == null)
                    {
                        Console.WriteLine("210");

                        nodeCurrent.nodeRight = nodeNew;
                        return;
                    }

                    nodeCurrent = nodeCurrent.nodeLeft;

                }
                */



                /*
                if (right == null)
                {
                    Console.WriteLine("220");

                    nodeRoot.nodeRight = nodeNew;
                    return;
                }
                */

                /*
                Node nodeCurrent = nodeRoot;
                Node nodeParent;
                while (true)
                {
                    Console.WriteLine("300");

                    nodeParent = nodeCurrent;
                    if (newvalue < nodeCurrent.item)
                    {
                        Console.WriteLine("410");

                        nodeCurrent = nodeCurrent.nodeLeft;
                        if (nodeCurrent == null)
                        {
                            Console.WriteLine("420");

                            nodeParent.nodeLeft = nodeNew;
                            return;
                        }

                    }
                    else
                    {
                        Console.WriteLine("500");

                        nodeCurrent = nodeCurrent.nodeRight;
                        if (nodeCurrent == null)
                        {
                            Console.WriteLine("520");

                            nodeParent.nodeRight = nodeNew;
                            return;

                        }
                    }
                }
                */
                
            }
            /*
            public void Preorder (Node Root)
            {
                if (Root != null)
                {
                    Console.Write(Root.item + " ");
                    Preorder(Root.nodeLeft);
                    Preorder(Root.nodeRight);
                }
            }

            public void Inorder (Node Root)
            {
                if (Root != null)
                {
                    Inorder(Root.nodeLeft);
                    Console.Write(Root.item + " ");
                    Inorder(Root.nodeRight);
                }
            }

            public void Postorder(Node Root)
            {
                if (Root != null)
                {
                    Console.Write(Root.item + " ");
                    Postorder(Root.nodeLeft);
                    Postorder(Root.nodeRight);
                }
            }

            public void BreadthFirst(Node Root)
            {
                if (Root != null)
                {
                    Console.Write(Root.item + " ");

                }
            }
            */

            public void ShowNode(int tree_level, Node nodeTmp)
            {
                string ShowSpaceChar = ".";
                int looptimes = Math.Abs(tree_level - 4);

                for (int ii=0; ii<looptimes; ii++)
                {
                    Console.Write(ShowSpaceChar);
                }
                Console.Write(nodeTmp.item);


                //Console.Write(ShowSpaceChar); Console.Write(nodeTmp.item); Console.Write(ShowSpaceChar);
            }

            /*
            public void DisplayTree()
            {
                if (nodeRoot == null)
                {
                    Console.WriteLine("Empty tree");
                    return;
                }
                int TreeLevel = 1;
                //string ShowSpaceChar = ".";
                Node nodeThis = nodeRoot;
                ShowNode(TreeLevel, nodeThis);
                //Console.Write(ShowSpaceChar); Console.Write(nodeThis.item); Console.Write(ShowSpaceChar);
                Console.WriteLine("");
                TreeLevel++;
                Node left = nodeThis.nodeLeft;
                ShowNode(TreeLevel, left);

                Node right = nodeThis.nodeRight;
                ShowNode(TreeLevel, right);

                Console.WriteLine("");




            }
            */


        }




        // ----------------------------------------
        // Main
        // ----------------------------------------
        static void Main(String[] args)
        {

            // tree
            //Tree BST = new Tree();

            BST.Insert(30);
            BST.Insert(35);
            BST.Insert(57);
            BST.Insert(15);
            BST.Insert(63);
            BST.Insert(49);
            BST.Insert(89);
            BST.Insert(77);
            BST.Insert(67);
            BST.Insert(98);
            BST.Insert(91);


            //BST.Insert2(1);
            //BST.Insert2(2);
            //BST.Insert2(3);
            //BST.Insert(4);
            //BST.Insert(5);
            //BST.Insert(6);
            //BST.Insert(7);

            Console.WriteLine("\nroot");
            BST.ReturnRoot().display();
            Console.WriteLine("\npreorder");
            BST.Preorder(BST.ReturnRoot());
            Console.WriteLine("\ninorder");
            BST.Inorder(BST.ReturnRoot());
            Console.WriteLine("\npostorder");
            BST.Postorder(BST.ReturnRoot());
            Console.WriteLine("\n");


            //BST.DisplayTree();



        }
    }


