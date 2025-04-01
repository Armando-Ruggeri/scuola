public class Albero {
    private Nodo radice;

    public Albero (Nodo n){
        radice = n;
    }

    public Albero (int n){
        radice = new Nodo(n);
    }

    public void add(int n){
        insert(radice, new Nodo(n));
    }
    public void insert(Nodo radice, Nodo n){
        if (radice == null)
            radice = n;

        if (radice.getValore()> n.getValore())
            insert(radice.getSx(), n);
        else
            insert(radice.getDx(), n);       
    }


    public void stampa(){
        stampa2(radice);
    }

    public void stampa2( Nodo n){
        if (n!= null){
            stampa2(n.getSx());
            System.out.println(n.getValore());
            stampa2(n.getDx());
        }        
    }


    public static void main(String[] args){
        Albero alb = new Albero (20);

        alb.add(10);
        alb.add(6);
        alb.add(15);

        alb.stampa();
    }
}

