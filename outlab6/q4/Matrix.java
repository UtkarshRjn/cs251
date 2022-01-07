public class Matrix
{

	private float[][] mat;
	private int num_rows, num_columns;

	public Matrix(int n, float v){
		mat = new float[n][n];
		num_rows = n;
		num_columns = n;
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				mat[i][j] = v;
			}
		}
	}

	public Matrix(int n, int m, float v){
		mat = new float[n][m];
		num_rows = n;
		num_columns = m;
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				mat[i][j] = v;
			}
		}	
	}

	public Matrix(int n, int m){
		mat = new float[n][m];
		num_rows = n;
		num_columns = m;		
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				mat[i][j] = 0f;
			}
		}	
	}  

	public Matrix(int n){
		mat = new float[n][n];
		num_rows = n;
		num_columns = n;
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				mat[i][j] = 0f;
			}
		}		
	}

	public Matrix add(Matrix arg_mat){
		if(num_rows == arg_mat.getrows() && num_columns == arg_mat.getcols()){
			Matrix result_mat = new Matrix(num_rows,num_columns);
			for(int i = 0; i < num_rows; i++) {
        		for(int j = 0; j < num_columns; j++) {
           			result_mat.mat[i][j] = mat[i][j] + arg_mat.mat[i][j];
        		}
    		}
    		return result_mat;
		}
		else{
			System.out.println("Matrices cannot be added");
			Matrix result_mat = new Matrix(1);
			return result_mat;
		}
	}

	public Matrix matmul(Matrix arg_mat){
		if(num_columns == arg_mat.getrows()){
			Matrix result_mat = new Matrix(num_rows,arg_mat.getcols());
			for(int i=0;i< num_rows;i++){
				for(int j=0;j<arg_mat.getcols();j++){
					float sum = 0f;
					for(int k=0;k<num_columns;k++){
						sum += getelem(i,k)*arg_mat.getelem(k,j);
					}
					result_mat.setelem(i,j,sum);
				}
			}
			return result_mat;
		}
		else{
			System.out.println("Matrices cannot be multiplied");
			Matrix result_mat = new Matrix(1);
			return result_mat;	
		}
	}

	public void scalarmul(int f){
		for(int i = 0; i < num_rows; i++) {
        	for(int j = 0; j < num_columns; j++) {
           		mat[i][j] *= f;
        	}
    	}
	}

	public int getrows(){ return num_rows;}
	public int getcols(){ return num_columns;}

	public float getelem(int i, int j){

		if(i>=num_rows || j>=num_columns){
			System.out.println("Index out of bound");
			return -100f;
		}
		return mat[i][j];
	}

	public void setelem(int i,int j, float v){
		
		if(i>=num_rows || j>=num_columns){
			System.out.println("Index out of bound");
			return;
		}
		mat[i][j] = v;
	}

	public void printmatrix(){
		for(int i = 0; i < num_rows; i++) {
        	for(int j = 0; j < num_columns; j++) {
           		if(j==num_columns-1) System.out.print(mat[i][j]); 
        		else System.out.print(mat[i][j]+" ");
        	}
        	System.out.println();
    	}
	}	
}
