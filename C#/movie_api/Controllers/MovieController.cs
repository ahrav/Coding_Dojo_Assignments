using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using DbConnection;

namespace movie_api.Controllers
{
    public class MovieController : Controller
    {
        // GET: /Home/
        [HttpGet]
        [Route("")]
        public IActionResult Index()
        {
            return View();
        }

        [HttpPost]
        [Route("movie/{title}")]
        public IActionResult GetMovie(string title)
        {
            Console.WriteLine(title);
            var MovieInfo = new Dictionary<string, object>();
            WebRequest.GetMovieInfo(title, ApiResponse =>
            {
                MovieInfo = ApiResponse;
            }
            ).Wait();
            var MovieStuff = MovieInfo["results"];
            Console.WriteLine(MovieStuff);
            // var MovieTitle = MovieInfo["results"];
            // Console.WriteLine(MovieTitle);
            // var Rating = MovieInfo["vote_average"];
            // var ReleaseYear = MovieInfo["release_date"];
            // string query = $"INSERT INTO movies (Title, Rating, Release_year, Created_at, Updated_at) Values('{MovieTitle}', '{Rating}', '{ReleaseYear}', NOW(), NOW()";
            // DbConnector.Execute(query);
            return View("Result");
        }
        
    }
}
