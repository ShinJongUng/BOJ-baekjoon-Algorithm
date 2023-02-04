using System;

namespace boj
{
    class Program
    {
        static void Main(string[] args)
        {
            int A = int.Parse(Console.ReadLine());
            int[] height = new int[A];
            int[] weight = new int[A];
            int cnt = 0;

            for (int i = 0; i < A; i++) {
                string write = Console.ReadLine();
                height[i] = int.Parse(write.Split()[0]);
                weight[i] = int.Parse(write.Split()[1]);
            }
            for (int i = 0; i < A; i++)
            {
                cnt = 0;
                for (int j = 0; j < A; j++)
                {
                    if (height[i] < height[j] && weight[i] < weight[j])
                    {
                        cnt++;
                    }
                }
                Console.WriteLine(cnt + 1);
            }
        }
    }
}
