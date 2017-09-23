using System.Collections.Generic;
using System;
// Looks good Ahrav. There was more to this assignment though right?  I'll let it slide for now :)
namespace CollectionPractice
{
    class Program
    {
        static void Main(string[] args)
        {
            List<string> iceCream = new List<string>();
            iceCream.Add("vanilla");
            iceCream.Add("Chocolate");
            iceCream.Add("Strawberry");
            iceCream.Add("Rocky Road");
            iceCream.Add("Chocolate Chip");
            iceCream.Remove("Strawberry");
            Console.WriteLine(iceCream.Count);
            // int[] numArr = {0,1,2,3,4,5,6,7,8,9};
            // string[] names = {"Tim", "Martin", "Nikki", "Sara"};
            // bool[] boolArr = {true, false, true, false, true, false, true, false, true, false};
            // int[,,] array3D = new int[2,1,10]
            //     {
            //         {1,2,3,4,5,6,7,8,9,10},
            //         {2,4,6,8,10,12,14,16,18,20}
            //     };
            Dictionary<string,string> userInfo = new Dictionary<string,string>();
            userInfo.Add("Tim", "Vanilla");
            userInfo.Add("Martin", "Strawberry");
            userInfo.Add("Nikki", "Chocolate");
            userInfo.Add("Sara", "Rocky Road");
            foreach (var entry in userInfo)
            {
                Console.WriteLine(entry.Key + " - " + entry.Value);
            }
        }
    }
}
