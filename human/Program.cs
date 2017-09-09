using System;

namespace human
{
    public class Human
    {
        public string name;
        public int strength;
        public int intelligence;
        public int dexterity;
        public int health;

        public Human(string val)
        {
            strength = 3;
            intelligence = 3;
            dexterity = 3;
            health = 100;
            name = val;
        }

        public Human(int str, int intel, int dext, int life, string val)
        {
            strength = str;
            intelligence = intel;
            dexterity = dext;
            health = life;
            name = val;
        }

        public void Attack(object target)
        {
            Human enemy = target as Human;
            if (enemy != null)
            {
                enemy.health -= 5 * strength;
            }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Human ahrav = new Human(4,6,7,100,"ahrav");
            Human loser = new Human(3,2,2,100,"loser");
            Console.WriteLine(ahrav.name);
            Console.WriteLine(loser.name);
            Console.WriteLine(loser.health);
            ahrav.Attack(loser);
            Console.WriteLine(loser.health);
        }
    }
}
}
