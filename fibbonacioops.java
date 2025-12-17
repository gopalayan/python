import java.util.*;
class fibo{
    int n;
    public fibo(int n){
        this.n=n;
    }
    public void display(){
        int f0=0;
        int f1=1;
        int f2;
        System.out.println(f0);
        System.out.println(f1);
        for(int i=2;i<n;i++){
            f2=f1+f0;
            System.out.println(f2+" ");
            f0=f1;
            f1=f2;
        }

    }
}
public class Fibonaccioops {
    public static void main(String[] args){
        Scanner scanner=new Scanner(System.in);
        int n=scanner.nextInt();
        fibo series=new fibo(n);
        series.display();

        scanner.close();

    }
    
}