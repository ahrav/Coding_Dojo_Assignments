using System;

namespace wizard_ninja_samurai{
    public class Human
    {
        public string name;

        //The { get; set; } format creates accessor methods for the field specified
        //This is done to allow flexibility
        public int health { get; set; }
        public int strength { get; set; }
        public int intelligence { get; set; }
        public int dexterity { get; set; }

        public Human(string person)
        {
            name = person;
            strength = 3;
            intelligence = 3;
            dexterity = 3;
            health = 100;
        }
        public Human(string person, int str, int intel, int dex, int hp)
        {
            name = person;
            strength = str;
            intelligence = intel;
            dexterity = dex;
            health = hp;
        }
        public void attack(object obj)
        {
            Human enemy = obj as Human;
            if(enemy == null)
            {
                Console.WriteLine("Failed Attack");
            }
            else
            {
                enemy.health -= strength * 5;
            }
        }
    }

    public class Wizard : Human
    {

        public Wizard(string person) : base(person)
        {
            health = 50;
            intelligence = 25;
        }

        public void Heal()
        {
            health += 10 * intelligence;
        }
        public void FireBall(object target)
        {
            Human enemy = target as Human;
            if(enemy == null)
            {
                Console.WriteLine("failed attack!");
            }
            else
            {
                Random rand = new Random();
                enemy.health -= rand.Next(20,50);
            }
        }
    }
    public class Ninja : Human
    {

        public Ninja(string person) : base(person)
        {
            dexterity = 175;
        }

        public void Steal(object target)
        {
            Human enemy = target as Human;
            if(enemy == null)
            {
                Console.WriteLine("Failed attack!");
            }
            else
            {
                attack(enemy);
                health += 10;
            }
        }
        public void GetAway()
        {
            health -= 15;
        }

    }

    public class Samurai : Human
    {

        public Samurai(string person) : base(person)
        {
            health = 200;
        }

        public void DeathBlow(object target)
        {
            Human enemy = target as Human;
            if(enemy.health <= 50)
            {
                enemy.health = 0;
            }
            else{
                Console.WriteLine("Attack failed");
            }
        }
        public void Meditate()
        {
            health = 200;
        }
    }
}