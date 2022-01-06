import { http } from './config'

export default{    
    createTicket: (ticket) =>{
        return http.post('ticket',ticket)
    },
    alterTicket: (public_id,ticket) =>{
        return http.put('ticket/'+public_id,ticket)
    },
    deleteTicket: (public_id) =>{
        return http.delete('ticket/'+public_id)
    },
    GetTicket: (public_id) =>{
        return http.get('ticket/'+public_id)
    },  
    ticket: () =>{
        return http.get('ticket')
    },    

    createEvent: (event) =>{
        return http.post('event',event)
    },
    alterEvent: (public_id,event) =>{
        return http.put('event/'+public_id,event)
    },
    deleteEvent: (public_id) =>{
        return http.delete('event/'+public_id)
    },
    GetEvent: (public_id) =>{
        return http.get('event/'+public_id)
    },  
    Event: () =>{
        return http.get('event')
    }, 
    myEvent: (public_id) =>{
        return http.get('myEvent/'+public_id)
    },

    Category: (category) =>{
        return http.get('category/'+category)
    },
    
    City: () =>{
        return http.get('city')
    }, 

    GetViacep: (cep) =>{
        return http.get(`viacep/${cep}`)
    }, 
}