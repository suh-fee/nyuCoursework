/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author safi_hasani
 */

import java.sql.*;
import java.io.*;
import java.util.*;
import java.util.Map.Entry;




public class questionTwo {
    static class Review{
        public int pid;
        public String name;
        public float avgRating;
        public int numRatings = 0;
        public int totalScore = 0;
        
        Review(int ipid, String iname){name = iname; pid=ipid;}
        Review(){this(0, "None");
            }
        
        
        }
    
    static class SortByKey implements Comparator<Review>{ // needed for sorting the array of reviews
        public int compare(Review a, Review b){
            return Float.compare(a.avgRating, b.avgRating);
        }
    }
    public static void main(String[] args) {
        Connection conn = null;
        ArrayList<Review>  finReviews = new ArrayList<Review>();
        
        try{
 
            String url = "localhost";
            String dbuser="CS3913";
            String password = "GettingAnA+";
            
            conn = DriverManager.getConnection(url,dbuser,password);

            
            Statement s = conn.createStatement();
            ResultSet products = s.executeQuery("select * from Products;");
            
            // add all products to the array of products w/ an initial max rating of 0
            
            while (products.next()){
                int id = products.getInt("PID"); // Get the ID number
                String name = products.getString("ProductName");
                finReviews.add(new Review(id, name));
            }
            
            products.close();
            
 
            // for each product, find all reviews
            for(Review r : finReviews){
                ResultSet reviews = s.executeQuery("select Rating from Reviews where PID=" + Integer.toString(r.pid));
                
                //look at each review, compare it to the max rating held for that product, update if necessary 
                while (reviews.next()){

                    int rating = products.getInt("Rating"); // Get the ID number
                    
                    r.totalScore += rating;
                    r.numRatings += 1;
             
                    r.avgRating = r.totalScore / r.numRatings;
                    
                }
                
                reviews.close(); //not the cleanest, but can't find a way to close after the loop without errors
                // because reviews isn't initialized if there are no reviews (edge case)
            }
            
    
            
            
            s.close();
            conn.close();

            
            Collections.sort(finReviews, new SortByKey()); // sorts the linked list of revies by the avg rating
            
            for(int i = finReviews.size() - 1; i >= 0; i--){ //goes through the array backwards, as the highest review must be printed first
                System.out.println(finReviews.get(i).name);
            }
            


            
            
            
            
            
        }
        catch (Exception e){System.out.println("Error: "+e.toString());}
    }
    
}

