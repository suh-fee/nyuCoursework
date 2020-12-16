/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.javafinalq1;

import java.awt.*;
import java.awt.Graphics;
import java.awt.event.MouseAdapter;
import javax.swing.*;
import java.util.*;
import java.awt.event.MouseEvent;
import java.text.NumberFormat;

//i wasn't able to run the provided .jar file prof. katz gave us,
//so i had to eyeball the grid size/window size from the provided screenshots.
//the actual way the code works though should match up nearly identically to the example
//in regards to the way lines are drawn, points are drawn, and the distnaces calculated



public class questionOne{
   
    public static JFrame jf = new JFrame("Question One");
    
    public static void main(String[] args) {
        
        jf.setSize(400,400);
        jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        DrawingGrid mp = new DrawingGrid();
        jf.add(mp);
        
        //listener to see if buttons are clicked
        mp.addMouseListener(new MouseAdapter(){ 
            public void mousePressed(MouseEvent m){

                if (m.getButton()==MouseEvent.BUTTON1){
                    MyPoint p = new MyPoint(m.getX(),m.getY());
                    mp.addPoint(p);
                    mp.repaint();
                }

            }
        });
        
        jf.setVisible(true);
    }

    
    
    
}

class MyPoint{
    int x;
    int y;
    MyPoint(int newx, int newy){x = newx; y=newy;}
    MyPoint(){this(0,0);}
}

class DrawingGrid extends JPanel{
    ArrayList<MyPoint> pointsClicked; // stores every point the user clicks on
    final int size=5; // size of the dots showing where the user clicked
    
    DrawingGrid(){
        
        super();
        pointsClicked = new ArrayList<MyPoint>(); 
    }
    
    
    void addPoint(MyPoint p){ pointsClicked.add(p);} // adds a point to pointsClicked
    
    void clearList(){pointsClicked.clear(); this.repaint();} // deletes all points, repaints
    
    private void drawGrid(Graphics g){ // draws the grid
        
        Rectangle r = questionOne.jf.getBounds();
        int height = r.height;
        int width = r.width;
                
                
        g.setColor(Color.black);  
        
        for(int i = 0; i <= height; i += height/10){
            g.drawLine(0, i, width, i);
        }
        
        for(int i = 0; i <= width; i += width/10){
            g.drawLine(i, 0, i, height);
        }
        
        
    }
    
    @Override
    protected void paintComponent(Graphics g){
        

        super.paintComponent(g);
        drawGrid(g); // sets up the grid
        
        g.setColor(Color.RED);
        int x;
        int y;
        int x2;
        int y2;
        //set up for distance calculation
        NumberFormat nf = NumberFormat.getInstance();
        nf.setMaximumFractionDigits(2); // exactly two decimal degits will be represented each time for distance
        nf.setMinimumFractionDigits(2);
        
        //iterates through each point in the array
        for(int i = 0; i < pointsClicked.size(); i++){
            x = pointsClicked.get(i).x;
            y = pointsClicked.get(i).y;
            
            
            // for the current point, draw the circle representing it
            g.fillOval(x - size/2, y - size/2, size, size);
            
            //draws the coordinates
            g.drawString("(" + x + "," + y + ")", x + size, y + size);

            // if there'sa point after the one we're looking at, draws a line to that
            // specific point and draws its distance
            if(i + 1 < pointsClicked.size()){
                
                x2 = pointsClicked.get(i+1).x;
                y2 = pointsClicked.get(i+1).y;
                
                g.drawLine(x,y,x2,y2);
                double dist = getDistance(x,y,x2,y2);

                String distStr = nf.format(dist); // turns the double into a string w/ 2 decimal places
                
                
                g.drawString(distStr, (x+x2)/2 + 5 , (y+y2)/2 - 5 ); 
                // draws the distance at the mid point between the two and at a slight offset to match example
                
            }
            
        }
        
    }
    
    //helper function to get distance between two points
    // not really needed, but looks nicer
    public double getDistance(int x, int y, int x2, int y2){
        double temp = ((x2-x) * (x2-x) + (y2 - y) * (y2-y));
        return Math.sqrt(temp);
    }
    
    
}




