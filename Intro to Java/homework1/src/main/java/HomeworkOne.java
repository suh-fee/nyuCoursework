
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author safi_hasani
 */


class Ingredient{
    String name;
    double amount;
    public Ingredient(){
        this.name = "null";
        this.amount = 0;
    }
    
    public Ingredient(String inpName, double inpAmount){
        this.name = inpName;
        this.amount = inpAmount;
    }
    
    public String toString(){
        String retString =  String.valueOf(this.amount) + " units of " + this.name;
        return retString;
    }
    
}

class IngredientList{
    Ingredient ingredients[] = new Ingredient[20];
    int size = 0;
    
    public boolean addIngredient(Ingredient x){
        if(size == 20){
            return false;
        }
        
        this.ingredients[this.size] = x;
        this.size++;
        
        return true;
    }
    
    public String toString(){
        String retString = "";
        for(int i = 0; i < this.size; i++){
            retString += this.ingredients[i].toString() + "\r\n";
        }
        return retString;
    }      
}
    
    


class Recipe{
    IngredientList ingredients = new IngredientList();
    String steps[] = new String[20];
    int stepSize = 0;
    String name;
    
    public Recipe(String inpString){
        this.name = inpString;
    }
    
    public boolean addIng(Ingredient inpIng){
        return this.ingredients.addIngredient(inpIng);
    }
    
    public boolean addStep(String inpStr){
        if(this.stepSize == 20){
            return false;
        }
        this.steps[this.stepSize] = inpStr;
        this.stepSize++;
        return true;
    }
    
    public String toString(){
        String retStr = "";
        for(int i = 0; i < stepSize; i++){
            retStr += steps[i] + "\r\n";
        }
        retStr += "\r\n";
        
        retStr += this.ingredients.toString();
        
        return retStr;
    }
}


    
public class HomeworkOne {
    public static void main(String[] args){
        Recipe rec = new Recipe("Scrambled Eggs");
        Ingredient eggs = new Ingredient("Eggs", 2);
        Ingredient butter = new Ingredient("Butter", 3);
        Ingredient sugar = new Ingredient("Seasoning", 4);
        
        rec.addIng(eggs);
        rec.addIng(butter);
        rec.addIng(sugar);
        rec.addStep("Crack eggs into bowl.");
        rec.addStep("Add butter to heated pan.");
        rec.addStep("Beat eggs to scramble.");
        rec.addStep("Put eggs in pan with seasoning and cook.");
        System.out.println(rec.toString());
    }
}

    

