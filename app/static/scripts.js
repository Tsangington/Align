const hamburger = document.querySelector(".hamburger");
const navbarLinks = document.querySelector(".navbar-links");

hamburger.addEventListener("click",() => {
    hamburger.classList.toggle("active");
    navbarLinks.classList.toggle("active");
})

document.querySelector(".nav-link").foreach(n => n.addEventListener("click",() => {
    hamburger.classList.remove("active")
}))