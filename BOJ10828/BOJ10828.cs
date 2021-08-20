using System;
using System.Collections.Generic;
using System.Text;

namespace boj
{
    class Program
    {
        static void Main(string[] args)
        {
            var A = int.Parse(Console.ReadLine());
            Stack<int> stack = new();
            StringBuilder sw = new();

            for (int i = 0; i < A; i++)
            {
                string[] input = Console.ReadLine().Split(' ');


                if (input[0] == "push")
                {
                    stack.Push(int.Parse(input[1]));
                }
                else if (input[0] == "pop")
                {
                    if (stack.Count == 0)
                    {
                        sw.AppendLine("-1");
                    }
                    else
                    {
                        sw.Append(stack.Pop() + "\n");
                    }
                }
                else if (input[0] == "size")
                {
                    sw.Append(stack.Count + "\n");
                }
                else if (input[0] == "empty")
                {
                    if (stack.Count == 0)
                    {
                        sw.AppendLine("1");
                    }
                    else
                    {
                        sw.AppendLine("0");
                    }
                }
                else if (input[0] == "top")
                {
                    if (stack.Count == 0)
                    {
                        sw.AppendLine("-1");
                    }
                    else
                    {
                        sw.Append(stack.Peek() + "\n");
                    }
                }
            }
            Console.WriteLine(sw.ToString());
        }
    }
}
