package Java;
import java.util.ArrayList;
import java.util.List;

public class p34{
    public static void main(String[] args){
       

        aNative n = new aNative(0);
        long som = 0;
        List<Long> tab = new ArrayList<Long>();


        for(n.nbr=0; n.nbr<=10000; n.nbr++){
            if(SumDigitFact(n.nbr)==n.nbr){
                tab.add(n.nbr);
                som =som + n.nbr;
            }
        }
        System.out.println(tab);
        System.out.println(factorial(20));
    }


    public static long SumDigitFact(long n){
        long sum=0;
        long ncp = n;

        while(ncp!=0){
            sum += factorial(ncp%10);
            ncp = (ncp-ncp%10)/10;
        }

        return sum;
    }



    public static long factorial(long n) {
        if(n==1 || n==0){
            return 1;
        }
        else{
            return factorial(n-1)*n;
        }
    }

    public static boolean belongsTo(long[] tab, long nbr){
        for(long elt : tab){
            if(nbr == elt){
                return true;
            }
        }
        return false;
    }

    
}