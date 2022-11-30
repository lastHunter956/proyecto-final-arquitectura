const container_cars = document.querySelector('.g-container_Mostrar_nuevos2')
const options = { method: 'GET' };

fetch('https://api-inventario-gv.onrender.com/stock', options)
    .then(response => response.json())
    .then(response => {
        const stock = response.vehiculos;
        stock.forEach(element => {
            if (element.Tipo == "nuevo"){
                const g_container_Mostrar_nuevos3 = document.createElement('div'); //
            g_container_Mostrar_nuevos3.classList.add('g-container_Mostrar_nuevos3')

            const g_container_Mostrar_nuevos4 = document.createElement('div'); //
            g_container_Mostrar_nuevos4.classList.add('g-container_Mostrar_nuevos4');

            const img = document.createElement('img');
            img.id = 'vehiculos'; 
            img.src = element.Imagen;

            g_container_Mostrar_nuevos4.append(img);

            g_container_Mostrar_nuevos3.append(g_container_Mostrar_nuevos4);

            const g_container_Mostrar_nuevos5 = document.createElement('div');
            g_container_Mostrar_nuevos5.classList.add('g-container_Mostrar_nuevos5');

            const h2 = document.createElement('h2');
            h2.id = 'min_titulo';
            h2.textContent = element.Nombre;

            const p_description = document.createElement('p');
            p_description.id = 'descripcion';
            p_description.textContent = element.Descripcion;

            const p__description = document.createElement('p');
            p__description.id = 'descripcion';
            p__description.textContent = element.Precio;

            const a = document.createElement('a');
            a.href = "./carro.html";


            const button = document.createElement('button');
            button.id = 'v_boton';
            button.textContent = 'VER DETALLES';

            a.append(button);

            g_container_Mostrar_nuevos5.append(h2, p_description, p__description, a);

            g_container_Mostrar_nuevos3.append(g_container_Mostrar_nuevos5);

            container_cars.append(g_container_Mostrar_nuevos3);   
            }
                  
        });
    })
    .catch(err => console.error(err));