using System;

namespace boj
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] str = Console.ReadLine().Split(' ');

            int[] src = { int.Parse(str[0]), int.Parse(str[1]), int.Parse(str[2]) };

            Array.Sort(src);

            Console.WriteLine("{0}", string.Join(" ", src));

        }
    }
}
