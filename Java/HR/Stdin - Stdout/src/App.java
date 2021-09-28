import java.util.Scanner;

public class App {
    

    public static void main(String[] args) throws Exception {

        // imprime un string un doule y una cadena de texto 
        
        Scanner scan = new Scanner(System.in);
        int i = scan.nextInt();
        System.out.println("Int: " + i);
        scan.nextLine();
        double d = scan.nextDouble();
        scan.nextLine();
        String s = scan.nextLine();

        System.out.println("String: " + s);
        System.out.println("Double: " + d);
        System.out.println("Int: " + i);
        
        scan.close();
        
    }

    
}
