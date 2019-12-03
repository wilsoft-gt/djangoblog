/* sirve para crear lost posts */
function addWrapper(textwrapper) {
    /* si lo hay llamamos al text area que contiene el texto deseado y lo asignamos en una variable*/
    var textareacont = document.getElementById("postBody");
    if (textwrapper != undefined) {
        /* verificamos si hay texto seleccionado */
        if (window.getSelection()) {
            if (textwrapper === "img"){
                /* aca cambiamos el nuevo texto y lo concatenamos junto con el texto que va a wrappear el texto seleccionado */
                var newContent = textareacont.value.slice(0, textareacont.selectionStart) + "<img class='img-fluid' src='#yourImageLinkHere' alt='#alternateTextHere'>" + textareacont.value.slice(textareacont.selectionEnd, textareacont.value.length)
                /* regresamos el texto cambiado al textarea original */
                textareacont.value = newContent;
    
                /* mandamos el texto actualizado al previsualizador */
                document.getElementById("result").innerHTML = newContent;

            } else if (textwrapper === "code") {
                var newContent = textareacont.value.slice(0, textareacont.selectionStart) + "<code><pre class='prettyprint linenums'>" + textareacont.value.substring(textareacont.selectionStart, textareacont.selectionEnd) + "</pre></code>" + textareacont.value.slice(textareacont.selectionEnd, textareacont.value.length);
                /* regresamos el texto cambiado al textarea original */
                textareacont.value = newContent;
    
                /* mandamos el texto actualizado al previsualizador */
                document.getElementById("result").innerHTML = newContent;

            } else {
                /* aca cambiamos el nuevo texto y lo concatenamos junto con el texto que va a wrappear el texto seleccionado */
                var newContent = textareacont.value.slice(0, textareacont.selectionStart) + "<" + textwrapper + ">" + textareacont.value.substring(textareacont.selectionStart, textareacont.selectionEnd) + "</" + textwrapper + ">" + textareacont.value.slice(textareacont.selectionEnd, textareacont.value.length);
                /* regresamos el texto cambiado al textarea original */
                textareacont.value = newContent;
    
                /* mandamos el texto actualizado al previsualizador */
                document.getElementById("result").innerHTML = newContent;
            }

        }
    } else {
        document.getElementById("result").innerHTML = textareacont.value;
    }
}

/* Estas dos funciones sirven para el menu de resources */
function returnUrl(elements) {
    var texto = document.createElement("textarea");
    texto.value = elements.src;
    document.body.appendChild(texto)
    texto.select()
    document.execCommand("copy");
    document.body.removeChild(texto);
    document.getElementById("imageLink").innerHTML = texto.value
    $(".alert").show()
    setTimeout(function () { $('.alert').hide(); }, 5000);
}

function alertHide() {
    $(".alert").hide()
}

function adminActiveTab() {
    var active = location.search.split('active=')[1].split("&")[0];
    var button = location.search.split("button=")[1];
    if (active){
        let tabactive = document.getElementsByClassName("active");
        tabactive[1].classList.remove("active")
        tabactive[0].classList.remove("active")
        document.getElementById(active).classList.add("active")
        document.getElementById(button).classList.add("active")
    } else {
        return ""
    }
}

