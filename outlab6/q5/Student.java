import java.util.*;

public class Student extends Person{
	public int rollno;
	public ArrayList<Teacher> teachers;
	public Student(String s, int a, int r){
		super(s,a);
		rollno = r;
		teachers = new ArrayList<Teacher>();
	}
	public Student(Person p,int r){
		super(p.getName(),p.getAge());
		rollno = r;
		teachers = new ArrayList<Teacher>();
	}
	public void addTeacher(Teacher teachr){
		teachers.add(teachr);
	}
	public ArrayList<Teacher> getTeachers(){
		return teachers;
	}
	public void intro(){
		System.out.println("I am a Student, "+ name+ ", "+age+", "+rollno);
	}
}
