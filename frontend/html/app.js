const backendStatus = document.getElementById("backend-status");      // para el cartel de estado
const teamBody = document.getElementById("team-body");               // para insertar las filas de la tabla
const emptyMessage = document.getElementById("empty-message");      // para mostrar mensaje cuando no hay datos o error

// Defino la URL del backend:
const TEAM_ENDPOINT = "http://localhost:5000/api/team";

// Actualizo el cartel de estado del backend, con diferentes estilos según el tipo (ok, error, loading):
function setBackendStatus(type, message) {
    backendStatus.textContent = message;
    backendStatus.className = `status ${type}`;
}

// Limpio la tabla antes de cargar nuevos datos:
function clearTable() {
    teamBody.innerHTML = "";
}

// Creo una fila de la tabla para cada integrante (objeto miembro) del equipo:
function buildRow(member) {
    const row = document.createElement("tr");

    const nombreCompleto = `${member.nombre} ${member.apellido}`;     // Combino nombre y apellido para mostrar en una sola celda

    // Armo las celdas de la fila con los datos del miembro:
    row.innerHTML = `
        <td>${nombreCompleto}</td>
        <td>${member.legajo}</td>
        <td>${member.feature}</td>
        <td>${member.servicio}</td>
        <td><span class="service-status">${member.estado}</span></td>
    `;

    return row;
}

async function loadTeam() {
    // Primero pone el estado en “Consultando backend...”, limpia la tabla y oculta el mensaje vacío:
    setBackendStatus("loading", "Consultando backend...");
    clearTable();
    emptyMessage.hidden = true;

    try {
        const response = await fetch(TEAM_ENDPOINT);    // Hace la consulta al backend para obtener los datos del equipo

        // Si la respuesta no fue correcta, lanza un error:
        if (!response.ok) {
            throw new Error(`Error HTTP ${response.status}`);
        }

        const members = await response.json();      // Convierte la respuesta a JSON

        setBackendStatus("ok", "Backend respondiendo correctamente");    // Si todo salió bien, actualiza el estado a “Backend respondiendo correctamente”

        // Si no vino un array o vino vacío, muestra el mensaje de que no hay integrantes:
        if (!Array.isArray(members) || members.length === 0) {
            emptyMessage.hidden = false;
            emptyMessage.textContent = "No hay integrantes para mostrar.";
            return;
        }

        // Si todo salió bien y hay datos, recorre el array de miembros y construye una fila para cada uno, insertándola en la tabla:
        members.forEach((member) => {
            const row = buildRow(member);
            teamBody.appendChild(row);
        });
    } catch (error) {                         // Si algo falla, entra al catch, muestra error en consola y cambia el estado visible:
        console.error("No se pudieron cargar los datos del equipo:", error);
        setBackendStatus("error", "Backend no disponible o sin respuesta");
        emptyMessage.hidden = false;
        emptyMessage.textContent =
            "No fue posible cargar los integrantes desde el backend.";
    }
}

loadTeam();      // Ejecuto todo