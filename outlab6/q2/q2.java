import java.util.*;
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;

public class q2
{
    public static void main(String[] args)
    {
       try {
            File file = new File(args[0]);  
            FileReader fr = new FileReader(file);
            BufferedReader br = new BufferedReader(fr); 
            StringBuffer sb= new StringBuffer();    
            String line;
            Path fileName = Path.of("./output.txt");

            while((line=br.readLine())!=null){ 
                
                
                HashMap<String, Integer> map = new HashMap<> ();  

                String lower_line = line.toLowerCase();
                for (int i=0; i < lower_line.length(); i++){
                    char c = lower_line.charAt(i);
                    if(c >= 'a' && c <= 'z'){
                        Integer f = map.get(Character.toString(c));
                        if(f == null) f = 0;
                        map.put(Character.toString(c),f+1);
                    }
                }

                TreeMap<String, Integer> sorted = new TreeMap<> ();  

                int maxValueInMap=(Collections.max(map.values()));  
                for (Map.Entry<String, Integer> entry : map.entrySet()) {  
                    if (entry.getValue()== maxValueInMap) {
                        sorted.put(entry.getKey(),entry.getValue());     
                    }
                }
                for (Map.Entry<String, Integer> entry : sorted.entrySet()) {  
                    if (entry.getKey() == sorted.lastEntry().getKey()) {
                        sb.append(entry.getKey()+"="+entry.getValue());    
                    }else{
                        sb.append(entry.getKey()+"="+entry.getValue()+",");    
                    }
                }
                sb.append("\n");

            }
            fr.close();   
            Files.writeString(fileName, sb);
        }  
        catch(IOException e){  
            e.printStackTrace();  
        }  

    }
}
