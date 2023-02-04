using System;
using System.Numerics;


namespace boj
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] str = Console.ReadLine().Split(' ');
            int A = int.Parse(str[0]);
            int B = int.Parse(str[1]);


            int i = B - A;

            Console.WriteLine(i + " " + B);
        }
    }
}