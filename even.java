import java.util.Scanner;
class add{
    public static void main(){
        int num;
        Scanner S = new Scanner(System.in);
        System.out.println("Enter the first number:");
        num = S.nextInt();
        if(num%2==0)
           System.out.println("It is an even number");
        else
           System.out.println("It is a odd number");
    }
}
