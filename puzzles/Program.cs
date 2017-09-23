using System;
using System.Collections.Generic;
using System.Linq;
namespace puzzles
{
    class Program
    {
        public static int[] RandomArray()
        {
            Random rand = new Random();
            List<int> myList = new List<int>();
            for (int num = 0; num < 10; num++)
            {
                myList.Add(rand.Next(5,25));
            }
            int max = myList[0];
            int min = myList[0];
            int total = 0;
            foreach (int num in myList)
            {
                if (num > max)
                {
                    max = num;
                }
                if (num < min)
                {
                    min = num;
                }
                // Console.WriteLine(num); See all the random numbers generated
                total += num;
            }
            Console.WriteLine("Min: {0}, Max: {1}, Total: {2}", min, max, total);
            return myList.ToArray();
        
        }

        // public string TossCoin(Random rand) {
        //     Console.WriteLine("Tossing a Coin!");
        //     string result = "Tails";
        //     if(rand.Next() == 0) {
        //         result = "Heads";
        //     }
        //     Console.WriteLine(result);
        //     return result;
        // }

        // public double TossMultiplecoints(int num)
        // {
        //     int numOfHeads = 0;
        //     for (int toss = 0; toss < num; toss++)
        //     {
        //         if (TossCoin(new Random()) == "Heads")
        //         {
        //             numOfHeads++;
        //         }
        //     }
        //     return (double)numOfHeads/(double)num;
        // }

        public static string[] Names()
        {
            string[] names = new string[5]{"Todd","Tiffany","Charlie","Geneva","Sydney"};
            Random rand = new Random();
            for (var i = 0; i < names.Length-1; i++)
            {
                int randI = rand.Next(i + 1, names.Length - 1);
                string temp = names[i];
                names[i] = names[randI];
                names[randI] = temp;
                Console.WriteLine(names[i]);
            }
            Console.WriteLine(names[names.Length - 1]);

            List<string> nameList = new List<string>();
            foreach (var name in names)
            {
                if (name.Length > 5)
                {
                    nameList.Add(name);
                }
            }
            return nameList.ToArray();
        }


        static void Main(string[] args)
        {
            RandomArray();
            // TossCoin();
            // TossMultiplecoints(5);
            Names();
        }
    }
}
