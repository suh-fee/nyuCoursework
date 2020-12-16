package com.mycompany.homework2;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author safi_hasani
 */

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.Random;

public abstract class Notes {
    static int size = 8; // can be changed to instead be set to user input, for larger sets of buttons
    static JButton[] jbuttons = makeButtons(size); 
    static JPanel jp = new JPanel();
    static JFrame jf = new JFrame("Homework 2");
    
    
    public static void main(String[] args) {
        jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        jf.setSize(1600,900);
        jp.setLayout(new GridLayout(0,4, 2, 2)); // 0 allows the panel to accept larger sets of buttons
        // since the size is set to 8, will create a 4x2 grid
        
        for(int i = 0; i < size; i++){
            jp.add(jbuttons[i]);
        }
        
        jf.add(jp);
        jf.setVisible(true);
        
    }
    
    
    public static JButton[] makeButtons(int size){ // helper function to make buttons and return an array of them
        JButton[] buttons = new JButton[size];
        Random rand = new Random();
        
        for(int i = 0; i < size; i++){
            
            JButton button = new JButton(""+i);
            button.addActionListener(new Button1Listener(i));
            button.setOpaque(true);
            button.setContentAreaFilled(true);
            button.setBorderPainted(false);
            button.setBackground(new Color(rand.nextInt(256),rand.nextInt(256),rand.nextInt(256))); 
            buttons[i] = button;

        }
        return buttons;
    }
}

class Button1Listener implements ActionListener{
    int buttonNum;
    public Button1Listener(int i){ 
        // when a button is constructed, the listener has a data member that
        // saves the index of the button in the array of buttons
        buttonNum = i;
    }
    
    @Override
    public void actionPerformed(ActionEvent arg0) {
        Random rand = new Random();
        for(int i = 0; i < Notes.size; i++){ //
            if(i != buttonNum){ //if the button being looked at isn't the button pressed
                int r = rand.nextInt(256);
                int g = rand.nextInt(256);
                int b = rand.nextInt(256);
                Notes.jbuttons[i].setBackground(new Color(r,g,b));
            }
        } 
}
    
}






