# Wordle_solver
How to use the worldle solver:

1) Some notation rules:
    - when inputting the result this is the notation scheme the solver goes by:
      1) Input a "." in the position if that letter is not in the word (i.e. it is a grey tile on the actual game)
      2) Input a lower case letter if the letter is correct but in the wrong position (i.e. it is an orange tile in the actual game)
      3) Input a capital letter if the letter is correct (i.e. it is a green tile in the actual game)
    
2) How to play:
    - run the program and it will prompt you to type this guess into the wordle game
    - after you have received the input type the program will promt to type the result into the program
    - then it will ask you to make a another guess and repeat the above process.
  
Example:

![image](https://user-images.githubusercontent.com/99989709/204924838-5155e36d-ae56-4383-9ce0-6a3f55eeea51.png)
![image](https://user-images.githubusercontent.com/99989709/204924866-a348dca8-bb95-4c1c-8f1d-9aa953024e43.png)

Explanation:

We run the program and the solver tells us to make the guess "RATED" which we type to the worldle game.

We then get the feedback that neither R,T or D are in the word, E is in the word but in the wrong place, and that A is in the correct place.

Thus we type the result as .A.e. (refer to the notation rules for further clarification).

Then we are told to make the guess "EAGLE" and repeat the process until the puzzle is solved!
