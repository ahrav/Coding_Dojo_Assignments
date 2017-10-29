using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;

namespace poke_info/.Controllers
{
    public class HomeController : Controller
    {
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
