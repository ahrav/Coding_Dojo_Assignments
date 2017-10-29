using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
 
namespace portfolio.Controllers
{
    public class PortfolioController : Controller
    {
        [HttpGet]
        [Route("home")]
        public IActionResult Index()
        {
            return View();
        }

        [HttpGet]
        [Route("projects")]
        public IActionResult Project()
        {
            return View();
        }
        [HttpGet]
        [Route("contact")]
        public IActionResult Contact()
        {
            return View();
        }
    }
}