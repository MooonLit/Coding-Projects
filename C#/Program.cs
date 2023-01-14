using System;

namespace CSharp
{
    internal class Program
    {
        static void Main(string[] args)
        {
            double num01, num02, num03;
            Console.Write("Input a number: ");
            num01 = Convert.ToDouble(Console.ReadLine());

            Console.Write("Input a second number: ");

            num02 = Convert.ToDouble(Console.ReadLine());

            Console.Write("Input a second number: ");
            num03 = Convert.ToDouble(Console.ReadLine());

            Double total = (num01  +num02 + num03);
            Double result = total / 3;

            // Console.WriteLine("The result is " + result);
            if (num01 == 5)
            {
                Console.Write("You typed the number 5\n");
            }
            // else if (num01 == num02)
            // {
            //     Console.Write("The first number is equal to the second number");
            // }
            // else
            // {
            //     Console.Write("You did not type 5 for the first number.");
            // }
            Console.ReadKey();
        }
    }
}