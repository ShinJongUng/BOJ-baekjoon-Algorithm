using System;

namespace boj
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] str = Console.ReadLine().Split(' ');
            int A = int.Parse(str[0]);
            int B = int.Parse(str[1]);
            int C = int.Parse(str[2]);

            if (B >= C)
            {
                Console.WriteLine("-1");
            }
            else
            {
                Console.WriteLine((A / (C - B)) + 1);
            }
        }
    }
}
