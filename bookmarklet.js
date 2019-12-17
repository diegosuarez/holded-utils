/***
 * Bookmarklet para automatizar la aprobacion de fichajes. Toma todos los pendientes y los marca como aprobados.
 * Añadir a la barra de marcadores de Chrome con nombre "HOLDED APROBEITOR" (imprescindible) y como URL el codigo.
 * Para usarlo, estando en la pagina de supervisor, pulsar el bookmarklet de la barra.
 */

javascript:(function(){document.querySelectorAll(".timetracking-container-pending tr[data-timetrackingid]").forEach(i=>$.post('/tp/supervisor/timetracking/'+i.getAttribute("data-timetrackingid")+'/review', { status: "approve" }));setTimeout(loadSupervisorData, 800);})()
