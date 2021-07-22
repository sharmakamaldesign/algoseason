function showSnackbar() {
    var x = document.getElementById("snackbar");
    x.className = "show";
    setTimeout(function() { x.className = x.className.replace("show", ""); }, 3000);
}



// $(document).ready(function() {
//     $('[data-toggle="tooltip"]').tooltip();
// });


function test() {
    alert("hello world");
}