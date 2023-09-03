document.addEventListener("DOMContentLoaded", function () {
  const dropdowns = document.querySelectorAll(".dropdown");
  dropdowns.forEach((dropbtn) => {
    dropbtn.addEventListener("click", function () {
      const dropdownContent = this.querySelector(".drop-links");
      if (dropdownContent.style.display === "flex") {
        dropdownContent.style.opacity = "0";
        setTimeout(() => {
          dropdownContent.style.display = "none";
        }, 300);
      } else {
        dropdownContent.style.display = "flex";
        setTimeout(() => {
          dropdownContent.style.opacity = "1";
        }, 10);
      }
    });
  });
});
