package com.mycompany.javamidterm;

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



public abstract class midterm {
    static int size = 8; // can be changed to instead be set to user input, for larger sets of buttons
    static JPanel jp1 = makePanel("Favorite ice cream?", "Vanilla", "Chocolate");
    static JPanel jp2 = makePanel("Which season is better?", "Winter", "Summer");
    static JPanel jp3 = makePanel("Which pet is better?", "Cat", "Dog");
    static JPanel jp4 = makePanel("Unicorns are real.", "True", "False");
    static JPanel jp5 = makePanel("Text or call?", "Text", "Call");
            
    static JPanel jp = new JPanel();
    static JFrame jf = new JFrame("Midterm Project");
    
    
    public static void main(String[] args) {
        jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        jf.setSize(900,900);
        
        
        jf.add(jp1);
        jf.setVisible(true);
        
    }
    
    
    public static JButton[] makeButtons(int size){ // helper function to make buttons and return an array of them
        JButton[] buttons = new JButton[size];
        Random rand = new Random();
        int r;
        int g;
        int b;
        for(int i = 0; i < size; i++){
            
            JButton button = new JButton(""+i);
            button.addActionListener(new ButtonListener("Yes"));
            button.setOpaque(true);
            button.setContentAreaFilled(true);
            button.setBorderPainted(false);
            r = rand.nextInt(256);
            g = rand.nextInt(256);
            b = rand.nextInt(256);
            button.setBackground(new Color(r,g,b)); 
            buttons[i] = button;

        }
        return buttons;
    }
    
    public static JPanel makePanel(String q, String a1, String a2){ // helper function to make the panels
        
        JPanel jp = new JPanel();
        jp.setLayout(new GridLayout(3,3,2,2));
        
        
        JButton answer1 = new JButton(""+ a1);
        answer1.addActionListener(new ButtonListener(a1));
        answer1.setOpaque(true);
        answer1.setContentAreaFilled(true);
        answer1.setBorderPainted(false);
        answer1.setBackground(new Color(0,0,0));
        
        JButton answer2 = new JButton(""+ a2);
        answer2.addActionListener(new ButtonListener(a2));
        answer2.setOpaque(true);
        answer2.setContentAreaFilled(true);
        answer2.setBorderPainted(false);
        answer2.setBackground(new Color(0,0,0));
        
        jp.add(new JLabel(q), 0);
        jp.add(answer1, 6);
        jp.add(answer2, 8);
        

        return jp;
    }
}

class ButtonListener implements ActionListener{
    String buttonVal;
    boolean bool;
    public ButtonListener(String i){ 
        // when a button is constructed, the listener has a data member that
        // saves the index of the button in the array of buttons
        buttonVal = i;
        bool = false;
        
    }
    
    @Override
    public void actionPerformed(ActionEvent arg0) {
        bool = true;
    }
    
}

