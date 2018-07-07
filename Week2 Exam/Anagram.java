import java.util.*;

public class Test1{

	public static void Anagram(String s, String t)	{

		String a = s.replaceAll("\\s", "");
		String b = t.replaceAll("\\s", "");
		boolean res = true;
		if(a.length() == b.length()){

			char s1[] = a.toLowerCase().toCharArray();
			char t1[] = b.toLowerCase().toCharArray();
			Arrays.sort(s1);
			Arrays.sort(t1);
			res = Arrays.equals(s1, t1);
		}

		else{

			res = false;
		}

		if(res){

			System.out.println(" true");
		}

		else{

			System.out.println(" false");
		}
	}

	public static void main(String[] args){

		Anagram("anagram", "nagaram");
		Anagram("Keep", "Peek");
		Anagram("Mother In Law", "Hitler Woman");
		Anagram("School Master","The Classroom ");
		Anagram("School MASTER", "The ClassROOM");
		Anagram("DORMITORY", "Dirty Room");
		Anagram("ASTRONOMERS", "NO MORE STARS");
		Anagram("Toss", "Shot");
		Anagram("joy", "enjoy");
		Anagram("Debit Card","Bad Credit");
		Anagram("Dormitory","Dirty Room");
		Anagram("SiLeNt CAT", "LisTen AcT");
	}
}
