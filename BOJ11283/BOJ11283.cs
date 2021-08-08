using System;
using System.Text;

namespace boj
{
    class Program
    {
        static void Main(string[] args)
        {
            char chr = char.Parse(Console.ReadLine());
            int i1 = Convert.ToInt32(chr);
            Console.WriteLine(i1 - 44031);
        }
    }
}
