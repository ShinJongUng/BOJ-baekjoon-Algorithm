using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace boj8370
{
    class Program
    {
        static void Main(string[] args)
        {
            string txt = Console.ReadLine();
            string[] text = txt.Split(' ');
            int first = int.Parse(text[0]);
            int second = int.Parse(text[1]);
            int third = int.Parse(text[2]);
            int forth = int.Parse(text[3]);

            Console.WriteLine((first * second) + (third * forth));
        }
    }
}
