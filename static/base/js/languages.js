var form = document.querySelector("#language-form");
var select = form.querySelector(".language-select");
select.addEventListener("change", function() {
    console.log("Selected language:", select.value);
    console.log("Next page:", form.querySelector("input[name=next]").value);

    var xhr = new XMLHttpRequest();
    xhr.open("POST", form.action, true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
    xhr.onload = function () {
      if (xhr.status === 200) {
        // добавляем язык в URL и перезагружаем страницу
        var currentUrl = window.location.href;
        var newUrl = currentUrl.replace(/\/(en|uk)\//, "/" + select.value + "/");
        window.location.replace(newUrl);
      }
    };
    xhr.send("language=" + select.value + "&next=" + form.querySelector("input[name=next]").value);
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}