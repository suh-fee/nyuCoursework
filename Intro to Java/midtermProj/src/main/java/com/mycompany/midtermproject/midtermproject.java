package com.mycompany.midtermproject;

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



public class midtermproject {
    public static int counter = 0; // can be changed to instead be set to user input, for larger sets of buttons

    public static JFrame jf = new JFrame("Midterm Project");
    public static Question[] questions = new Question[6];
    public static String answer = "";
    public static JPanel curr;
    public static JButton answer1;
    public static JButton answer2;
    public static JButton answer3;
    public static JLabel question;
    public static Timer time;
    
    public static void main(String[] args) {
        jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        jf.setSize(900,900);
        time = new Timer(5000, new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent ae) {
                counter += 1;
                if(counter < 5){
                    answer += "NO RESPONSE, ";
                    answer1.setText(questions[counter].left);
                    answer2.setText(questions[midtermproject.counter].right);
                    question.setText(questions[midtermproject.counter].question);
                }
                
            }
        });
        
        questions[0] = new Question("Favorite ice cream?", "Vanilla", "Chocolate");
        questions[1] = new Question("Which season is better?", "Winter", "Summer");
        questions[2] = new Question("Which pet is better?", "Cat", "Dog");
        questions[3] = new Question("Unicorns are real.");       
        questions[4] = new Question("Text or call?", "Text", "Call");
        questions[5] = new Question(answer);

        question = new JLabel(questions[0].question);
        answer1 = new JButton(questions[0].left);
        answer2 = new JButton(questions[0].right);
        answer1.addActionListener(new ButtonListener(0));
        answer2.addActionListener(new ButtonListener(1));
        
        answer3 = new JButton();
        answer3.addActionListener(new ButtonListener(2));
        
        
        curr = new JPanel(new GridLayout(3,3,2,2));
        curr.add(question);
        curr.add(new JLabel());
        curr.add(new JLabel());
        curr.add(new JLabel());
        curr.add(new JLabel());
        curr.add(new JLabel());
        curr.add(answer1);
        curr.add(new JLabel());
        curr.add(answer2);
        
        
        jf.add(curr);
        time.start();
        
        
        jf.setVisible(true);
        
        
    }
    

}

class Question{
    String left = "True";
    String right = "False";
    String question;
    String answer = "NO RESPONSE";
    
    public Question(String q, String l, String r){
        left = l;
        right = r;
        question = q;

    }
    
    public Question(String q){
        question = q;

    }
    
    public void answer(String a){
        answer = a;
    }
   
}

class ButtonListener implements ActionListener{

    int buttonVal;

    public ButtonListener(int i){ 
        // when a button is constructed, the listener has a data member that
        // saves the index of the button in the array of buttons
        buttonVal = i;

    }
    
    @Override
    public void actionPerformed(ActionEvent arg0) {
        midtermproject.time.restart();
        
        if(midtermproject.counter < 5){
            if (buttonVal==0){
            midtermproject.answer += midtermproject.questions[midtermproject.counter].left + ", ";
            } else {
                midtermproject.answer += midtermproject.questions[midtermproject.counter].right + ", ";
            }
            midtermproject.questions[5] = new Question(midtermproject.answer);
            midtermproject.counter++;
            midtermproject.answer1.setText(midtermproject.questions[midtermproject.counter].left);
            midtermproject.answer2.setText(midtermproject.questions[midtermproject.counter].right);
            midtermproject.question.setText(midtermproject.questions[midtermproject.counter].question);
        } else {
            
            midtermproject.question.setText(midtermproject.answer);
        }

    }

}

