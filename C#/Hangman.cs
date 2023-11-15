using System;
using System.Collections.Generic;
using System.Text;  // Include this namespace for StringBuilder

class Hangman
{
    static void Main(string[] args)
    {
        string[] wordBank = { "apple", "banana", "cherry", "date", "elderberry" };
        var random = new Random();
        string wordToGuess = wordBank[random.Next(wordBank.Length)];
        string wordToGuessUppercase = wordToGuess.ToUpper();

        StringBuilder displayToPlayer = new StringBuilder(wordToGuess.Length);
        for (int i = 0; i < wordToGuess.Length; i++)
            displayToPlayer.Append('_');

        List<char> correctGuesses = new List<char>();
        List<char> incorrectGuesses = new List<char>();

        int lives = 5;
        bool won = false;
        int lettersRevealed = 0;

        string input;
        char guess;

        while (!won && lives > 0)
        {
            Console.Write("Guess a letter: ");
            input = Console.ReadLine().ToUpper();

            if (string.IsNullOrEmpty(input) || input.Length > 1)
            {
                Console.WriteLine("Please enter a single letter.");
                continue;
            }

            guess = input[0];

            if (correctGuesses.Contains(guess) || incorrectGuesses.Contains(guess))
            {
                Console.WriteLine("You've already tried '{0}', and it was incorrect.", guess);
                continue;
            }

            if (wordToGuessUppercase.Contains(guess))
            {
                correctGuesses.Add(guess);

                for (int i = 0; i < wordToGuess.Length; i++)
                {
                    if (wordToGuessUppercase[i] == guess)
                    {
                        displayToPlayer[i] = wordToGuess[i];
                        lettersRevealed++;
                    }
                }

                if (lettersRevealed == wordToGuess.Length)
                    won = true;
            }
            else
            {
                incorrectGuesses.Add(guess);

                Console.WriteLine("Nope, there's no '{0}' in it!", guess);
                lives--;
            }

            Console.WriteLine(displayToPlayer.ToString());
        }

        if (won)
            Console.WriteLine("You won!");
        else
            Console.WriteLine("You lost! The word was '{0}'", wordToGuess);
    }
}
