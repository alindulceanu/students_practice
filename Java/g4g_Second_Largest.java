import java.util.Arrays;


public class g4g_Second_Largest {
    int print2largest(int arr[], int n){
        Arrays.sort(arr);

        int i = n - 1;

        try{
            while((arr[i] == arr[n - 1]) && i >= 0)
                i--;
        }
        catch(Exception e){
            return -1;
        }

        return arr[i];
    }


    public static void main(String[] args) {
        g4g_Second_Largest ob = new g4g_Second_Largest();

        int[] ar = {642, 642, 642};

        System.out.println(ob.print2largest(ar, 3));
    }
}
