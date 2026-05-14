// 🚀 FUNCIÓN PRINCIPAL
async function enviar(textoManual = null){

    let input = document.getElementById("mensaje")

    let texto = textoManual !== null ? textoManual : input.value

    if(!texto.trim()) return

    let chat = document.getElementById("chat")

    // 👤 Mensaje usuario
    chat.innerHTML += `<div class="mensaje-usuario">${texto}</div>`

    try{

        let response = await fetch("https://chatbot-indicadores.onrender.com/chat",{
            method:"POST",
            mode: "cors",
            headers:{
                "Content-Type":"application/json"
            },
            body: JSON.stringify({
                texto: texto
            })
        })

        let data = await response.json()

        console.log("respuesta:", data)

        // 🤖 Mensaje bot
        chat.innerHTML += `<div class="mensaje-bot">${data.respuesta || "Sin respuesta"}</div>`

        // 📊 GRAFICA
        if(data.grafica){

            let canvas = document.createElement("canvas")
            chat.appendChild(canvas)

            new Chart(canvas, {
                type: data.grafica.tipo,
                data: {
                    labels: data.grafica.anios,
                    datasets: [{
                        label: "Matricula",
                        data: data.grafica.valores
                    }]
                }
            })
        }

        // 🔽 scroll automático
        chat.scrollTop = chat.scrollHeight

        // 🧹 limpiar input
        input.value = ""
        input.focus()

    }catch(error){

        console.error(error)

        chat.innerHTML += `<div class="mensaje-bot">Error de conexión</div>`
    }

    setTimeout(() => {
        input.focus()
    }, 50)
}

function enviarSugerido(texto){
    enviar(texto)

    setTimeout(() => {
        document.getElementById("mensaje").focus()
    }, 50)
}

document.getElementById("mensaje").addEventListener("keypress", function(e){
    if (e.key === "Enter"){
        enviar()
    }
})