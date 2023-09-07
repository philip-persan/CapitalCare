const btn = document.getElementById("btn-filter");
const form = document.getElementById("form-filter");

btn.addEventListener("click", () => {
  if (form.style.display === "flex") {
    form.style.opacity = "0";
    setTimeout(() => {
      form.style.display = "none";
    }, 300);
  } else {
    form.style.display = "flex";
    setTimeout(() => {
      form.style.opacity = "1";
    }, 300);
  }
});
