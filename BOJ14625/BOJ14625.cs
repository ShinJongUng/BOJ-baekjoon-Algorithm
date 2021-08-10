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
            int n = int.Parse(spt[0]);
            int m = int.Parse(spt[1]);
            int k = int.Parse(spt[2]);

            for(int i = 0; i < n * m; i++)
            {
                if(i == k)
                {
                    break;
                }
            }
            int coor1 = k / m;
            int coor2 = k % m;


            Console.WriteLine(coor1+" "+coor2);
        }
    }
}
