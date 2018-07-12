import java.util.*;

class Test4{

	public static int min(int[][] grid) {

		int m=grid.length;
		int n=grid[0].length;
		ArrayList<Integer> c = new ArrayList<Integer>();
		ArrayList<Integer> r = new ArrayList<Integer>();
		for(int i=0; i<m; i++){

			for(int j=0; j<n; j++){

				if(grid[i][j]==1){

					c.add(j);
					r.add(i);
				}
			}
		}
		int sum=0;
		for(Integer i: r){
			sum = sum + Math.abs(i - r.get(r.size()/2));
		}
		Collections.sort(c);
		for(Integer i: c){
			sum = sum + Math.abs(i - c.get(c.size()/2));
		}
		return sum;
	}

	public static void main(String[] args) {

		int a [][] = {{1, 0, 0, 0, 1},{0, 0, 0, 0, 0},{0, 0, 1, 0, 0}};
		System.out.println(min(a));
		int b [][] = {{1, 0, 1, 0, 1},{0, 1, 0, 0, 0},{0, 1, 1, 0, 0}};
		System.out.println(min(b)); 
		int c [][] = {{1,1},{1,1}};
		System.out.println(min(c));
		int d [][] = {{1,0},{0,0}};
		System.out.println(min(d));
		int e [][] = {{0,0},{0,0}};
		System.out.println(min(e));
	}
}
