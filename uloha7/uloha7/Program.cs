using System;
using System.Collections.Generic;

//při tvorbě programu jsem používal chatGPT
//https://chatgpt.com/share/974de3dc-b179-4f38-9028-dda73f071544
//https://chatgpt.com/share/07766dda-1a49-4a05-b677-16f41d146070
namespace DiceGame
{
    class Program
    {
        static void Main(string[] args)
        {
            Game game = new Game(100);

            int numberOfPlayers = 0;
            while (numberOfPlayers < 2 || numberOfPlayers > 5)
            {
                Console.WriteLine("Zadejte počet hráčů (2-5):");
                if (int.TryParse(Console.ReadLine(), out numberOfPlayers))
                {
                    if (numberOfPlayers < 2 || numberOfPlayers > 5)
                    {
                        Console.WriteLine("Neplatný počet hráčů. Zadejte číslo od 2 do 5.");
                    }
                }
                else
                {
                    Console.WriteLine("Neplatný vstup. Zadejte číslo od 2 do 5.");
                }
            }

            for (int i = 1; i <= numberOfPlayers; i++)
            {
                Console.WriteLine($"Zadejte jméno hráče {i}:");
                string playerName = Console.ReadLine();
                game.AddPlayer(playerName);
            }

            game.Start();
        }
    }

    class Player
    {
        public string Name { get; private set; }
        public int Score { get; private set; }

        public Player(string name)
        {
            Name = name;
            Score = 0;
        }

        public void RollDice(Dice dice1, Dice dice2)
        {
            Console.WriteLine($"\n{Name}, stiskněte Enter pro hod kostkami...");
            Console.ReadLine();

            int roll1 = dice1.Roll();
            int roll2 = dice2.Roll();
            Console.WriteLine($"{Name} hodil: {roll1} a {roll2}");
            Dice.DisplayDice(roll1, roll2);

            if (roll1 == 1 && roll2 == 1)
            {
                Score = 0;
                Console.WriteLine($"{Name} ztrácí všechny body!");
            }
            else if (roll1 == 1 || roll2 == 1)
            {
                Console.WriteLine($"{Name} nezískává žádné body tento tah.");
            }
            else
            {
                int roundScore = roll1 + roll2;
                Score += roundScore;
                Console.WriteLine($"{Name} získal {roundScore} bodů, aktuální skóre: {Score}");
            }
        }
    }

    class Dice
    {
        private static Random _random = new Random();

        public int Roll()
        {
            return _random.Next(1, 7);
        }

        public static void DisplayDice(int number1, int number2)
        {
            string[][] dice = new string[6][];
            dice[0] = new string[]
            {
                "-------",
                "|     |",
                "|  *  |",
                "|     |",
                "-------"
            };
            dice[1] = new string[]
            {
                "-------",
                "|*    |",
                "|     |",
                "|    *|",
                "-------"
            };
            dice[2] = new string[]
            {
                "-------",
                "|*    |",
                "|  *  |",
                "|    *|",
                "-------"
            };
            dice[3] = new string[]
            {
                "-------",
                "|*   *|",
                "|     |",
                "|*   *|",
                "-------"
            };
            dice[4] = new string[]
            {
                "-------",
                "|*   *|",
                "|  *  |",
                "|*   *|",
                "-------"
            };
            dice[5] = new string[]
            {
                "-------",
                "|*   *|",
                "|*   *|",
                "|*   *|",
                "-------"
            };

            for (int i = 0; i < 5; i++)
            {
                Console.WriteLine(dice[number1 - 1][i] + " " + dice[number2 - 1][i]);
            }
        }
    }

    class Game
    {
        private List<Player> players;
        private Dice dice1;
        private Dice dice2;
        private int winningScore;

        public Game(int winningScore)
        {
            players = new List<Player>();
            dice1 = new Dice();
            dice2 = new Dice();
            this.winningScore = winningScore;
        }

        public void AddPlayer(string name)
        {
            players.Add(new Player(name));
        }

        public void Start()
        {
            bool gameWon = false;
            int currentPlayerIndex = 0;

            while (!gameWon)
            {
                Console.Clear();
                DisplayScores();

                Player currentPlayer = players[currentPlayerIndex];
                Console.WriteLine($"\n{currentPlayer.Name} je na řadě.");
                currentPlayer.RollDice(dice1, dice2);

                if (currentPlayer.Score >= winningScore)
                {
                    Console.WriteLine($"\n{currentPlayer.Name} vyhrává hru s {currentPlayer.Score} body!");
                    gameWon = true;
                }
                else
                {
                    currentPlayerIndex = (currentPlayerIndex + 1) % players.Count;
                }

                Console.WriteLine("\nStiskněte Enter pro pokračování...");
                Console.ReadLine();
            }
        }

        private void DisplayScores()
        {
            Console.WriteLine("Aktuální skóre:");
            foreach (var player in players)
            {
                Console.WriteLine($"{player.Name}: {player.Score} bodů");
            }
        }
    }
}

