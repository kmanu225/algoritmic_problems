import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        new App().explore(0, 0);
        print2D(new App().adjacencymatrix);

    }

    public static void print2D(int mat[][])
    {
        // Loop through all rows
        for (int[] row : mat)
 
            // converting each row as string
            // and then printing in a separate line
            System.out.println(Arrays.toString(row));
    }
    
}
