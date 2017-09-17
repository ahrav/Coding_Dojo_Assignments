using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
 
namespace dojo_survey.Controllers
{
    public class SurveyController : Controller
    {
        [HttpGet]
        [Route("")]
        public IActionResult Index()
        {
            ViewBag.Errors = new List<string>();
            return View();
        }

        [HttpPost]
        [Route("result")]
        public IActionResult Result(string name, string location, string language, string comment)
        {
            ViewBag.Errors = new List<string>();

            if(name == null)
            {
                ViewBag.Errors.Add("Name can not be empty");
            }
            if(comment == null)
            {
                ViewBag.Errors.Add("Commnet can not be empty");
            }
            if(ViewBag.Errors.Count > 0)
            {
                return View("Index");
            }
            ViewBag.Name = name;
            ViewBag.Location = location;
            ViewBag.Language = language;
            ViewBag.Comment = comment;
            return View();
        }
    }
}