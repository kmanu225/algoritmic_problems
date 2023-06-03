package Java;
public class p19 {

    public p19(int j, int m, int a){
        this.jour = j;
        this.mois = m;
        this.an = a;
    }
    public static boolean check(int[] tab, int val) {
        boolean b = false;
    
        for(int i : tab){
            if(i == val){
                b = true;
                break;
            }
        }
        return b;
    }

    public static boolean biss(int a){
        if(a%100==0){
            if(a%400!=0){
                return false;
            }
        }

        else if(a%4!=0){
            return false;
        }
        return true;
    }

    public int nbJoursMois(){
        int[] tab1 = {1, 3, 5, 7, 8, 10, 12};
        int[] tab2 = {4, 6, 9, 11};
        int mbiss = 2;

        if (check(tab1, this.mois)){
            return 31;
        }

        else if (check(tab2, this.mois)){
            return 30;}

        else if(this.mois==mbiss){
            if(p19.biss(this.an)){
                return 29;
            }
        }

        return 28;}
    
    private static int nbJoursMois_(int mois, int an){
        int[] tab1 = {1, 3, 5, 7, 8, 10, 12};
        int[] tab2 = {4, 6, 9, 11};
        int mbiss = 2;
    
        if (check(tab1, mois)){
                return 31;
            }
            
        else if (check(tab2, mois)){
            return 30;}
    
        else if(mois==mbiss){
            if(p19.biss(an)){
                return 29;
                }
            }
    
        return 28;}
        
    public int nbJoursDepuis1600(){
        int countBiss = 0;
        int countDays = 0;
        int ian = 1600;
        int imois = 1;

        for(imois=1; imois<this.mois; imois++){
            countDays+=p19.nbJoursMois_(imois, this.an);
        }
        countDays+=this.jour;

        for(ian=1600; ian<this.an; ian++){
            if(biss(ian)){
                countBiss++;
            }
        }

        countDays += 366*countBiss+(this.an-1600-countBiss)*365;
        return countDays;}

    public int distance(p19 d){
        return d.nbJoursDepuis1600()-this.nbJoursDepuis1600();}

    public int numJourDeLaSemaine(){
        int ecart = Math.abs(this.distance(p19.mardi010102));
        ecart = ecart%7;

        if(this.an<2002){
            if(3<=ecart &&  ecart <=6){
                return 6-ecart+3;
            }

            else{
                return 2-ecart;
            }
        }

        return (ecart+2)%7;}

    public int compareTo(p19 d){
        if(this.distance(d)==0){
            return 0;
        }
        else if(this.distance(d)<0){
            return 1;
        }

        return -1;}

    public String toString(){
        return this.jour+"/"+this.mois+"/"+this.an;}

    public void afficheCal(){
        System.out.println("Calendrier du mois de "+p19.months[this.mois-1]+" "+this.an+ " :");

        int jrMois = this.nbJoursMois();
        int j = 1;

        for(j=1; j<=jrMois; j++){
            p19 d = new p19(j, this.mois, this.an);
            System.out.println(semaine[d.numJourDeLaSemaine()]+" "+j);
        }
    }

    public static int findDimanche(){
        int count = 0;
        int mois_ = 1;
        int an_ = 1901;

        for(mois_=1; mois_<=12; mois_++){
            for (an_=1901; an_<2001; an_++){
                p19 d = new p19(1, mois_, an_);

                if(p19.semaine[d.numJourDeLaSemaine()].equals("dimanche")){
                    System.out.println(p19.semaine[d.numJourDeLaSemaine()]+" "+1+"er "+p19.months[mois_-1]+" "+an_);
                    count+=1;
                }
            }
        }
        
        
        return count;
    }

    
    //Attributs de ma classe
    public int jour;
    public int mois;
    public int an;
    public final static p19 mardi010102=new p19(1,1,2002);
    public final static String[] semaine={"dimanche", "lundi", "mardi", "mercredi","jeudi", "vendredi", "samedi"};
    public final static String[] months = {"Janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"};
}
