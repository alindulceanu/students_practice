
public class g4g_missing_number_in_array {
    public static void main(String[] args) {
        int[] arr = {1,2,4,5};
        int result = missingNumber(arr, 5);
        System.out.println(result);
    }
    
    static int missingNumber(int array[], int n){
        int totalSum = n * (n + 1) / 2;
        int arrSum = 0;

        for (int i : array){
            arrSum += i;
        }

        return (totalSum - arrSum);

    }
}
