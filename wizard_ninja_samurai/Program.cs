using System;

namespace wizard_ninja_samurai
{
    class Program
    {
        static void Main(string[] args)
        {
            Human loser = new Human("loser");
            Ninja ninja = new Ninja("ninja man");
            Wizard wizard = new Wizard("wizard man");
            Samurai samurai = new Samurai("samurai man");
            Console.WriteLine(loser.name);
            Console.WriteLine(ninja.name);
            Console.WriteLine(wizard.name);
            Console.WriteLine(samurai.name);
            ninja.Steal(loser);
            Console.WriteLine(loser.health);
            wizard.FireBall(loser);
            wizard.FireBall(loser);
            Console.WriteLine(loser.health);
            samurai.DeathBlow(loser);
            Console.WriteLine(loser.health);
        }
    }
}
