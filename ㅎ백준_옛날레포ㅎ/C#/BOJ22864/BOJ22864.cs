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
            string[] spt = str.Split(' ');

            int value = 0;
            int work = 0;

            int A = int.Parse(spt[0]);
            int B = int.Parse(spt[1]);
            int C = int.Parse(spt[2]);
            int M = int.Parse(spt[3]);

            if (M < A)
            {
                work = 0;
            }
            else
            {
                for (int time = 0; time < 24; time++)
                {
                    if (value < 0)
                    {
                        value = 0;
                    }
                    value += A;
                    if (value > M)
                    {
                        value -= A;
                        value -= C;
                    }
                    else
                    {
                        work += B;
                    }
                }
            }
            Console.WriteLine(work);
        }
    }
}
