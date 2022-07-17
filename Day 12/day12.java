package competetive.prog;

import java.io.File;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

/**
 *
 * @author thiru
 */
public class passagepathingp1 {
    
    private static HashMap<String, ArrayList<String>> adjacencyList;

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        adjacencyList = new HashMap<String, ArrayList<String>>();
        
        try {
            File f = new File("C:\\Users\\thiru\\Documents\\NetBeansProjects\\Competetive Prog\\src\\competetive\\prog\\input.txt");
            Scanner reader = new Scanner(f);
            while (reader.hasNextLine()) {
                String[] data = reader.nextLine().split("-");
                
                if (!adjacencyList.containsKey(data[0])) {
                    adjacencyList.put(data[0], new ArrayList<String>());
                }
                if (!adjacencyList.containsKey(data[1])) {
                    adjacencyList.put(data[1], new ArrayList<String>());
                }
                adjacencyList.get(data[0]).add(data[1]);
                if (!data[0].equals("start")) {
                    adjacencyList.get(data[1]).add(data[0]);
                }
                    
            }
            reader.close();
        } catch (Exception e) {
            System.out.println("an unexpected error occured");
        }
        
        ArrayList<String> path = new ArrayList<String>();
        path.add("start");
        
        HashMap<String, Boolean> seen = new HashMap<String, Boolean>();
        seen.put("start", true);
        
        System.out.println(find("start", path, seen));
        
    }
    
    public static int find(String point, ArrayList<String> path, HashMap<String, Boolean> seen) {
        int paths = 0;
        
        if (point.equals("end")) {
//            for (String s : path) {
//                System.out.print(s + " ");
//            }
//            System.out.println();
            return 1;
        }
        
        ArrayList<String> vistablePoints = adjacencyList.get(point);
        
        for (String p : vistablePoints) {
            ArrayList<String> new_path = (ArrayList)path.clone();
            HashMap<String, Boolean> new_seen = (HashMap)seen.clone();
            
            if (seen.containsKey(p)) {
                if (p.equals(p.toUpperCase())) {
                    new_path.add(p);
                    new_seen.put(p, true);
                    paths += find(p, new_path, new_seen);
                }
            } else {
                new_path.add(p);
                new_seen.put(p, true);
                paths += find(p, new_path, new_seen);
            }
        }
        return paths;
        
    }
    
}
