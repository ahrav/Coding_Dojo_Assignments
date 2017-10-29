using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using System;
 
namespace random_passcode.Controllers
{
    public class PasscodeController : Controller
    {
        [HttpGet]
        [Route("")]
        public IActionResult Index()
        {
            int? Number = HttpContext.Session.GetInt32("Number");
            if(Number == null)
            {
                Number = 0;
            }
            Number += 1;
            string Chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
            string Password = "";
            Random Rand = new Random();
            for(int i = 1; i <= 14; i++)
            {
                Password = Password + Chars[Rand.Next(0, Chars.Length)];
            }
            ViewBag.Password = Password;
            ViewBag.Count = Number;
            HttpContext.Session.SetInt32("Number", (int)Number);
            return View();
        }

        [HttpGet]
        [Route("reset")]
        public IActionResult Reset()
        {
            HttpContext.Session.Clear();
            return RedirectToAction("Index");
        }
    }
}