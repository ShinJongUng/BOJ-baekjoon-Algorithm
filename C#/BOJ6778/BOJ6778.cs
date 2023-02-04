using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp2
{
    class Program
    {
        static void Main(string[] args)
        {
            int antenna = int.Parse(Console.ReadLine());
            int eyes = int.Parse(Console.ReadLine());


            if (antenna >= 3 && eyes <= 4)
                Console.WriteLine("TroyMartian");
            if (antenna <= 6 && eyes >= 2)
                Console.WriteLine("VladSaturnian");
            if (antenna <= 2 & eyes <= 3)
                Console.WriteLine("GraemeMercurian");
        }
    }
}
