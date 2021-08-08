using System;
using System.Text;

namespace boj
{
    class Program
    {
        static void Main(string[] args)
        {
            int i1 = int.Parse(Console.ReadLine());
            char chr = Convert.ToChar(i1 + 44031);
            Console.WriteLine(chr);
        }
    }
}
