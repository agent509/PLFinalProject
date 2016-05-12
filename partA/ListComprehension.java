
import java.util.*;
import java.util.stream.Collector;
import java.lang.Math;

public class ListComprehension {
    public static ArrayList<ArrayList<Integer>> prime1mod3(List<Integer> li){
        ArrayList<ArrayList<Integer>> newlist = new ArrayList<ArrayList<Integer>>();
        li.stream().filter(e -> isprime(e)&& (e % 3 == 1)).map(e -> tripleplusone(e)).forEach(e -> {newlist.add(e);});

        return newlist;

    }
    public static boolean isprime(int a){
        if (a == 2 || a == 3 || a == 5 || a == 7){
            return true;
        }
        if (a % 2 == 0 || a == 1 || a == 9){
            return false;
        }
        for (int i = 3; i < Math.sqrt(a); i += 2){
            if (a % i == 0){
                return false;
            }
        }
        return true;
    }

    public static ArrayList<Integer> tripleplusone(int a){
        ArrayList<Integer> pair = new ArrayList<Integer>();
        pair.add(a);
        pair.add(3 * a + 1);
        return(pair);
    }

}
