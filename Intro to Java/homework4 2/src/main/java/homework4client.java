/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author safi_hasani
 */

import java.io.*;
import java.net.*;
import java.util.*;


public class homework4client {
    public static void main(String[] args) {
        try{
            Socket s = new Socket("localhost",5190);
            if (s.isConnected()){
                Scanner sin = new Scanner(s.getInputStream());
                PrintStream sout = new PrintStream(s.getOutputStream());
                

                while (true){
                    String line = "";
                    
                    line = "Yes\r\n";
                    System.out.println(line);
                    sout.print(line);
                    
                    
                    

                    while(sin.hasNext()){
                        System.out.println(sin.nextLine());
                        System.out.println(line);
                    }

                    
                }
            }
//            if (s.isConnected()){
//                Scanner userInput = new Scanner(System.in);
//                Scanner sin = new Scanner(s.getInputStream());
//                PrintStream sout = new PrintStream(s.getOutputStream());
//                sout.print("");
//
//                while (true){
//                    String line = "";
//                    if(userInput.hasNext()){
//                        line = userInput.nextLine();
//                        System.out.println(line);
//                        sout.print(line);
//                    }
//                    
//                    if(sin.hasNext()){
//                        System.out.println("We got here! " + line);
//                        while(sin.hasNext()){
//                            System.out.println(sin.nextLine());
//                        }
//                    }
//                    
//                    System.out.println(sin.nextLine());
//                        
//                    
//                    
//                }
//            }
            else{
                System.out.println("Socket COnnection Failed!");
            }
        }
        catch(IOException e){
            System.out.println("Welp... that didn't work!");
        }
    }
}
