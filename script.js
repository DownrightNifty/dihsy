let cbs = document.querySelectorAll(".collapse-btn");

for (let cb of cbs) {
  cb.addEventListener("click", ev => {
    let button = ev.currentTarget;
    let icon = button.children[0];
    let heading = button.parentElement;
    let section = heading.parentElement;

    // collapse button hit
    if (!section.classList.contains("collapsed")) {
      // hide elements
      section.classList.add("collapsed");
  
      // change self into an expand button
      icon.classList.remove("minus-icon");
      icon.classList.remove("fa-angle-down");
      icon.classList.add("plus-icon");
      icon.classList.add("fa-angle-right");
    }
    else { // expand button hit
      // unhide elements
      section.classList.remove("collapsed");

      // change self into an expand button
      icon.classList.remove("plus-icon");
      icon.classList.remove("fa-angle-right");
      icon.classList.add("minus-icon");
      icon.classList.add("fa-angle-down");
    }
  });
}

let sl = document.querySelector("#subscribe-link");
let rbs = document.querySelectorAll(".rss-btn");

for (let rb of rbs) {
  rb.addEventListener("click", ev => {
    sl.click();
  });
}
