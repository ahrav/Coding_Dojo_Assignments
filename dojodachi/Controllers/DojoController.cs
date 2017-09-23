using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using System;
 
namespace dojodachi.Controllers
{
    public class DojoController : Controller
    {
        [HttpGet]
        [Route("")]
        public IActionResult Index()
        {
            int? Happiness = HttpContext.Session.GetInt32("Happiness");
            if(Happiness == null)
            {
                Happiness = 20;
            }
            int? Fullness = HttpContext.Session.GetInt32("Fullness");
            if(Fullness == null)
            {
                Fullness = 20;
            }
            int? Energy = HttpContext.Session.GetInt32("Energy");
            if(Energy == null)
            {
                Energy = 50;
            }
            int? Meals = HttpContext.Session.GetInt32("Meals");
            if(Meals == null)
            {
                Meals = 3;
            }
            bool reset = false;
            if(Energy >= 100 && Fullness >= 100 && Happiness >= 100)
            {
                HttpContext.Session.SetString("Message", "Congratulations you won");
                reset = true;
            }
            if(Fullness == 0 || Happiness == 0)
            {
                HttpContext.Session.SetString("Message", "Your Dojodachi passed away");
                reset = true;
            }
            string Message = HttpContext.Session.GetString("Message");
            ViewBag.Reset = reset;
            ViewBag.Message = Message;
            ViewBag.Happiness = Happiness;
            ViewBag.Fullness = Fullness;
            ViewBag.Energy = Energy;
            ViewBag.Meals = Meals;
            HttpContext.Session.SetInt32("Fullness", (int)Fullness);
            HttpContext.Session.SetInt32("Happiness", (int)Happiness);
            HttpContext.Session.SetInt32("Energy", (int)Energy);
            HttpContext.Session.SetInt32("Meals", (int)Meals);
            return View();
        }

        [HttpGet]
        [Route("feed")]
        public IActionResult Feed()
        {
            int? Meals = HttpContext.Session.GetInt32("Meals");
            string Message = HttpContext.Session.GetString("Message");
            if(Meals == 0)
            {
                HttpContext.Session.SetString("Message", "You can not feed the Dojodachi with 0 meals remaining.");
                return RedirectToAction("index");
            }
            else
            {
                int? Fullness = HttpContext.Session.GetInt32("Fullness");
                Meals --;
                HttpContext.Session.SetInt32("Meals",(int) Meals);
                Random Like = new Random();
                int num = Like.Next(1,100);
                if(num > 25)
                {
                    Random Rand = new Random();
                    int number = Rand.Next(5,10);
                    Fullness += number;
                    string Note = $"You fed the Dojodachi Fullness +{number} Meals -1";
                    HttpContext.Session.SetString("Message", Note);
                }
                else
                {
                    string Note = "You fed the Dojodachi and it did not like it! Meals -1";
                    HttpContext.Session.SetString("Message", Note);
                }
                HttpContext.Session.SetInt32("Fullness",(int)Fullness);
                return RedirectToAction("Index");
            }
        }

        [HttpGet]
        [Route("play")]
        public IActionResult Play()
        {
            int? Energy = HttpContext.Session.GetInt32("Energy");
            string Message = HttpContext.Session.GetString("Message");
            if(Energy < 5)
            {
                HttpContext.Session.SetString("Message", "You can not play with the Dojodachi with less than 5 energy");
                return RedirectToAction("Index");
            }
            else
            {
                Energy -= 5;
                HttpContext.Session.SetInt32("Energy", (int)Energy);
                Random Like = new Random();
                int number = Like.Next(1,100);
                if(number > 25)
                {
                    Random Num = new Random();
                    int value = Num.Next(5,10);
                    int? Happiness = HttpContext.Session.GetInt32("Happiness");
                    Happiness += value;
                    HttpContext.Session.SetInt32("Happiness", (int)Happiness);
                    string Note = $"You played with your Dojodachi Happiness +{value} Energy -5";
                    HttpContext.Session.SetString("Message", Note);
                }
                else
                {
                    string Note = "You played with your Dojodachi and it did not like it! Energy -5";
                    HttpContext.Session.SetString("Message", Note);
                }
                return RedirectToAction("Index");
            }
        }

        [HttpGet]
        [Route("work")]
        public IActionResult Work()
        {
            int? Energy = HttpContext.Session.GetInt32("Energy");
            string Message = HttpContext.Session.GetString("Message");
            if(Energy < 5)
            {
                HttpContext.Session.SetString("Message", "You can not work with the Dojodachi with less than 5 energy");
                return RedirectToAction("Index");
            }
            else
            {
                Energy -= 5;
                HttpContext.Session.SetInt32("Energy", (int)Energy);
                Random Num = new Random();
                int Number = Num.Next(1,3);
                int? Meals = HttpContext.Session.GetInt32("Meals");
                Meals += Number;
                HttpContext.Session.SetInt32("Meals", (int)Meals);
                string Note = $"Your Dojodachi worked Meals +{Number} Energy -5";
                HttpContext.Session.SetString("Message", Note);
            }
            return RedirectToAction("Index");
        }
        [HttpGet]
        [Route("sleep")]
        public IActionResult Sleep()
        {
            int? Happiness = HttpContext.Session.GetInt32("Happiness");
            int? Fullness = HttpContext.Session.GetInt32("Fullness");
            string Message = HttpContext.Session.GetString("Message");
            if(Happiness < 5 || Fullness < 5)
            {
                HttpContext.Session.SetString("Message", "Can not sleep if fullness or happiness are less than 5");
                return RedirectToAction("Index");
            }
            else
            {
                Fullness -= 5;
                Happiness -= 5;
                HttpContext.Session.SetInt32("Fullness", (int)Fullness);
                HttpContext.Session.SetInt32("Happiness", (int)Happiness);
                int? Energy = HttpContext.Session.GetInt32("Energy");
                Energy += 15;
                HttpContext.Session.SetInt32("Energy", (int)Energy);
                string Note = $"Your Dojodachi slept Energy +15 Fullness -5 Happiness -5";
                HttpContext.Session.SetString("Message", Note);
            }
            return RedirectToAction("Index");
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