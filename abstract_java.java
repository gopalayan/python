import java.util.*;
abstract class person{
    String name;
    int age;
    abstract void read();
    abstract void print();
}
class student extends person{
    @Override
    void read(){
      Scanner scanner=new Scanner(System.in);
      System.out.println("entr ur name  :");
      name=scanner.nextLine();
      System.out.println("entr ur age :");
      age=scanner.nextInt();

      scanner.close();

    }
    @Override
    void print(){
        System.out.println("I am a student my name..:" + name);
        System.out.print("my age is :"+ age);
    }
}
class techer extends person{
    @Override
    void read(){
        Scanner scanner=new Scanner(System.in);
        System.out.println("entr ur name  :");
        name=scanner.nextLine();
        System.out.println("entr ur age :");
        age=scanner.nextInt();
        scanner.close();
    }
    @Override
    void print(){
        System.out.println("i am a teacher my name is  :"+name);
        System.out.print("my age is :"+age);
    }

}
public class abstract_java {
    public static void main(String[] args){
        person s1=new student();
        s1.read();
        s1.print();
        System.out.println();
        person t1=new techer();
        t1.read();
        t1.print();


    }
    
}