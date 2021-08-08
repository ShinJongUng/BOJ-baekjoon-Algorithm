using System;
using System.Text;
using System.Numerics;

namespace boj
{
    class Program
    {
        static void Main(string[] args)
        {
            string str = Console.ReadLine();
            string[] arr = str.Split(' ');
            BigInteger i1 = BigInteger.Parse(arr[0]);
            BigInteger i2 = BigInteger.Parse(arr[1]);
            Console.WriteLine(i1 * i2);
        }
    }
}
