using System;
using System.Collections.Generic;
using System.Linq;
using JsonData;
// Good work Ahrav.  Hope it was a nice eye-opener for a different way to do queries.
namespace ConsoleApplication
{
    public class Program
    {
        public static void Main(string[] args)
        {
            //Collections to work with
            List<Artist> Artists = JsonToFile<Artist>.ReadJson();
            List<Group> Groups = JsonToFile<Group>.ReadJson();

            //========================================================
            //Solve all of the prompts below using various LINQ queries
            //========================================================

            //There is only one artist in this collection from Mount Vernon, what is their name and age?
            var artist = from match in Artists
                        where match.Hometown == "Mount Vernon"
                        select new {match.ArtistName, match.Age};

            foreach (var item in artist)
            {
                Console.WriteLine(item);
            }
            //Who is the youngest artist in our collection of artists?
            Artist YoungestArtist = Artists.OrderBy(youngestArtist => youngestArtist.Age)
                                            .First();
            Console.WriteLine(YoungestArtist.RealName);
            //Display all artists with 'William' somewhere in their real name
            List<Artist> NamesWithWilliam = Artists.Where(myArtist => myArtist.RealName.Contains("William")).ToList();
            foreach (var user in NamesWithWilliam)
            {
                Console.WriteLine(user.RealName);
            }
            //Display the 3 oldest artist from Atlanta
            List<Artist> OldestArtists = Artists.OrderByDescending(myArtist => myArtist.Age)
                                                .Take(3).ToList();
            foreach (var myArtist in OldestArtists)
            {
                Console.WriteLine(myArtist.ArtistName);
            }
            //(Optional) Display the Group Name of all groups that have members that are not from New York City

            //(Optional) Display the artist names of all members of the group 'Wu-Tang Clan'
        }
    }
}
