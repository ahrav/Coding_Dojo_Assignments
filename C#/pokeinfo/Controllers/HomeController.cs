using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;

namespace pokeinfo.Controllers
{
    public class HomeController : Controller
    {
        [HttpGet]
        [Route("")]
        public IActionResult Index()
        {
            return View();
        }
        // GET: /Home/
        [HttpGet]
        [Route("/pokemon/{pokeid}")]
        public IActionResult GetPokemonInfo(int pokeid)
        {
            var PokeInfo = new Dictionary<string, object>();
            WebRequest.GetPokemonInfo(pokeid, ApiResponse => 
            {
                PokeInfo = ApiResponse;
            }
            ).Wait();
            ViewBag.PokeInfo = PokeInfo;
            return View();
        }
    }
}
