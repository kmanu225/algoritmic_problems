public class App {
    public App(){
    }

// nombre de sommets dans le graphe
int n=4;
 
// matrice d'adjacence du graphe 
int[][] adjacencymatrix = new int[][] {
	new int[] {0,1,1,0}, //    1
	new int[] {0,0,0,0}, //  / | \
	new int[] {0,0,2,1}, // 0  |  3 - 4
	new int[] {1,1,0,0}, //  \ | /
	                       //    2
};

// stockage du chemin pendant l'exploration recursive
int[] path = new int[n];
 
// verrou pour la recherche taboo (tous initialisés à "false" par défaut)
boolean[] taboo = new boolean[n];
 
// sommets de départ/arrivé souhaités
int source=0;
int target=1;

void explore(int position, int depth) {
	path[depth]=position+1;

 
	// on est sur le sommet d'arrivé -> fini
	if (position==target) {
		// affiche la solution
		for(int i=0;i<=depth;i++) System.out.print(path[i]+" ");
		System.out.print("\n");
		return;
	}
 
	// sinon...
 
	taboo[position]=true; // on pose un caillou
 
	// on explore les chemins restants
	for(int i=0;i<n;i++) {
		if (adjacencymatrix[position][i]==0 || taboo[i]) continue;
		explore(i,depth+1);
	}
 
	taboo[position]=false; // on retire le caillou
}

}
