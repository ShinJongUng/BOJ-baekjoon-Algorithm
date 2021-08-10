using System;
using System.Numerics;


namespace boj
{
    class Program
    {
        static void Main(string[] args)
        {
            double L = double.Parse(Console.ReadLine());

            double t = Math.Ceiling(L / 5);

            Console.WriteLine(t);
        }
    }
}