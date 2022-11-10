package Java;
public class apalyndrome {
    public apalyndrome(){

    }
    
    public static boolean isPaL( int n){
        //StringBuffer nb = new StringBuffer(n);

        int pow=0;
        int nRev=0;
        int ncp = n;

        while(ncp!=0){
            //nb.append(ncp%10);
            nRev += (int) ((ncp%10)*Math.pow(10, pow));
            ncp = (ncp-ncp%10)/10;
            pow+=1;
        }

        //System.out.println(nb.reverse().toString());
        System.out.println(nRev);

        // if(nb.reverse() == nb){
        //     return true;
        // }

        if(nRev==n){
            return true;
        }
        return false;
    }

    
}
