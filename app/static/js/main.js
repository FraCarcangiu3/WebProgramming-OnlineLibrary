// URL delle API
const API_URL = '/books';

// Elementi DOM
const sezioneLibri = document.getElementById('sezione-libri');
const sezioneFormLibro = document.getElementById('sezione-form-libro');
const sezioneFormRecensione = document.getElementById('sezione-form-recensione');
const listaLibri = document.getElementById('lista-libri');
const formLibro = document.getElementById('form-libro');
const formRecensione = document.getElementById('form-recensione');
const titoloForm = document.getElementById('titolo-form');
const pulsanteOrdina = document.getElementById('pulsante-ordina');
const pulsanteAggiungi = document.getElementById('pulsante-aggiungi');
const pulsanteAnnullaForm = document.getElementById('annulla-form');
const pulsanteAnnullaRecensione = document.getElementById('annulla-recensione');
const contenitoreAvvisi = document.getElementById('contenitore-avvisi');
const tabellaLibri = document.getElementById('tabella-libri');

// Stato dell'applicazione
let staModificando = false;
let ordinamentoAttuale = false;
let valutazioneSelezionata = 0;

// Carica i libri all'avvio
document.addEventListener('DOMContentLoaded', () => {
    caricaLibri();
    impostaGestoriEventi();
});

// Configurazione degli event listener
function impostaGestoriEventi() {
    // Pulsante Ordinamento
    pulsanteOrdina.addEventListener('click', () => {
        ordinamentoAttuale = !ordinamentoAttuale;
        caricaLibri();
    });

    // Pulsante Aggiungi Libro
    pulsanteAggiungi.addEventListener('click', () => {
        mostraFormLibro();
    });

    // Pulsanti Annulla
    pulsanteAnnullaForm.addEventListener('click', nascondiFormLibro);
    pulsanteAnnullaRecensione.addEventListener('click', nascondiFormRecensione);

    // Form Libro
    formLibro.addEventListener('submit', gestisciInvioLibro);
    
    // Form Recensione
    formRecensione.addEventListener('submit', gestisciInvioRecensione);

    // Stelle per la recensione
    document.getElementById('valutazione-stelle').addEventListener('click', (e) => {
        if (e.target.classList.contains('stella')) {
            valutazioneSelezionata = parseInt(e.target.dataset.value);
            aggiornaVisualizzazioneStelle();
        }
    });
}

// Funzioni per la gestione dei libri
async function caricaLibri() {
    try {
        const risposta = await fetch(`${API_URL}?sort=${ordinamentoAttuale}`);
        if (!risposta.ok) {
            throw new Error('Errore durante il caricamento dei libri');
        }
        const libri = await risposta.json();
        renderizzaLibri(libri);
    } catch (error) {
        mostraAvviso(error.message, 'errore');
    }
}

function renderizzaLibri(libri) {
    listaLibri.innerHTML = '';
    
    if (libri.length === 0) {
        listaLibri.innerHTML = '<tr><td colspan="5">Nessun libro trovato</td></tr>';
        return;
    }

    libri.forEach(libro => {
        const riga = document.createElement('tr');
        riga.innerHTML = `
            <td>${libro.id}</td>
            <td>${libro.title}</td>
            <td>${libro.author}</td>
            <td>${renderizzaValutazione(libro.review)}</td>
            <td class="azioni-libro">
                <button class="pulsante-modifica" data-id="${libro.id}">Modifica</button>
                <button class="pulsante-recensione" data-id="${libro.id}">Recensisci</button>
                <button class="pulsante-elimina elimina" data-id="${libro.id}">Elimina</button>
            </td>
        `;
        listaLibri.appendChild(riga);
    });

    // Aggiungi event listener per i pulsanti nelle righe
    document.querySelectorAll('.pulsante-modifica').forEach(btn => {
        btn.addEventListener('click', () => modificaLibro(parseInt(btn.dataset.id)));
    });

    document.querySelectorAll('.pulsante-recensione').forEach(btn => {
        btn.addEventListener('click', () => mostraFormRecensione(parseInt(btn.dataset.id)));
    });

    document.querySelectorAll('.pulsante-elimina').forEach(btn => {
        btn.addEventListener('click', () => eliminaLibro(parseInt(btn.dataset.id)));
    });
}

function renderizzaValutazione(valutazione) {
    if (!valutazione) {
        return '<span class="no-recensione">Nessuna recensione</span>';
    }
    
    let stelle = '';
    for (let i = 0; i < valutazione; i++) {
        stelle += '★';
    }
    return `<span class="stelle">${stelle}</span> (${valutazione}/5)`;
}

async function gestisciInvioLibro(e) {
    e.preventDefault();

    const datiLibro = {
        id: parseInt(document.getElementById('id-libro').value),
        title: document.getElementById('titolo-libro').value,
        author: document.getElementById('autore-libro').value,
        review: null
    };

    try {
        let risposta;
        if (staModificando) {
            risposta = await fetch(`${API_URL}/${datiLibro.id}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(datiLibro)
            });
        } else {
            risposta = await fetch(API_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(datiLibro)
            });
        }

        if (!risposta.ok) {
            const errore = await risposta.json();
            throw new Error(errore.detail || 'Si è verificato un errore');
        }

        mostraAvviso(
            staModificando ? 'Libro aggiornato con successo' : 'Libro aggiunto con successo', 
            'successo'
        );
        nascondiFormLibro();
        caricaLibri();
    } catch (error) {
        mostraAvviso(error.message, 'errore');
    }
}

async function modificaLibro(id) {
    try {
        const risposta = await fetch(`${API_URL}/${id}`);
        if (!risposta.ok) {
            throw new Error('Libro non trovato');
        }
        const libro = await risposta.json();
        
        document.getElementById('id-libro').value = libro.id;
        document.getElementById('titolo-libro').value = libro.title;
        document.getElementById('autore-libro').value = libro.author;
        
        document.getElementById('id-libro').disabled = true;
        titoloForm.textContent = 'Modifica Libro';
        staModificando = true;
        mostraFormLibro();
    } catch (error) {
        mostraAvviso(error.message, 'errore');
    }
}

async function eliminaLibro(id) {
    if (!confirm('Sei sicuro di voler eliminare questo libro?')) {
        return;
    }

    try {
        const risposta = await fetch(`${API_URL}/${id}`, {
            method: 'DELETE'
        });

        if (!risposta.ok) {
            throw new Error('Errore durante l\'eliminazione del libro');
        }

        mostraAvviso('Libro eliminato con successo', 'successo');
        caricaLibri();
    } catch (error) {
        mostraAvviso(error.message, 'errore');
    }
}

// Funzioni per la gestione delle recensioni
function mostraFormRecensione(idLibro) {
    document.getElementById('id-libro-recensione').value = idLibro;
    valutazioneSelezionata = 0;
    aggiornaVisualizzazioneStelle();
    
    sezioneLibri.style.display = 'none';
    sezioneFormLibro.style.display = 'none';
    sezioneFormRecensione.style.display = 'block';
}

function aggiornaVisualizzazioneStelle() {
    const stelle = document.querySelectorAll('.stella');
    stelle.forEach((stella, indice) => {
        stella.classList.toggle('attiva', indice < valutazioneSelezionata);
    });
}

async function gestisciInvioRecensione(e) {
    e.preventDefault();
    
    if (valutazioneSelezionata === 0) {
        mostraAvviso('Seleziona una valutazione da 1 a 5', 'errore');
        return;
    }

    const idLibro = document.getElementById('id-libro-recensione').value;
    
    try {
        const risposta = await fetch(`${API_URL}/${idLibro}/review`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ review: valutazioneSelezionata })
        });

        if (!risposta.ok) {
            throw new Error('Errore durante l\'invio della recensione');
        }

        mostraAvviso('Recensione aggiunta con successo', 'successo');
        nascondiFormRecensione();
        caricaLibri();
    } catch (error) {
        mostraAvviso(error.message, 'errore');
    }
}

// Funzioni per la gestione dei form
function mostraFormLibro() {
    // Resetta il form
    formLibro.reset();
    document.getElementById('id-libro').disabled = false;
    titoloForm.textContent = 'Aggiungi Libro';
    staModificando = false;
    
    // Mostra il form e nascondi altre sezioni
    sezioneLibri.style.display = 'none';
    sezioneFormRecensione.style.display = 'none';
    sezioneFormLibro.style.display = 'block';
}

function nascondiFormLibro() {
    // Nascondi il form e mostra la lista libri
    sezioneFormLibro.style.display = 'none';
    sezioneFormRecensione.style.display = 'none';
    sezioneLibri.style.display = 'block';
}

function nascondiFormRecensione() {
    // Nascondi il form recensione e mostra la lista libri
    sezioneFormRecensione.style.display = 'none';
    sezioneFormLibro.style.display = 'none';
    sezioneLibri.style.display = 'block';
}

// Funzione per mostrare messaggi di avviso all'utente
function mostraAvviso(messaggio, tipo) {
    const avviso = document.createElement('div');
    avviso.className = `alert ${tipo}`;
    avviso.innerHTML = `
        ${messaggio}
        <button class="chiudi-avviso">×</button>
    `;
    
    contenitoreAvvisi.appendChild(avviso);
    
    // Aggiungi event listener per chiudere l'avviso
    avviso.querySelector('.chiudi-avviso').addEventListener('click', () => {
        avviso.remove();
    });
    
    // Rimuovi automaticamente l'avviso dopo 5 secondi
    setTimeout(() => {
        if (avviso.parentNode) {
            avviso.remove();
        }
    }, 5000);
}

// Funzione per applicare l'indice alla riga per le animazioni
function applicaIndiceRighe() {
    const righe = document.querySelectorAll('#lista-libri tr');
    righe.forEach((riga, indice) => {
        riga.style.setProperty('--row-index', indice);
    });
}

// Funzione per mostrare i form con animazione
function mostraFormConAnimazione(elementoForm) {
    // Rimuovi display: none
    elementoForm.style.display = 'block';
    
    // Forza un reflow per permettere l'animazione
    void elementoForm.offsetWidth;
    
    // Aggiungi la classe per attivare l'animazione
    elementoForm.classList.add('visible');
}

// Funzione per nascondere i form con animazione
function nascondiFormConAnimazione(elementoForm, callback) {
    // Rimuovi la classe per attivare l'animazione di uscita
    elementoForm.classList.remove('visible');
    
    // Aspetta che l'animazione finisca
    setTimeout(() => {
        elementoForm.style.display = 'none';
        if (callback) callback();
    }, 300); // Durata corrispondente alla transizione CSS
}

// Sostituisci questa funzione con quella che usa le animazioni
function mostraFormLibro(libro = null) {
    const form = document.getElementById('sezione-form-libro');
    const formRecensione = document.getElementById('sezione-form-recensione');
    
    // Se il form recensione è aperto, chiudilo prima
    if (formRecensione.style.display !== 'none') {
        nascondiFormConAnimazione(formRecensione);
    }
    
    // Popola il form se c'è un libro (modifica)
    if (libro) {
        document.getElementById('titolo-form').textContent = 'Modifica Libro';
        document.getElementById('id-libro').value = libro.id;
        document.getElementById('id-libro').disabled = true;
        document.getElementById('titolo-libro').value = libro.title;
        document.getElementById('autore-libro').value = libro.author;
    } else {
        document.getElementById('titolo-form').textContent = 'Aggiungi Libro';
        document.getElementById('id-libro').disabled = false;
        document.getElementById('form-libro').reset();
    }
    
    // Mostra il form con animazione
    mostraFormConAnimazione(form);
}

// Sostituisci questa funzione con quella che usa le animazioni
function mostraFormRecensione(id) {
    const form = document.getElementById('sezione-form-recensione');
    const formLibro = document.getElementById('sezione-form-libro');
    
    // Se il form libro è aperto, chiudilo prima
    if (formLibro.style.display !== 'none') {
        nascondiFormConAnimazione(formLibro);
    }
    
    // Imposta l'ID del libro da recensire
    document.getElementById('id-libro-recensione').value = id;
    
    // Resetta la selezione delle stelle
    document.querySelectorAll('.stella').forEach(stella => {
        stella.classList.remove('attiva');
    });
    
    // Mostra il form con animazione
    mostraFormConAnimazione(form);
}

// Sostituisci questa funzione con quella che usa le animazioni
function annullaModificaLibro() {
    const form = document.getElementById('sezione-form-libro');
    nascondiFormConAnimazione(form);
}

// Sostituisci questa funzione con quella che usa le animazioni
function annullaRecensione() {
    const form = document.getElementById('sezione-form-recensione');
    nascondiFormConAnimazione(form);
}

// Aggiungi questo al caricamento iniziale
document.addEventListener('DOMContentLoaded', function() {
    // Codice esistente...
    
    // Applica indice alle righe quando vengono caricate/aggiornate
    caricaLibri().then(() => {
        applicaIndiceRighe();
    });
}); 