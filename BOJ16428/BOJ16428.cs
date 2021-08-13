using System;
using System.Numerics;

namespace boj
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] str = Console.ReadLine().Split(' ');
            BigInteger A = BigInteger.Parse(str[0]);
            BigInteger B = BigInteger.Parse(str[1]);

            if (A > 0 && B < 0)
            {
                Console.WriteLine(-(A / BigInteger.Abs(B)));
                Console.WriteLine(A % BigInteger.Abs(B));
            }
            else if (A < 0 && B < 0)
            {
                Console.WriteLine(BigInteger.Abs(A / B));
                Console.WriteLine(A % (BigInteger.Abs(B)));
            }
            else
            {
                Console.WriteLine(A / B);
                Console.WriteLine(A % B);
            }

        }
    }
}
