using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
// Super simple right? Hope you're getting the hang of setting up a .NET Core app
namespace YourNamespace.Controllers
{
    public class HelloController : Controller
    {
        [HttpGet]
        [Route("/{first_name}/{last_name}/{age}/{color}")]
        public JsonResult DisplayInfo(string first_name, string last_name, int age, string color)
        {
            return Json(new {FirstName = first_name, LastName = last_name, Age = age, Color = color});
        }
    }
}
