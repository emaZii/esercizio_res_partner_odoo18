### Esercizio Odoo

## Obiettivo 
  Creare un modulo personalizzato che aggiunga nuovi campi al modello res.partner 
  (Clienti/Contatti) e mostrarlo nella vista form dei contatti.  
  Di seguito vengono descritti i punti per la realizzazione della modifica. 

## Creazione modulo 
  Tramite il comando scaffold di odoo, creare un modulo di nome partner_field_custom.  
  Il modulo avrà una struttura di questo tipo: 
  # Aggiungere un campo al modello ResPartner 
  Tramite l’inherit del modello res.partner, aggiungere i seguenti campi personalizzati: 
    -Tipo cliente: campo selezione con opzioni  
    -Numero identificativo cliente: campo solo intero 
    -Codice cliente: campo stringa in sola lettura, dipende da tipo cliente e numero identificativo. o Formato:
    -“<tipocliente>-<n.id>” o Quando cambia uno dei due, va cambiata anche la stringa 
    -Data Creazione: campo data 
  Creazione Vista con campi personalizzati 
  Creare una scheda sulla pagina dei contatti, chiamata  SpecifichePixora 
   
 
La scheda deve mostrare i campi precedentemente aggiunti al modello.
