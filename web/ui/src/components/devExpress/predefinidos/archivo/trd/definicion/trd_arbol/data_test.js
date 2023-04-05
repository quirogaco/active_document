const data = [{
    "id": 1,
    "padre_id": -1,
    "tipo": "dependencia",
    "nombre": "Secretaria general",    
}, {
    "id": 2,
    "padre_id": 1,
    "tipo": "serie",
    "nombre": "Actas",    
}, {
    "id": 3,
    "padre_id": 2,
    "tipo": "subserie",
    "nombre": "Actas de comite",    
}, {
    "id": 4,
    "padre_id": 3,
    "tipo": "tipo",
    "nombre": "Acta",  
}, {
    "id": 5,
    "padre_id": -1,
    "tipo": "dependencia",
    "nombre": "Oficina juridica",   
}]

export default {
    trd_data: data
}