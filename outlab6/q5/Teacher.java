import java.util.*;

public class Teacher extends Person{
	public int salary;
	public ArrayList<Student> students;
	public Teacher(String s, int a, int sal){
		super(s,a);
		salary=sal;
		students = new ArrayList<Student>(); 
	}
	public Teacher(String s, int a){
		super(s,a);
		salary=10000;
		students = new ArrayList<Student>(); 
	}
	public Teacher(Person p, int sal){
		super(p.getName(),p.getAge());
		salary=sal;
		students = new ArrayList<Student>(); 
	}
	public int getSalary(){
		return salary;
	}
	public void addStudent(Student stud){
		students.add(stud);
		return;
	}
	public ArrayList<Student> getStudents(){
		return students;
	}
	public void intro(){
		System.out.println("I am a Teacher, "+ name+ ", "+age+", "+salary);
	}
}
