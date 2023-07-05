import java.util.HashMap;
import java.util.ArrayList;


public class g4g_two_repeated_elements {
    public static void main(String[] args) {
        int[] arr = {1,2,1,3,4,3};
        int[] result = twoRepeated(arr, 4);

        for (int i : result){
            System.out.println(i);
        }
    }

    static public int[] twoRepeated(int arr[], int N)
    {
        HashMap<Integer, Integer> hash = new HashMap<>();
        ArrayList<Integer> repeatedElements = new ArrayList<>();

        for(int i : arr){
            if (hash.containsKey(i)){
                hash.put(i, hash.get(i) + 1);

                if(hash.get(i) > 1){
                    repeatedElements.add(i);
                }
            }
            
            else{
                hash.put(i, 1);
            }
        }

        int[] twoRepeated = new int[repeatedElements.size()];

        for(int i = 0; i < repeatedElements.size(); i++){
            twoRepeated[i] = repeatedElements.get(i);
        }

        return twoRepeated;
    }
    
}
