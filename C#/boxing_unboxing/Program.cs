using System;
using System.Collections.Generic;


namespace boxing_unboxing
{
    class Program
    {
        static void Main(string[] args)
        {
            List<object> AllTypes = new List<object>();
            AllTypes.Add(7);
            AllTypes.Add(28);
            AllTypes.Add(-1);
            AllTypes.Add(true);
            AllTypes.Add("chair");

            // for (var idx = 0; idx < AllTypes.Count; idx++)
            // {
            //     Console.WriteLine(AllTypes[idx]);
            // }
            var sum = 0;
            for (var idx = 0; idx < AllTypes.Count; idx++)
            {
                if (AllTypes[idx] is int){
                    int num = (int)AllTypes[idx];
                    sum+= num;
                }
            }
            Console.WriteLine(sum);    
        }
    }
}
