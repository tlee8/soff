//Team TomLee -- Angela Tom and Thomas Lee
//SoftDev1 pd6
//K29 -- Sequential Progression II: Electric Boogaloo
//2018-12-20

var fibonacci = function(n) {
  if (n < 2) return n;
  var a = 0;
  var b = 1;
  var temp;
  while (n > 1) {
    temp = b;
    b = a + b;
    a = temp;
    n--;
  }
  return b;
};

var gcd = function(a,b) {
  if (a == b) return a;
  else if (a > b) return gcd(a-b,b);
  else return gcd(b-a,a);
};

var students = ["Kevin","Thomas","Angela","Sophia"];

var randomStudent = function() {
  return students[Math.floor(Math.random() * students.length)];
};



var fibbut = document.getElementById("fib")

var fib = function() {
  console.log('The Tenth Fibonacci Number')
  console.log(fibonacci(10));
};

fibbut.addEventListener('click', fib)



var gcdbut = document.getElementById("gcd")

var greatComDiv = function() {
  console.log('The Greatest Common Divisor of 45 and 72')
  console.log(gcd(45, 72));
};

gcdbut.addEventListener('click', greatComDiv)



var randbut = document.getElementById("rand")

var rand = function() {
  console.log('Here is a Random Student')
  console.log(randomStudent());
};

randbut.addEventListener('click', rand)
