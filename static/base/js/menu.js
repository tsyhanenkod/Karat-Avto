const toggleBtn = document.getElementById("toggle-menu");
const menu = document.getElementById("menu");
const closeBtn = document.getElementById("close")

toggleBtn.addEventListener("click", () => {
  menu.style.right = menu.style.right === "-200px" ? "0" : "-200px";
});

closeBtn.addEventListener("click", () => {
  menu.style.right = menu.style.right === "-200px" ? "0" : "-200px";
});