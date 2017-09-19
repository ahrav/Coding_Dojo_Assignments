using System;
using System.Collections.Generic;
// Overall, pretty good job Ahrav.  I saw a dependency growing with using Lists instead of in-place operations.  Challenge yourself in the future.
namespace Basic13
{
    class Program
    {
        public static void PrintTo255()
        {
            for (int i = 1; i < 256; i++)
            {
                Console.WriteLine(i);
            }
        }

        public static void PrintTo255Odd()
        {
            for (int i = 1; i <= 255; i+=2)
            {
                Console.WriteLine(i);
            }
        }

        public static void PrintSum()
        {
            int sum = 0;
            for (int i = 1; i <= 255; i++)
            {
                sum += i;
                Console.WriteLine("New number: {0} Sum: {1}", i, sum);
            }
        }

        public static void IterArray()
        {
            int[] numArray = {1,3,5,7,9,13};
            foreach (int num in numArray)
            {
                Console.WriteLine(num);
            }
        }

        public static void FindMax(int[] myArray)
        {
            int maxNum = myArray[0]; // maxNum is first value
            foreach (int num in myArray) // foreach starts at first value, try for loop instead
            {
                if (num > maxNum)
                {
                    maxNum = num;
                }
            }
            Console.WriteLine(maxNum);
        }

        public static void GetAverage(int[] myArray)
        {
            int total = 0;
            foreach (int num in myArray)
            {
                total += num;
            }
            total = total / myArray.Length; // does total end up always giving you a whole number? What about an average of 4.5, does making it an int coerce it to 4?
            Console.WriteLine(total);
        }

        public static void OddNumbers()
        {
            List<int> oddList = new List<int>();
            for (int i = 1; i <= 255; i+=2)
            {
                oddList.Add(i);
            }
            int[] newList = oddList.ToArray();
            foreach (int num in newList)
            {
                Console.WriteLine(num);
            }
        }

        public static void GreaterThanY(int[] myArray, int myNum)
        {
            int total = 0;
            foreach (int num in myArray)
            {
                if (num > myNum)
                {
                    total+=1;
                }
            }
            Console.WriteLine(total);
        }

        public static void SquareValues(int[] myArray)
        {
            // what if you had to do this in-place? You wouldn't make a separate List would you?
            List<int> myList = new List<int>();
            foreach (int num in myArray)
            {
                myList.Add(num * num);
            }
            int[] newList = myList.ToArray();
            foreach (int num in newList)
            {
                Console.WriteLine(num);
            }
        }

        public static void EliminateNegative(int[] myArray)
        {
            // not bad.  I like your ability to build a new List anytime you need the workspace, but challenge yourself to do in-place operations
            List<int> myList = new List<int>();
            foreach (int num in myArray)
            {
                if (num < 0)
                {
                    myList.Add((int)0);
                }
                else
                {
                    myList.Add(num);
                }
            }
            int[] newList = myList.ToArray();
            foreach (int val in newList)
            {
                Console.WriteLine(val);
            }
        }

        public static void MinMaxAverage(int[] myArray)
        {
            int minInt = myArray[0];
            int maxInt = myArray[0];
            int total = 0;
            foreach (int num in myArray)
            {
                if (num < minInt)
                {
                    minInt = num;
                }
                if (num > maxInt)
                {
                    maxInt = num;
                }
                total += num;
            }
            int average = total/myArray.Length;
            Console.WriteLine("Min: {0} Max: {1} Avg: {2}", minInt, maxInt, average);
        }

        public static void ShiftArray(int[] myArray)
        {
            List<int> myList = new List<int>();
            for (int i = 1; i < myArray.Length; i++)
            {
                myList.Add(myArray[i]);
            }
            myList.Add((int)0);
            int[] newList = myList.ToArray();
            foreach (int num in newList)
            {
                Console.WriteLine(num);
            }
        }

        public static void NumToString(int[] myArray)
        {
            List<object> myList = new List<object>();
            foreach (int num in myArray)
            {
                if (num < 0)
                {
                    myList.Add("Dojo");
                }
                else
                {
                    myList.Add(num);
                }
            }
            foreach (var obj in myList)
            {
                Console.WriteLine(obj);
            }
        }


        static void Main(string[] args)
        {
            PrintTo255();
            PrintTo255Odd();
            PrintSum();
            IterArray();
            GetAverage(myArray);
            OddNumbers();
            int myNum = 2;
            GreaterThanY(myArray, myNum);
            SquareValues(myArray);
            int[] myArray = {10,2,3,-6,4,-2,1,2};
            EliminateNegative(myArray);
            MinMaxAverage(myArray);
            ShiftArray(myArray);
            NumToString(myArray);
        }
    }
}
