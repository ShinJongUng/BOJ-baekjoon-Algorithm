using System;
using System.Collections.Generic;
using System.Linq;

namespace boj
{
    class Program
    {
        static void Main(string[] args)
        {
            int cnt = int.Parse(Console.ReadLine());

            List<string> slist = new List<string>();


            for (int i = 0; i < cnt; i++)
            {
                string word = Console.ReadLine();
                slist.Add(word.ToLower());
            }

            slist = slist.Distinct().ToList();
            slist.Sort();
            slist = slist.OrderBy(c => c.Length).ToList();

            foreach (string ans in slist)
            {
                Console.WriteLine(ans);
            }
        }
    }
}
