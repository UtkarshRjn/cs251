import java.util.regex.*; 
import java.io.*;
import java.util.*;

public class q3{
	public boolean func1(String s){
		return Pattern.matches("[a-zA-Z0-9]{0,5}", s);
	}
	public boolean func2(String s){
		return Pattern.matches("a*b+c", s);
	}
	public boolean func3(String s){
		int l = s.length();
		if(l%2== 1 || l/2 < 1) return false;
		else {
			String regex = String.format("a{%d}b{%d}",l/2,l/2);
			return Pattern.matches(regex,s);
		}
	}
	public List<String> func4(String input,String s){
		List<String> allMatches = new ArrayList<String>();
		Matcher m = Pattern.compile(s).matcher(input);
		while (m.find()) {
   			allMatches.add(m.group());
 		}
 		return allMatches;
	}
}
