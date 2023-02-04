using System;

namespace boj
{
    class Program
    {
        static void Main(string[] args)
        {
            int str = int.Parse(Console.ReadLine());

            int row = str / 2;
            int col = str - row;

            Console.WriteLine((row + 1) * (col + 1));
        }
    }
}
