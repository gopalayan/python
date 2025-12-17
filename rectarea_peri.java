import java.util.*;
class rectangle{
    private double l;
    private double w;
    public rectangle(double l,double w){
        this.l=l;
        this.w=w;
    }
    public double cal_area(){
        return l*w;
    }
    public double cal_peri(){
        return 2*(l+w);
    }
}
public class rectarea_peri {

    public static void main(String[] args){
        Scanner scanner=new Scanner(System.in);
        System.out.println("entr ur length size :");
        int l=scanner.nextInt();
        System.out.println("entr ur breath size :");
        int w=scanner.nextInt();
        rectangle rectangle1=new rectangle(l,w);
        double area=rectangle1.cal_area();
        System.out.print(area);
        scanner.close();
    }
    
}