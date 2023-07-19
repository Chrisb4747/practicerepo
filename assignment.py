{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "Checking for ingredients... Not enough ingridients for pancakes, go buy more!\n",
      "The supermarket is open you may proceed to buying the ingredients!\n"
     ]
    }
   ],
   "source": [
    "\n",
    "#User should Enter ingridients they would like to use for a pancake, the boolean generator will give either a true of false statement  \n",
    "#if true the user will be given a list of their ingriedients entered with instructions on how to make pancakes\n",
    "#if false the user will be prompted to enter a time, this time will indicate whether the user can go to the store or not based on its closing time (18:00)\n",
    "\n",
    "import random\n",
    "import timemodule as mod #shortening the timemodule file to mod \n",
    "\n",
    "wheat   = str(input(\"Enter the wheat product you want to use (Flour, protein powder...)\")) #allowing the user to input string which will be stored as a variable \n",
    "liquid  = str(input(\"Enter the liquid you want to use for your pancakes (Milk...)\"))\n",
    "food    = str(input(\"Enter the protein you want to use for your pancakes (Eggs, Buttermilk..) \"))\n",
    "fruit   = str(input(\"What food would you like as a topping? (Strawberries, berries...)\"))\n",
    "pan     = str(input(\"What would you like to cook the pancakes on? (Pot, pan, skillet...)\"))\n",
    "\n",
    "\n",
    "def print_text():\n",
    "    print(\"Lets make some pancakes\")   \n",
    "\n",
    "def cook(liquid, wheat, food, fruit, pan):\n",
    "   \n",
    "    print(\"Pour 300ml of\", liquid)\n",
    "    print(\"put 100g of\", wheat)\n",
    "    print(\"Crack two\", food)\n",
    "    print(\"Whisk until you have a thick batter, then pour into\", pan)\n",
    "    print(\"Add a topping of\", fruit)\n",
    "\n",
    "random_output =  random.choice([True, False]) \n",
    "print(random_output)\n",
    "if random_output == True : #if the answer is true it will call the function or else print the next text\n",
    "    print_text()\n",
    "    cook(liquid.title(), wheat.title(), food.title(), fruit.title(), pan.title()) #calling the function that has the users inputs\n",
    "else:\n",
    "    print(\"Checking for ingredients... Not enough ingridients for pancakes, go buy more!\")\n",
    "    mod.time_function() #calling the time_function from the timemodule file\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
