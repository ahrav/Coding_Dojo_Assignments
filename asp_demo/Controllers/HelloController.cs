using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
 
namespace asp_demo.Controllers
{
    public class HelloController : Controller
    {
        [HttpGet]
        [Route("")]
        public IActionResult Index()
        {
            return View();
        }

        [HttpPost]
        [Route("show")]
        public IActionResult Show(string Name, int Age) 
        {
            ViewBag.PersonName = Name;
            ViewBag.PersonAge = Age;
            return View();
        }
    }
}