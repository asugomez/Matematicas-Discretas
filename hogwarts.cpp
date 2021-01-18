#include <bits/stdc++.h>
using namespace std;
typedef vector<int> vi; //cada nodo guarda un vector con los numeros que corresponden a los magos dentro del cuarto
typedef pair<int, int> ii; //vector que contenga el nro del mago y su tiempo
typedef vector<ii> vii; //vector de pares
typedef vector<vii> wgraph; //vector de vector de pares --> en la posicion k se encuentran todos los pares a los q puede llegar

void Dijsktra(int s, wgraph &M, vector<long long> &dist, vi &p) {
	dist[s] = 0;
	priority_queue<ii, vii, greater<ii> > pq; pq.push(ii(0, s));

	while (!pq.empty()) {
		ii front = pq.top(); pq.pop();
		int d = front.first, u = front.second;
		if (d > dist[u]) continue;

		for (int j = 0; j < M[u].size(); j++) {
			ii v = M[u][j];
			if (dist[u] + v.first < dist[v.second]) {
				dist[v.second] = dist[u] + v.first;
				pq.push(ii(dist[v.second], v.second));
				p[v.second] = u;
			}
		}
	}
}

int main(){
    int n,t;
    cin>>n;//nro de magos
    vector<long long> dists(n+1, LLONG_MAX); //distancias maximas en un principio para todos los nodos (costos de tiempo)
    int s = 1;
    vi tiempo(n+1,INT_MAX); //Vector en que cada indice corresponde a un mago y contenga su tiempo
    wgraph graph(n+1); 
    vi p(n+1, 0);
    for(int i=0;i<n;i++){ 
        cin>>t; //el tiempo de cada nodo
        tiempo[i]=t;        //tiempo minimo entre los magos que se encuenran en el arreglo (cuarto)
    }
    //----------no logro definir bien el grafo uwu-----------
    for(int i=0;i<n;i++){
    	//costo entre el mago i y el mago j
        for(int j=0;j<n;j++){
	    	graph[i].push_back(pair<int, int>(j, max(tiempo[i],tiempo[j]))); //par arreglo de mago con su costo en tiempo
	    	graph[j].push_back(pair<int, int>(i, max(tiempo[i],tiempo[j]))); //par arreglo de mago con su costo en tiempo
	    }
    }

    Dijsktra(s, graph, dists, p);

    int i = n;
    vector<int> path;
    while (p[i]!=0){
        path.push_back(i);
        i = p[i];
    }

    int costo=0;

    if(path.size() == 0)
        cout<<-1<<"\n";
    else{
        //cout<<1<<" ";
        for(int j=path.size(); j>=0; j--){
        	//costo segun el camino
        	costo=costo+dists[path[j]-1];//graph[path[j]][j](1);
        }
        cout<<"\n";
    } 
}
