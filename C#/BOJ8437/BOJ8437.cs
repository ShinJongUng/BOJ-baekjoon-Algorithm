using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace boj8437
{
    class Program
    {
        static void Main(string[] args)
        {
            BigInteger first = BigInteger.Parse(Console.ReadLine());
            BigInteger second = BigInteger.Parse(Console.ReadLine());
            BigInteger a = first / 2 - second / 2;
            BigInteger b = first - a;
            Console.WriteLine(b);
            Console.WriteLine(a);
        }
    }
}
