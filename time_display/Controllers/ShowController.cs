using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
 
namespace time_display.Controllers
{
    public class ShowController : Controller
    {
        [HttpGet]
        [Route("")]
        public IActionResult Index()
        {
            return View();
        }
    }
}