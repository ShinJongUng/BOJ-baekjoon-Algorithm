using System;
using System.Text;

namespace boj
{
    class Program
    {
        static void Main(string[] args)
        {
            string str = Console.ReadLine();
            string [] arr = str.Split(' ');
            long i1 = long.Parse(arr[0]);
            long i2 = long.Parse(arr[1]);
            long i3 = long.Parse(arr[2]);
            Console.WriteLine(i1 + i2 + i3);
        }
    }
}
