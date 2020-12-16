/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author safi_hasani
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 */

import java.io.*;
import java.net.*;
import java.util.*;

public class homework4 {
    static int portNum=5190;
    static List<Socket> listClients = new ArrayList();
    public static void main(String[] args) {
        ServerSocket ss = null;
        int id=0;
        try{
            ss = new ServerSocket(portNum);
            System.out.println("Waiting for connections on port number: "+portNum);
            while (true){
                Socket client = ss.accept(); //Program will wait here for a LONG time!
                listClients.add(client);
                new ProcessConnection(id++,client).start();
            }

        }
        catch(IOException e){ System.out.println("IOError: "+e.toString());}
    }
}


class ProcessConnection extends Thread{
    int id;
    Socket client;
    ProcessConnection(int newid, Socket newclient){id=newid; client=newclient;}
    public void run(){
        try{
            System.out.println("Connection from: " +client.getInetAddress().toString()+" client "+id);
            PrintStream sout = new PrintStream(client.getOutputStream());
            Scanner sin = new Scanner(client.getInputStream());
            
            
            


            sout.print("Please enter your username. \r\n");
            
            
            
            

            

            String user = "";
            String line = "";
            
            while (!"EXIT".equals(line)){

                if(sin.hasNext()){
                    line = sin.nextLine();

                    
                    if(user == ""){
                        user = line;
                        sout.print("Welcome to the chatroom!\r\n");
                    } else {
                        System.out.println("Client ("+id+") Said: "+line);
                        for(Socket client : homework4.listClients){
                          new PrintStream(client.getOutputStream()).print(user + ": " + line + "\r\n");
                        }
                    } 
                }

            }

            sout.print("Goodbye!\r\n");
            System.out.println("Client ("+id+" Disconnected");
            client.close();
        }
        catch(IOException e){

        }
    }
}