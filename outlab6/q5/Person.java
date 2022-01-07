import java.io.*;

public class Person {
	public String name;
	public int age;
	public Person(String s, int x){
		name=s;
		age=x;
	}
	public String getName(){
		return name;
	}
	public int getAge(){
		return age;
	}
	public void intro(){
		System.out.println("I am a person, "+ name+ ", "+age);
	}
}
