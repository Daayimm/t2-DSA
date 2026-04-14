
import java.util.Scanner;








public class generate_MagicSqaure{
    // public int n;
    public int y;
    public int x;
    // public int[][] square;
        
    // int [][] sqaure = new int[n][n];

    public int[][] generateMagicSqaure(int n){
        
        int [][] square = new int[n][n];

        x = 0;
        y = (n-1)/2;

        square[x][y] = 1;
        
    for (int i = 2;i <= Math.pow(n,2);i++){

    
    if (square[(x-1+n)%n][(y-1+n)%n] == 0){
            x = (x-1+n) % n;
            y = (y-1+n) %n ;

            }else{
                x = (x+1) % n;


            }
            square[x][y] = i;
        }return square;
    }

    public static void printMagicSquare(int[][] sqaure){

        for (int i = 0; i< sqaure.length;i++){

            for (int j =0; j<sqaure.length;j++){
                System.out.print(sqaure[i][j]);
                System.out.print('\t'); 

        }
        System.out.print('\n');        
    }


    }

    public static void main(String[] args) {
        Scanner userInput = new Scanner(System.in);
        System.out.println("Enter an odd positive Integer: ");
        int userInt = userInput.nextInt();

        while (userInt <= 0 || userInt % 2 != 1){

        System.out.println("Enter an odd positive Integer: ");
        userInt = userInput.nextInt();


        }
        generate_MagicSqaure magicSqaure = new generate_MagicSqaure();    
        int [][] num = magicSqaure.generateMagicSqaure(userInt);
      
        printMagicSquare(num);
    }        
    
}