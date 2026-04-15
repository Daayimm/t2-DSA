
import java.util.ArrayList;
import java.util.Scanner;


/**
 * TODO: Error prevention
 *       Fix input
 *       No print statements when asking user for moves
 *       winning message 
 *       crashes if user inputs invalid input
 * 
 */



public class MagicSquareGame{
    




    public static void shuffle(int[][] square){

        int n = square.length;
        int n_swap = n*n;
        // int i ,j =0;

        int i_random;
        int j_random;

        for (int i =0;i<n_swap;i++){
            ArrayList<int []> arr = new ArrayList<int []>();

            i_random = (int) Math.floor(Math.random() * (n));
            j_random = (int) Math.floor(Math.random() * (n));

            int[] up = {i_random - 1 , j_random};
            int[] down = {i_random +1,j_random};
            int[] right = {i_random,j_random+1};
            int[] left = {i_random,j_random-1};

            if (i_random > 0) {
                arr.add(up);
                
            }if (i_random+1 < n){
                arr.add(down);
            }if (j_random>0){
                arr.add(left);

            }if (j_random+1 < n){
                arr.add(right);
            }


            int rand_neighbour = (int) Math.floor(Math.random() * (arr.size()));




            int[] neighbour = arr.get(rand_neighbour);
            int ni = neighbour[0];
            int nj = neighbour[1];

            swap(square,i_random,j_random,ni,nj);

        }



    }
    public static void display(int[][] square){

        for (int i = 0; i < square.length;i++){
            for (int j = 0;j< square.length;j++){
                System.out.print(square[i][j]);
                System.out.print('\t');
            }System.out.print('\n');
        }
    }

    public static void move(int square[][],int i,int j, String direction){

        int n = square.length;
        // Scanner scanner = new Scanner(System.in);

        // String userInput = scanner.nextLine();

        if(direction.equalsIgnoreCase("D")){
            if(i+1< n){
            swap(square,i,j,i+1,j);
            } else{
                System.out.println("invalid input");
            }
        }else if (direction.equalsIgnoreCase("U")){
            if(i > 0){
            swap(square,i,j,i-1,j);}
            else{
                System.out.println("invalid input");
            }
        }else if(direction.equalsIgnoreCase("R")){
            if(j +1 < n){
            swap(square,i,j,i,j+1);}
             else{
                System.out.println("invalid input");
            }
        }else if(direction.equalsIgnoreCase("L")){
            if(j > 0){
            swap(square,i,j,i,j-1);
            } else{
                System.out.println("invalid input");
            }
        }
        

    }

    public static boolean isMagicSquare(int [][] square){
        int n = square.length;
        int target = n *((n*n) +1 ) / 2;


        // each row
        for (int i = 0; i< n;i++){
            int row_sum = 0;

            for (int j = 0;j<n;j++){
                row_sum += square[i][j];
            }

            if(row_sum != target){
                return false;
            }
        } 
        // each column
        for (int i = 0;i<n;i++){
            int column_sum = 0;

            for (int j=0;j<n;j++){
                column_sum += square[j][i];
            }
            if (column_sum != target){
                return false;
            }


        }
        int one_diagonal_sum = 0;
        // top left to bottom right diagonal
        for (int i = 0;i<n;i++){
            one_diagonal_sum += square[i][i];
        }
            if(one_diagonal_sum != target){
                return false;
            }

        int two_diagonal_sum = 0;
        // top right to bottom left diagonal
        for (int i = 0;i<n;i++){
            two_diagonal_sum += square[i][n-1-i];
        }
            if(two_diagonal_sum != target){
                return false;
            }


            return true;
    }


    public static void swap(int [][]square,int i, int j,int ni,int nj){

        int temp = square[i][j];
        square[i][j] = square[ni][nj];
            square[ni][nj] = temp;



    }




    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int n;
        String userInput;
        int count =0;
        do { 
            System.out.println("Please input a postive odd integer: ");
            n = scanner.nextInt();
        } while (n <= 0 || n % 2 == 0);

            scanner.nextLine();


          generate_MagicSqaure magicSqaure = new generate_MagicSqaure();
          int [][] square = magicSqaure.generateMagicSqaure(n);
        
        shuffle(square);
        display(square);

        while (!isMagicSquare(square)){
            System.out.println("Enter move as: row column direction (e.g. 1 2 R): ");
            userInput = scanner.nextLine().trim();
             if (userInput.isEmpty()) {
                System.out.println("Empty input. Please try again.");
                continue;
            }
            String[] parts = userInput.split("\\s+");

            if (parts.length != 3) {
                System.out.println("Invalid format. Use: row column direction");
                continue;
            }


            int row;
            int column;
            String direction = parts[2];

            try {
                row = Integer.parseInt(parts[0] );
                column = Integer.parseInt(parts[1]);
            } catch (NumberFormatException e) {
                System.out.println("Row and column must be integers.");
                continue;
            }
            move(square, row, column, direction);
            count ++;

            display(square);
        }System.out.println(count);


    }


}