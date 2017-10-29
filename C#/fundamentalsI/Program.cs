using System;

namespace fundamentalsI
{
    class Program
    {
        static void Main(string[] args)
        {
            for (int i = 1; i <= 255; i++)
            {
                Console.WriteLine(i);
            }
            for (int i = 1; i <= 100; i++)
            {
                if (i % 3 == 0 && i % 5 == 0)
                {
                    Console.WriteLine("{0} FizzBuzz", i);
                }
                else if (i % 3 == 0)
                {
                    Console.WriteLine("{0} Fizz", i);
                }
                else if (i % 5 == 0)
                {
                    Console.WriteLine("{0} Buzz", i);
                }
            }
        }
    }
}
