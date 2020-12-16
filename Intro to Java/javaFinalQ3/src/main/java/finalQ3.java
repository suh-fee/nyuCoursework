/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author safi_hasani
 */

import java.util.*;



public class finalQ3 {

    public static void main(String args[]){
        
        // since we only needed a class definition
        
    }
    
   
}


//it's a simple solution, but it should work
class CafeQueue {

    LinkedList<String> line = new LinkedList<String>();

    public void enterQueue(String newCustomer){
        synchronized(this){ // since only one thread can be in a synchronized block at a time, no two threads will be reading/writing at once
            line.addFirst(newCustomer);
        }
    }
    
    public String serveCustomer(){
        synchronized(this){
            return line.pop();
        }
    }


}

