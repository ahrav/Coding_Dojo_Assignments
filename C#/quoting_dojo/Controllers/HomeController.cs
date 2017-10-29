using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using DbConnection;

namespace quoting_dojo.Controllers
{
    public class HomeController : Controller
    {
        // GET: /Home/
        [HttpGet]
        [Route("")]
        public IActionResult Index()
        {
            if(TempData["Error"] != null)
            {
                ViewBag.Error = TempData["Error"];
            }
            return View();
        }

        [HttpPost]
        [Route("submit")]
        public IActionResult SubmitForm(string name, string quote)
        {
            if(name == null || quote == null)
            {
                TempData["Error"] = "Fields can not be empty";
                return RedirectToAction("Index");
            }
            if(name == "" || quote == "")
            {
                TempData["Error"] = "Fields can not be empty";
                return RedirectToAction("Index");
            }
            DbConnector.Execute($"INSERT INTO Users (Name, Quote, Created_at, Updated_at) VALUES ('{name}', '{quote}', NOW(), NOW())");
            return RedirectToAction("ShowQuotes");
        }

        [HttpGet]
        [Route("quotes")]
        public IActionResult ShowQuotes()
        {
            var allUsers = DbConnector.Query("SELECT * FROM Users ORDER BY Created_at DESC");
            ViewBag.allUsers = allUsers;
            return View();
        }
    }
}
