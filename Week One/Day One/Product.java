
public class Product {

    public static int[] getProduct(int[] a) {
        int l = a.length;
        int prod[] = new int[l];
        
        if (a.length < 2) {
        throw new IllegalArgumentException("Minimum 2 integers are required");
        }
        
        int mul = 1	;
        for (int i=0; i < l; i++)
        {
        	prod[i] = mul;
        	mul *= a[i];
        }
        
        mul = 1;
        for (int i= l-1; i>0; i--)
        {
        	prod[i] *= mul;
        	mul *= a[i];
        }
        prod[0] *= mul;
        
        return prod;
    }
}
