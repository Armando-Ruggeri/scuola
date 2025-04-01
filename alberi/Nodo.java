public class Nodo {
    private int valore;
    private Nodo sx;
    private Nodo dx;

    public Nodo(){
        valore = 0;
        sx = null;
        dx = null;
    }

    public Nodo(int n){
        valore = n;
        sx = null;
        dx = null;
    }

    public int getValore(){
        return valore;
    }

    public Nodo getSx(){
        return sx;
    }

    public Nodo getDx(){
        return dx;
    }

    public void setSx( Nodo n){
        sx = n;
    }

    public void setDx( Nodo n){
        dx = n;
    }
}
