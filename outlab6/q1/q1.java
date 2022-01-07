public class q1
{
    public static void main(String[] args)
    {
        int N = args.length, sum = 0, product = 1;
        for(int i=0;i<args.length;i++){
            int temp = Integer.parseInt(args[i]);
            sum += temp;
            product *= temp;
        }
        
        System.out.println(N+","+sum+","+product);
    }   
}
