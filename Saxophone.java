import java.util.Map;
import java.util.HashMap;
import java.util.Scanner;
public class Saxophone
{
	public static void main(String [] args)
	{
		Map<Character, int[]> notes = new HashMap<Character, int[]>();
		notes.put('c', new int[]{2, 3, 4, 7, 8, 9, 10});
		notes.put('d', new int[]{2, 3, 4, 7, 8, 9});
		notes.put('e', new int[]{2, 3, 4, 7, 8});
		notes.put('f', new int[]{2, 3, 4, 7});
		notes.put('g', new int[]{2, 3, 4});
		notes.put('a', new int[]{2, 3});
		notes.put('b', new int[]{2});
		notes.put('C', new int[]{3});
		notes.put('D', new int[]{1, 2, 3, 4, 7, 8, 9});
		notes.put('E', new int[]{1, 2, 3, 4, 7, 8});
		notes.put('F', new int[]{1, 2, 3, 4, 7});
		notes.put('G', new int[]{1, 2, 3, 4});
		notes.put('A', new int[]{1, 2, 3});
		notes.put('B', new int[]{1, 2});
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int t = 0;
		String tmp = in.nextLine();
		while(t < n)
		{
			String line = in.nextLine();
			int[] fingers = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
			int[] fingers_numbers = {0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0};
			int j = 0;
			while(j < line.length())
			{
				int[] note = notes.get(line.charAt(j));
				int k = 0;
				while(k < 10)
				{
					boolean a = false;
					int m = 0;
					while(m < note.length)
					{
						if(note[m] == k + 1)
							a = true;
						m++;
					}
					if(a && fingers[k] == 0)
					{
						fingers[k] = 1;
						fingers_numbers[k] += 1;
					}
					else if (!a)
						fingers[k] = 0;
					k++;
				}
				j++;
			}
			int i = 1;
			System.out.print(fingers_numbers[0]);
			while (i < fingers_numbers.length)
			{
				System.out.print(" ");
				System.out.print(fingers_numbers[i]);
				i++;
			}
			System.out.println();
			t++;
		}
	}
}